import simpy.rt
import math
import tkinter as tk
import time
from tkintermapview import TkinterMapView
import traindataset
import numpy as np
import matplotlib.pyplot as plt
import datetime
from datetime import datetime
from pytz import timezone


vel= []
timelst = []

class map():
    def __init__(self,root,index):
        self.root = root
        self.map_widget = TkinterMapView(self.root,width=600,height=400,corner_radius=0)
        self.map_widget.place(x=1200,y=300)
        self.root.update()
        self.map_widget.set_tile_server("https://mt0.google.com/vt/lyrs=m&hl=e...{x}&y={y}&z={z}&s=Ga", max_zoom=22)
        self.map_widget.set_address("Delhi",marker=True)
        self.map_widget.set_address(traindataset.map[index]['destination'],marker=True)
        self.index = index
        path_1 = self.map_widget.set_path(traindataset.map[index]['pathlist'])
        self.root.update()
        self.map_widget.fit_bounding_box((30.782630667272393, 75.14595236585862),(28.60072822864227, 78.74207076565204))
        self.root.update()

def curve():
    # Create the main figure and subplots
    fig, axs = plt.subplots(1, 2, figsize=(8, 4))
    plt.title('Analytics')


    # Plot the speed-time curve on the first subplot
    axs[0].plot(timelst, vel)
    axs[0].set_title("Speed-Time Curve")
    axs[0].set_xlabel("Time: (minutes)")
    axs[0].set_ylabel("Speed: (km/hr)")

    # Create a bar graph of the top speed on the second subplot
    top_speed = np.max(vel)
    axs[1].bar(0, top_speed, width=0.2)
    axs[1].set_title("Top Speed")
    axs[1].set_xticks([])
    axs[1].set_ylabel("Speed: (km/hr)")

    plt.show()

class speedometer():
    # Set the self.canvas size and scale factor
    def __init__(self, root):
        self.root = root
        self.canvas_width = 600
        self.canvas_height = 450
        self.scale_factor = 1.2
        self.center_x = int(self.canvas_width * self.scale_factor) // 2
        self.center_y = int(self.canvas_height * self.scale_factor) // 2
        
        self.canvas = tk.Canvas(root, width=self.canvas_width, height=self.canvas_height)
        self.canvas.scale("all", 0, 0, self.scale_factor, self.scale_factor)
        self.canvas.place(x = 1200, y = 700)
        
        self.arc_start = 0
        self.arc_end = 180
        self.radius = int(200 * self.scale_factor)
        self.num_markings = 21  # 0 to 200 inclusive, with 10 unit increments
        self.marking_length = int(20 * self.scale_factor)
        self.speed=0
        self.draw()
        self.needle_length = self.radius - int(40 * self.scale_factor)
        self.needle_width = int(3 * self.scale_factor)
        self.lb = tk.Label(self.canvas,text='Km/Hr').place(x=self.center_x-25,y=self.center_y-150)
        

    # Create the self.canvas and scale it 


    # Set the center point of the arc

    # Set the self.radius of the arc

    # Draw the arc
    def draw(self):
        arc = self.canvas.create_arc(self.center_x - self.radius, self.center_y - self.radius, self.center_x + self.radius, self.center_y + self.radius, start=self.arc_start, extent=self.arc_end, style='arc',outline='blue')
        # Draw the markings with text
        for i in range(self.num_markings):
            value = i * 10
            theta = (1 - value / 200) * self.arc_end  # adjust theta angle to reverse direction
            theta_radians = math.radians(theta)
            x1 = self.center_x + (self.radius - self.marking_length) * math.cos(theta_radians)
            y1 = self.center_y - (self.radius - self.marking_length) * math.sin(theta_radians)
            x2 = self.center_x + self.radius * math.cos(theta_radians)
            y2 = self.center_y - self.radius * math.sin(theta_radians)
            self.canvas.create_line(x1, y1, x2, y2,fill="blue")
            text_x = self.center_x + (self.radius - self.marking_length - int(25 * self.scale_factor)) * math.cos(theta_radians)
            text_y = self.center_y - (self.radius - self.marking_length - int(25 * self.scale_factor)) * math.sin(theta_radians)
            self.canvas.create_text(text_x, text_y, text=str(value),fill='brown')
        needle_length = self.radius - int(40 * self.scale_factor)
        needle_width = int(3 * self.scale_factor)
        self.needle = self.canvas.create_line(self.center_x, self.center_y, self.center_x + needle_length, self.center_y, width=needle_width, fill='#0049b5')

    # Define a function to move the needle
    def move_needle(self,speed):
        angle = (1 - speed / 200) * self.arc_end  # adjust angle to reverse direction
        angle_radians = math.radians(angle)
        x2 = self.center_x + self.needle_length * math.cos(angle_radians)
        y2 = self.center_y - self.needle_length * math.sin(angle_radians)
        self.canvas.coords(self.needle, self.center_x, self.center_y, x2, y2)

    # Set the speed of the needle (0 to 200

    # Set the speed of the needle and move it every second
    def update_speed(self,speed1):
        self.move_needle(speed1)
        time.sleep(0.1)
        self.root.update()

