import customtkinter as ctk
import tkinter as tk
from settings import *
try:
    from ctypes import windll, byref, sizeof, c_int
except:
    pass
from widgets import *

class BMI(ctk.CTk):
    def __init__(self):
        # setup
        super().__init__(fg_color = GREEN)
        self.title("BMI")
        self.geometry('400x400')
        self.resizable(width = False, height = False)
        self.title_bar_color()

        # variables
        self.height = ctk.IntVar(value = 170)
        self.weight = ctk.DoubleVar(value = 65.0)
        self.bmi = ctk.StringVar()
        self.update_bmi(1, 2, 3)

        # layout
        self.columnconfigure(0, weight = 1)
        self.rowconfigure((0,1,2,3), weight = 1, uniform = 'a')

        # widgets
        ResultText(self, self.bmi)
        WeightInput(self, self.weight)
        HeightInput(self, self.height)
        UnitSwitch(self)

        self.height.trace_add('write', self.update_bmi)
        self.weight.trace_add('write', self.update_bmi)

        # run
        self.mainloop()

    def update_bmi(self, i, y, t):
        h_meter = self.height.get() / 100
        w_meter = self.weight.get()
        new_bmi = w_meter / (h_meter ** 2)
        new_bmi = round(new_bmi, 2)
        self.bmi.set(new_bmi)

    def title_bar_color(self):
        try:
            HWND = windll.user32.GetParent(self.winfo_id())
            DWMWA_ATTRIBUTE = 35
            COLOR = TITLE_HEX_COLOR
            windll.dwmapi.DwmSetWindowAttribute(HWND, DWMWA_ATTRIBUTE, byref(c_int(COLOR)), sizeof(c_int))
        except:
            pass

def main():
    bmi = BMI()
    bmi

if __name__=="__main__":
    main()
