import customtkinter as ctk
from settings import *

class ResultText(ctk.CTkLabel):
    def __init__(self, parent):
        super().__init__(master = parent, text = '22.5')
        self.grid(column = 0, row = 0, rowspan = 2, sticky = 'nswe')