class Train:
    def __init__(self, env, acceleration, retard, sp, index, waiting_time, root, output_frame):
        self.env = env
        self.acceleration = acceleration
        self.position = 0
        self.velocity = 0
        self.retard =  retard
        self.sp = sp
        self.i = index
        self.speed = traindataset.sard[self.i]['topspeed']
        self.slowdowndis = (self.speed**2)//(2*retard)
        self.wait = waiting_time
        self.root = root
        self.output_frame = output_frame
        sp.update_speed(0)
        
    def move(self):
        print(self.slowdowndis)
        current_station = 0
        l = len(traindataset.trains[self.i]['distances'])
        while(current_station<l):
            adj = True
            flag = False
            d = traindataset.trains[self.i]['distances'][current_station]/100
            name = traindataset.trains[self.i]['stations'][current_station]
            print(d)
            while(self.position<=d):
                yield self.env.timeout(1)
                if(self.velocity<self.speed and not(flag)):
                    self.velocity = self.velocity + self.acceleration
                    if(self.velocity>self.speed):
                     self.velocity=self.speed
                elif(d-self.position<=self.slowdowndis):
                    flag = True
                    a = (d-self.position)-self.slowdowndis
                    if(adj):
                        self.slowdowndis = self.slowdowndis + a
                        self.retard = (self.speed**2)/(2*self.slowdowndis)
                        print(f'new retard : {self.retard}')
                        adj = False
                    self.velocity-=self.retard
                if(self.velocity<0):
                    break

                self.position+=self.velocity
                a = self.velocity*(18/5)
                vel.append(a)
                timelst.append(self.env.now)
                self.sp.update_speed(speed1=a)
                # print(f'Velocity:{self.velocity}')

                
            print(f'[{datetime.now(timezone("Asia/Kolkata")).strftime("%H:%M:%S")}]: Train arrived at {name}')
            arrive_label = tk.Label(self.output_frame, text = f'[{datetime.now(timezone("Asia/Kolkata")).strftime("%H:%M:%S")}]: Train arrived at {name}', font = ('Segoe UI', 14), fg='black', width='80', anchor='w')
            arrive_label.pack()
            self.sp.update_speed(speed1=0)
            print(f'Waiting For Passengers To Get Out')
            waiting_label =  tk.Label(self.output_frame, text = 'Waiting For Passengers To Get Out', font = ('Segoe UI', 14), fg='black', width='80', anchor='w')
            waiting_label.pack()
            yield self.env.timeout(self.wait)
            if name!=traindataset.trains[self.i]['stations'][-1]:
                final_label = tk.Label(self.output_frame, text = f'[{datetime.now(timezone("Asia/Kolkata")).strftime("%H:%M:%S")}]: Train Leaving {name}', font = ('Segoe UI', 14), fg='black', width='80', anchor='w')
                final_label.pack()
            else:
                    destination_label = tk.Label(self.output_frame, text = f'[{datetime.now(timezone("Asia/Kolkata")).strftime("%H:%M:%S")}]: You have reached your destination', font = ('Segoe UI', 14), fg='black', width='80', anchor='w')
                    destination_label.pack()
                    anal_button = tk.Button(self.root, 
                                                text = 'Show Analytics',
                                                command=curve,
                                                bd=5,
                                                bg='#0049b5',
                                                fg='white',
                                                font = ('Segoe UI', 20, 'bold'),
                                                activebackground='#0049b5',
                                                activeforeground='black')
                    anal_button.place(x = 300, y = 900)
                    home_button = tk.Button(self.root,
                            text='Back',
                            command=self.root.destroy,
                            bd=5,
                            bg='#0049b5',
                            fg='white',
                            width=9,
                            font = ('Segoe UI', 20, 'bold'),
                            activebackground='#0049b5',
                            activeforeground='black')
                    home_button.place(x = 550, y = 900)
            current_station = current_station+1

