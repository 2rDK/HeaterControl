# -*- coding: utf-8 -*-
from datetime import datetime

def printCurrentTime():
    print("["+datetime.strftime(datetime.now(), '%d-%m-%Y %H:%M:%S')+"] ")
    
if __name__ == "__main__":
    printCurrentTime()