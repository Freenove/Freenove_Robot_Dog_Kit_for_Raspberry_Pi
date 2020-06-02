# -*- coding: utf-8 -*-
import sys
from ui_led import Ui_led
from ui_client import Ui_client
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from Client import *
from Calibration import *
class MyWindow(QMainWindow,Ui_client):
    def __init__(self):
        super(MyWindow,self).__init__()
        self.setupUi(self)
        self.setWindowIcon(QIcon('Picture/logo_Mini.png'))
        self.Video.setScaledContents (True)
        self.Video.setPixmap(QPixmap('Picture/dog_client.png'))

        self.setFocusPolicy(Qt.StrongFocus)
        self.Key_W=False
        self.Key_A=False
        self.Key_S=False
        self.Key_D=False
        self.Key_Q=False
        self.Key_E=False
        self.Key_Space=False

        self.client=Client()
        self.client.move_speed=str(self.slider_speed.value())
        file = open('IP.txt', 'r')
        self.lineEdit_IP_Adress.setText(str(file.readline()))
        file.close()
        
        #ProgressBar
        self.progress_Power.setMinimum(0)
        self.progress_Power.setMaximum(100)
        self.progress_Power.setValue(90)
        
        #Button click event
        self.Button_Connect.clicked.connect(self.connect)
        self.Button_Video.clicked.connect(self.video)
        self.Button_Ball_And_Face.clicked.connect(self.chase_ball_and_find_face)
        self.Button_IMU.clicked.connect(self.imu)
        self.Button_Calibration.clicked.connect(self.showCalibrationWindow)
        self.Button_LED.clicked.connect(self.showLedWindow)
        self.Button_Sonic.clicked.connect(self.sonic)
        self.Button_Relax.clicked.connect(self.relax)
        
        self.Button_ForWard.pressed.connect(self.forward)
        self.Button_ForWard.released.connect(self.stop)
        self.Button_BackWard.pressed.connect(self.backward)
        self.Button_BackWard.released.connect(self.stop)
        self.Button_Left.pressed.connect(self.left)
        self.Button_Left.released.connect(self.stop)
        self.Button_Right.pressed.connect(self.right)
        self.Button_Right.released.connect(self.stop)
        self.Button_Step_Left.pressed.connect(self.step_left)
        self.Button_Step_Left.released.connect(self.stop)
        self.Button_Step_Right.pressed.connect(self.step_right)
        self.Button_Step_Right.released.connect(self.stop)
        self.Button_Buzzer.pressed.connect(self.buzzer)
        self.Button_Buzzer.released.connect(self.buzzer)

        #Slider
        self.slider_head.setMinimum(50)
        self.slider_head.setMaximum(180)
        self.slider_head.setSingleStep(1)
        self.slider_head.setValue(90)
        self.slider_head.valueChanged.connect(self.head)
        
        self.slider_horizon.setMinimum(-20)
        self.slider_horizon.setMaximum(20)
        self.slider_horizon.setSingleStep(1)
        self.slider_horizon.setValue(0)
        self.slider_horizon.valueChanged.connect(self.horizon)
        
        self.slider_height.setMinimum(-20)
        self.slider_height.setMaximum(20)
        self.slider_height.setSingleStep(1)
        self.slider_height.setValue(0)
        self.slider_height.valueChanged.connect(self.height)

        self.slider_pitch.setMinimum(-20)
        self.slider_pitch.setMaximum(20)
        self.slider_pitch.setSingleStep(1)
        self.slider_pitch.setValue(0)
        self.slider_pitch.valueChanged.connect(lambda:self.attitude(self.label_pitch,self.slider_pitch))

        self.slider_yaw.setMinimum(-20)
        self.slider_yaw.setMaximum(20)
        self.slider_yaw.setSingleStep(1)
        self.slider_yaw.setValue(0)
        self.slider_yaw.valueChanged.connect(lambda:self.attitude(self.label_yaw,self.slider_yaw))

        self.slider_roll.setMinimum(-20)
        self.slider_roll.setMaximum(20)
        self.slider_roll.setSingleStep(1)
        self.slider_roll.setValue(0)
        self.slider_roll.valueChanged.connect(lambda:self.attitude(self.label_roll,self.slider_roll))
        
        self.slider_speed.setMinimum(2)
        self.slider_speed.setMaximum(10)
        self.slider_speed.setSingleStep(1)
        self.slider_speed.setValue(8)
        self.slider_speed.valueChanged.connect(self.speed)
        self.client.move_speed=str(self.slider_speed.value())

        #Timer
        self.timer=QTimer(self)
        self.timer.timeout.connect(self.refresh_image)

        self.time_out = QTimer(self)
        self.time_out.timeout.connect(self.power)

        self.drawpoint=[585,135]
    #keyboard
    def keyPressEvent(self, event):
        if(event.key() == Qt.Key_C):
            print("C")
            self.connect()
        if(event.key() == Qt.Key_V):
            print("V")
            if self.Button_Video.text() == 'Open Video':
                self.timer.start(34)
                self.Button_Video.setText('Close Video')
            else:
                self.timer.stop()
                self.Button_Video.setText('Open Video')
           
        if(event.key() == Qt.Key_R):
            print("R")
            self.relax()
        if(event.key() == Qt.Key_L):
            print("L")
            self.showLedWindow()
        if(event.key() == Qt.Key_U):
            print("U")
            self.sonic()
        if(event.key() == Qt.Key_F):
            print("F")
            self.chase_ball_and_find_face()
        if(event.key() == Qt.Key_B):
            print("B")
            self.imu()
        if(event.key() == Qt.Key_M):
            print("M")
            self.showCalibrationWindow()
            

        if event.isAutoRepeat():
            pass
        else :
            if event.key() == Qt.Key_W:
                print("W")
                self.forward()
                self.Key_W=True
            elif event.key() == Qt.Key_S:
                print("S")
                self.backward()
                self.Key_S=True
            elif event.key() == Qt.Key_A:
                print("A")
                self.left()
                self.Key_A=True
            elif event.key() == Qt.Key_D:                  
                print("D")
                self.right()
                self.Key_D=True
            elif event.key() == Qt.Key_Q:                  
                print("Q")
                self.step_left()
                self.Key_Q=True
            elif event.key() == Qt.Key_E:                  
                print("E")
                self.step_right()
                self.Key_E=True 
            elif event.key() == Qt.Key_Space:  
                print("Space")
                self.buzzer()
                self.Key_Space=True

    def keyReleaseEvent(self, event):
        if(event.key() == Qt.Key_W):
            if not(event.isAutoRepeat()) and self.Key_W==True:
                print("release W")
                self.stop()
                self.Key_W=False
        elif(event.key() == Qt.Key_A):
            if not(event.isAutoRepeat()) and self.Key_A==True:
                print("release A")
                self.stop()
                self.Key_A=False
        elif(event.key() == Qt.Key_S):
            if not(event.isAutoRepeat()) and self.Key_S==True:
                print("release S")
                self.stop()
                self.Key_S=False
        elif(event.key() == Qt.Key_D):
            if not(event.isAutoRepeat()) and self.Key_D==True:
                print("release D")
                self.stop()
                self.Key_D=False
        elif(event.key() == Qt.Key_Q):
            if not(event.isAutoRepeat()) and self.Key_Q==True:
                print("release Q")
                self.stop()
                self.Key_Q=False
        elif(event.key() == Qt.Key_E):
            if not(event.isAutoRepeat()) and self.Key_E==True:
                print("release E")
                self.stop()
                self.Key_E=False
                
        if(event.key() == Qt.Key_Space):
            if not(event.isAutoRepeat()) and self.Key_Space==True:
                print("release Space")
                self.buzzer()
                self.Key_Space=False

    def paintEvent(self,e):
        try:
            qp=QPainter()
            qp.begin(self)
            pen=QPen(Qt.white,2,Qt.SolidLine)
            qp.setPen(pen)
            qp.drawRect(485,35,200,200)
            pen=QPen(QColor(0,138,255),2,Qt.SolidLine)
            qp.setPen(pen)
            qp.drawLine(self.drawpoint[0],35,self.drawpoint[0],235)
            qp.drawLine(485,self.drawpoint[1],685,self.drawpoint[1])

            self.label_point.move(self.drawpoint[0] + 10, self.drawpoint[1] + 10)
            pitch = round((self.drawpoint[1] - 135) / 100.0 * 20)
            yaw = round((self.drawpoint[0] - 585) / 100.0 * 20)
            self.label_point.setText(str((yaw, pitch)))
            if pitch !=self.slider_pitch.value():
                self.slider_pitch.setValue(pitch)
            if yaw !=self.slider_yaw.value():
                self.slider_yaw.setValue(yaw)
            qp.end()
        except Exception as e:
            print(e)
        
    
    def mouseMoveEvent(self, event):
        x=event.pos().x()
        y=event.pos().y()
        if x > 485 and x < 685 and y > 35 and y < 235:
            try:
                self.drawpoint[0]=x
                self.drawpoint[1]=y
                self.update()
            except Exception as e:
                print(e)
        

    def mousePressEvent(self, event):
        x=event.pos().x()
        y=event.pos().y()
        if x > 485 and x < 685 and y > 35 and y < 235:
            try:
                self.drawpoint[0]=x
                self.drawpoint[1]=y
                self.update()
            except Exception as e:
                print(e)
    
    def closeEvent(self,event):
        try:
            self.time_out.stop()
            self.timer.stop()
            stop_thread(self.video)
            stop_thread(self.instruction)
        except Exception as e:
            print(e)
        self.client.turn_off_client()
        QCoreApplication.instance().quit()
        #os._exit(0)

    def video(self):
        if self.Button_Video.text() == 'Open Video':
            self.timer.start(34)
            self.Button_Video.setText('Close Video')
        else:
            self.timer.stop()
            self.Button_Video.setText('Open Video')
    def receive_instruction(self,ip):
        try:
            self.client.client_socket1.connect((ip,5001))
            self.client.tcp_flag=True
            print ("Connecttion Successful !")
        except Exception as e:
            print ("Connect to server Faild!: Server IP is right? Server is opend?")
            self.client.tcp_flag=False
        while True:
            try:
                alldata=self.client.receive_data()
            except:
                self.client.tcp_flag=False
                break
            #print(alldata)
            if alldata=='':
                break
            else:
                cmdArray=alldata.split('\n')
                #print(cmdArray)
                if cmdArray[-1] !="":
                    cmdArray==cmdArray[:-1]
            for oneCmd in cmdArray:
                data=oneCmd.split("#")
                #print(data)
                if data=="":
                    self.client.tcp_flag=False
                    break
                elif data[0]==cmd.CMD_SONIC:
                    self.label_sonic.setText('Obstacle:'+data[1]+'cm')
                    #print('Obstacle:',data[1])
                elif data[0]==cmd.CMD_POWER:
                    if data[1]!="":
                        power_value=round((float(data[1]) - 7.00) / 1.40 * 100)
                        self.progress_Power.setValue(power_value)
                elif data[0]==cmd.CMD_RELAX:
                    if data[1]=="0":
                        self.Button_Relax.setText('Relax')
                    else:
                        self.Button_Relax.setText('"Too tired..."')


    def refresh_image(self):
        if self.client.video_flag == False:
            height, width, bytesPerComponent=self.client.image.shape
            #print (height, width, bytesPerComponent)
            cv2.cvtColor(self.client.image, cv2.COLOR_BGR2RGB, self.client.image)
            QImg = QImage(self.client.image.data, width, height, 3 * width, QImage.Format_RGB888)
            self.Video.setPixmap(QPixmap.fromImage(QImg))
            self.client.video_flag = True
    #BALL
    def chase_ball_and_find_face(self):
        if self.Button_Ball_And_Face.text() == 'Face':
            self.client.face_flag=True
            self.client.ball_flag = False
            self.Button_Ball_And_Face.setText('Ball')
        elif self.Button_Ball_And_Face.text() == 'Ball':
            self.client.face_flag=False
            self.client.ball_flag = True
            self.Button_Ball_And_Face.setText('Close')
        else:
            self.client.face_flag = False
            self.client.ball_flag = False
            self.stop()
            self.Button_Ball_And_Face.setText('Face')

    #CONNECT
    def connect(self):
        file=open('IP.txt','w')
        file.write(self.lineEdit_IP_Adress.text())
        file.close()
        if self.Button_Connect.text()=='Connect':
            self.IP = self.lineEdit_IP_Adress.text()
            self.client.turn_on_client(self.IP)
            self.video=threading.Thread(target=self.client.receiving_video,args=(self.IP,))
            self.instruction=threading.Thread(target=self.receive_instruction,args=(self.IP,))
            self.video.start() 
            self.instruction.start()
            self.Button_Connect.setText('Disconnect')
            self.time_out.start(1000)
        else:
            try:
                stop_thread(self.video)
            except:
                pass
            try:
                stop_thread(self.instruction)
            except:
                pass
            self.client.tcp_flag=False
            self.client.turn_off_client()
            self.Button_Connect.setText('Connect')
            self.time_out.stop()

    def stand(self):
        self.Button_IMU.setText('Balance')
        self.slider_roll.setValue(0)
        self.slider_pitch.setValue(0)
        self.slider_yaw.setValue(0)
        self.slider_horizon.setValue(0)

    #MOVE
    def stop(self):
        command=cmd.CMD_MOVE_STOP+"#"+str(self.slider_speed.value())+'\n'
        self.client.send_data(command)
        #print (command)
        
    def forward(self):
        self.stand()
        command=cmd.CMD_MOVE_FORWARD+"#"+str(self.slider_speed.value())+'\n'
        self.client.send_data(command)
        #print (command)

    def backward(self):
        self.stand()
        command=cmd.CMD_MOVE_BACKWARD+"#"+str(self.slider_speed.value())+'\n'
        self.client.send_data(command)
        #print (command)
        
    def step_left(self):
        self.stand()
        command=cmd.CMD_MOVE_LEFT+"#"+str(self.slider_speed.value())+'\n'
        self.client.send_data(command)
        #print (command)

    def step_right(self):
        self.stand()
        command=cmd.CMD_MOVE_RIGHT+"#"+str(self.slider_speed.value())+'\n'
        self.client.send_data(command)
        #print (command)
        
    def left(self):
        self.stand()
        command=cmd.CMD_TURN_LEFT+"#"+str(self.slider_speed.value())+'\n'
        self.client.send_data(command)
        #print (command)

    def right(self):
        self.stand()
        command=cmd.CMD_TURN_RIGHT+"#"+str(self.slider_speed.value())+'\n'
        self.client.send_data(command)
        #print (command)

    def speed(self):
        self.client.move_speed=str(self.slider_speed.value())
        self.label_speed.setText(str(self.slider_speed.value()))

    #relax
    def relax(self):
        if self.Button_Relax.text() == 'Relax':
            command=cmd.CMD_RELAX+'\n'
            self.client.send_data(command)
            #print (command)
        else:
            pass
    #BUZZER
    def buzzer(self):
        if self.Button_Buzzer.text() == 'Buzzer':
            command=cmd.CMD_BUZZER+'#1'+'\n'
            self.client.send_data(command)
            self.Button_Buzzer.setText('Noise')
            #print (command)
        else:
            command=cmd.CMD_BUZZER+'#0'+'\n'
            self.client.send_data(command)
            self.Button_Buzzer.setText('Buzzer')
            #print (command)
            
    #BALANCE
    def imu(self):
        if self.Button_IMU.text()=='Balance':
            command=cmd.CMD_BALANCE+'#1'+'\n'
            self.client.send_data(command)
            self.Button_IMU.setText("Close")
            #print (command)
        else:
            command=cmd.CMD_BALANCE+'#0'+'\n'
            self.client.send_data(command)
            self.Button_IMU.setText('Balance')
            #print (command)


    #SNOIC
    def sonic(self):
        if self.Button_Sonic.text() == 'Sonic':
            command=cmd.CMD_SONIC+'#1'+'\n'
            self.client.send_data(command)
            self.Button_Sonic.setText('Close')
            #print (command)
        else:
            command=cmd.CMD_SONIC+'#0'+'\n'
            self.client.send_data(command)
            self.Button_Sonic.setText('Sonic')
            #print (command)

    #HEIGHT
    def height(self):
        try:
            hei=str(self.slider_height.value())
            self.label_height.setText(hei)
            command=cmd.CMD_HEIGHT+"#"+hei+'\n'
            self.client.send_data(command)
            #print(command)
        except Exception as e:
            print(e)

    #HORIZON
    def horizon(self):
        try:
            hor=str(self.slider_horizon.value())
            self.label_horizon.setText(hor)
            command=cmd.CMD_HORIZON+"#"+hor+'\n'
            self.client.send_data(command)
            #print(command)
        except Exception as e:
            print(e)

    #HEAD
    def head(self):
        try:
            angle=str(self.slider_head.value())
            self.label_head.setText(angle)
            command=cmd.CMD_HEAD+"#"+angle+'\n'
            self.client.send_data(command)
            #print(command)
        except Exception as e:
            print(e)

    #POWER
    def power(self):
        try:
            command=cmd.CMD_POWER+'\n'
            self.client.send_data(command)
            #print (command)
        except Exception as e:
            print(e)

    #ATTITUDE        
    def attitude(self,target1,target2):
        try:
            r=str(self.slider_roll.value())
            p=str(self.slider_pitch.value())
            y=str(self.slider_yaw.value())
            target1.setText(str(target2.value()))
            self.drawpoint[0]=585+self.slider_yaw.value()*5
            self.drawpoint[1]=135+self.slider_pitch.value()*5
            self.update()
            command=cmd.CMD_ATTITUDE+'#'+r+'#'+p+'#'+y+'\n'
            self.client.send_data(command)
            #print(command)

        except Exception as e:
            print(e)
        
    def showCalibrationWindow(self):
        self.stop()
        self.calibrationWindow=calibrationWindow(self.client)
        self.calibrationWindow.setWindowModality(Qt.ApplicationModal)
        self.calibrationWindow.show()

        #LED
    def showLedWindow(self):
        try:
            self.ledWindow=ledWindow(self.client)
            self.ledWindow.setWindowModality(Qt.ApplicationModal)
            self.ledWindow.show()
        except Exception as e:
            print(e)


