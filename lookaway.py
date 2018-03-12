import time
import ctypes
def run():
    time.sleep(1800)
    ctypes.windll.user32.MessageBoxW(0, "Please look away, you've been gazing at screen for 30 min!!",time.ctime(), 0)

while True:
    run()
           
            
