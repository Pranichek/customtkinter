import customtkinter
from .read_json import read_json
import tkinter

dict = read_json(file_name="config.json")

width = dict["main_frame"]["width"]
height = dict["main_frame"]["height"]
title = dict["main_frame"]["title"]

app = customtkinter.CTk()
app.geometry(f"{width}x{height}")
app.title(title)


def optionmenu_callback(choice):
    print("optionmenu dropdown clicked:", choice)

optionmenu_var = customtkinter.StringVar(value="option 2")
optionmenu = customtkinter.CTkOptionMenu(app,values=["option 1", "option 2"],
                                         command=optionmenu_callback,
                                         variable=optionmenu_var)

optionmenu.pack(pady=20)

def radiobutton_event():
    print("radiobutton toggled, current value:", radio_var.get())

radio_var = tkinter.IntVar(value=0)
radiobutton_1 = customtkinter.CTkRadioButton(app, text="CTkRadioButton 1",
                                             command=radiobutton_event, variable= radio_var, value=1)
radiobutton_2 = customtkinter.CTkRadioButton(app, text="CTkRadioButton 2",
                                             command=radiobutton_event, variable= radio_var, value=2)


radiobutton_1.pack()
radiobutton_2.pack()

def segmented_button_callback(value):
    print("segmented button clicked:", value)

segemented_button_var = customtkinter.StringVar(value="Value 1")
segemented_button = customtkinter.CTkSegmentedButton(app, values=["Value 1", "Value 2", "Value 3"],
                                                     command=segmented_button_callback,
                                                     variable=segemented_button_var)

segemented_button.pack(side = "left",pady = 100 , padx = 100)

