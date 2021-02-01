from gpiozero import Button #import module Button
from gpiozero import LED    #import module LED
from time import sleep      #import sleep
button = Button(2)
led = LED(17)

while True:
    if button.is_pressed:
        print("Pressed")
        led.on()
    else:
        print("Released")
        led.off()
    sleep(1)