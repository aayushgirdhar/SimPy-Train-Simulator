import simpy.rt
import math
import random
import math
import tkinter as tk
import time
from tkintermapview import *
import traindataset

# Create the Tkinter window
root = tk.Tk()
root.geometry('1280x720')


class speedometer():
    # Set the self.canvas size and scale factor
    def __init__(self):
        self.canvas_width = 500
        self.canvas_height = 500
        self.scale_factor = 1
        self.center_x = int(self.canvas_width * self.scale_factor) // 2
        self.center_y = int(self.canvas_height * self.scale_factor) // 2
        self.canvas = tk.Canvas(root, width=self.canvas_width, height=self.canvas_height)
        self.canvas.scale("all", 0, 0, self.scale_factor, self.scale_factor)
        self.canvas.place(x=400,y=50)
        self.arc_start = 0
        self.arc_end = 180
        self.radius = int(200 * self.scale_factor)
        self.num_markings = 21  # 0 to 200 inclusive, with 10 unit increments
        self.marking_length = int(20 * self.scale_factor)
        self.speed=0
        self.draw()
        self.needle_length = self.radius - int(40 * self.scale_factor)
        self.needle_width = int(3 * self.scale_factor)
        

    # Create the self.canvas and scale it


    # Set the center point of the arc

    # Set the self.radius of the arc

    # Draw the arc
    def draw(self):
        arc = self.canvas.create_arc(self.center_x - self.radius, self.center_y - self.radius, self.center_x + self.radius, self.center_y + self.radius, start=self.arc_start, extent=self.arc_end, style='arc')
        # Draw the markings with text
        for i in range(self.num_markings):
            value = i * 10
            theta = (1 - value / 200) * self.arc_end  # adjust theta angle to reverse direction
            theta_radians = math.radians(theta)
            x1 = self.center_x + (self.radius - self.marking_length) * math.cos(theta_radians)
            y1 = self.center_y - (self.radius - self.marking_length) * math.sin(theta_radians)
            x2 = self.center_x + self.radius * math.cos(theta_radians)
            y2 = self.center_y - self.radius * math.sin(theta_radians)
            self.canvas.create_line(x1, y1, x2, y2)
            text_x = self.center_x + (self.radius - self.marking_length - int(25 * self.scale_factor)) * math.cos(theta_radians)
            text_y = self.center_y - (self.radius - self.marking_length - int(25 * self.scale_factor)) * math.sin(theta_radians)
            self.canvas.create_text(text_x, text_y, text=str(value))
        needle_length = self.radius - int(40 * self.scale_factor)
        needle_width = int(3 * self.scale_factor)
        self.needle = self.canvas.create_line(self.center_x, self.center_y, self.center_x + needle_length, self.center_y, width=needle_width, fill='red')

    # Define a function to move the needle
    def move_needle(self,speed):
        angle = (1 - speed / 200) * self.arc_end  # adjust angle to reverse direction
        angle_radians = math.radians(angle)
        x2 = self.center_x + self.needle_length * math.cos(angle_radians)
        y2 = self.center_y - self.needle_length * math.sin(angle_radians)
        self.canvas.coords(self.needle, self.center_x, self.center_y, x2, y2)

    # Set the speed of the needle (0 to 200
    # Move the needle initially

    # Set the speed of the needle and move it every second
    def update_speed(self,speed1):
        self.move_needle(speed1)
        time.sleep(0.1)
        root.update()
 
map_widget = TkinterMapView(root,width=500,height=500)
map_widget.place(x=150,y=300)
map_widget.set_tile_server("https://mt0.google.com/vt/lyrs=m&hl=en&x={x}&y={y}&z={z}&s=Ga")
delchdpathlst = [(28.668599920844756, 77.20044427610303),(28.994171577218825, 77.01441420757034), (29.413128099019627, 76.96481089994793), (29.99229637203275, 76.86211939091326),(29.98160834083052, 76.84663127808665),(30.70643990617078, 76.82081632927672)]
path_1 = map_widget.set_path(delchdpathlst)

