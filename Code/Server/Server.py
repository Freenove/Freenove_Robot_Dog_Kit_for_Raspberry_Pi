# -*- coding: utf-8 -*-
import io
import os
import time
import fcntl
import socket
import struct
from picamera2 import Picamera2,Preview
from picamera2.encoders import JpegEncoder
from picamera2.outputs import FileOutput
from picamera2.encoders import Quality
from threading import Condition
import threading
from Led import *
from Servo import *
from Thread import *
from Buzzer import *
from Control import *
from ADS7830 import *
from Ultrasonic import *
from Command import COMMAND as cmd

class StreamingOutput(io.BufferedIOBase):
    def __init__(self):
        self.frame = None
        self.condition = Condition()

    def write(self, buf):
        with self.condition:
            self.frame = buf
            self.condition.notify_all()

class Server:
    def __init__(self):
        
        self.tcp_flag=False
        self.led=Led()
        self.servo=Servo()
        self.adc=ADS7830()
        self.buzzer=Buzzer()
        self.control=Control()
        self.sonic=Ultrasonic()
        self.control.Thread_conditiona.start()
        self.battery_voltage=[8.4,8.4,8.4,8.4,8.4]
    def get_interface_ip(self):
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        return socket.inet_ntoa(fcntl.ioctl(s.fileno(),
                                            0x8915,
                                            struct.pack('256s',b'wlan0'[:15])
                                            )[20:24])
    def turn_on_server(self):
        #ip adress
        HOST=self.get_interface_ip()
        #Port 8001 for video transmission
        self.server_socket = socket.socket()
        self.server_socket.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEPORT,1)
        self.server_socket.bind((HOST, 8001))              
        self.server_socket.listen(1)
        
        #Port 5001 is used for instruction sending and receiving
        self.server_socket1 = socket.socket()
        self.server_socket1.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEPORT,1)
        self.server_socket1.bind((HOST, 5001))
        self.server_socket1.listen(1)
        print('Server address: '+HOST)
        
    def turn_off_server(self):
        try:
            self.connection.close()
            self.connection1.close()
        except :
            print ('\n'+"No client connection")
    
    def reset_server(self):
        self.turn_off_server()
        self.turn_on_server()
        self.video=threading.Thread(target=self.transmission_video)
        self.instruction=threading.Thread(target=self.receive_instruction)
        self.video.start()
        self.instruction.start()
    def send_data(self,connect,data):
        try:
            connect.send(data.encode('utf-8'))
            #print("send",data)
        except Exception as e:
            print(e)
    def transmission_video(self):
        try:
            self.connection,self.client_address = self.server_socket.accept()
            self.connection=self.connection.makefile('wb')
        except:
            pass
        self.server_socket.close()
        print ("socket video connected ... ")
        camera = Picamera2()
        camera.configure(camera.create_video_configuration(main={"size": (400, 300)}))
        output = StreamingOutput()
        encoder = JpegEncoder(q=95)
        camera.start_recording(encoder, FileOutput(output),quality=Quality.VERY_HIGH) 
        while True:
            with output.condition:
                output.condition.wait()
                frame = output.frame
            try:                
                lenFrame = len(output.frame) 
                #print("output .length:",lenFrame)
                lengthBin = struct.pack('<I', lenFrame)
                self.connection.write(lengthBin)
                self.connection.write(frame)
            except Exception as e:
                camera.stop_recording()
                camera.close()
                print ("End transmit ... " )
                break

    def measuring_voltage(self,connect):
        try:
            for i in range(5):
                self.battery_voltage[i]=round(self.adc.power(0),2)
            command=cmd.CMD_POWER+'#'+str(max(self.battery_voltage))+"\n"
            self.send_data(connect,command)
            self.sednRelaxFlag()
            self.battery_reminder()
        except Exception as e:
            print(e)
    def battery_reminder(self):
        if max(self.battery_voltage) < 6.4:
            self.turn_off_server()
            self.control.relax(True)
            print("The batteries power are too low. Please recharge the batteries or replace batteries.")
            print("Close the server")
            os._exit(0)
    def sednRelaxFlag(self):
        if self.control.move_flag!=2:
            command=cmd.CMD_RELAX+"#"+str(self.control.move_flag)+"\n"
            self.send_data(self.connection1,command)
            self.control.move_flag= 2  
                  
    def receive_instruction(self):
        try:
            self.connection1,self.client_address1 = self.server_socket1.accept()
            print ("Client connection successful !")
        except:
            print ("Client connect failed")
        self.server_socket1.close()
        while True:
            try:
                allData=self.connection1.recv(1024).decode('utf-8')
                #print(allData)
            except:
                if self.tcp_flag:
                    if max(self.battery_voltage) > 6.4:
                        self.reset_server()
                    break
                else:
                    break
            
            if allData=="" and self.tcp_flag:
                self.reset_server()
                break
            else:
                cmdArray=allData.split('\n')
                #print(cmdArray)
                if cmdArray[-1] !="":
                    cmdArray==cmdArray[:-1]
            
            for oneCmd in cmdArray:
                data=oneCmd.split("#")
                if data==None or data[0]=='':
                    continue
                elif cmd.CMD_BUZZER in data:
                    self.buzzer.run(data[1])
                elif cmd.CMD_LED in data:
                    try:
                        stop_thread(thread_led)
                    except:
                        pass
                    thread_led=threading.Thread(target=self.led.light,args=(data,))
                    thread_led.start()   
                elif cmd.CMD_LED_MOD in data:
                    try:
                        stop_thread(thread_led)
                    except:
                        pass
                    thread_led=threading.Thread(target=self.led.light,args=(data,))
                    thread_led.start()
                elif cmd.CMD_HEAD in data:
                    self.servo.setServoAngle(15,int(data[1]))
                elif cmd.CMD_SONIC in data:
                    command=cmd.CMD_SONIC+'#'+str(self.sonic.getDistance())+"\n"
                    self.send_data(self.connection1,command)
                elif cmd.CMD_POWER in data:
                    self.measuring_voltage(self.connection1)
                elif cmd.CMD_WORKING_TIME in data: 
                    if self.control.move_timeout!=0 and self.control.relax_flag==True:
                        if self.control.move_count >180:
                            command=cmd.CMD_WORKING_TIME+'#'+str(180)+'#'+str(round(self.control.move_count-180))+"\n"
                        else:
                            if self.control.move_count==0:
                                command=cmd.CMD_WORKING_TIME+'#'+str(round(self.control.move_count))+'#'+str(round((time.time()-self.control.move_timeout)+60))+"\n"
                            else:
                                command=cmd.CMD_WORKING_TIME+'#'+str(round(self.control.move_count))+'#'+str(round(time.time()-self.control.move_timeout))+"\n"
                    else:
                        command=cmd.CMD_WORKING_TIME+'#'+str(round(self.control.move_count))+'#'+str(0)+"\n"
                    self.send_data(self.connection1,command)
                else:
                    self.control.order=data
                    self.control.timeout=time.time()

        try:    
            stop_thread(thread_power)
        except:
            pass
        try:    
            stop_thread(thread_led)
        except:
            pass
        print("close_recv")
        self.control.relax_flag=False
        self.control.order[0]=cmd.CMD_RELAX
        

if __name__ == '__main__':
    pass
    
