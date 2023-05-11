from tkinter import *
from PIL import Image, ImageTk
import traindataset as td
import main

user_settings = {
        'index': '',
        'acceleration': '',
        'retardation': '',
        'waiting_time': ''
}

class settings:
    def __init__(self):
        self.settings_window = Tk()
        self.settings_window.attributes('-fullscreen', True)
        Label(self.settings_window, 
              text='Settings', 
              font = ('Segoe UI', 60, 'bold'), 
              fg='#0049b5').pack()
        self.index = 0
        self.selected_train = ''
        self.train_select = StringVar(self.settings_window)
        self.options = [td.trains[0]['name'], td.trains[1]['name'], td.trains[2]['name']]
        self.conditionSelect = StringVar(self.settings_window)
        self.values_accel = []
        self.values_retard = []
        self.accel_select = StringVar(self.settings_window)
        self.retard_select = StringVar(self.settings_window)
        self.wait_select = StringVar(self.settings_window)
        self.elements()
        self.flag = False
        self.get_index()
        self.accel_select.set(f'Select Train Acceleration(m/s\u00b2 )')
        self.retard_select.set('Select Train Retardation (m/s\u00b2 )')
        self.train_select.set('Select a Train')
        self.wait_select.set('Select Waiting Time for Each Station (Minutes)')
     
    def print_data(self):
        r = 450
        count = 1
        self.selected_train = self.train_select.get()
        self.selected_accel = self.accel_select.get()
        self.selected_retard = self.retard_select.get()
        self.selected_wait = self.wait_select.get()
        
        user_settings.update({'index': self.index}) 
        user_settings.update({'acceleration': self.selected_accel}) 
        user_settings.update({'retardation': self.selected_retard}) 
        user_settings.update({'waiting_time': self.selected_wait}) 
        
        print(user_settings)
        name_label = Label(self.settings_window, 
                            text= self.selected_train,
                            font = ('Segoe UI', 20, 'bold'), 
                            fg='#0049b5').place(x = 1000, y = 300)
        stations = td.trains[self.index]['stations']
        header = Label(self.settings_window, 
                       text="Intermediate Stations",
                       font = ('Segoe UI', 14), 
                       fg='#0049b5')
        header.place(x = 1000, y = 400)
        for i in stations:
            station_label = Label(self.settings_window, 
                                  text=f'{count}.{i}',
                                  font = ('Segoe UI', 14), 
                                  fg='black')
            station_label.place(x=1030, y=r)
            r += 30
            count = count + 1
            
        accel_label = Label(self.settings_window, 
                            text = f'Acceleration = {self.selected_accel} m/s\u00b2 ',
                            font = ('Segoe UI', 14), 
                            fg='black')
        retard_label = Label(self.settings_window, 
                            text = f'Retardation = {self.selected_retard} m/s\u00b2 ',
                            font = ('Segoe UI', 14), 
                            fg='black')
        wait_label = Label(self.settings_window, 
                            text = f'Waiting Time = {self.selected_wait} minutes',
                            font = ('Segoe UI', 14), 
                            fg='black')
        accel_label.place(x = 1000, y = 600)
        retard_label.place(x = 1000, y = 650)
        wait_label.place(x = 1000, y = 700)
            
    def get_index(self, *args):
        selected_train = self.train_select.get()
        for item in td.trains:
            if item['name'] == selected_train:
                self.index = item['no']
                break

        
    def radio(self):
        self.selected_conditions = self.conditionSelect.get()
        if self.selected_conditions == '0':
            self.values_accel = td.sard[self.index]['accelerationsun']
            self.values_retard = td.sard[self.index]['retardationsun']
        elif self.selected_conditions == '1':
            self.values_accel = td.sard[self.index]['accelerationrain']
            self.values_retard = td.sard[self.index]['retardationrain']
        self.accel_drop['menu'].delete(0, 'end')
        self.retard_drop['menu'].delete(0, 'end')
 
        for values in self.values_accel:
            self.accel_drop['menu'].add_command(label=values, command=lambda v=values: self.accel_select.set(v))
            self.accel_drop["menu"]["background"] = "white"
            self.accel_drop["menu"]["foreground"] = "#0049b5"
            self.accel_drop["menu"]["font"] = ('Segoe UI', 14)
            self.accel_drop["menu"]["selectcolor"] = "#0049b5"
            self.accel_drop["menu"]["activeborderwidth"] = '4'
            self.accel_drop["menu"]["bd"] = '7'
        for values in self.values_retard:
            self.retard_drop['menu'].add_command(label=values,command=lambda v=values: self.retard_select.set(v))
            self.retard_drop["menu"]["background"] = "white"
            self.retard_drop["menu"]["foreground"] = "#0049b5"
            self.retard_drop["menu"]["font"] = ('Segoe UI', 14)
            self.retard_drop["menu"]["selectcolor"] = "#0049b5"
            self.retard_drop["menu"]["activeborderwidth"] = '4'
            self.retard_drop["menu"]["bd"] = '7'

    def enable(self):
        start_button['state'] = 'normal'
        self.settings_window.destroy()
      
    def elements(self):
        self.drop = OptionMenu(self.settings_window, self.train_select, *self.options, command=self.get_index)
        self.drop['background'] = '#0049b5'
        self.drop['foreground'] = 'white'
        self.drop["activebackground" ] = "#0049b5"
        self.drop["activeforeground" ] = "white"
        self.drop["font"] = ("Segoe UI", 14)
        self.drop["height"] = '1'
        self.drop["bd"] = 5
        self.drop["relief"] = "ridge"
        self.drop["pady"] = 10
        self.drop["padx"] = 10
        self.drop["menu"]["background"] = "white"
        self.drop["menu"]["foreground"] = "#0049b5"
        self.drop["menu"]["font"] = ('Segoe UI', 14)
        self.drop["menu"]["selectcolor"] = "#0049b5"
        self.drop["menu"]["activeborderwidth"] = '4'
        self.drop["menu"]["bd"] = '7'
        self.drop.place(x = 150, y = 300)
        
        Label(self.settings_window, 
                text="Select Weather Conditions", 
                font = ('Segoe UI', 14), 
                fg='#0049b5').place(x = 150, y = 380)
        self.sunny = Radiobutton(self.settings_window, 
                                 text='Sunny', 
                                 variable=self.conditionSelect, 
                                 value='0', 
                                 command=self.radio,
                                 font=("Segoe UI", 14), 
                                 fg="black", 
                                 padx=10, 
                                 pady=5)
        self.rainy = Radiobutton(self.settings_window, 
                                 text='Rainy', 
                                 variable=self.conditionSelect, 
                                 value='1', 
                                 command=self.radio,
                                 font=("Segoe UI", 14), 
                                 fg="black",
                                 padx=10, 
                                 pady=5)
        self.sunny.place(x = 140, y = 410)
        self.rainy.place(x = 240, y = 410)
        self.accel_drop = OptionMenu(self.settings_window,self.accel_select,"")
        self.accel_drop['background'] = '#0049b5'
        self.accel_drop['foreground'] = 'white'
        self.accel_drop["activebackground" ] = "#0049b5"
        self.accel_drop["activeforeground" ] = "white"
        self.accel_drop["font"] = ("Segoe UI", 14)
        self.accel_drop["height"] = '1'
        self.accel_drop["bd"] = 5
        self.accel_drop["relief"] = "ridge"
        self.accel_drop["pady"] = 10
        self.accel_drop["padx"] = 10
        self.accel_drop.place(x = 150, y = 480)
        self.retard_drop = OptionMenu(self.settings_window,self.retard_select,"")
        self.retard_drop['background'] = '#0049b5'
        self.retard_drop['foreground'] = 'white'
        self.retard_drop["activebackground" ] = "#0049b5"
        self.retard_drop["activeforeground" ] = "white"
        self.retard_drop["font"] = ("Segoe UI", 14)
        self.retard_drop["height"] = '1'
        self.retard_drop["bd"] = 5
        self.retard_drop["relief"] = "ridge"
        self.retard_drop["padx"] = 10
        self.retard_drop["pady"] = 10
        self.retard_drop.place(x = 150, y = 560)
        
        self.waiting_drop = OptionMenu(self.settings_window, self.wait_select, 10, 20, 30, 40, 50, 60)
        self.waiting_drop['background'] = '#0049b5'
        self.waiting_drop['foreground'] = 'white'
        self.waiting_drop["activebackground" ] = "#0049b5"
        self.waiting_drop["activeforeground" ] = "white"
        self.waiting_drop["font"] = ("Segoe UI", 14)
        self.waiting_drop["height"] = '1'
        self.waiting_drop["bd"] = 5
        self.waiting_drop["relief"] = "ridge"
        self.waiting_drop["pady"] = 10
        self.waiting_drop["padx"] = 10
        self.waiting_drop["menu"]["background"] = "white"
        self.waiting_drop["menu"]["foreground"] = "#0049b5"
        self.waiting_drop["menu"]["font"] = ('Segoe UI', 14)
        self.waiting_drop["menu"]["selectcolor"] = "#0049b5"
        self.waiting_drop["menu"]["activeborderwidth"] = '4'
        self.waiting_drop["menu"]["bd"] = '7'
        self.waiting_drop.place(x = 150, y = 640)
        
        
        submit_button = Button(self.settings_window,
                     text='Submit',
                     command=self.print_data,
                     bd=5,
                     bg='#0049b5',
                     fg='white',
                     width=9,
                     font = ('Segoe UI', 20, 'bold'),
                     activebackground='#0049b5',
                     activeforeground='black')
        submit_button.place(x = 150, y = 800)
        
        home_button = Button(self.settings_window,
                     text='Home',
                     command=self.enable,
                     bd=5,
                     bg='#0049b5',
                     fg='white',
                     width=9,
                     font = ('Segoe UI', 20, 'bold'),
                     activebackground='#0049b5',
                     activeforeground='black')
        home_button.place(x = 350, y = 800)


