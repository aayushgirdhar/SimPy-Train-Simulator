from tkinter import *

def main():
    main_window = Tk()
    main_window.config(background='beige')
    main_window.attributes('-fullscreen', True)
    
    Label(main_window, text='MAIN').pack()
    
    start_button = Button(main_window, 
                          text = 'Start', 
                          command = start,
                          bd=8,
                          bg='teal',
                          fg='white',
                          width=7,
                          padx=15,
                          pady=15,
                          font = ('Helvetica', 50, 'bold'),
                          activebackground='teal',
                          activeforeground='black').place(x = 450, y = 450)
    settings_button = Button(main_window, 
                             text = 'Settings', 
                             command = settings,
                             bd=8,
                             bg='teal',
                             fg='white',
                             width=7,
                             padx=15,
                             pady=15,
                             font = ('Helvetica', 50, 'bold'),
                             activebackground='teal',
                             activeforeground='black').place(x = 1100, y = 450)

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