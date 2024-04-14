from machine import Pin
from neopixel import NeoPixel
import time
import requests

pin38 = Pin(38, Pin.IN)
pin34 = Pin(34, Pin.IN)
pin2 = Pin(2, Pin.OUT)

blinkSeconds = 5

def NeoOff():
    pin2.value(0)

def NeoOn(color):
    pin2.value(1)
    pin = Pin(0, Pin.OUT)   # set GPIO0 to output to drive NeoPixels
    np = NeoPixel(pin, 1)   # create NeoPixel driver on GPIO0 for 8 pixels
    np[0] = color   # set the first pixel to RGB of your choice
    np.write()
    # write data to all pixels
    
def update_neopixel(door_state):
    if door_state == 'closed':
        NeoOn((0x00, 0x10, 0x00))
    else:
        NeoOn((0x10, 0x00, 0x00))
    time.sleep(0.05)
    NeoOff()

def wlan_connect(ssid='MYSSID', password='MYPASS'):
    import network
    wlan = network.WLAN(network.STA_IF)
    if not wlan.active() or not wlan.isconnected():
        wlan.active(True)
        print('connecting to:', ssid)
        wlan.connect(ssid, password)
        while not wlan.isconnected():
            pass
    print('network config:', wlan.ifconfig())
   
wlan_connect("Queensbridge", "7308Vajirkar")

def getButtonState():
    if pin38.value() == 0:
        state = "opened"
    else:
        state = "closed"
    return state

def getDoorState():
    if pin34.value() == 0:
        state = "opened"
    else:
        state = "closed"
    return state

def notify(msg):
    msgText = 'Hello%2C%20Your%20Garage%20Door%20has%20been%20'+msg+'.'
    #msgText = 'Hello%2C%0AYour%20Garage%20Door%20has%20been%20left%20'+msg+'%0Afor%20more%20than%205%20minutes.Emoji%3f%f0%9f%90%af'
    r = requests.get('https://api.callmebot.com/whatsapp.php?phone=14082563212&text='+msgText+'&apikey=3294453')
    print(r.text)
    
doorStatePrior = "none"
while True:
    doorStateNow = getDoorState() 
    if doorStateNow != doorStatePrior:
        blinkSeconds = 0
        notify(doorStateNow)
        
    if blinkSeconds <= 0:
        blinkSeconds = 5
        update_neopixel(doorStateNow)
    else:
        blinkSeconds = blinkSeconds - 1
        
    doorStatePrior = doorStateNow
    time.sleep(1)
    #print(doorStatePrior)
    
    

