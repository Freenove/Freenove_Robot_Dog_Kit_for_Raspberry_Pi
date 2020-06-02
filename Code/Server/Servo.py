#coding:utf-8
import Adafruit_PCA9685
import time 
class Servo:
    def __init__(self):
        self.pwm = Adafruit_PCA9685.PCA9685()   
        self.pwm.set_pwm_freq(50)               # Set the cycle frequency of PWM
    #Convert the input angle to the value of pca9685
    def setServoAngle(self,channel, angle):  
        date = 4096 * ((angle * 10) + 850) / 20000
        self.pwm.set_pwm(channel, 0, int(date))
 
# Main program logic follows:
if __name__ == '__main__':
    print ('Program is starting ... ')
    S=Servo()
    while True:
        try:
            for i in range(16):
                S.setServoAngle(i,90)
        except KeyboardInterrupt:
            print ("\nEnd of program")
            break
        


        
        
        
        
