# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_client(object):
    def setupUi(self, client):
        client.setObjectName("client")
        client.resize(769, 551)
        font = QtGui.QFont()
        font.setFamily("Arial")
        client.setFont(font)
        client.setStyleSheet("QWidget{\n"
"background:#484848;\n"
"}\n"
"QAbstractButton{\n"
"border-style:none;\n"
"border-radius:0px;\n"
"padding:5px;\n"
"color:#DCDCDC;\n"
"background:qlineargradient(spread:pad,x1:0,y1:0,x2:0,y2:1,stop:0 #858585,stop:1 #383838);\n"
"}\n"
"QAbstractButton:hover{\n"
"color:#000000;\n"
"background-color:#008aff;\n"
"}\n"
"QAbstractButton:pressed{\n"
"color:#DCDCDC;\n"
"border-style:solid;\n"
"border-width:0px 0px 0px 4px;\n"
"padding:4px 4px 4px 2px;\n"
"border-color:#008aff;\n"
"background-color:#444444;\n"
"}\n"
"\n"
"QLabel{\n"
"color:#DCDCDC;\n"
"\n"
"\n"
"}\n"
"QLabel:focus{\n"
"border:1px solid #00BB9E;\n"
"\n"
"}\n"
"\n"
"QLineEdit{\n"
"border:1px solid #242424;\n"
"border-radius:3px;\n"
"padding:2px;\n"
"background:none;\n"
"selection-background-color:#484848;\n"
"selection-color:#DCDCDC;\n"
"}\n"
"QLineEdit:focus,QLineEdit:hover{\n"
"border:1px solid #242424;\n"
"}\n"
"QLineEdit{\n"
"border:1px solid #242424;\n"
"border-radius:3px;\n"
"padding:2px;\n"
"background:none;\n"
"selection-background-color:#484848;\n"
"selection-color:#DCDCDC;\n"
"}\n"
"\n"
"QLineEdit:focus,QLineEdit:hover{\n"
"border:1px solid #242424;\n"
"}\n"
"QLineEdit{\n"
"lineedit-password-character:9679;\n"
"}\n"
"QSlider::groove:horizontal,QSlider::add-page:horizontal{\n"
"height:3px;\n"
"border-radius:3px;\n"
"background:#18181a;\n"
"}\n"
"\n"
"\n"
"QSlider::sub-page:horizontal{\n"
"height:8px;\n"
"border-radius:3px;\n"
"background:#008aff;\n"
"}\n"
"\n"
"\n"
"QSlider::handle:horizontal{\n"
"width:12px;\n"
"margin-top:-5px;\n"
"margin-bottom:-4px;\n"
"border-radius:6px;\n"
"background:qradialgradient(spread:pad,cx:0.5,cy:0.5,radius:0.5,fx:0.5,fy:0.5,stop:0.6 #DCDCDC,stop:0.8 #DCDCDC);\n"
"}\n"
"QSlider::groove:vertical,QSlider::sub-page:vertical{\n"
"width:3px;\n"
"border-radius:3px;\n"
"background:#18181a;\n"
"}\n"
"\n"
"\n"
"QSlider::add-page:vertical{\n"
"width:8px;\n"
"border-radius:3px;\n"
"background:#008aff;\n"
"}\n"
"\n"
"\n"
"QSlider::handle:vertical{\n"
"height:12px;\n"
"margin-left:-5px;\n"
"margin-right:-4px;\n"
"border-radius:6px;\n"
"background:qradialgradient(spread:pad,cx:0.5,cy:0.5,radius:0.5,fx:0.5,fy:0.5,stop:0.6 #DCDCDC,stop:0.8 #DCDCDC);\n"
"}\n"
"\n"
"QProgressBar {\n"
"border: 2px solid grey;\n"
"border-radius: 5px;\n"
"background-color: #FFFFFF;\n"
"}\n"
"QProgressBar::chunk {\n"
"background-color:#26fa03;\n"
"width: 20px;\n"
"}\n"
"QProgressBar {\n"
"text-align: center; \n"
"color: rgb(0,0,0);\n"
"}\n"
"\n"
"QGroupBox::title {\n"
"pading:2px;\n"
"color:white;\n"
"subcontrol-position: top center;\n"
"border-top:0px ;\n"
"background:  transparent;} ")
        client.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.Video = QtWidgets.QLabel(client)
        self.Video.setGeometry(QtCore.QRect(5, 10, 400, 300))
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.Video.setFont(font)
        self.Video.setStyleSheet("font: 10pt \"Arial\";")
        self.Video.setText("")
        self.Video.setObjectName("Video")
        self.Button_Left = QtWidgets.QPushButton(client)
        self.Button_Left.setGeometry(QtCore.QRect(45, 490, 90, 30))
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.Button_Left.setFont(font)
        self.Button_Left.setStyleSheet("font: 10pt \"Arial\";")
        self.Button_Left.setObjectName("Button_Left")
        self.Button_ForWard = QtWidgets.QPushButton(client)
        self.Button_ForWard.setGeometry(QtCore.QRect(155, 430, 90, 30))
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.Button_ForWard.setFont(font)
        self.Button_ForWard.setStyleSheet("font: 10pt \"Arial\";")
        self.Button_ForWard.setObjectName("Button_ForWard")
        self.Button_Right = QtWidgets.QPushButton(client)
        self.Button_Right.setGeometry(QtCore.QRect(265, 490, 90, 30))
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.Button_Right.setFont(font)
        self.Button_Right.setStyleSheet("font: 10pt \"Arial\";")
        self.Button_Right.setObjectName("Button_Right")
        self.Button_BackWard = QtWidgets.QPushButton(client)
        self.Button_BackWard.setGeometry(QtCore.QRect(155, 510, 90, 30))
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.Button_BackWard.setFont(font)
        self.Button_BackWard.setStyleSheet("font: 10pt \"Arial\";")
        self.Button_BackWard.setObjectName("Button_BackWard")
        self.Button_Buzzer = QtWidgets.QPushButton(client)
        self.Button_Buzzer.setGeometry(QtCore.QRect(155, 470, 90, 30))
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.Button_Buzzer.setFont(font)
        self.Button_Buzzer.setStyleSheet("font: 10pt \"Arial\";")
        self.Button_Buzzer.setObjectName("Button_Buzzer")
        self.lineEdit_IP_Adress = QtWidgets.QLineEdit(client)
        self.lineEdit_IP_Adress.setGeometry(QtCore.QRect(230, 330, 130, 20))
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.lineEdit_IP_Adress.setFont(font)
        self.lineEdit_IP_Adress.setStyleSheet("font: 10pt \"Arial\";")
        self.lineEdit_IP_Adress.setObjectName("lineEdit_IP_Adress")
        self.Button_Step_Left = QtWidgets.QPushButton(client)
        self.Button_Step_Left.setGeometry(QtCore.QRect(45, 450, 90, 30))
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.Button_Step_Left.setFont(font)
        self.Button_Step_Left.setStyleSheet("font: 10pt \"Arial\";")
        self.Button_Step_Left.setObjectName("Button_Step_Left")
        self.Button_Step_Right = QtWidgets.QPushButton(client)
        self.Button_Step_Right.setGeometry(QtCore.QRect(265, 450, 90, 30))
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.Button_Step_Right.setFont(font)
        self.Button_Step_Right.setStyleSheet("font: 10pt \"Arial\";")
        self.Button_Step_Right.setObjectName("Button_Step_Right")
        self.Button_Connect = QtWidgets.QPushButton(client)
        self.Button_Connect.setGeometry(QtCore.QRect(265, 380, 90, 30))
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.Button_Connect.setFont(font)
        self.Button_Connect.setStyleSheet("font: 10pt \"Arial\";")
        self.Button_Connect.setObjectName("Button_Connect")
        self.Button_Video = QtWidgets.QPushButton(client)
        self.Button_Video.setGeometry(QtCore.QRect(155, 380, 90, 30))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setBold(False)
        font.setWeight(50)
        self.Button_Video.setFont(font)
        self.Button_Video.setStyleSheet("font: 10pt \"Arial\";")
        self.Button_Video.setObjectName("Button_Video")
        self.Button_IMU = QtWidgets.QPushButton(client)
        self.Button_IMU.setGeometry(QtCore.QRect(670, 510, 90, 30))
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.Button_IMU.setFont(font)
        self.Button_IMU.setStyleSheet("font: 10pt \"Arial\";")
        self.Button_IMU.setObjectName("Button_IMU")
        self.slider_height = QtWidgets.QSlider(client)
        self.slider_height.setGeometry(QtCore.QRect(500, 390, 160, 22))
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.slider_height.setFont(font)
        self.slider_height.setStyleSheet("font: 10pt \"Arial\";")
        self.slider_height.setOrientation(QtCore.Qt.Horizontal)
        self.slider_height.setObjectName("slider_height")
        self.slider_horizon = QtWidgets.QSlider(client)
        self.slider_horizon.setGeometry(QtCore.QRect(500, 360, 160, 22))
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.slider_horizon.setFont(font)
        self.slider_horizon.setStyleSheet("font: 10pt \"Arial\";")
        self.slider_horizon.setOrientation(QtCore.Qt.Horizontal)
        self.slider_horizon.setObjectName("slider_horizon")
        self.label_2 = QtWidgets.QLabel(client)
        self.label_2.setGeometry(QtCore.QRect(700, 390, 50, 20))
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("font: 10pt \"Arial\";")
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(client)
        self.label_3.setGeometry(QtCore.QRect(700, 360, 60, 20))
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("font: 10pt \"Arial\";")
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.label_height = QtWidgets.QLabel(client)
        self.label_height.setGeometry(QtCore.QRect(450, 390, 30, 20))
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.label_height.setFont(font)
        self.label_height.setStyleSheet("font: 10pt \"Arial\";")
        self.label_height.setObjectName("label_height")
        self.label_horizon = QtWidgets.QLabel(client)
        self.label_horizon.setGeometry(QtCore.QRect(450, 360, 30, 20))
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.label_horizon.setFont(font)
        self.label_horizon.setStyleSheet("font: 10pt \"Arial\";")
        self.label_horizon.setObjectName("label_horizon")
        self.Button_Calibration = QtWidgets.QPushButton(client)
        self.Button_Calibration.setGeometry(QtCore.QRect(45, 380, 90, 30))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setBold(False)
        font.setWeight(50)
        self.Button_Calibration.setFont(font)
        self.Button_Calibration.setStyleSheet("font: 10pt \"Arial\";")
        self.Button_Calibration.setObjectName("Button_Calibration")
        self.Button_Ball_And_Face = QtWidgets.QPushButton(client)
        self.Button_Ball_And_Face.setGeometry(QtCore.QRect(670, 470, 90, 30))
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.Button_Ball_And_Face.setFont(font)
        self.Button_Ball_And_Face.setStyleSheet("font: 10pt \"Arial\";")
        self.Button_Ball_And_Face.setObjectName("Button_Ball_And_Face")
        self.Button_Sonic = QtWidgets.QPushButton(client)
        self.Button_Sonic.setGeometry(QtCore.QRect(555, 510, 90, 30))
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.Button_Sonic.setFont(font)
        self.Button_Sonic.setStyleSheet("font: 10pt \"Arial\";")
        self.Button_Sonic.setObjectName("Button_Sonic")
        self.Button_Face_ID = QtWidgets.QPushButton(client)
        self.Button_Face_ID.setGeometry(QtCore.QRect(555, 470, 90, 30))
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.Button_Face_ID.setFont(font)
        self.Button_Face_ID.setStyleSheet("font: 10pt \"Arial\";")
        self.Button_Face_ID.setObjectName("Button_Sonic")
        self.Button_LED = QtWidgets.QPushButton(client)
        self.Button_LED.setGeometry(QtCore.QRect(440, 510, 90, 30))
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.Button_LED.setFont(font)
        self.Button_LED.setStyleSheet("font: 10pt \"Arial\";")
        self.Button_LED.setObjectName("Button_LED")
        self.label_speed = QtWidgets.QLabel(client)
        self.label_speed.setGeometry(QtCore.QRect(385, 520, 35, 20))
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.label_speed.setFont(font)
        self.label_speed.setStyleSheet("font: 10pt \"Arial\";")
        self.label_speed.setAlignment(QtCore.Qt.AlignCenter)
        self.label_speed.setObjectName("label_speed")
        self.slider_speed = QtWidgets.QSlider(client)
        self.slider_speed.setGeometry(QtCore.QRect(390, 380, 22, 125))
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.slider_speed.setFont(font)
        self.slider_speed.setStyleSheet("font: 10pt \"Arial\";")
        self.slider_speed.setOrientation(QtCore.Qt.Vertical)
        self.slider_speed.setObjectName("slider_speed")
        self.label_7 = QtWidgets.QLabel(client)
        self.label_7.setGeometry(QtCore.QRect(375, 350, 50, 20))
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.label_7.setFont(font)
        self.label_7.setStyleSheet("font: 10pt \"Arial\";")
        self.label_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_7.setObjectName("label_7")
        self.slider_head = QtWidgets.QSlider(client)
        self.slider_head.setGeometry(QtCore.QRect(500, 420, 160, 22))
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.slider_head.setFont(font)
        self.slider_head.setStyleSheet("font: 10pt \"Arial\";")
        self.slider_head.setOrientation(QtCore.Qt.Horizontal)
        self.slider_head.setObjectName("slider_head")
        self.label_8 = QtWidgets.QLabel(client)
        self.label_8.setGeometry(QtCore.QRect(700, 420, 50, 20))
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.label_8.setFont(font)
        self.label_8.setStyleSheet("font: 10pt \"Arial\";")
        self.label_8.setAlignment(QtCore.Qt.AlignCenter)
        self.label_8.setObjectName("label_8")
        self.label_head = QtWidgets.QLabel(client)
        self.label_head.setGeometry(QtCore.QRect(450, 420, 30, 20))
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.label_head.setFont(font)
        self.label_head.setStyleSheet("font: 10pt \"Arial\";")
        self.label_head.setObjectName("label_head")
        self.progress_Power = QtWidgets.QProgressBar(client)
        self.progress_Power.setEnabled(False)
        self.progress_Power.setGeometry(QtCore.QRect(40, 330, 130, 20))
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.progress_Power.setFont(font)
        self.progress_Power.setStyleSheet("font: 10pt \"Arial\";")
        self.progress_Power.setProperty("value", 24)
        self.progress_Power.setObjectName("progress_Power")
        self.label_6 = QtWidgets.QLabel(client)
        self.label_6.setGeometry(QtCore.QRect(700, 270, 50, 20))
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.label_6.setFont(font)
        self.label_6.setStyleSheet("font: 10pt \"Arial\";")
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.label_5 = QtWidgets.QLabel(client)
        self.label_5.setGeometry(QtCore.QRect(700, 330, 50, 20))
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("font: 10pt \"Arial\";")
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.label_point = QtWidgets.QLabel(client)
        self.label_point.setGeometry(QtCore.QRect(595, 145, 60, 20))
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.label_point.setFont(font)
        self.label_point.setStyleSheet("font: 10pt \"Arial\";")
        self.label_point.setAlignment(QtCore.Qt.AlignCenter)
        self.label_point.setObjectName("label_point")
        self.slider_yaw = QtWidgets.QSlider(client)
        self.slider_yaw.setGeometry(QtCore.QRect(500, 330, 160, 22))
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.slider_yaw.setFont(font)
        self.slider_yaw.setStyleSheet("font: 10pt \"Arial\";")
        self.slider_yaw.setOrientation(QtCore.Qt.Horizontal)
        self.slider_yaw.setObjectName("slider_yaw")
        self.label_roll = QtWidgets.QLabel(client)
        self.label_roll.setGeometry(QtCore.QRect(450, 270, 30, 20))
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.label_roll.setFont(font)
        self.label_roll.setStyleSheet("font: 10pt \"Arial\";")
        self.label_roll.setObjectName("label_roll")
        self.label_4 = QtWidgets.QLabel(client)
        self.label_4.setGeometry(QtCore.QRect(700, 300, 50, 20))
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("font: 10pt \"Arial\";")
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.label_pitch = QtWidgets.QLabel(client)
        self.label_pitch.setGeometry(QtCore.QRect(450, 300, 30, 20))
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.label_pitch.setFont(font)
        self.label_pitch.setStyleSheet("font: 10pt \"Arial\";")
        self.label_pitch.setObjectName("label_pitch")
        self.slider_pitch = QtWidgets.QSlider(client)
        self.slider_pitch.setGeometry(QtCore.QRect(500, 300, 160, 22))
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.slider_pitch.setFont(font)
        self.slider_pitch.setStyleSheet("font: 10pt \"Arial\";")
        self.slider_pitch.setOrientation(QtCore.Qt.Horizontal)
        self.slider_pitch.setObjectName("slider_pitch")
        self.slider_roll = QtWidgets.QSlider(client)
        self.slider_roll.setGeometry(QtCore.QRect(500, 270, 160, 22))
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.slider_roll.setFont(font)
        self.slider_roll.setStyleSheet("font: 10pt \"Arial\";")
        self.slider_roll.setOrientation(QtCore.Qt.Horizontal)
        self.slider_roll.setObjectName("slider_roll")
        self.label_yaw = QtWidgets.QLabel(client)
        self.label_yaw.setGeometry(QtCore.QRect(450, 330, 30, 20))
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.label_yaw.setFont(font)
        self.label_yaw.setStyleSheet("font: 10pt \"Arial\";")
        self.label_yaw.setObjectName("label_yaw")
        self.label_Y = QtWidgets.QLabel(client)
        self.label_Y.setGeometry(QtCore.QRect(685, 236, 30, 20))
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.label_Y.setFont(font)
        self.label_Y.setStyleSheet("font: 10pt \"Arial\";")
        self.label_Y.setAlignment(QtCore.Qt.AlignCenter)
        self.label_Y.setObjectName("label_Y")
        self.label_Y_2 = QtWidgets.QLabel(client)
        self.label_Y_2.setGeometry(QtCore.QRect(570, 236, 30, 20))
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.label_Y_2.setFont(font)
        self.label_Y_2.setStyleSheet("font: 10pt \"Arial\";")
        self.label_Y_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_Y_2.setObjectName("label_Y_2")
        self.label_Y_3 = QtWidgets.QLabel(client)
        self.label_Y_3.setGeometry(QtCore.QRect(470, 236, 30, 20))
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.label_Y_3.setFont(font)
        self.label_Y_3.setStyleSheet("font: 10pt \"Arial\";")
        self.label_Y_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_Y_3.setObjectName("label_Y_3")
        self.label_Y_4 = QtWidgets.QLabel(client)
        self.label_Y_4.setGeometry(QtCore.QRect(720, 236, 40, 20))
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.label_Y_4.setFont(font)
        self.label_Y_4.setStyleSheet("font: 10pt \"Arial\";")
        self.label_Y_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_Y_4.setObjectName("label_Y_4")
        self.label_X = QtWidgets.QLabel(client)
        self.label_X.setGeometry(QtCore.QRect(454, 215, 30, 20))
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.label_X.setFont(font)
        self.label_X.setStyleSheet("font: 10pt \"Arial\";")
        self.label_X.setAlignment(QtCore.Qt.AlignCenter)
        self.label_X.setObjectName("label_X")
        self.label_X_2 = QtWidgets.QLabel(client)
        self.label_X_2.setGeometry(QtCore.QRect(454, 142, 30, 20))
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.label_X_2.setFont(font)
        self.label_X_2.setStyleSheet("font: 10pt \"Arial\";")
        self.label_X_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_X_2.setObjectName("label_X_2")
        self.label_X_3 = QtWidgets.QLabel(client)
        self.label_X_3.setGeometry(QtCore.QRect(454, 35, 30, 20))
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.label_X_3.setFont(font)
        self.label_X_3.setStyleSheet("font: 10pt \"Arial\";")
        self.label_X_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_X_3.setObjectName("label_X_3")
        self.label_X_4 = QtWidgets.QLabel(client)
        self.label_X_4.setGeometry(QtCore.QRect(430, 51, 50, 20))
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.label_X_4.setFont(font)
        self.label_X_4.setStyleSheet("font: 10pt \"Arial\";")
        self.label_X_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_X_4.setObjectName("label_X_4")
        self.label_X_5 = QtWidgets.QLabel(client)
        self.label_X_5.setGeometry(QtCore.QRect(520, 10, 130, 20))
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.label_X_5.setFont(font)
        self.label_X_5.setStyleSheet("font: 10pt \"Arial\";")
        self.label_X_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_X_5.setObjectName("label_X_5")
        '''
        self.label_sonic = QtWidgets.QLabel(client)
        self.label_sonic.setGeometry(QtCore.QRect(540, 470, 120, 30))
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.label_sonic.setFont(font)
        .setStyleSheet("font: 10pt \"Arial\";")
        self.label_sonic.setAlignment(QtCore.Qt.AlignCenter)
        self.label_sonic.setObjectName("label_sonic")
        '''
        self.Button_Relax = QtWidgets.QPushButton(client)
        self.Button_Relax.setGeometry(QtCore.QRect(440, 470, 90, 30))
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.Button_Relax.setFont(font)
        self.Button_Relax.setStyleSheet("font: 10pt \"Arial\";")
        self.Button_Relax.setObjectName("Button_Relax")
        self.retranslateUi(client)
        QtCore.QMetaObject.connectSlotsByName(client)

    def retranslateUi(self, client):
        _translate = QtCore.QCoreApplication.translate
        client.setWindowTitle(_translate("client", "Freenove Client for Smart Dog"))
        self.Button_Left.setText(_translate("client", "Turn Left"))
        self.Button_ForWard.setText(_translate("client", "ForWard"))
        self.Button_Right.setText(_translate("client", "Turn Right"))
        self.Button_BackWard.setText(_translate("client", "BackWard"))
        self.Button_Buzzer.setText(_translate("client", "Buzzer"))
        self.lineEdit_IP_Adress.setText(_translate("client", "0"))
        self.Button_Step_Left.setText(_translate("client", "Step Left"))
        self.Button_Step_Right.setText(_translate("client", "Step Right"))
        self.Button_Connect.setText(_translate("client", "Connect"))
        self.Button_Video.setText(_translate("client", "Open Video"))
        self.Button_IMU.setText(_translate("client", "Balance"))
        self.label_2.setText(_translate("client", "Height"))
        self.label_3.setText(_translate("client", "Horizon"))
        self.label_height.setText(_translate("client", "0"))
        self.label_horizon.setText(_translate("client", "0"))
        self.Button_Calibration.setText(_translate("client", "Calibration"))
        self.Button_Ball_And_Face.setText(_translate("client", "Face"))
        self.Button_Sonic.setText(_translate("client", "Sonic"))
        self.Button_Face_ID.setText(_translate("client", "Face ID"))
        self.Button_LED.setText(_translate("client", "LED"))
        self.label_speed.setText(_translate("client", "8"))
        self.label_7.setText(_translate("client", "Speed"))
        self.label_8.setText(_translate("client", "Head"))
        self.label_head.setText(_translate("client", "90"))
        self.label_6.setText(_translate("client", "Roll"))
        self.label_5.setText(_translate("client", "Yaw"))
        self.label_point.setText(_translate("client", "(0,0)"))
        self.label_roll.setText(_translate("client", "0"))
        self.label_4.setText(_translate("client", "Pitch"))
        self.label_pitch.setText(_translate("client", "0"))
        self.label_yaw.setText(_translate("client", "0"))
        self.label_Y.setText(_translate("client", "20"))
        self.label_Y_2.setText(_translate("client", "0"))
        self.label_Y_3.setText(_translate("client", "-20"))
        self.label_Y_4.setText(_translate("client", "(Yaw)"))
        self.label_X.setText(_translate("client", "-20"))
        self.label_X_2.setText(_translate("client", "0"))
        self.label_X_3.setText(_translate("client", "-20"))
        self.label_X_4.setText(_translate("client", "(Pitch)"))
        self.label_X_5.setText(_translate("client", "Attitude Angle"))
        #self.label_sonic.setText(_translate("client", "Obstacle:0cm"))
        self.Button_Relax.setText(_translate("client", "Relax"))
