import customtkinter as ctk
from settings import *

class ResultText(ctk.CTkLabel):
    def __init__(self, parent):
        font = ctk.CTkFont(family = FONT, size = MAIN_TEXT_SIZE, weight = 'bold')
        super().__init__(master = parent, text = '22.5', font = font)
        self.grid(column = 0, row = 0, rowspan = 2, sticky = 'nswe')

class WeightInput(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(master = parent, fg_color = WHITE)
        self.grid(column = 0, row = 2, sticky = 'nswe', padx = 10, pady = 10)

        self.rowconfigure(0, weight = 1, uniform = 'b')
        self.columnconfigure(0, weight = 2, uniform = 'b')
        self.columnconfigure(1, weight = 1, uniform = 'b')
        self.columnconfigure(2, weight = 3, uniform = 'b')
        self.columnconfigure(3, weight = 1, uniform = 'b')
        self.columnconfigure(4, weight = 2, uniform = 'b')

        # weight display
        font = ctk.CTkFont(family = FONT, size = INPUT_FONT_SIZE)
        label = ctk.CTkLabel(self, text = '70kg', text_color = BLACK, font = font)
        label.grid(row = 0, column = 2)
        
        # buttons
        minus_button = ctk.CTkButton(self, text = '-', font = font, text_color = BLACK, fg_color = LIGHT_GRAY, hover_color = GRAY, corner_radius = BUTTON_CORNER_RADIUS) 
        minus_button.grid(row = 0, column = 0, sticky = 'ns', padx = 8, pady = 8)
        mini_minus_button = ctk.CTkButton(self, text = '-', font = font, text_color = BLACK, fg_color = LIGHT_GRAY, hover_color = GRAY, corner_radius = BUTTON_CORNER_RADIUS) 
        mini_minus_button.grid(row = 0, column = 1, padx = 4, pady = 4)

        plus_button = ctk.CTkButton(self, text = '+', font = font, text_color = BLACK, fg_color = LIGHT_GRAY, hover_color = GRAY, corner_radius = BUTTON_CORNER_RADIUS) 
        plus_button.grid(row = 0, column = 4, sticky = 'ns', padx = 8, pady = 8)
        mini_plus_button = ctk.CTkButton(self, text = '+', font = font, text_color = BLACK, fg_color = LIGHT_GRAY, hover_color = GRAY, corner_radius = BUTTON_CORNER_RADIUS) 
        mini_plus_button.grid(row = 0, column = 3, padx = 4, pady = 4)

class HeightInput(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(master = parent, fg_color = WHITE)
        self.grid(column = 0, row = 3, sticky = 'nswe', padx = 10, pady = 10)

        slider = ctk.CTkSlider(self, button_color = GREEN, button_hover_color = GRAY, progress_color = GREEN, fg_color = LIGHT_GRAY)
        slider.pack(side = 'left', fill = 'x', expand = True, pady = 10, padx = 10)

        output = ctk.CTkLabel(self, text = '1.80', text_color = BLACK, font = ctk.CTkFont(family = FONT, size = INPUT_FONT_SIZE))
        output.pack(side = 'left', padx = 20)