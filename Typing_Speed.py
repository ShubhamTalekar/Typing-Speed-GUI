import tkinter as tk
import time
import random
import threading
from tkinter.constants import END, S
import os

class typespeedGUI:
    def __init__(self):
        self.r =tk.Tk()
        self.r.title("Typing Speed Test")
        self.r.geometry("800x600")
        
        self.texts = "This is a test can you pass?"#open("text.txt", "r").read().split("\n")
        
        self.frame = tk.Frame(self.r)
        
        self.sample_label = tk.Label(self.frame, text = random.choice(self.texts), font=("Helvetica", 18))
        self.sample_label.grid(row=0, column=0, columnspan=2, padx=5, pady=10)
        
        self.input_entry = tk.Entry(self.frame, width=40, font=("Helvetica", 24))
        self.input_entry.grid(row=1, column=0, columnspan=2, padx=5, pady=10)
        self.input_entry.bind("<KeyPress>", self.start)
        
        self.speed_label = tk.Label(self.frame, text = "Speed : \n0.00 CPS\n0.00 CPM", font=("Helvetica", 18))
        self.speed_label.grid(row=2, column=0, columnspan=2, padx=5, pady=10)
        
        self.resetbutton = tk.Button(self.frame, text="Reset", command=self.reset)
        self.resetbutton.grid(row=3, column=0, columnspan=2, padx=5, pady=10)
        
        self.frame.pack(expand=True)
        
        self.counter = 0
        self.running = False
        
        self.r.mainloop()
        
    def start(self):
        if not self.running:
            if not tk.Event.keycode in [16, 17 ,18]:
                self.running =True
                t = threading.Thread(target=self.time_thread)
                t.start()
        if not self.sample_label.cget('text').startswith(self.input_entry.get()):
            self.input_entry.config(fg="red")
        else:
            self.input_entry.config(fg="black")
        if self.input_entry.get()==self.sample_label.cget('text')[:-1]:
            self.running = False
            self.input_entry.config(fg="green")
            
    def time_thread(self):
        while self.running:
            time.sleep(0.1)
            self.counter += 0.1
            cps = len(self.input_entry.get())/self.counter
            cpm = cps * 60
            self.speed_label.config(text =f"Speed: \n{cps:.2f}, CPS\n{cpm:.2f} CPM")
    
    def reset(self):
        self.running = False
        self.counter = 0
        self.speed_label.config(text ="Speed : \n0.00 CPS\n0.00 CPM")
        self.sample_label.config(text = random.choice(self.texts))
        self.input_entry.delete(0, tk.END)
    
typespeedGUI()