map_widget.set_address("Delhi",marker=True)
map_widget.set_marker(30.70643990617078, 76.82081632927672,text='Chandigarh')
map_widget.fit_bounding_box((30.782630667272393, 75.14595236585862),(28.60072822864227, 78.74207076565204))

class Train:
    def __init__(self, env, speed, acceleration,retard,sp):
        self.env = env
        self.speed = speed
        self.acceleration = acceleration
        self.position = 0
        self.velocity = 0
        self.retard =  retard
        self.slowdowndis = (self.speed**2)//(2*retard)
        self.sp = sp
        
    def move(self):
        print(self.slowdowndis)
        current_station = 0
        l = len(traindataset.trains[0]['distances'])
        while(current_station<l):
            adj = True
            flag = False
            d = traindataset.trains[0]['distances'][current_station]/10
            print(d)
            while(self.position<=d):
                yield self.env.timeout(1)
                if(self.velocity<self.speed and not(flag)):
                    self.velocity = self.velocity + acceleration
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
                self.sp.update_speed(speed1=self.velocity)
                print(f'Velocity:{self.velocity}')
                
            name = traindataset.trains[0]['stations'][current_station]
            print(f'Train arrived at {name} at {self.env.now}')
            print(f'Waiting For Passengers To Get Out')
            yield self.env.timeout(15)
            current_station = current_station+1
        print('Train arrived at the destination')
                 
        # while(self.position<traindataset.trains[0]['distances'][ct] and ct<l-1):
        #         yield self.env.timeout(1)
        #         if ((self.velocity<self.speed) and not(flag)):
        #             self.velocity+=self.acceleration
        #             if(self.velocity>self.speed):
        #                 self.velocity = self.speed   
        #         elif(traindataset.trains[0]['distances'][ct]-self.position<=self.slowdowndis):
        #             print('retard')
        #             a = (traindataset.trains[0]['distances'][ct] - self.position) - self.slowdowndis
        #             if(adj):
        #                 self.slowdowndis = self.slowdowndis + a
        #                 self.retard = (self.speed**2)/(2*self.slowdowndis)
        #                 print(f'new retard : {self.retard}')
        #                 adj = False
        #             print(f'd:{a}')
        #             self.velocity-=self.retard
        #         if(self.velocity<=0):
        #             break
        #         self.position+=self.velocity
        #         update_speed(self.velocity)
        #         name = traindataset.trains[0]['stations'][ct]
        #         print(f'Train arrived at {name} at {self.env.now}')
        #         ct+=1
        #         print(self.position)
        #         a = (traindataset.trains[0]['distances'][ct] - self.position) - self.slowdowndis
        #         print(f'diff:{a}')
        # print(f'Train arrived arrived at the station after {self.env.now} seconds')
       
            

class RailwayStation:
    def __init__(self, env, train,delay):
        self.env = env
        self.train = train
        self.arrival_time = None
        self.train_board_delay = delay

        
    def arrive (self):
        yield self.env.timeout(1)
        print(f'You have arrived at the railway station at {self.env.now}')
        print(f'Train boarding will take {self.train_board_delay} minutes')
        yield self.env.timeout(self.train_board_delay)
        print(f'You are now boarding the train at {self.env.now}')
        self.env.process(self.train.move())

        

def run_simulation(destination, top_speed, acceleration,retard):
    env = simpy.rt.RealtimeEnvironment(factor=0.1,strict=False)
    sp = speedometer()
    train = Train(env, top_speed, acceleration, destination,retard,sp)
    railway_station = RailwayStation(env, train,board_delay)
    env.process(railway_station.arrive())
    env.run()
    root.mainloop()
   

top_speed = 36.11 # m/s
acceleration = 2 # m/s^2
retard = 5
board_delay = 5

arrival_time = run_simulation(top_speed, acceleration,retard)

