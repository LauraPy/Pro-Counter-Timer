
import time
from tkinter import *
from tkinter import messagebox

class CountdownApp:
    def __init__(self, root):
        self.root = root
        self.root.geometry("350x300")
        self.root.title("Pro Countdown Timer")
        self.root.config(bg="#e40909")
        self.root.attributes('-alpha',0.9)
        
        self.is_running = False
        self.temp = 0

        # Variables
        self.hour = StringVar(value="00")
        self.minute = StringVar(value="00")
        self.second = StringVar(value="00")

        # UI Design
        Label(root, text="COUNTDOWN", font=("Arial", 14, "bold"), bg="#000000", fg="white",bd=2, relief="groove").pack(pady=10)
        
        entry_frame = Frame(root, bg="#e41616")
        entry_frame.pack(pady=10)

        # Entry fields
        self.create_entry(entry_frame, self.hour).grid(row=0, column=0, padx=5)
        self.create_entry(entry_frame, self.minute).grid(row=0, column=1, padx=5)
        self.create_entry(entry_frame, self.second).grid(row=0, column=2, padx=5)

        # Buttons
        self.start_btn = Button(root, text="START", bg="#0f0f0f", fg="white", width=10, command=self.start_timer)
        self.start_btn.pack(pady=5)

        self.stop_btn = Button(root, text="STOP", bg="#0c0c0c", fg="white", width=10, command=self.stop_timer)
        self.stop_btn.pack(pady=5)

        self.reset_btn = Button(root, text="RESET", bg="#111111", fg="white", width=10, command=self.reset_timer)
        self.reset_btn.pack(pady=5)

    def create_entry(self, frame, var):
        return Entry(frame, textvariable=var, width=3, font=("Courier", 24, "bold"), 
                     bg="#0F0F0F", fg="#fcf9f9", justify="center", insertbackground="white")

    def start_timer(self):
        if not self.is_running:
            try:
                self.temp = int(self.hour.get())*3600 + int(self.minute.get())*60 + int(self.second.get())
            except ValueError:
                messagebox.showerror("Error", "Please enter numbers only")
                return
            
            if self.temp > 0:
                self.is_running = True
                self.countdown()

    def countdown(self):
        if self.is_running and self.temp >= 0:
            mins, secs = divmod(self.temp, 60)
            hours, mins = divmod(mins, 60)

            self.hour.set(f"{hours:02d}")
            self.minute.set(f"{mins:02d}")
            self.second.set(f"{secs:02d}")

            if self.temp == 0:
                self.is_running = False
                messagebox.showinfo("Time's Up", "Countdown finished!")
            else:
                self.temp -= 1
                self.root.after(1000, self.countdown)

    def stop_timer(self):
        self.is_running = False

    def reset_timer(self):
        self.is_running = False
        self.temp = 0
        self.hour.set("00")
        self.minute.set("00")
        self.second.set("00")


    
root = Tk()
app = CountdownApp(root)
root.mainloop()
