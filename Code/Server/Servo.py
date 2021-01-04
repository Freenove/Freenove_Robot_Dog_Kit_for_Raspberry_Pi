#coding:utf-8
import Adafruit_PCA9685
import time 
class Servo:
    def __init__(self):
        self.angleMin=18
        self.angleMax=162
        self.pwm = Adafruit_PCA9685.PCA9685()   
        self.pwm.set_pwm_freq(50)               # Set the cycle frequency of PWM
    #Convert the input angle to the value of pca9685
    def map(self,value,fromLow,fromHigh,toLow,toHigh):
        return (toHigh-toLow)*(value-fromLow) / (fromHigh-fromLow) + toLow
    def setServoAngle(self,channel, angle):
        if angle < self.angleMin:
            angle = self.angleMin
        elif angle >self.angleMax:
            angle=self.angleMax
        date=self.map(angle,0,180,102,512)
        #print(date,date/4096*0.02)
        self.pwm.set_pwm(channel, 0, int(date))
 
# Main program logic follows:
if __name__ == '__main__':
    print("Now servos will rotate to 90°.") 
    print("If they have already been at 90°, nothing will be observed.")
    print("Please keep the program running when installing the servos.")
    print("After that, you can press ctrl-C to end the program.")
    S=Servo()
    while True:
        try:
            for i in range(16):
                S.setServoAngle(i,90)
        except KeyboardInterrupt:
            print ("\nEnd of program")
            break

           
        
        


        
        
        
        