class RailwayStation:
    def __init__(self, env, train, delay, index, root, output_frame):
        self.env = env
        self.train = train
        self.arrival_time = None
        self.train_board_delay = delay
        self.index = index
        self.root = root
        self.output_frame = output_frame

        
    def arrive (self):
        yield self.env.timeout(1)
        print(f'[{datetime.now(timezone("Asia/Kolkata")).strftime("%H:%M:%S")}]: You have arrived at the railway station')
        arrival_label = tk.Label(self.output_frame, text = f'[{datetime.now(timezone("Asia/Kolkata")).strftime("%H:%M:%S")}]: You have arrived at the railway station', font = ('Segoe UI', 14), fg='black', width='80', anchor='w')
        arrival_label.pack()        
        print(f' Train boarding will take {self.train_board_delay} minutes')
        boarding_time_label = tk.Label(self.output_frame, text = f'Train boarding will take {self.train_board_delay} minutes', font = ('Segoe UI', 14), fg='black', width='80', anchor='w')
        boarding_time_label.pack()
        self.root.update()
        yield self.env.timeout(self.train_board_delay)
        
        print(f'[{datetime.now(timezone("Asia/Kolkata")).strftime("%H:%M:%S")}]: You are now boarding the ' + traindataset.trains[self.index]['name'] )
        self.root.update()
        boarding_label = tk.Label(self.output_frame, text = f'[{datetime.now(timezone("Asia/Kolkata")).strftime("%H:%M:%S")}]: You are now boarding the ' + traindataset.trains[self.index]['name'], font = ('Segoe UI', 14), fg='black', width='80', anchor='w')
        boarding_label.pack()
        self.root.update()
        leaving_label = tk.Label(self.output_frame, text = f'[{datetime.now(timezone("Asia/Kolkata")).strftime("%H:%M:%S")}]: Train Leaving New Delhi Railway Station', font = ('Segoe UI', 14), fg='black', width='80', anchor='w')
        leaving_label.pack()
        self.root.update()
        
        self.env.process(self.train.move())

        

def run_simulation(acceleration,retard, index, waiting_time, root):
    output_frame = tk.Frame(root, borderwidth = 2, highlightbackground = '#0049b5', highlightthickness=1, relief=tk.SOLID, width='80')
    output_frame.pack(side=tk.TOP, padx=120, pady=220, anchor= tk.W)
    print(acceleration)
    print(retard)
    print(index)
    print(waiting_time)
    env = simpy.rt.RealtimeEnvironment(factor=0.1,strict=False)
    sp = speedometer(root)
    train = Train(env, acceleration, retard,sp, index, waiting_time, root, output_frame)
    railway_station = RailwayStation(env, train, waiting_time, index, root, output_frame)
    map_view = map(root,index)
    env.process(railway_station.arrive())
    env.run()
    root.mainloop()
