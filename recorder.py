import pygame, os
from datetime import date, datetime

def GetDate():
    _date = str(date.today().day) + "_" + str(date.today().month) + "_" + str(date.today().year)
    _time = str(datetime.now().hour) + "_" + str(datetime.now().minute) + "_" + str(datetime.now().second)
    return _date + "_" + _time

def Screenshot(_screen, _name):
    _filename = _name + "_"+ GetDate()
    pygame.image.save(_screen, _filename)

def CaptureVideoFrame(_screen, _frame, _path):
    _fullpath = _path + "\\frame%08d.png"%_frame
    pygame.image.save(_screen, _fullpath)

def MakeMP4(_path, _name, _fps):
    os.system("ffmpeg -r " + str(_fps) + " -i " + _path + "\\frame%08d.png -vcodec mpeg4 -q:v 0 -y " + _name + ".mp4")