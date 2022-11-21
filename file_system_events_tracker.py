import sys
import time
import random
import os
import shutil
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

class FileEventHandler(FileSystemEventHandler):
    def on_created(self, event):
        print(f"Hey,{event.src_path} has been created")

    def on_deleted(self, event):
        print(f"Oops, someone deleted {event.src_path}")

    def  on_modified(self, event):
        print(f"{event.src_path} has been modified !")
    
    def on_moved(self, event):
        print(f"Oops!{event.src_path} has been moved or renamed!")

    try:
        while True:
            time.sleep(2)
            print("running....")
    except KeyboardInterrupt:
        print("stopped.")
        Observer.stop()