# ESP32-Garage-Door-Sensor

Whenever I step inside the house after playing basketball in my driveway, my parents always ask me: "Did you close the garage door?" It's always a painful and unnecessary task for me to do, so I decided to do something about it. 

Using an ESP32 microcontroller, along with a hall effect sensor, I decided to create a garage door notification system, in which I would be notified whenever the state of the garage door changes (ex. from open to closed or vice versa). 

## Hardware
In January, I got a Prusa MK3s+ 3D Printer (I got the kit, so I could learn how all the parts fit together so it would be easier to fix when it needs maintenance). However, me being the busy junior I am, never got a chance to finish it. So, I spent the first day of my Spring Break racing to finish the printer. And finally, at 1 in the morning on Sunday, it was ready to go.
(Insert 3D Printer image here)

Since the garage (especially the specific corner of the garage) always gets dusty fast, my first priority was to create a case for the ESP32 in order to ensure it was shielded from the elements. I used onshape to CAD a 3D printed case and cover for it, and then set my new 3D printer to do some forced labor for me at 3 in the morning. 
(Insert 3dp cover CAD here)

I was quite impressed with how well it printed the engraved "ESP32" on the cover, it turned out great!
(Insert 3dp cover here)

Next, I wanted a mounting system that provided a mounting platform for the ESP32 case and the wired half of the hall effect sensor. I also wanted to make sure that this system could mount to the rolling track of the door, so it was time for a home depot run.



Using an ESP32 microcontroller, I created a garage door sensor that notifies 
ESP32 Beginner project to detect state of a garage door and send Whatsapp notifications.

## References

- https://docs.micropython.org/en/latest/search.html?q=neopixel&check_keywords=yes&area=default
- https://learn.adafruit.com/adafruit-esp32-feather-v2/pinouts
- https://www.callmebot.com/blog/free-api-whatsapp-messages/
