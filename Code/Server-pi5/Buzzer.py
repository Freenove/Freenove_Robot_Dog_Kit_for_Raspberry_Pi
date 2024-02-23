import time
from gpiozero import Buzzer
buzzer = Buzzer(17)
class Buzzer:
    def run(self,command):
        if command!="0":
            buzzer.on()
        else:
            buzzer.off()
if __name__=='__main__':
    pass




