import tkinter as tk
import tkinter.font 

'''
class BatteryApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Battery Power Bank")
        self.geometry("300x200")

        self.battery_level = 0

        self.label_battery = tk.Label(self, text="Battery Level: 0%")
        self.label_battery.pack(pady=10)

        self.button_increase = tk.Button(self, text="Increase", command=self.increase_battery)
        self.button_increase.pack(side="left", padx=10)

        self.button_decrease = tk.Button(self, text="Decrease", command=self.decrease_battery)
        self.button_decrease.pack(side="right", padx=10)

    def update_battery_label(self):
        self.label_battery.config(text="Battery Level: {}%".format(self.battery_level))

    def increase_battery(self):
        if self.battery_level < 200:
            self.battery_level += 10
            self.update_battery_label()
    

    def decrease_battery(self):
        if self.battery_level > 0:
            self.battery_level -= 10
            self.update_battery_label()
            
    def check_available_fonts(self):
        available_fonts = tkinter.font.families()
        for font in available_fonts:
            print(font)



if __name__ == "__main__":
    app = BatteryApp()
    app.check_available_fonts()
    app.mainloop()
'''

import tkinter as tk
from tkinter import ttk

class StartPage(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)

        # Ensure the style instance is accessible
        self.style = ttk.Style()
        self.style.configure("TButton1",
                             foreground="#000000",
                             background="#ff0000",  # Red
                             width=20,
                             font=("Comic Sans MS", 10),
                             padding=[10, 10, 10, 10])

        self.style.configure("TButton2",
                             foreground="#000000",
                             background="#ffff00",  # Yellow
                             width=20,
                             font=("Comic Sans MS", 10),
                             padding=[10, 10, 10, 10])

        self.style.configure("TButton3",
                             foreground="#000000",
                             background="#00ff00",  # Green
                             width=20,
                             font=("Comic Sans MS", 10),
                             padding=[10, 10, 10, 10])

        button1 = ttk.Button(self, text="Practice Mode 練習模式",
                                  style="TButton1",
                                  width=20,)
                                  #command=lambda: controller.show_frame(PageOne))
        button1.pack(pady=20, side="top")

        button2 = ttk.Button(self, text="Test Mode 測試模式",
                                  style="TButton2",
                                  width=20,)
                                  #command=lambda: controller.show_frame(PageTwo))
        button2.pack(pady=20, side="top")

        button3 = ttk.Button(self, text="Games - 遊戲",
                                  style="TButton3",
                                  width=20,)
                                  #command=lambda: controller.show_frame(PageThree))
        button3.pack(pady=20)

class SampleApp(tk.Tk):
    def __init__(self):
        super().__init__()

        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (StartPage,):  # removed PageOne, PageTwo, PageThree
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(StartPage)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()

if __name__ == "__main__":
    
    app = SampleApp()
    app.mainloop()
