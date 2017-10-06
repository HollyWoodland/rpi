##imports
import explorerhat
from time import sleep
from guizero import App, PushButton

##function definitions

def test_buttons():
    explorerhat.touch.one
    explorerhat.touch.two
    explorerhat.touch.three
    explorerhat.touch.is_pressed()
    explorerhat.touch.is_held()
    #explorerhat.touch.pressed( handler_function )
    #calls handler_function when pad is touched
    #def handle(channel, event)
    #channel is the number of the pad
    #eg handle(explorerhat.touch.one,
    
def test_lights():
    explorerhat.light.yellow.on() #yellow, green, blue, red
    explorerhat.light.green.blink(50,50)
    explorerhat.light.red.fade(20,100,50)
    explorerhat.light.red.stop()
    explorerhat.light.green.stop()
    explorerhat.light.yellow.off()
    
##move forwards
def forwards():
    
    ##testing tthe motors
    explorerhat.motor.one.forward(100) #100 is the speed
    explorerhat.motor.two.forward(100)
    explorerhat.motor.one.speed(50)
    explorerhat.motor.two.invert()

    sleep(2)

    explorerhat.motor.one.stop()
    explorerhat.motor.two.stop()


##move forwards
def backwards():
    
    ##testing tthe motors
    explorerhat.motor.one.backward(100)
    explorerhat.motor.two.backward(100)

    sleep(2)

    explorerhat.motor.one.stop()
    explorerhat.motor.two.stop()
    
##GUI app
app = App("Buggy controller")
drive = PushButton(app, forwards, text="Forwards")
reverse = PushButton(app, backwards, text="Reverse")
lighttest = PushButton(app, test_lights, text="Lights")
app.display()
