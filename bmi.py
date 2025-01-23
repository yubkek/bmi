import customtkinter as ctk
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

        # layout
        self.columnconfigure(0, weight = 1)
        self.rowconfigure((0,1,2,3), weight = 1, uniform = 'a')

        # widgets
        ResultText(self)
        WeightInput(self)
        HeightInput(self)

        # run
        self.mainloop()

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
