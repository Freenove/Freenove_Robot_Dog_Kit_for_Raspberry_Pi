# -*- coding: utf-8 -*-
import io
import time
import fcntl
import socket
import struct
import picamera
import threading
from Led import *
from Servo import *
from Thread import *
from Buzzer import *
from Control import *
from ADS7830 import *
from Ultrasonic import *
from Command import COMMAND as cmd

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
    def get_interface_ip(self):
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        return socket.inet_ntoa(fcntl.ioctl(s.fileno(),
                                            0x8915,
                                            struct.pack('256s',b'wlan0'[:15])
                                            )[20:24])
    def turn_on_server(self):
        #ip adress
        HOST=self.get_interface_ip()
        #Port 8000 for video transmission
        self.server_socket = socket.socket()
        self.server_socket.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEPORT,1)
        self.server_socket.bind((HOST, 8001))              
        self.server_socket.listen(1)
        
        #Port 5000 is used for instruction sending and receiving
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
        try:
            with picamera.PiCamera() as camera:
                camera.resolution = (400,300)       # pi camera resolution
                camera.framerate = 15               # 15 frames/sec
                camera.saturation = 80              # Set image video saturation
                camera.brightness = 50              # Set the brightness of the image (50 indicates the state of white balance)
                time.sleep(2)                       # give 2 secs for camera to initilize
                start = time.time()
                stream = io.BytesIO()
                # send jpeg format video stream
                print ("Start transmit ... ")
                for foo in camera.capture_continuous(stream, 'jpeg', use_video_port = True):
                    try:
                        self.connection.flush()
                        stream.seek(0)
                        b = stream.read()
                        lengthBin = struct.pack('L', len(b))
                        self.connection.write(lengthBin)
                        self.connection.write(b)
                        stream.seek(0)
                        stream.truncate()
                    except BaseException as e:
                        #print (e)
                        print ("End transmit ... " )
                        break
        except BaseException as e:
            #print(e)
            print ("Camera unintall")
            
    def measuring_voltage(self,connect):
        try:
            data=round(self.adc.power(0),2)
            command=cmd.CMD_POWER+'#'+str(data)+"\n"
            self.send_data(connect,command)
            self.sednRelaxFlag()
        except Exception as e:
            print(e)
    def measuring_distance(self,connect):
        while True:
            try:
                command=cmd.CMD_SONIC+'#'+str(self.sonic.getDistance())+"\n"
                self.send_data(connect,command)
                time.sleep(0.05)
            except Exception as e:
                print(e)
                break
    
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
                    if len(data) < 2:
                        command=cmd.CMD_SONIC+'#'+str(self.sonic.getDistance())+"\n"
                        self.send_data(self.connection1,command)
                    else:
                        if data[1]=="1":
                            thread_sonic=threading.Thread(target=self.measuring_distance,args=(self.connection1,))
                            thread_sonic.start()
                        else:
                            try:
                                stop_thread(thread_sonic)
                            except:
                                pass
                elif cmd.CMD_POWER in data:
                    self.measuring_voltage(self.connection1)
                else:
                    self.control.order=data
                    self.control.timeout=time.time()
        try:    
            stop_thread(thread_sonic)
        except:
            pass
        try:    
            stop_thread(thread_power)
        except:
            pass
        try:    
            stop_thread(thread_led)
        except:
            pass
        try:    
            stop_thread(thread_relax)
        except:
            pass
        print("close_recv")

if __name__ == '__main__':
    pass
    
