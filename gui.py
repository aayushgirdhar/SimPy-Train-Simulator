from tkinter import *
from PIL import Image, ImageTk

def main():
    main_window = Tk()
    main_window.attributes('-fullscreen', True)
    
    train_image = ImageTk.PhotoImage(Image.open("D:/College/GitHub/TrainStationSimulator/resources/closed.png"))

    train_image_label = Label(main_window, image = train_image)
    train_image_label.pack()
    
    start_button = Button(main_window, 
                          text = 'Start', 
                          command = start,
                          bd=8,
                          bg='teal',
                          fg='white',
                          width=7,
                          padx=15,
                          pady=15,
                          font = ('Helvetica', 40, 'bold'),
                          activebackground='teal',
                          activeforeground='black')
    start_button.place(x = 1200, y = 350)
    settings_button = Button(main_window, 
                             text = 'Settings', 
                             command = settings,
                             bd=8,
                             bg='teal',
                             fg='white',
                             width=7,
                             padx=15,
                             pady=15,
                             font = ('Helvetica', 40, 'bold'),
                             activebackground='teal',
                             activeforeground='black')
    settings_button.place(x = 1200, y = 550)

def start():
    start_window = Tk()
    start_window.attributes('-fullscreen', True)
    
    Label(start_window, text='START').pack()

def settings():
    settings_window = Tk()
    settings_window.attributes('-fullscreen', True)
    
    Label(settings_window, text='Settings').pack()
    
    
main()
mainloop()