main_window = Tk()
main_window.attributes('-fullscreen', True)

title = Label(main_window, 
              text = "Train Simulator", 
              font = ('Segoe UI', 60, 'bold'), 
              fg='#0049b5')
title.pack()


train_photo = PhotoImage(file = "resources/train.png").subsample(2)
label = Label(main_window, image=train_photo)
label.place(x=50, y=360)


def start_sim():
    start_window = Tk()
    start_window.attributes('-fullscreen', True)
    Label(start_window, text=td.trains[int(user_settings['index'])]['name'], 
                font = ('Segoe UI', 40, 'bold'), 
                fg='#0049b5').pack()
    main.run_simulation(int(user_settings['acceleration']), int(user_settings['retardation']), int(user_settings['index']), int(user_settings['waiting_time']), start_window)
start_button = Button(main_window, 
                      text = 'Start',
                      command=start_sim, 
                      bd=8,
                      bg='#0049b5',
                      fg='white',
                      width=9,
                      font = ('Segoe UI', 40, 'bold'),
                      activebackground='#0049b5',
                      activeforeground='black')
start_button.place(x = 1400, y = 400)
start_button['state'] = 'disabled'

settings_button = Button(main_window, 
                         text = 'Settings', 
                         command = settings,
                         bd=8,
                         bg='#0049b5',
                         fg='white',
                         width=9,
                         font = ('Segoe UI', 40, 'bold'),
                         activebackground='#0049b5',
                         activeforeground='black')
settings_button.place(x = 1400, y = 600)
mainloop()