class calibrationWindow(QMainWindow,Ui_calibration):
    def __init__(self,client):
        super(calibrationWindow,self).__init__()
        self.setupUi(self)
        self.setWindowIcon(QIcon('Picture/logo_Mini.png'))
        self.label_picture.setScaledContents (True)
        self.label_picture.setPixmap(QPixmap('Picture/dog_calibration.png'))
        self.point=self.Read_from_txt('point')
        self.set_point(self.point)
        self.client=client
        self.leg='one'
        self.x=0
        self.y=0
        self.z=0
        self.radioButton_one.setChecked(True)
        self.radioButton_one.toggled.connect(lambda: self.leg_point(self.radioButton_one))
        self.radioButton_two.setChecked(False)
        self.radioButton_two.toggled.connect(lambda: self.leg_point(self.radioButton_two))
        self.radioButton_three.setChecked(False)
        self.radioButton_three.toggled.connect(lambda: self.leg_point(self.radioButton_three))
        self.radioButton_four.setChecked(False)
        self.radioButton_four.toggled.connect(lambda: self.leg_point(self.radioButton_four))
        self.Button_Save.clicked.connect(self.save)
        self.Button_X1.clicked.connect(self.X1)
        self.Button_X2.clicked.connect(self.X2)
        self.Button_Y1.clicked.connect(self.Y1)
        self.Button_Y2.clicked.connect(self.Y2)
        self.Button_Z1.clicked.connect(self.Z1)
        self.Button_Z2.clicked.connect(self.Z2)
    def X1(self):
        self.get_point()
        self.x +=1
        command=cmd.CMD_CALIBRATION+'#'+self.leg+'#'+str(self.x)+'#'+str(self.y)+'#'+str(self.z)+'\n'
        self.client.send_data(command)
        #print(command)
        self.set_point()
    def X2(self):
        self.get_point()
        self.x -= 1
        command=cmd.CMD_CALIBRATION+'#'+self.leg+'#'+str(self.x)+'#'+str(self.y)+'#'+str(self.z)+'\n'
        self.client.send_data(command)
        #print(command)
        self.set_point()
    def Y1(self):
        self.get_point()
        self.y += 1
        command=cmd.CMD_CALIBRATION+'#'+self.leg+'#'+str(self.x)+'#'+str(self.y)+'#'+str(self.z)+'\n'
        self.client.send_data(command)
        #print(command)
        self.set_point()
    def Y2(self):
        self.get_point()
        self.y -= 1
        command=cmd.CMD_CALIBRATION+'#'+self.leg+'#'+str(self.x)+'#'+str(self.y)+'#'+str(self.z)+'\n'
        self.client.send_data(command)
        #print(command)
        self.set_point()
    def Z1(self):
        self.get_point()
        self.z += 1
        command=cmd.CMD_CALIBRATION+'#'+self.leg+'#'+str(self.x)+'#'+str(self.y)+'#'+str(self.z)+'\n'
        self.client.send_data(command)
        #print(command)
        self.set_point()
    def Z2(self):
        self.get_point()
        self.z -= 1
        command=cmd.CMD_CALIBRATION+'#'+self.leg+'#'+str(self.x)+'#'+str(self.y)+'#'+str(self.z)+'\n'
        self.client.send_data(command)
        #print(command)
        self.set_point()
    def set_point(self,data=None):
        if data==None:
            if self.leg== "one":
                self.one_x.setText(str(self.x))
                self.one_y.setText(str(self.y))
                self.one_z.setText(str(self.z))
                self.point[0][0]=self.x
                self.point[0][1]=self.y
                self.point[0][2]=self.z
            elif self.leg== "two":
                self.two_x.setText(str(self.x))
                self.two_y.setText(str(self.y))
                self.two_z.setText(str(self.z))
                self.point[1][0]=self.x
                self.point[1][1]=self.y
                self.point[1][2]=self.z
            elif self.leg== "three":
                self.three_x.setText(str(self.x))
                self.three_y.setText(str(self.y))
                self.three_z.setText(str(self.z))
                self.point[2][0]=self.x
                self.point[2][1]=self.y
                self.point[2][2]=self.z
            elif self.leg== "four":
                self.four_x.setText(str(self.x))
                self.four_y.setText(str(self.y))
                self.four_z.setText(str(self.z))
                self.point[3][0]=self.x
                self.point[3][1]=self.y
                self.point[3][2]=self.z
        else:
            self.one_x.setText(str(data[0][0]))
            self.one_y.setText(str(data[0][1]))
            self.one_z.setText(str(data[0][2]))
            self.two_x.setText(str(data[1][0]))
            self.two_y.setText(str(data[1][1]))
            self.two_z.setText(str(data[1][2]))
            self.three_x.setText(str(data[2][0]))
            self.three_y.setText(str(data[2][1]))
            self.three_z.setText(str(data[2][2]))
            self.four_x.setText(str(data[3][0]))
            self.four_y.setText(str(data[3][1]))
            self.four_z.setText(str(data[3][2]))
    def get_point(self):
        if self.leg== "one":
            self.x = int(self.one_x.text())
            self.y = int(self.one_y.text())
            self.z = int(self.one_z.text())
        elif self.leg== "two":
            self.x = int(self.two_x.text())
            self.y = int(self.two_y.text())
            self.z = int(self.two_z.text())
        elif self.leg== "three":
            self.x = int(self.three_x.text())
            self.y = int(self.three_y.text())
            self.z = int(self.three_z.text())
        elif self.leg== "four":
            self.x = int(self.four_x.text())
            self.y = int(self.four_y.text())
            self.z = int(self.four_z.text())
    def save(self):
        command=cmd.CMD_CALIBRATION+'#'+'save'+'\n'
        self.client.send_data(command)

        self.point[0][0] = self.one_x.text()
        self.point[0][1] = self.one_y.text()
        self.point[0][2] = self.one_z.text()

        self.point[1][0] = self.two_x.text()
        self.point[1][1] = self.two_y.text()
        self.point[1][2] = self.two_z.text()

        self.point[2][0] = self.three_x.text()
        self.point[2][1] = self.three_y.text()
        self.point[2][2] = self.three_z.text()

        self.point[3][0] = self.four_x.text()
        self.point[3][1] = self.four_y.text()
        self.point[3][2] = self.four_z.text()

        self.Save_to_txt(self.point,'point')
        reply = QMessageBox.information(self,                        
                                        "Message",  
                                        "Saved successfully",  
                                        QMessageBox.Yes)
        #print(command)
    def Read_from_txt(self,filename):
        file1 = open(filename + ".txt", "r")
        list_row = file1.readlines()
        list_source = []
        for i in range(len(list_row)):
            column_list = list_row[i].strip().split("\t")
            list_source.append(column_list)
        for i in range(len(list_source)):
            for j in range(len(list_source[i])):
                list_source[i][j] = int(list_source[i][j])
        file1.close()
        return list_source

    def Save_to_txt(self,list, filename):
        file2 = open(filename + '.txt', 'w')
        for i in range(len(list)):
            for j in range(len(list[i])):
                file2.write(str(list[i][j]))
                file2.write('\t')
            file2.write('\n')
        file2.close()
        
    def leg_point(self,leg):
        if leg.text() == "One":
            if leg.isChecked() == True:
                self.leg = "one"
        elif leg.text() == "Two":
            if leg.isChecked() == True:
                self.leg = "two"
        elif leg.text() == "Three":
            if leg.isChecked() == True:
                self.leg = "three"
        elif leg.text() == "Four":
            if leg.isChecked() == True:
                self.leg = "four"


