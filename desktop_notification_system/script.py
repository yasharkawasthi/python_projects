# Desktop Notification System - Reminder for Drinking Water 

import time
from plyer import notification

while True:
    notification.notify(
        title = "Please drink water now!",
        message = "The Institute of Medicine (IOM) recommends a total of 13 cups (about 3 liters) of fluid each day.",
        app_icon = "water.ico",
        timeout = 15    # Displays notification for 15 seconds
    )
    time.sleep(60*60)   # Sleeps for 3600 seconds (1 hour)
    
# To run this process in background, try : pythonw .\script.py
# To terminate this process: Go to Task Manager and find pythonw.exe in processes tab and then terminate it.
# If you don't find pythonw.exe in processes tab then go to details tab, you'll find it their.