from gpiozero import LED
from time import sleep
num = " "

led1 = LED(17)
led2= LED(6)
led3 = LED(19)
led4= LED(26)
led5= LED(21)
led6= LED(20)
led7= LED(16)
led8 = LED(24)

leds = [led1,led2,led3,led4,led5,led6,led7,led8]
class Digit:
    def __init__(self):
        pass
        
    

    def off(self):
        led1.on()
        led2.on()
        led3.on()
        led4.on()
        led5.on()
        led6.on()
        led7.on()
        led8.on()


    def one(self):
        led2.off()
        led4.off()
        led1.on()
        led3.on()
        led5.on()
        led6.on()
        led7.on()
        led8.on()


    
    def two(self):
        led3.off()
        led2.off()
        led1.off()
        led7.off()
        led6.off()
        led4.on()
        led5.on()               
        led8.on()


    def three(self):
        led3.off()
        led2.off()
        led1.off()
        led4.off()
        led6.off()
        led5.on()
        led7.on()
        led8.on()

    def four(self):
        led8.off()
        led1.off()
        led2.off()
        led4.off()               
        led3.on()        
        led5.on()
        led6.on()
        led7.on()
       

    def five(self):
        led3.off()
        led8.off()
        led1.off()
        led4.off()
        led6.off()
        led2.on()         
        led5.on()        
        led7.on()
       

    def six(self):
        led8.off()
        led7.off()
        led6.off()
        led4.off()
        led2.on()
        led1.off()       
        led3.on()        
        led5.on()
       
       
        

    def seven(self):
        led3.off()
        led2.off()
        led4.off()
        led1.on()       
        led5.on()
        led6.on()
        led7.on()
        led8.on()

    def eight(self):
        led1.off()
        led2.off()
        led3.off()
        led4.off()
        led6.off()
        led7.off()
        led8.off()
        led5.on()
    
    def nine(self):
        led1.off()
        led2.off()
        led3.off()
        led4.off()
        led8.off()
        led5.on()
        led7.on()
        led6.on()

    def zero(self):
        led2.off()
        led3.off()
        led4.off()
        led6.off()
        led7.off()
        led8.off()
        led1.on()
        led5.on()

    def dot(self):
        led5.off()
        led1.on()
        led2.on()
        led3.on()
        led4.on()
        led6.on()
        led7.on()
        led8.on()
        

        


      
while num != "q":
    

    num = input("please enter a number 0 through 10 or q  ")
    
    if num == "1":
        num=Digit()
        num.one()
        
    elif num== "2":
        num=Digit()
        num.two()

    elif num=="3":
        num=Digit()
        num.three()
        
   

    elif num== "4":
        num=Digit()
        num.four()

    elif num== "5":
        num=Digit()
        num.five()         


    elif num== "6":
        num=Digit()
        num.six()

    elif num== "7":
        num=Digit()
        num.seven()

    elif num== "8":
        num=Digit()
        num.eight()

    elif num=="9":
        num=Digit()
        num.nine()

    elif num== "10":
        num=Digit()
        num.dot()

    elif num=="0":
        num=Digit()
        num.zero()

   
    

