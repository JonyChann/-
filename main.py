import sys
#import ffmpeg
#import matplotlib
import tkinter as tk

global filepath

def get_arg():
    global filepath
    argc=len(sys.argv)
    argv=sys.argv
    for arg in range(0,argc):
        if argv[arg] == '-i': #接受传入文件的路径
            filename=(argv[arg+1])
        #elif argv[arg] == '-l' 接受其它参数，暂时空置

get_arg()
tk.TK()