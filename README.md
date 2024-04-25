# ESP32-Garage-Door-Sensor

Whenever I step inside the house after playing basketball in my driveway, my parents always ask me: "Did you close the garage door?" It's always a painful and unnecessary task for me to go back and check, so I decided to do something to end this chronic misery. 

Using an ESP32 microcontroller, along with a hall effect sensor, I decided to create a garage door notification system, in which I would be notified whenever the state of the garage door changes (ex. from open to closed or vice versa). 

## Hardware
In January, I unboxed my new Prusa MK3s+ 3D Printer (I got the kit, so I could learn how all the parts fit together so it would be easier to fix when it needs maintenance). However, me being the busy junior I am, never got a chance to finish it. So, I spent the first day of my Spring Break racing to finish the printer. And finally, at 1 in the morning on Sunday, it was ready to go.
![3D Printer]((3dprints/Images/3dprinter.jpg) | width=100)

Since the garage (especially the specific corner of the garage) always gets dusty fast, my first priority was to create a case for the ESP32 in order to ensure it was shielded from the elements. I used onshape to CAD a 3D printed case and cover for it, and then set my new 3D printer to work at 3 in the morning. 
![3DPrinted ESP32 Cover](3dprints/Images/bottomboximg.png)

I was quite impressed with how well the parts were printed, esepecially with the engraved "ESP32" on the cover. They both turned out great!
![3D Printed Parts](3dprints/Images/printed_parts.jpg)

Next, I wanted a mounting system that provided a mounting platform for the ESP32 case and the wired half of the hall effect sensor. I CADded a mounting system that achieved these goals while also fitting the size constraints needed to fit in the small corner of the door. 
(Insert mounting system here)

I decided to put a 3M velcro lock to mount the ESP32 case to the mounting system.

Unfortunately, I didn't take the additional electrical components required for the ESP32 into account when designing the ESP32 casing, so the casing fit was a bit... interesting. Learning experience! 

Finally, in order to make sure the unwired portion of the sensor is close to the wired portion of the sensor, I used a wood block and mounted the unwired part of the sensor onto it with two wood screws to hold it in place.

With the hardware done, it was time to move onto the electrical and software components of the project.

## Electrical
I connected the ESP32 to the hall effect sensor with wire connectors and some soldering. This was my first time soldering, so I was really excited.  
(wiring diagram here)

## Software
I wanted the ESP32 to send a WhatsApp message to my phone whenever it detects a change in the state of the door. So, I decided to create a continuous loop that compares a prior state to a current state, and sends a message to my phone when the prior and current state differ. The two possible states in this situation are an open door (no hall effect sensor detected) and a closed door (hall effect sensor detected). In addition to sending a message to my phone, the ESP32 gives a visual indicator as to whether it detects a closed or open door state through controllng its neopixel. The neopixel LED blinks green if it detects a closed door, and a flashes red if it detects an open door. Finally, in order to send messages from the ESP32 to my phone, the program on the microcontroller connects to the home Wifi to access the internet, and uses CallMeBot's API in order to send the message to my phone.

(add code pic here)
(add video)





Using an ESP32 microcontroller, I created a garage door sensor that notifies 
ESP32 Beginner project to detect state of a garage door and send Whatsapp notifications.

## References

- https://docs.micropython.org/en/latest/search.html?q=neopixel&check_keywords=yes&area=default
- https://learn.adafruit.com/adafruit-esp32-feather-v2/pinouts
- https://www.callmebot.com/blog/free-api-whatsapp-messages/