class ColorDialog(QtWidgets.QColorDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setOptions(self.options() | QtWidgets.QColorDialog.DontUseNativeDialog)
        for children in self.findChildren(QtWidgets.QWidget):
            classname = children.metaObject().className()
            if classname not in ("QColorPicker", "QColorLuminancePicker"):
                children.hide()
class ledWindow(QMainWindow,Ui_led):
    def __init__(self,client):
        super(ledWindow,self).__init__()
        self.setupUi(self)
        self.client = client
        self.setWindowIcon(QIcon('Picture/logo_Mini.png'))
        self.hsl = [0, 0, 1]
        self.rgb = [0, 0, 0]
        self.dial_color.setRange(0, 360)
        self.dial_color.setNotchesVisible(True)
        self.dial_color.setWrapping(True)
        self.dial_color.setPageStep(10)
        self.dial_color.setNotchTarget(10)
        self.dial_color.valueChanged.connect(self.dialValueChanged)
        composite_2f = lambda f, g: lambda t: g(f(t))
        self.hsl_to_rgb255 = composite_2f(self.hsl_to_rgb01, self.rgb01_to_rgb255)
        self.hsl_to_rgbhex = composite_2f(self.hsl_to_rgb255, self.rgb255_to_rgbhex)
        self.rgb255_to_hsl = composite_2f(self.rgb255_to_rgb01, self.rgb01_to_hsl)
        self.rgbhex_to_hsl = composite_2f(self.rgbhex_to_rgb255, self.rgb255_to_hsl)
        self.colordialog = ColorDialog()
        self.colordialog.currentColorChanged.connect(self.onCurrentColorChanged)
        lay = QtWidgets.QVBoxLayout(self.widget)
        lay.addWidget(self.colordialog, alignment=QtCore.Qt.AlignCenter)

        self.pushButtonLightsOut.clicked.connect(self.turnOff)
        self.radioButtonOne.setChecked(True)
        self.radioButtonOne.toggled.connect(lambda: self.ledMode(self.radioButtonOne))
        self.radioButtonTwo.setChecked(False)
        self.radioButtonTwo.toggled.connect(lambda: self.ledMode(self.radioButtonTwo))
        self.radioButtonThree.setChecked(False)
        self.radioButtonThree.toggled.connect(lambda: self.ledMode(self.radioButtonThree))
        self.radioButtonFour.setChecked(False)
        self.radioButtonFour.toggled.connect(lambda: self.ledMode(self.radioButtonFour))
        self.radioButtonFive.setChecked(False)
        self.radioButtonFive.toggled.connect(lambda: self.ledMode(self.radioButtonFive))

    def turnOff(self):
        command = cmd.CMD_LED_MOD + '#' + '0' + '\n'
        self.client.send_data(command)
        #print(command)
    def ledMode(self,index):
        if index.text() == "Mode 1":
            if index.isChecked() == True:
                command = cmd.CMD_LED_MOD + '#' + '1' + '\n'
                self.client.send_data(command)
                #print(command)
        elif index.text() == "Mode 2":
            if index.isChecked() == True:
                command = cmd.CMD_LED_MOD + '#' + '2' + '\n'
                self.client.send_data(command)
                #print(command)
        elif index.text() == "Mode 3":
            if index.isChecked() == True:
                command = cmd.CMD_LED_MOD + '#' + '3' + '\n'
                self.client.send_data(command)
                #print(command)
        elif index.text() == "Mode 4":
            if index.isChecked() == True:
                command = cmd.CMD_LED_MOD + '#' + '4' + '\n'
                self.client.send_data(command)
                #print(command)
        elif index.text() == "Mode 5":
            if index.isChecked() == True:
                command = cmd.CMD_LED_MOD + '#' + '5' + '\n'
                self.client.send_data(command)
                #print(command)
    def mode1Color(self):
        if (self.radioButtonOne.isChecked() == True) or (self.radioButtonThree.isChecked() == True):
            command = cmd.CMD_LED + '#' + '255' + '#' + str(self.rgb[0]) + '#' + str(self.rgb[1]) + '#' + str(self.rgb[2]) + '\n'
            self.client.send_data(command)
            #print(command)
    def onCurrentColorChanged(self, color):
        try:
            self.rgb = self.rgbhex_to_rgb255(color.name())
            self.hsl = self.rgb255_to_hsl(self.rgb)
            self.changeHSLText()
            self.changeRGBText()
            #print(color.name(), self.rgb, self.hsl)
            self.mode1Color()
            self.update()
        except Exception as e:
            print(e)

    def paintEvent(self, e):
        try:
            qp = QPainter()
            qp.begin(self)
            brush = QBrush(QColor(self.rgb[0], self.rgb[1], self.rgb[2]))
            qp.setBrush(brush)
            qp.drawRect(20, 10, 80, 30)
            qp.end()
        except Exception as e:
            print(e)

    def dialValueChanged(self):
        try:
            self.lineEdit_H.setText(str(self.dial_color.value()))
            self.changeHSL()
            self.hex = self.hsl_to_rgbhex((self.hsl[0], self.hsl[1], self.hsl[2]))
            self.rgb = self.rgbhex_to_rgb255(self.hex)
            self.changeRGBText()
            #print(self.rgb, self.hsl)
            self.mode1Color()
            self.update()
        except Exception as e:
            print(e)

    def changeHSL(self):
        self.hsl[0] = float(self.lineEdit_H.text())
        self.hsl[1] = float(self.lineEdit_S.text())
        self.hsl[2] = float(self.lineEdit_L.text())

    def changeHSLText(self):
        self.lineEdit_H.setText(str(int(self.hsl[0])))
        self.lineEdit_S.setText(str(round(self.hsl[1], 1)))
        self.lineEdit_L.setText(str(round(self.hsl[2], 1)))

    def changeRGBText(self):
        self.lineEdit_R.setText(str(self.rgb[0]))
        self.lineEdit_G.setText(str(self.rgb[1]))
        self.lineEdit_B.setText(str(self.rgb[2]))

    def rgb255_to_rgbhex(self, rgb: np.array) -> str:
        f = lambda n: 0 if n < 0 else 255 if n > 255 else int(n)
        return '#%02x%02x%02x' % (f(rgb[0]), f(rgb[1]), f(rgb[2]))

    def rgbhex_to_rgb255(self, rgbhex: str) -> np.array:
        if rgbhex[0] == '#':
            rgbhex = rgbhex[1:]
        r = int(rgbhex[0:2], 16)
        g = int(rgbhex[2:4], 16)
        b = int(rgbhex[4:6], 16)
        return np.array((r, g, b))

    def rgb01_to_rgb255(self, rgb: np.array) -> np.array:
        return rgb * 255

    def rgb255_to_rgb01(self, rgb: np.array) -> np.array:
        return rgb / 255

    def rgb01_to_hsl(self, rgb: np.array) -> np.array:
        r, g, b = rgb
        lmin = min(r, g, b)
        lmax = max(r, g, b)
        if lmax == lmin:
            h = 0
        elif lmin == b:
            h = 60 + 60 * (g - r) / (lmax - lmin)
        elif lmin == r:
            h = 180 + 60 * (b - g) / (lmax - lmin)
        elif lmin == g:
            h = 300 + 60 * (r - b) / (lmax - lmin)
        else:
            h = 0
        s = lmax - lmin
        l = (lmax + lmin) / 2
        hsl = np.array((h, s, l))
        return hsl

    def hsl_to_rgb01(self, hsl: np.array) -> np.array:
        h, s, l = hsl
        lmin = l - s / 2
        lmax = l + s / 2
        ldif = lmax - lmin
        if h < 60:
            r, g, b = lmax, lmin + ldif * (0 + h) / 60, lmin
        elif h < 120:
            r, g, b = lmin + ldif * (120 - h) / 60, lmax, lmin
        elif h < 180:
            r, g, b = lmin, lmax, lmin + ldif * (h - 120) / 60
        elif h < 240:
            r, g, b = lmin, lmin + ldif * (240 - h) / 60, lmax
        elif h < 300:
            r, g, b = lmin + ldif * (h - 240) / 60, lmin, lmax
        else:
            r, g, b = lmax, lmin, lmin + ldif * (360 - h) / 60
        rgb = np.array((r, g, b))
        return rgb

if __name__ == '__main__':
    app = QApplication(sys.argv)
    myshow=MyWindow()
    myshow.show()
    sys.exit(app.exec_())
