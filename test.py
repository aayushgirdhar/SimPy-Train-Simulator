from tkinter import *

root = Tk()

def start():
    run('hello')
    
def run(text):
    print('Hi' + text)
Button(root, command = start, text='click').pack()

mainloop()