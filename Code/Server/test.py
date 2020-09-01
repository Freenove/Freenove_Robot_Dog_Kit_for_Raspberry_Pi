import time
from Led import *
led=Led()
def test_Led():
    try:
        #Red wipe
        print ("\nRed wipe")
        led.colorWipe(led.strip, Color(255, 0, 0)) 
        time.sleep(1)
        
        
        #Green wipe
        print ("\nGreen wipe")
        led.colorWipe(led.strip, Color(0, 255, 0)) 
        time.sleep(1)
        
        
        #Blue wipe
        print ("\nBlue wipe")
        led.colorWipe(led.strip, Color(0, 0, 255)) 
        time.sleep(1)
        
        
        #White wipe
        print ("\nWhite wipe")
        led.colorWipe(led.strip, Color(255, 255, 255)) 
        time.sleep(1)
        
        led.colorWipe(led.strip, Color(0, 0, 0))   #turn off the light
        print ("\nEnd of program")
    except KeyboardInterrupt:
        led.colorWipe(led.strip, Color(0, 0, 0))   #turn off the light
        print ("\nEnd of program")

from Ultrasonic import *
ultrasonic=Ultrasonic()                
def test_Ultrasonic():
    try:
        while True:
            data=ultrasonic.getDistance()   #Get the value
            print ("Obstacle distance is "+str(data)+"CM")
            time.sleep(1)
    except KeyboardInterrupt:
        print ("\nEnd of program")

from Servo import *
servo=Servo()
def test_Servo():
    try:
        for i in range(90):
            servo.setServoAngle(4,90-i)
            servo.setServoAngle(7,90-i)
            servo.setServoAngle(8,90+i)
            servo.setServoAngle(11,90+i)
            time.sleep(0.01)
        for i in range(90):
            servo.setServoAngle(2,90-i)
            servo.setServoAngle(5,90-i)
            servo.setServoAngle(10,90+i)
            servo.setServoAngle(13,90+i)
            time.sleep(0.01)
        for i in range(60):
            servo.setServoAngle(3,90-i)
            servo.setServoAngle(6,90-i)
            servo.setServoAngle(9,90+i)
            servo.setServoAngle(12,90+i)
            time.sleep(0.01)
        print ("\nEnd of program")      
    except KeyboardInterrupt:
        print ("\nEnd of program")
        
        
from ADS7830 import *
adc=ADS7830()
def test_Adc():
    try:
        while True:
            Power=adc.readAdc(0)/255.0*5.0*3
            print ("The battery voltage is "+str(Power)+"V")
            time.sleep(1)
            print ('\n')
    except KeyboardInterrupt:
        print ("\nEnd of program")

from Buzzer import *
buzzer=Buzzer()
def test_Buzzer():
    try:
        buzzer.run('1')
        time.sleep(1)
        print ("1S")
        time.sleep(1)
        print ("2S")
        time.sleep(1)
        print ("3S")
        buzzer.run('0')
        print ("\nEnd of program")
    except KeyboardInterrupt:
        buzzer.run('0')
        print ("\nEnd of program")
     
# Main program logic follows:
if __name__ == '__main__':

    print ('Program is starting ... ')
    import sys
    if len(sys.argv)<2:
        print ("Parameter error: Please assign the device")
        exit() 
    if sys.argv[1] == 'Led':
        test_Led()
    elif sys.argv[1] == 'Ultrasonic':
        test_Ultrasonic()
    elif sys.argv[1] == 'Servo': 
        test_Servo()               
    elif sys.argv[1] == 'ADC':   
        test_Adc()  
    elif sys.argv[1] == 'Buzzer':   
        test_Buzzer() 


        
        
        
        
