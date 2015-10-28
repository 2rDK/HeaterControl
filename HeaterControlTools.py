# -*- coding: utf-8 -*-
from datetime import datetime

def printCurrentTime():
    return("["+datetime.strftime(datetime.now(), '%d-%m-%Y %H:%M:%S')+"] ")
    
if __name__ == "__main__":
    print(printCurrentTime())