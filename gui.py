from tkinter import *
from PIL import Image, ImageTk
import traindataset as td

main_window = Tk()
main_window.attributes('-fullscreen', True)

def start():
    start_window = Tk()
    start_window.attributes('-fullscreen', True)
    
    Label(start_window, text='START').pack()

def settings():
    def unlock_dropdown():
        accel_drop = OptionMenu(settings_window, accel_select, values_accel)
        accel_drop.pack()
        retard_drop = OptionMenu(settings_window, retard_select, values_retard)
        retard_drop.pack()
    def getData():
        r = 50
        count = 1
        index = -1
        selected_train = trainSelect.get()
        values_accel = []
        values_retard = []
        for item in td.trains:
            if item['name'] == selected_train:
                index = item['no']
                break
        name_label = Label(settings_window, text=f'Train Selected - {selected_train}').pack()
        stations = td.trains[index]['stations']
        header = Label(settings_window, text="Intermediate Stations")
        header.pack()
        for i in stations:
            station_label = Label(settings_window, text =f'{count}.{i}')
            station_label.place(x = 20, y = r)
            r += 20
            count = count + 1
        
        selected_conditions = conditionSelect.get()
        accel_select = StringVar(settings_window)
        accel_select.set('Select Train Acceleration')
        
        retard_select = StringVar(settings_window)
        retard_select.set('Select Train Retardation')
        
        if(selected_conditions == '0'):
            values_accel = td.sard[index]['accelerationsun']
            values_retard = td.sard[index]['retardationsun']
        elif(selected_conditions == '1'):
            values_accel = td.sard[index]['accelerationrain']
            values_retard = td.sard[index]['retardationrain']
    
        
    settings_window = Tk()
    settings_window.attributes('-fullscreen', True)
    Label(settings_window, text='Settings').pack()
    
    options = [td.trains[0]['name'], td.trains[1]['name'], td.trains[2]['name']]
    
    trainSelect = StringVar(settings_window)
    trainSelect.set('Select a train')
    
    drop = OptionMenu(settings_window, trainSelect, *options)
    drop.pack()
    
    conditionSelect = StringVar(settings_window)
    sunny = Radiobutton(settings_window, text = 'Sunny', variable=conditionSelect, value = 0, command=unlock_dropdown)
    sunny.pack()
    
    rainy = Radiobutton(settings_window, text = 'Rainy', variable=conditionSelect, value = 1, command=unlock_dropdown)
    rainy.pack()
    
    button = Button(settings_window, text='Submit', command=getData)
    button.pack()
    
    
title = Label(main_window, text = "Train Station Simulator", font = ('Segoe UI', 60, 'bold'), fg='#0049b5',)
title.pack()


train_photo = PhotoImage(file = "resources/train.png").subsample(2)
label = Label(main_window, image=train_photo)
label.place(x=50, y=310)

start_button = Button(main_window, 
                      text = 'Start', 
                      command = start,
                      bd=8,
                      bg='#0049b5',
                      fg='white',
                      width=9,
                      font = ('Segoe UI', 40, 'bold'),
                      activebackground='#0049b5',
                      activeforeground='black')
start_button.place(x = 1400, y = 350)
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
settings_button.place(x = 1400, y = 550)


mainloop()