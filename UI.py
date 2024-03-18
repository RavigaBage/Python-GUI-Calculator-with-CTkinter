import customtkinter
import tkinter as tk
import math
from fractions import Fraction
from decimal import Decimal
from ctypes import windll, byref, create_unicode_buffer, create_string_buffer
from sympy import Symbol, solve
from sympy import Matrix as Mx
import ast


FR_PRIVATE = 0x10
FR_NOT_ENUM = 0x20


customtkinter.set_appearance_mode("dark")

customtkinter.set_default_color_theme("dark-blue")
root = customtkinter.CTk()
root.geometry("380x570")

WINW = 380
WINH = 570
FunctionFramesBtnWidth = (WINW / 6) - 4
FramesBtnWidth = (WINW / 5) - 3

frame = customtkinter.CTkFrame(master=root)
frame.grid(column=5, row=4)

x = Symbol("x")
OriginalData = ""
numericObg = ""
basicArrays = ["+", "-", "÷", "×"]
complexArrays = ["R", "D", "t", "c", "S", "l", "π", "√", "%", "x²"]
subscriptValues = [
    "\u2080",
    "\u2081",
    "\u2082",
    "\u2083",
    "\u2084",
    "\u2085",
    "\u2086",
    "\u2087",
    "\u2088",
    "\u2089",
]
subscript_move = False
userInput = []
new = []
ExpFormation = ""
Ans = " "
data = ""
# modes
PerformSpeed = False
PerformEquation = False
PerformMatrix = False
PerformTime = False
PerformTemperature = False
PerformMass = False
PerformVolume = False
PerformArea = False
PerformLength = False
mode_menu_convert = False
resetFrames = 0

SpeedAns = ""
SpeedData = ""
Equation = False
AMatrix = False
BMatrix = False
Matrix = False
Expression = False
compute = True
volume = False
Length = False
speed = False
Area = False
Time = False
Temperature = False
Mass = False
ConvertTo = 0
ConvertFrom = 0
mode_more = 0
direction = False

his_data = customtkinter.StringVar()
MenuFrame = customtkinter.CTkFrame(
    master=frame,
    width=WINW,
    height=140,
    fg_color="#2c2c2c",
    corner_radius=0,
)
ModeMenu_main_convert_speed = customtkinter.CTkFrame(
    master=MenuFrame,
    width=WINW,
    height=140,
    fg_color="#2c2c2c",
    corner_radius=0,
)
ModeMenu_main_convert_Time = customtkinter.CTkFrame(
    master=MenuFrame,
    width=WINW,
    height=140,
    fg_color="#2c2c2c",
    corner_radius=0,
)
ModeMenu_main_convert_Length = customtkinter.CTkFrame(
    master=MenuFrame,
    width=WINW,
    height=140,
    fg_color="#2c2c2c",
    corner_radius=0,
)
ModeMenu_main_convert_Temperature = customtkinter.CTkFrame(
    master=MenuFrame,
    width=WINW,
    height=140,
    fg_color="#2c2c2c",
    corner_radius=0,
)
ModeMenu_main_convert_Mass = customtkinter.CTkFrame(
    master=MenuFrame,
    width=WINW,
    height=140,
    fg_color="#2c2c2c",
    corner_radius=0,
)
ModeMenu_main_convert_equation = customtkinter.CTkFrame(
    master=MenuFrame,
    width=WINW,
    height=140,
    fg_color="#2c2c2c",
    corner_radius=0,
)
ModeMenu_main_convert_matrix = customtkinter.CTkFrame(
    master=MenuFrame,
    width=WINW,
    height=140,
    fg_color="#2c2c2c",
    corner_radius=0,
)

MenuFrame.grid(column=1, row=2)
entry = customtkinter.CTkTextbox(
    master=MenuFrame,
    width=WINW,
    height=140,
    font=("casio-fx-9860gii", 24),
    fg_color="#2c2c2c",
    corner_radius=0,
)
ModeMenu_main_convert = customtkinter.CTkFrame(
    master=MenuFrame,
    width=WINW,
    height=140,
    fg_color="#2c2c2c",
    corner_radius=0,
)
ModeMenu_main_convert_select = customtkinter.CTkFrame(
    master=MenuFrame,
    width=WINW,
    height=140,
    fg_color="#2c2c2c",
    corner_radius=0,
)
ModeMenu_main_convert_Area = customtkinter.CTkFrame(
    master=MenuFrame,
    width=WINW,
    height=140,
    fg_color="#2c2c2c",
    corner_radius=0,
)
ModeMenu_main_convert_volume = customtkinter.CTkFrame(
    master=MenuFrame,
    width=WINW,
    height=140,
    fg_color="#2c2c2c",
    corner_radius=0,
)
ModeMenu_main_convert_select_speed = customtkinter.CTkFrame(
    master=MenuFrame,
    width=WINW,
    height=140,
    fg_color="#2c2c2c",
    corner_radius=0,
)
ModeMenu_main_convert_select_Length = customtkinter.CTkFrame(
    master=MenuFrame,
    width=WINW,
    height=140,
    fg_color="#2c2c2c",
    corner_radius=0,
)
ModeMenu_main_convert_select_matrix = customtkinter.CTkFrame(
    master=MenuFrame,
    width=WINW,
    height=140,
    fg_color="#2c2c2c",
    corner_radius=0,
)

ModeMenu_main_modes = customtkinter.CTkFrame(
    master=MenuFrame,
    width=WINW,
    height=140,
    fg_color="#2c2c2c",
    corner_radius=0,
)
ModeMenu_main_convert_select_Time = customtkinter.CTkFrame(
    master=MenuFrame,
    width=WINW,
    height=140,
    fg_color="#2c2c2c",
    corner_radius=0,
)

ModeMenu_main_convert_select_equation = customtkinter.CTkFrame(
    master=MenuFrame,
    width=WINW,
    height=140,
    fg_color="#2c2c2c",
    corner_radius=0,
)

ModeMenu_main_convert_select_Temperature = customtkinter.CTkFrame(
    master=MenuFrame,
    width=WINW,
    height=140,
    fg_color="#2c2c2c",
    corner_radius=0,
)
ModeMenu_main_convert_select_Area = customtkinter.CTkFrame(
    master=MenuFrame,
    width=WINW,
    height=140,
    fg_color="#2c2c2c",
    corner_radius=0,
)
ModeMenu_main_convert_select_volume = customtkinter.CTkFrame(
    master=MenuFrame,
    width=WINW,
    height=140,
    fg_color="#2c2c2c",
    corner_radius=0,
)
ModeMenu_main_convert_select_Mass = customtkinter.CTkFrame(
    master=MenuFrame,
    width=WINW,
    height=140,
    fg_color="#2c2c2c",
    corner_radius=0,
)

entry_Time = customtkinter.CTkTextbox(
    master=ModeMenu_main_convert_select_Time,
    width=WINW,
    height=100,
    font=("Roboto", 24),
    fg_color="#2c2c2c",
    corner_radius=0,
)

entry_equation = customtkinter.CTkTextbox(
    master=ModeMenu_main_convert_select_equation,
    width=WINW,
    height=100,
    font=("Roboto", 24),
    fg_color="#2c2c2c",
    corner_radius=0,
)
entry_matrix = customtkinter.CTkTextbox(
    master=ModeMenu_main_convert_select_matrix,
    width=WINW,
    height=100,
    font=("Roboto", 24),
    fg_color="#2c2c2c",
    corner_radius=0,
)


entry_Length = customtkinter.CTkTextbox(
    master=ModeMenu_main_convert_select_Length,
    width=WINW,
    height=100,
    font=("Roboto", 24),
    fg_color="#2c2c2c",
    corner_radius=0,
)
entry_speed = customtkinter.CTkTextbox(
    master=ModeMenu_main_convert_select_speed,
    width=WINW,
    height=100,
    font=("Roboto", 24),
    fg_color="red",
    corner_radius=0,
)
entry_volume = customtkinter.CTkTextbox(
    master=ModeMenu_main_convert_select_volume,
    width=WINW,
    height=100,
    font=("Roboto", 24),
    fg_color="red",
    corner_radius=0,
)
entry_Temperature = customtkinter.CTkTextbox(
    master=ModeMenu_main_convert_select_Temperature,
    width=WINW,
    height=100,
    font=("Roboto", 24),
    fg_color="blue",
    corner_radius=0,
)
entry_Mass = customtkinter.CTkTextbox(
    master=ModeMenu_main_convert_select_Mass,
    width=WINW,
    height=100,
    font=("Roboto", 24),
    fg_color="#2c2c2c",
    corner_radius=0,
)
entry_Area = customtkinter.CTkTextbox(
    master=ModeMenu_main_convert_select_Area,
    width=WINW,
    height=100,
    font=("Roboto", 24),
    fg_color="#2c2c2c",
    corner_radius=0,
)
entry.grid(column=1, row=1)

label = customtkinter.CTkLabel(
    master=frame,
    width=WINW,
    textvariable=his_data,
    height=70,
    font=("Roboto", 16),
    corner_radius=0,
)
label.grid(column=1, row=1)
FunctionFrames = customtkinter.CTkFrame(
    master=frame,
    width=WINW,
    height=90,
    fg_color="#2c2c2c",
    corner_radius=0,
)
FunctionFrames.grid(columnspan=5, row=3)

FunctionFrames_innerFrame = customtkinter.CTkFrame(
    master=FunctionFrames,
    width=WINW,
    height=90,
    corner_radius=0,
)
FunctionFrames_innerFrame.grid(column=6, row=4)

Btns_innerFrame = customtkinter.CTkFrame(
    master=frame,
    width=WINW,
    height=90,
    fg_color="red",
    corner_radius=0,
)
Btns_innerFrame.grid(columnspan=5, row=4)

Btns_innserFrame_innerFrame = customtkinter.CTkFrame(
    master=Btns_innerFrame,
    width=WINW,
    height=90,
    corner_radius=0,
)
Btns_innserFrame_innerFrame.grid(column=5, row=4)
direction = 0


ControlFrameBtns = customtkinter.CTkFrame(
    master=FunctionFrames_innerFrame,
    width=FunctionFramesBtnWidth * 2,
    height=35 * 2,
)
ControlFrameBtns.grid(
    row=2, rowspan=2, column=3, columnspan=2, padx=(0, 3), pady=(0, 5)
)

ControlFrameBtnsFrame = customtkinter.CTkFrame(
    master=ControlFrameBtns,
    width=FunctionFramesBtnWidth * 2,
    fg_color="#2c2c2c",
    height=35 * 2,
)
ControlFrameBtnsFrame.grid(
    row=3,
    column=3,
)
controlBtnWidth = (FunctionFramesBtnWidth * 2) / 3
controlBtnHeight = 30
buttonUp = customtkinter.CTkButton(
    master=ControlFrameBtnsFrame,
    text="↑",
    font=("Roboto", 15, "bold"),
    width=controlBtnWidth,
    height=controlBtnHeight,
    fg_color="#000",
    hover_color="#0773a4",
    command=lambda: CursorPosition("u"),
)
buttonUp.grid(row=1, column=2)

buttonDown = customtkinter.CTkButton(
    master=ControlFrameBtnsFrame,
    text="↓",
    font=("Roboto", 15, "bold"),
    width=controlBtnWidth,
    height=controlBtnHeight,
    fg_color="#000",
    hover_color="#0773a4",
    command=lambda: CursorPosition("d"),
)
buttonDown.grid(row=3, column=2)


buttonleft = customtkinter.CTkButton(
    master=ControlFrameBtnsFrame,
    text="←",
    font=("Roboto", 15, "bold"),
    width=controlBtnWidth,
    height=controlBtnHeight,
    fg_color="#000",
    hover_color="#0773a4",
    command=lambda: CursorPosition("l"),
)
buttonleft.grid(
    row=2,
    column=1,
)

buttonright = customtkinter.CTkButton(
    master=ControlFrameBtnsFrame,
    text="→",
    font=("Roboto", 15, "bold"),
    width=controlBtnWidth,
    height=controlBtnHeight,
    fg_color="#000",
    hover_color="#0773a4",
    command=lambda: CursorPosition("r"),
)
buttonright.grid(row=2, column=3, padx=(0, 3), pady=(0, 5))
ActiveEntry = entry


def CursorPosition(dr):
    global ActiveEntry
    ActiveEntry.focus_set()
    cursor = ActiveEntry.index("insert")
    splitData = cursor.split(".")
    Vertical = splitData[0]
    horizontal = splitData[1]
    if dr == "l":
        if int(horizontal) >= 0:
            horizontal = int(horizontal) - 1
    if dr == "r":
        if int(horizontal) >= 0:
            horizontal = int(horizontal) + 1
    if dr == "d":
        if int(Vertical) >= 0:
            Vertical = int(Vertical) + 1
    if dr == "u":
        if int(Vertical) >= 0:
            Vertical = int(Vertical) - 1
    newCursor = str(Vertical) + "." + str(horizontal)
    print(newCursor)
    ActiveEntry.mark_set("insert", newCursor)


def Convertion_speed(a, b, val):
    Ans = val
    val = int(val)
    # m/s
    if a == 0 and b == 0:  # m/s - m/h
        Ans = val
    elif a == 0 and b == 1:  # m/s - m/h
        Ans = val * 3600
    elif a == 0 and b == 2:  # m/s - km/s
        Ans = val * 0.001
    elif a == 0 and b == 3:  # m/s - km/h
        Ans = val * 3.6
    elif a == 0 and b == 4:  # m/s - in/s
        Ans = val * 39.37007877402
    elif a == 0 and b == 5:  # m/s - in/h
        Ans = val * 141732.28346457
    elif a == 0 and b == 6:  # m/s - mi/s
        Ans = val * 0.006213712
    elif a == 0 and b == 7:  # m/s - mi/h
        Ans = val * 2.2369362921
    # m/h
    elif a == 1 and b == 0:  # m/h - m/s
        Ans = val * 0.0002777778
    elif a == 1 and b == 1:  # m/h - m/h
        Ans = val
    elif a == 1 and b == 2:  # m/h - km/s
        Ans = val * 1 / 3600000
    elif a == 1 and b == 3:  # m/h - km/h
        Ans = val * 0.001
    elif a == 1 and b == 4:  # m/h - in/s
        Ans = val * 0.010936133
    elif a == 1 and b == 5:  # m/h - in/h
        Ans = val * 39.37007877402
    elif a == 1 and b == 6:  # m/h - mi/s
        Ans = val * 0
    elif a == 1 and b == 7:  # m/h - mi/h
        Ans = val * 0.006213712
    # km/s
    elif a == 2 and b == 0:  # km/s - m/s
        Ans = val * 1000
    elif a == 2 and b == 1:  # km/s - m/h
        Ans = val * 3600000
    elif a == 2 and b == 2:  # km/s - km/s
        Ans = val
    elif a == 2 and b == 3:  # km/s - km/h
        Ans = val * 3600
    elif a == 2 and b == 4:  # km/s - in/s
        Ans = val * 39370.0787740157
    elif a == 2 and b == 5:  # km/s - in/h
        Ans = val * 141732283.46457
    elif a == 2 and b == 6:  # km/s - mi/s
        Ans = val * 0.06213711922
    elif a == 2 and b == 7:  # km/s - mi/h
        Ans = val * 2236.9362920544
    # km/h
    elif a == 3 and b == 0:  # km/h - m/s
        Ans = val * 0.2777777778
    elif a == 3 and b == 1:  # km/h - m/h
        Ans = val * 1000
    elif a == 3 and b == 2:  # km/h - km/s
        Ans = val * 0.0002777778
    elif a == 3 and b == 3:  # km/h
        Ans = val * 1
    elif a == 3 and b == 4:  # km/h - in/s
        Ans = val * 10.9361329834
    elif a == 3 and b == 5:  # km/h - in/h
        Ans = val * 39370.078740157
    elif a == 3 and b == 6:  # km/h - mi/s
        Ans = val * 0.0001726031
    elif a == 3 and b == 7:  # kh/s - mi/h
        Ans = val * 0.06213711922
    # in/s
    elif a == 4 and b == 0:  # in/s - m/s
        Ans = val * 0.0254
    elif a == 4 and b == 1:  # in/s - m/h
        Ans = val * 91.44
    elif a == 4 and b == 2:  # in/s - km/s
        Ans = val * 0.0000254
    elif a == 4 and b == 3:  # in/s - km/h
        Ans = val * 0.09144
    elif a == 4 and b == 4:  # in/s - in/s
        Ans = val * 1
    elif a == 4 and b == 5:  # in/s - in/h
        Ans = val * 3600
    elif a == 4 and b == 6:  # in/s - mi/s
        Ans = val * 0.0000157828
    elif a == 4 and b == 7:  # in/s - mi/h
        Ans = val * 0.0568181818
    # in/h
    elif a == 5 and b == 0:  # in/h - m/s
        Ans = val * 0.0000070556
    elif a == 5 and b == 1:  # in/h - m/h
        Ans = val * 0.0254
    elif a == 5 and b == 2:  # in/h - km/s
        Ans = val * 0
    elif a == 5 and b == 3:  # in/h - km/h
        Ans = val * 0.0000254
    elif a == 5 and b == 4:  # in/h - in/s
        Ans = val * 0.0002777778
    elif a == 5 and b == 5:  # in/h - in/h
        Ans = val * 1
    elif a == 5 and b == 6:  # in/h - mi/s
        Ans = val * 0
    elif a == 5 and b == 7:  # in/h - mi/h
        Ans = val * 0.0000157828
    # mi/s
    elif a == 6 and b == 0:  # mi/s - m/s
        Ans = val * 1609.344
    elif a == 6 and b == 1:  # mi/s - m/h
        Ans = val * 5793638.4
    elif a == 6 and b == 2:  # mi/s - km/s
        Ans = val * 1.609344
    elif a == 6 and b == 3:  # mi/s - km/h
        Ans = val * 5793.6384
    elif a == 6 and b == 4:  # mi/s - in/s
        Ans = val * 0.0002777778
    elif a == 6 and b == 5:  # mi/s - in/h
        Ans = val * 63360
    elif a == 6 and b == 6:  # mi/s - mi/s
        Ans = val * 1
    elif a == 6 and b == 7:  # mi/s - mi/h
        Ans = val * 3600
    # mi/h
    elif a == 7 and b == 0:  # mi/s - m/s
        Ans = val * 0.44704
    elif a == 7 and b == 1:  # mi/s - m/h
        Ans = val * 1609.344
    elif a == 7 and b == 2:  # mi/s - km/s
        Ans = val * 0.00044704
    elif a == 7 and b == 3:  # mi/s - km/h
        Ans = val * 1.609344
    elif a == 7 and b == 4:  # mi/s - in/s
        Ans = val * 17.6
    elif a == 7 and b == 5:  # mi/s - in/h
        Ans = val * 63360
    elif a == 7 and b == 6:  # mi/s - mi/s
        Ans = val * 0.0002777778
    elif a == 7 and b == 7:  # mi/s - mi/h
        Ans = val * 1

    return Ans


def Convertion_Time(a, b, val):

    Ans = val
    val = int(val)
    # m/s
    if a == 0 and b == 0:  # ms - ms
        Ans = val
    elif a == 0 and b == 1:  # ms - s
        Ans = val * 0.001
    elif a == 0 and b == 2:  # ms - min
        Ans = val * 0.0000166667
    elif a == 0 and b == 3:  # ms - h
        Ans = val * 0
    elif a == 0 and b == 4:  # ms - d
        Ans = val * 0
    elif a == 0 and b == 5:  # ms - wk
        Ans = val * 0
    # s
    elif a == 1 and b == 0:  # s - ms
        Ans = val * 1000
    elif a == 1 and b == 1:  # s - s
        Ans = val
    elif a == 1 and b == 2:  # s - min
        Ans = val * 0.0166666667
    elif a == 1 and b == 3:  # s - h
        Ans = val * 0.0002777778
    elif a == 1 and b == 4:  # s - d
        Ans = val * 0.0000115741
    elif a == 1 and b == 5:  # s - wk
        Ans = val * 0.0000016534

    # min
    elif a == 2 and b == 0:  # min - m/s
        Ans = val * 60000
    elif a == 2 and b == 1:  # min - s
        Ans = val * 60
    elif a == 2 and b == 2:  # min - min
        Ans = val
    elif a == 2 and b == 3:  # min - h
        Ans = val * 0.0166666667
    elif a == 2 and b == 4:  # min - d
        Ans = val * 0.0006944444
    elif a == 2 and b == 5:  # min - wk
        Ans = val * 0.0000992063

    # hours
    elif a == 3 and b == 0:  # hours - ms
        Ans = val * 3600000
    elif a == 3 and b == 1:  # hours - m/h
        Ans = val * 3600
    elif a == 3 and b == 2:  # hours - km/s
        Ans = val * 60
    elif a == 3 and b == 3:  # hours
        Ans = val * 1
    elif a == 3 and b == 4:  # hours - d
        Ans = val * 0.0416666667
    elif a == 3 and b == 5:  # hours - wk
        Ans = val * 0.005952381

    # d
    elif a == 4 and b == 0:  # d - ms
        Ans = val * 86, 400000
    elif a == 4 and b == 1:  # d - s
        Ans = val * 86400
    elif a == 4 and b == 2:  # d - min
        Ans = val * 1440
    elif a == 4 and b == 3:  # d - hours
        Ans = val * 24
    elif a == 4 and b == 4:  # d - d
        Ans = val * 1
    elif a == 4 and b == 5:  # d - wk
        Ans = val * 0.1428571429

    # wk
    elif a == 5 and b == 0:  # wk - m/s
        Ans = val * 604800000
    elif a == 5 and b == 1:  # wk - s
        Ans = val * 604800
    elif a == 5 and b == 2:  # wk - min
        Ans = val * 10080
    elif a == 5 and b == 3:  # wk - h
        Ans = val * 168
    elif a == 5 and b == 4:  # wk - d
        Ans = val * 7
    elif a == 5 and b == 5:  # wk - wk
        Ans = val * 1

    return Ans


def Convertion_Temperature(a, b, val):

    Ans = val
    val = int(val)
    # c
    if a == 0 and b == 0:  # c - c
        Ans = val
    elif a == 0 and b == 1:  # c - f
        Ans = val * 33.8
    elif a == 0 and b == 2:  # c -k
        Ans = val * 274.15
    # s
    elif a == 1 and b == 0:  # f - c
        Ans = val * -17.2222222222
    elif a == 1 and b == 1:  # f - f
        Ans = val
    elif a == 1 and b == 2:  # f - k
        Ans = val * 255.9277777778

    # min
    elif a == 2 and b == 0:  # k - c
        Ans = val * -272.15
    elif a == 2 and b == 1:  # k - f
        Ans = val * -457.87
    elif a == 2 and b == 2:  # k - k
        Ans = val

    return Ans


def Convertion_Mass(a, b, val):

    Ans = val
    val = int(val)
    # t
    if a == 0 and b == 0:  # t - t
        Ans = val
    elif a == 0 and b == 1:  # t - ukt
        Ans = val * 0.0984206527
    elif a == 0 and b == 2:  # t -USk
        Ans = val * 1.1023113109
    elif a == 0 and b == 3:  # t -lb
        Ans = val * 2204.6226218488
    elif a == 0 and b == 4:  # t -oz
        Ans = val * 35273.96194958
    elif a == 0 and b == 5:  # t -kg
        Ans = val * 1000
    elif a == 0 and b == 6:  # t -g
        Ans = val * 1000000

    # Ukt
    elif a == 1 and b == 0:  # Ukt - t
        Ans = val * 1.0160469088
    elif a == 1 and b == 1:  # Ukt - ukt
        Ans = val
    elif a == 1 and b == 2:  # Ukt -USk
        Ans = val * 1.12
    elif a == 1 and b == 3:  # Ukt -lb
        Ans = val * 2240
    elif a == 1 and b == 4:  # Ukt -oz
        Ans = val * 35840
    elif a == 1 and b == 5:  # Ukt -kg
        Ans = val * 1016.0469088
    elif a == 1 and b == 6:  # Ukt -g
        Ans = val * 1016046.9088
    # USt
    elif a == 2 and b == 0:  # USt - t
        Ans = val * 0.90718474
    elif a == 2 and b == 1:  # USt - ukt
        Ans = val * 0.892851429
    elif a == 2 and b == 2:  # USt -USk
        Ans = val
    elif a == 2 and b == 3:  # USt -lb
        Ans = val * 2000
    elif a == 2 and b == 4:  # USt -oz
        Ans = val * 32000
    elif a == 2 and b == 5:  # USt -kg
        Ans = val * 907.18474
    elif a == 2 and b == 6:  # USt -g
        Ans = val * 907184.74
    # lb
    if a == 3 and b == 0:  # lb - t
        Ans = val * 0.0004535924
    elif a == 3 and b == 1:  # lb - ukt
        Ans = val * 0.0004464286
    elif a == 3 and b == 2:  # lb -USk
        Ans = val * 0.0005
    elif a == 3 and b == 3:  # lb -lb
        Ans = val
    elif a == 3 and b == 4:  # lb -oz
        Ans = val * 16
    elif a == 3 and b == 5:  # lb -kg
        Ans = val * 0.45359237
    elif a == 3 and b == 6:  # lb -g
        Ans = val * 453.59237

        # ouz
    elif a == 4 and b == 0:  # ouz - t
        Ans = val * 0.0000283495
    elif a == 4 and b == 1:  # ouz - ukt
        Ans = val * 0.0000279018
    elif a == 4 and b == 2:  # ouz -USk
        Ans = val * 0.00003125
    elif a == 4 and b == 3:  # ouz -lb
        Ans = val * 0.0625
    elif a == 4 and b == 4:  # ouz -oz
        Ans = val
    elif a == 4 and b == 5:  # ouz -kg
        Ans = val * 0.0283495231
    elif a == 4 and b == 6:  # ouz -g
        Ans = val * 28.34953125

        # in
    elif a == 5 and b == 0:  # in - t
        Ans = val * 0
    elif a == 5 and b == 1:  # in - ukt
        Ans = val * 0.0000064516
    elif a == 5 and b == 2:  # in -USk
        Ans = val * 0
    elif a == 5 and b == 3:  # in -lb
        Ans = val * 6.4516
    elif a == 5 and b == 4:  # in -oz
        Ans = val * 0.0069444444
    elif a == 5 and b == 5:  # in -kg
        Ans = val
    elif a == 5 and b == 6:  # in -g
        Ans = val * 0.00064516
        # g
    elif a == 6 and b == 0:  # g - t
        Ans = val * 0.0002471054
    elif a == 6 and b == 1:  # g - ukt
        Ans = val * 0.01
    elif a == 6 and b == 2:  # g -USk
        Ans = val * 0.0001
    elif a == 6 and b == 3:  # g -lb
        Ans = val * 10000
    elif a == 6 and b == 4:  # g -oz
        Ans = val * 10.7639104167
    elif a == 6 and b == 5:  # g -kg
        Ans = val * 1550.0031000062
    elif a == 6 and b == 6:  # g -g
        Ans = val

    return Ans


def Convertion_Area(a, b, val):

    Ans = val
    val = int(val)
    # ac
    if a == 0 and b == 0:  # ac - ac
        Ans = val
    elif a == 0 and b == 1:  # ac - a
        Ans = val * 40.468564224
    elif a == 0 and b == 2:  # ac -ha
        Ans = val * 0.4046856422
    elif a == 0 and b == 3:  # ac -cm
        Ans = val * 40468564.224
    elif a == 0 and b == 4:  # ac -ft
        Ans = val * 43560
    elif a == 0 and b == 5:  # ac -in
        Ans = val * 6272640
    elif a == 0 and b == 6:  # ac -m
        Ans = val * 4046.8564224

    # a
    elif a == 1 and b == 0:  # a - t
        Ans = val * 0.0247105381
    elif a == 1 and b == 1:  # a - ukt
        Ans = val
    elif a == 1 and b == 2:  # a -USk
        Ans = val * 0.01
    elif a == 1 and b == 3:  # a -lb
        Ans = val * 1000000
    elif a == 1 and b == 4:  # a -oz
        Ans = val * 1076.391041671
    elif a == 1 and b == 5:  # a -kg
        Ans = val * 155000.31000062
    elif a == 1 and b == 6:  # a -g
        Ans = val * 100
    # ha
    elif a == 2 and b == 0:  # ha - t
        Ans = val * 2.4710538147
    elif a == 2 and b == 1:  # ha - ukt
        Ans = val * 100
    elif a == 2 and b == 2:  # ha -USk
        Ans = val
    elif a == 2 and b == 3:  # ha -lb
        Ans = val * 100000000
    elif a == 2 and b == 4:  # ha -oz
        Ans = val * 107639.1041671
    elif a == 2 and b == 5:  # ha -kg
        Ans = val * 15500031.000062
    elif a == 2 and b == 6:  # ha -g
        Ans = val * 10000
    # cm
    if a == 3 and b == 0:  # cm - t
        Ans = val * 0
    elif a == 3 and b == 1:  # cm - ukt
        Ans = val * 0.000001
    elif a == 3 and b == 2:  # cm -USk
        Ans = val * 0
    elif a == 3 and b == 3:  # cm -lb
        Ans = val
    elif a == 3 and b == 4:  # cm -oz
        Ans = val * 0.001076391
    elif a == 3 and b == 5:  # cm -kg
        Ans = val * 0.15500031
    elif a == 3 and b == 6:  # cm -g
        Ans = val * 0.0001

        # ft
    elif a == 4 and b == 0:  # ft - t
        Ans = val * 0.0000229568
    elif a == 4 and b == 1:  # ft - ukt
        Ans = val * 0.00009290304
    elif a == 4 and b == 2:  # ft -USk
        Ans = val * 0.00000929030
    elif a == 4 and b == 3:  # ft -lb
        Ans = val * 929.0304
    elif a == 4 and b == 4:  # ft -oz
        Ans = val
    elif a == 4 and b == 5:  # ft -kg
        Ans = val * 144
    elif a == 4 and b == 6:  # ft -g
        Ans = val * 0.09290304

        # kg
    elif a == 1 and b == 0:  # kg - t
        Ans = val * 0.001
    elif a == 1 and b == 1:  # kg - ukt
        Ans = val * 0.000029842065
    elif a == 1 and b == 2:  # kg -USk
        Ans = val * 0.0011023113
    elif a == 1 and b == 3:  # kg -lb
        Ans = val * 2.2046226218
    elif a == 1 and b == 4:  # kg -oz
        Ans = val * 35.2739619496
    elif a == 1 and b == 5:  # kg -kg
        Ans = val
    elif a == 1 and b == 6:  # kg -g
        Ans = val * 1000
        # g
    elif a == 1 and b == 0:  # g - t
        Ans = val * 0
    elif a == 1 and b == 1:  # g - ukt
        Ans = val * 0
    elif a == 1 and b == 2:  # g -USk
        Ans = val * 0.0000011023
    elif a == 1 and b == 3:  # g -lb
        Ans = val * 0.0022046226
    elif a == 1 and b == 4:  # g -oz
        Ans = val * 0.0352739619
    elif a == 1 and b == 5:  # g -kg
        Ans = val * 0.001
    elif a == 1 and b == 6:  # g -g
        Ans = val

    return Ans


def Convertion_equation(a, val):
    try:
        x = Symbol("x")
        X_index = val.index("x")
        if "x" in val and X_index != 0 and val[X_index - 1].isnumeric():
            newVal = ""
            for char in val:
                if val.index(char) == X_index - 1:
                    newVal += char + "*"
                else:
                    newVal += char
        print("newVal", newVal)

        solutions = "2"
        matrix = newVal.replace("×", "*")
        matrix = matrix.replace("÷", "/")

        solutions = solve(matrix, x)

        Answer = ""

        print("solution", solutions)
        for sl in solutions:
            Answer += "x = " + str(sl) + ". "

        Answer = Answer.replace("sqrt", "√")
        Answer = Answer.replace("*", "×")
        Answer = Answer.replace("××", "^")

        print("answer", Answer)
        return str(Answer)
    except Exception as e:
        return "Cannot solve expression"


def Convertion_matrix(a, val):
    global Expression
    global AMatrix
    global BMatrix

    try:
        if Expression == True:
            AnsExp = val
            Step1, Split2 = AnsExp.split("A->List")
            value = Step1.split("×")
            Original = int(eval(str(value[0])))

            Step2, Step3 = Split2.split("×")
            Step2 = Step2.strip()
            symbol = Step2[0]
            value_1 = Step2.split(Step2[0])[1]
            Expression = 0
            Original2 = int(eval(value_1))
            AMatrix = "[" + AMatrix + "]".strip()
            AMatrix = ast.literal_eval(AMatrix)
            BMatrix = "[" + BMatrix + "]".strip()
            BMatrix = ast.literal_eval(BMatrix)

            if symbol == "+":
                Expression = Original * Mx(AMatrix) + Original2 * Mx(BMatrix)
            elif symbol == "-":
                Expression = Original * Mx(AMatrix) - Original2 * Mx(BMatrix)

            return Expression
        else:
            valuesSplit = val.split("\n")
            AMatrix = valuesSplit[0].split("=")[1]
            BMatrix = valuesSplit[1].split("=")[1]
            entry_matrix.delete("0.0", "end")
            entry_matrix.insert("0.0", "1 × A->List + 1 × B->List")
            return "exp"

    except Exception as e:
        return "Invalid Syntax"


def Convertion_volume(a, b, val):
    Ans = val
    val = int(val)
    # t
    if a == 0 and b == 0:  # t - t
        Ans = val
    elif a == 0 and b == 1:  # t - ukt
        Ans = val * 1.2009499255
    elif a == 0 and b == 2:  # t -USk
        Ans = val * 4.54609
    elif a == 0 and b == 3:  # t -lb
        Ans = val * 4546.09
    elif a == 0 and b == 4:  # t -oz
        Ans = val * 4546.09
    elif a == 0 and b == 5:  # t -kg
        Ans = val * 0.00454609
    elif a == 0 and b == 6:  # t -g
        Ans = val * 277.4194327916
    elif a == 0 and b == 7:  # t -g
        Ans = val * 0.1605436532

    # Ukt
    elif a == 1 and b == 0:  # Ukt - t
        Ans = val * 0.8326741846
    elif a == 1 and b == 1:  # Ukt - ukt
        Ans = val
    elif a == 1 and b == 2:  # Ukt -USk
        Ans = val * 3.785411784
    elif a == 1 and b == 3:  # Ukt -lb
        Ans = val * 3785.411784
    elif a == 1 and b == 4:  # Ukt -oz
        Ans = val * 3785.411784
    elif a == 1 and b == 5:  # Ukt -kg
        Ans = val * 0.0037854118
    elif a == 1 and b == 6:  # Ukt -g
        Ans = val * 231
    elif a == 1 and b == 7:  # Ukt -g
        Ans = val * 0.1336805556
    # USt
    elif a == 2 and b == 0:  # USt - t
        Ans = val * 0.2199692483
    elif a == 2 and b == 1:  # USt - ukt
        Ans = val * 0.2641720524
    elif a == 2 and b == 2:  # USt -USk
        Ans = val
    elif a == 2 and b == 3:  # USt -lb
        Ans = val * 1000
    elif a == 2 and b == 4:  # USt -oz
        Ans = val * 1000
    elif a == 2 and b == 5:  # USt -kg
        Ans = val * 0.001
    elif a == 2 and b == 6:  # USt -g
        Ans = val * 61.0237440947
    elif a == 2 and b == 7:  # USt -g
        Ans = val * 0.0353146667
    # lb
    if a == 3 and b == 0:  # lb - t
        Ans = val * 0.0002199692
    elif a == 3 and b == 1:  # lb - ukt
        Ans = val * 0.0002641721
    elif a == 3 and b == 2:  # lb -USk
        Ans = val * 0.001
    elif a == 3 and b == 3:  # lb -lb
        Ans = val
    elif a == 3 and b == 4:  # lb -oz
        Ans = val * 1
    elif a == 3 and b == 5:  # lb -kg
        Ans = val * 0.000001
    elif a == 3 and b == 6:  # lb -g
        Ans = val * 0.0610237441
    elif a == 2 and b == 7:  # USt -g
        Ans = val * 0.0000353147

        # ouz
    elif a == 4 and b == 0:  # ouz - t
        Ans = val * 0.0002199692
    elif a == 4 and b == 1:  # ouz - ukt
        Ans = val * 0.0002641721
    elif a == 4 and b == 2:  # ouz -USk
        Ans = val * 0.001
    elif a == 4 and b == 3:  # ouz -lb
        Ans = val * 1
    elif a == 4 and b == 4:  # ouz -oz
        Ans = val
    elif a == 4 and b == 5:  # ouz -kg
        Ans = val * 0.000001
    elif a == 4 and b == 6:  # ouz -g
        Ans = val * 0.0610237441
    elif a == 4 and b == 7:  # ouz -g
        Ans = val * 0.0000353147

        # in
    elif a == 5 and b == 0:  # in - t
        Ans = val * 219.9692482991
    elif a == 5 and b == 1:  # in - ukt
        Ans = val * 264.1720523581
    elif a == 5 and b == 2:  # in -USk
        Ans = val * 1000
    elif a == 5 and b == 3:  # in -lb
        Ans = val * 1000000
    elif a == 5 and b == 4:  # in -oz
        Ans = val * 1000000
    elif a == 5 and b == 5:  # in -kg
        Ans = val
    elif a == 5 and b == 6:  # in -g
        Ans = val * 61023.744094732
    elif a == 5 and b == 7:  # in -g
        Ans = val * 35.3146667215

        # g
    elif a == 6 and b == 0:  # g - t
        Ans = val * 0.0036046501
    elif a == 6 and b == 1:  # g - t
        Ans = val * 0.0043290043
    elif a == 6 and b == 2:  # g - ukt
        Ans = val * 0.016387064
    elif a == 6 and b == 3:  # g -USk
        Ans = val * 16.387064
    elif a == 6 and b == 4:  # g -lb
        Ans = val * 16.387064
    elif a == 6 and b == 5:  # g -oz
        Ans = val * 0.0000163871
    elif a == 6 and b == 6:  # g -kg
        Ans = val * 1
    elif a == 6 and b == 7:  # g -g
        Ans = val * 0.0005787037

    elif a == 6 and b == 0:  # g - t
        Ans = val * 6.228835459
    elif a == 6 and b == 1:  # g - t
        Ans = val * 7.4805194805
    elif a == 6 and b == 2:  # g - ukt
        Ans = val * 28.316846592
    elif a == 6 and b == 3:  # g -USk
        Ans = val * 28316.846592
    elif a == 6 and b == 4:  # g -lb
        Ans = val * 28316.846592
    elif a == 6 and b == 5:  # g -oz
        Ans = val * 0.0283168466
    elif a == 6 and b == 6:  # g -kg
        Ans = val * 1728
    elif a == 6 and b == 7:  # g -g
        Ans = val

    return Ans


def Convertion_Length(a, b, val):

    Ans = val
    val = int(val)
    # mm
    if a == 0 and b == 0:  # mm
        Ans = val
    elif a == 0 and b == 1:  # mm
        Ans = val * 0.1
    elif a == 0 and b == 2:  # mm
        Ans = val * 0.001
    elif a == 0 and b == 3:  # mm
        Ans = val * 0.000001
    elif a == 0 and b == 4:  # mm
        Ans = val * 0.0393700787
    elif a == 0 and b == 5:  # mm
        Ans = val * 0.0032808399
    elif a == 0 and b == 6:  # mm
        Ans = val * 0.0010936133
    elif a == 0 and b == 7:  # mm
        Ans = val * 0
    elif a == 0 and b == 8:  # mm
        Ans = val * 0
    elif a == 0 and b == 9:  # mm
        Ans = val * 39.3700787402

    # cm
    if a == 1 and b == 0:  # cm
        Ans = val * 10
    elif a == 1 and b == 1:  # cm
        Ans = val
    elif a == 1 and b == 2:  # cm
        Ans = val * 0.01
    elif a == 1 and b == 3:  # cm
        Ans = val * 0.00001
    elif a == 1 and b == 4:  # cm
        Ans = val * 0.3937007874
    elif a == 1 and b == 5:  # cm
        Ans = val * 0.032808399
    elif a == 1 and b == 6:  # cm
        Ans = val * 0.010936133
    elif a == 1 and b == 7:  # cm
        Ans = val * 0.0000062137
    elif a == 1 and b == 8:  # cm
        Ans = val * 0.0000053996
    elif a == 1 and b == 9:  # cm
        Ans = val * 393.7007874016
    # m
    elif a == 2 and b == 0:  # m
        Ans = val * 1000
    elif a == 2 and b == 1:  # m
        Ans = val * 100
    elif a == 2 and b == 2:  # m
        Ans = val
    elif a == 2 and b == 3:  # m
        Ans = val * 0.001
    elif a == 2 and b == 4:  # m
        Ans = val * 39.3700787402
    elif a == 2 and b == 5:  # m
        Ans = val * 3.280839895
    elif a == 2 and b == 6:  # m
        Ans = val * 1.0936132983
    elif a == 2 and b == 7:  # m
        Ans = val * 0.0006213712
    elif a == 2 and b == 8:  # m
        Ans = val * 0.0005399568
    elif a == 2 and b == 9:  # m
        Ans = val * 39370.078740157
    # km
    if a == 3 and b == 0:  # km
        Ans = val * 1000000
    elif a == 3 and b == 1:  # km
        Ans = val * 100000
    elif a == 3 and b == 2:  # km
        Ans = val * 1000
    elif a == 3 and b == 3:  # km
        Ans = val
    elif a == 3 and b == 4:  # km
        Ans = val * 39370.078740157
    elif a == 3 and b == 5:  # km
        Ans = val * 3280.8398950131
    elif a == 3 and b == 6:  # km
        Ans = val * 1093.6132983377
    elif a == 2 and b == 7:  # km
        Ans = val * 0.6213711922
    elif a == 2 and b == 8:  # km
        Ans = val * 0.5399568035
    elif a == 2 and b == 9:  # km
        Ans = val * 39370078.740157

        # in
    elif a == 4 and b == 0:  # in
        Ans = val * 25.4
    elif a == 4 and b == 1:  # in
        Ans = val * 2.54
    elif a == 4 and b == 2:  # in
        Ans = val * 0.0254
    elif a == 4 and b == 3:  # in
        Ans = val * 0.0000254
    elif a == 4 and b == 4:  # in
        Ans = val
    elif a == 4 and b == 5:  # in
        Ans = val * 0.0833333333
    elif a == 4 and b == 6:  # in
        Ans = val * 0.0277777778
    elif a == 4 and b == 7:  # in
        Ans = val * 0.0000157828
    elif a == 4 and b == 8:  # in
        Ans = val * 0.0000137149
    elif a == 4 and b == 9:  # in
        Ans = val * 1000

        # ft
    elif a == 5 and b == 0:  # ft
        Ans = val * 304.8
    elif a == 5 and b == 1:  # ft
        Ans = val * 30.48
    elif a == 5 and b == 2:  # ft
        Ans = val * 0.3048
    elif a == 5 and b == 3:  # ft
        Ans = val * 0.0003048
    elif a == 5 and b == 4:  # ft
        Ans = val * 12
    elif a == 5 and b == 5:  # ft
        Ans = val
    elif a == 5 and b == 6:  # ft
        Ans = val * 0.3333333333
    elif a == 5 and b == 7:  # ft
        Ans = val * 0.0001893939
    elif a == 5 and b == 8:  # ft
        Ans = val * 0.0001645788
    elif a == 5 and b == 9:  # ft
        Ans = val * 12000
        # yd
    elif a == 6 and b == 0:  # yd
        Ans = val * 914.4
    elif a == 6 and b == 1:  # yd
        Ans = val * 91.44
    elif a == 6 and b == 2:  # yd
        Ans = val * 0.9144
    elif a == 6 and b == 3:  # yd
        Ans = val * 0.0009144
    elif a == 6 and b == 4:  # yd
        Ans = val * 36
    elif a == 6 and b == 5:  # yd
        Ans = val * 3
    elif a == 6 and b == 6:  # yd
        Ans = val
    elif a == 6 and b == 7:  # yd
        Ans = val * 0.0005681818
    elif a == 6 and b == 8:  # yd
        Ans = val * 0.0004937365
    elif a == 6 and b == 9:  # yd
        Ans = val * 36000

    elif a == 7 and b == 0:  # mi
        Ans = val * 1609344
    elif a == 7 and b == 1:  # mi
        Ans = val * 160934.4
    elif a == 7 and b == 2:  # mi
        Ans = val * 1609.344
    elif a == 7 and b == 3:  # mi
        Ans = val * 1.609344
    elif a == 7 and b == 4:  # mi
        Ans = val * 63360
    elif a == 7 and b == 5:  # mi
        Ans = val * 5280
    elif a == 7 and b == 6:  # mi
        Ans = val * 1760
    elif a == 7 and b == 7:  # mi
        Ans = val
    elif a == 7 and b == 8:  # mi
        Ans = val * 0.8689762419
    elif a == 7 and b == 9:  # mi
        Ans = val * 63360000

    elif a == 8 and b == 0:  # NM
        Ans = val * 1852000
    elif a == 8 and b == 1:  # NM
        Ans = val * 185200
    elif a == 8 and b == 2:  # NM
        Ans = val * 1852
    elif a == 8 and b == 3:  # NM
        Ans = val * 1.852
    elif a == 8 and b == 4:  # NM
        Ans = val * 72913.385826772
    elif a == 8 and b == 5:  # NM
        Ans = val * 6076.1154855643
    elif a == 8 and b == 6:  # NM
        Ans = val * 2025.3718285214
    elif a == 8 and b == 7:  # NM
        Ans = val * 1.150779448
    elif a == 8 and b == 8:  # NM
        Ans = val
    elif a == 8 and b == 9:  # NM
        Ans = val * 72, 913385.826772

    elif a == 9 and b == 0:  # NM
        Ans = val * 0.0254
    elif a == 9 and b == 1:  # NM
        Ans = val * 0.00254
    elif a == 9 and b == 2:  # NM
        Ans = val * 0.0000254
    elif a == 9 and b == 3:  # NM
        Ans = val * 0
    elif a == 9 and b == 4:  # NM
        Ans = val * 0.001
    elif a == 9 and b == 5:  # NM
        Ans = val * 0.0000833333
    elif a == 9 and b == 6:  # NM
        Ans = val * 0.0000277778
    elif a == 9 and b == 7:  # NM
        Ans = val * 0
    elif a == 9 and b == 8:  # NM
        Ans = val * 0
    elif a == 9 and b == 9:  # NM
        Ans = val
    return Ans


def SpeedConvertion(a, b, val):
    global ModeMenu_main_convert_select
    global ModeMenu_main_convert
    global PerformSpeed
    global SpeedData
    global SpeedAns
    global ActiveEntry
    global resetFrames

    print(a, b, "speed")
    a = int(a) - 1
    b = int(b) - 1
    Speed_functions = [
        "(m/s)",
        "(m/h)",
        "(km/s)",
        "(km/h)",
        "(in/s)",
        "(in/h)",
        "(mi/s)",
        "(mi/h)",
    ]
    if not PerformSpeed:
        PerformSpeed = True
        ModeMenu_main_convert.grid_remove()
        ModeMenu_main_convert_speed.grid_remove()
        ModeMenu_main_convert_select_speed.grid(column=1, row=2)
        label_speed = customtkinter.CTkLabel(
            master=ModeMenu_main_convert_select_speed,
            width=(WINW),
            text=str("convert: " + Speed_functions[a] + "to: " + Speed_functions[b]),
            height=(40),
            font=("Roboto", 12),
            corner_radius=0,
        )
        label_speed.grid(column=1, row=1)
        entry_speed.grid(column=1, row=2)
        ActiveEntry = entry_speed
        resetFrames = 1

    else:
        a_str = str(val)
        SpeedData += a_str

        if a_str == "AC":
            his_data.set(SpeedData + " " + str(SpeedAns))
            entry.delete("0.0", "end")
            entry_speed.insert("0.0", "")
            SpeedData = ""
        elif a_str == "C":
            entry_speed.delete("insert-1c")
            SpeedData = entry_speed.get("0.0", tk.END)

        elif val == "Ans":
            entry.delete("0.0", "end")
            entry_speed.insert("0.0", SpeedAns)

        elif val == "=":
            print(
                entry_speed.get("0.0", tk.END),
                entry_speed.get("0.0", tk.END).isnumeric(),
            )
            if int(entry_speed.get("0.0", tk.END)):
                SpeedAns = Convertion_speed(a, b, entry_speed.get("0.0", tk.END))
                entry_speed.delete("0.0", "end")
                entry_speed.insert("0.0", str(SpeedAns) + " " + Speed_functions[b])
            else:
                SpeedAns = "Syntax Error"
                entry_speed.delete("0.0", "end")
                entry_speed.insert("0.0", SpeedAns)
        else:

            entry_speed.insert(entry_speed.index("insert"), val)


def EquationConvertion(a, val):
    global ModeMenu_main_convert_select
    global ModeMenu_main_convert
    global PerformEquation
    global SpeedData
    global SpeedAns
    global ActiveEntry
    global resetFrames

    if not PerformEquation and isfloat(a) and int(a) > 0 and int(a) < 5:
        equation_functions = [
            1 * x + 10,
            1 * x**2 + 1 * x + 10,
            1 * x**3 + 1 * x**2 + 1 * x + 10,
            1 * x**4 + 1 * x**3 + 1 * x**2 + 1 * x + 10,
        ]
        PerformEquation = True
        ModeMenu_main_convert.grid_remove()
        ModeMenu_main_convert_equation.grid_remove()
        ModeMenu_main_convert_select_equation.grid(column=1, row=2)
        label_equation = customtkinter.CTkLabel(
            master=ModeMenu_main_convert_select_equation,
            width=(WINW),
            text=str("Performing equation expression"),
            height=(40),
            font=("Roboto", 12),
            corner_radius=0,
        )
        label_equation.grid(column=1, row=1)
        entry_equation.grid(column=1, row=2)
        entry_equation.delete("0.0", "end")
        entry_equation.insert("0.0", equation_functions[int(a) - 1])
        ActiveEntry = entry_equation
        resetFrames = 1
    else:
        a_str = str(val)
        SpeedData += a_str

        if a_str == "AC":
            his_data.set(SpeedData + " " + str(SpeedAns))
            entry_equation.delete("0.0", "end")
            entry_equation.insert("0.0", "")
            SpeedData = ""
        elif a_str == "C":
            entry_equation.delete("insert-1c")
            SpeedData = entry_equation.get("1.0", tk.END)
        elif val == "Ans":
            entry_equation.delete("0.0", "end")
            entry_equation.insert("0.0", SpeedAns)

        elif val == "=":
            SpeedAns = Convertion_equation(a, entry_equation.get("1.0", tk.END))
            entry_equation.delete("0.0", "end")
            entry_equation.insert("0.0", SpeedAns)
        else:
            entry_equation.insert(entry_equation.index("insert"), val)


def MatrixConvertion(a, val):
    global ModeMenu_main_convert_select
    global ModeMenu_main_convert
    global PerformMatrix
    global Expression
    global SpeedData
    global SpeedAns
    global ActiveEntry
    global resetFrames

    if not PerformMatrix and isfloat(a) and int(a) > 0 and int(a) < 5:
        matrix_functions = [
            "[0,0],[0,0]",
            "[0,0],[0,0],[0,0]",
            "[0,0,0],[0,0,0]",
            "[0,0,0],[0,0,0],[0,0,0]",
        ]
        PerformMatrix = True
        ModeMenu_main_convert.grid_remove()
        ModeMenu_main_convert_matrix.grid_remove()
        ModeMenu_main_convert_select_matrix.grid(column=1, row=2)
        label_matrix = customtkinter.CTkLabel(
            master=ModeMenu_main_convert_select_matrix,
            width=(WINW),
            text=str("Performing matrix expression"),
            height=(40),
            font=("Roboto", 12),
            corner_radius=0,
        )
        label_matrix.grid(column=1, row=1)
        entry_matrix.grid(column=1, row=2)
        entry_matrix.delete("0.0", "end")
        entry_matrix.insert(
            "0.0",
            "A->List = "
            + matrix_functions[int(a) - 1]
            + "\n"
            + "B->List = "
            + matrix_functions[int(a) - 1],
        )
        ActiveEntry = entry_matrix
        resetFrames = 1
    else:
        a_str = str(val)
        SpeedData += a_str

        if a_str == "AC":
            his_data.set(SpeedData + " " + str(SpeedAns))
            entry_matrix.delete("0.0", "end")
            entry_matrix.insert("0.0", "")
            SpeedData = ""
        elif a_str == "C":
            item = entry_matrix.get("insert-1c")
            print(item, item.isnumeric())
            if item.isnumeric() and item != ".":
                entry_matrix.delete("insert-1c")
        elif val == "Ans":
            entry_matrix.delete("0.0", "end")
            entry_matrix.insert("0.0", SpeedAns)

        elif val == "=":
            if Expression == True:
                SpeedAns = Convertion_matrix(a, entry_matrix.get("1.0", tk.END))
                entry_matrix.delete("0.0", "end")
                entry_matrix.insert("0.0", SpeedAns)
            else:
                SpeedAns = Convertion_matrix(a, entry_matrix.get("1.0", tk.END))
                Expression = True
        else:
            entry_matrix.insert(entry_matrix.index("insert"), val)


def TemperatureConvertion(a, b, val):
    global ModeMenu_main_convert_select_Temperature
    global ModeMenu_main_convert
    global PerformTemperature
    global SpeedData
    global SpeedAns
    global ActiveEntry
    global resetFrames

    a = int(a) - 1
    b = int(b) - 1
    Temperature_functions = [
        "(⁰C)",
        "(⁰F)",
        "(K)",
    ]
    print("forces...")
    if not PerformTemperature:
        PerformTemperature = True
        ModeMenu_main_convert.grid_remove()
        ModeMenu_main_convert_Temperature.grid_remove()
        ModeMenu_main_convert_select_Temperature.grid(column=1, row=2)
        label_Temperature = customtkinter.CTkLabel(
            master=ModeMenu_main_convert_select_Temperature,
            width=(WINW),
            text=str(
                "convert: "
                + Temperature_functions[a]
                + "to: "
                + Temperature_functions[b]
            ),
            height=(40),
            font=("Roboto", 12),
            corner_radius=0,
        )
        label_Temperature.grid(column=1, row=1)
        entry_Temperature.grid(column=1, row=2)
        ActiveEntry = entry_Temperature
        resetFrames = 1

    else:

        a_str = str(val)
        SpeedData += a_str

        if a_str == "AC":
            his_data.set(SpeedData + " " + str(SpeedAns))
            entry_Temperature.delete("0.0", "end")
            entry_Temperature.insert("0.0", "")
            SpeedData = ""
        elif a_str == "C":
            entry_Temperature.delete("insert-1c")
            SpeedData = entry_Temperature.get("0.0", tk.END)

        elif val == "Ans":
            entry_Temperature.delete("0.0", "end")
            entry_Temperature.insert("0.0", SpeedAns)

        elif val == "=":
            if int(entry_Temperature.get("0.0", tk.END)):
                SpeedAns = Convertion_Temperature(
                    a, b, entry_Temperature.get("0.0", tk.END)
                )
                print(
                    a,
                    b,
                    entry_Temperature.get("0.0", tk.END),
                    Convertion_Temperature(a, b, entry_Temperature.get("0.0", tk.END)),
                    "....",
                )
                entry_Temperature.delete("0.0", "end")
                entry_Temperature.insert(
                    "0.0", str(SpeedAns) + " " + Temperature_functions[b]
                )
            else:
                SpeedAns = "Syntax Error"
                entry_Temperature.delete("0.0", "end")
                entry_Temperature.insert("0.0", SpeedAns)
        else:

            entry_Temperature.insert(entry_Temperature.index("insert"), val)


def AreaConvertion(a, b, val):
    global ModeMenu_main_convert_select_Area
    global ModeMenu_main_convert
    global PerformArea
    global SpeedData
    global SpeedAns
    global ActiveEntry
    global resetFrames

    a = int(a) - 1
    b = int(b) - 1
    Area_functions = [
        "(ac)",
        "(a)",
        "(ha)",
        "(cm)",
        "(in)",
        "(m)",
    ]
    if not PerformArea:
        PerformArea = True
        print("truetem")
        ModeMenu_main_convert.grid_remove()
        ModeMenu_main_convert_Area.grid_remove()
        ModeMenu_main_convert_select_Area.grid(column=1, row=2)
        label_Area = customtkinter.CTkLabel(
            master=ModeMenu_main_convert_select_Area,
            width=(WINW),
            text=str("convert: " + Area_functions[a] + "to: " + Area_functions[b]),
            height=(40),
            font=("Roboto", 12),
            corner_radius=0,
        )
        label_Area.grid(column=1, row=1)
        entry_Area.grid(column=1, row=2)
        ActiveEntry = entry_Area
        resetFrames = 1

    else:

        a_str = str(val)
        SpeedData += a_str

        if a_str == "AC":
            his_data.set(SpeedData + " " + str(SpeedAns))
            entry_Area.delete("0.0", "end")
            entry_Area.insert("0.0", "")
            SpeedData = ""
        elif a_str == "C":
            entry_Area.delete("insert-1c")
            SpeedData = entry_Area.get("0.0", tk.END)

        elif a_str == "Ans":
            entry_Area.delete("0.0", "end")
            entry_Area.insert("0.0", SpeedAns)

        elif a_str == "=":
            if int(entry_Area.get("0.0", tk.END)):
                SpeedAns = Convertion_Area(a, b, entry_Area.get("0.0", tk.END))
                print(
                    a,
                    b,
                    entry_Area.get("0.0", tk.END),
                    Convertion_Area(a, b, entry_Area.get("0.0", tk.END)),
                    "....",
                )
                entry_Area.delete("0.0", "end")
                entry_Area.insert("0.0", str(SpeedAns) + " " + Area_functions[b])
            else:
                SpeedAns = "Syntax Error"
                entry_Area.delete("0.0", "end")
                entry_Area.insert("0.0", SpeedAns)
        else:
            entry_Area.insert(entry_Area.index("insert"), val)


def MassConvertion(a, b, val):
    global ModeMenu_main_convert_select_Mass
    global ModeMenu_main_convert
    global PerformMass
    global SpeedData
    global SpeedAns
    global ActiveEntry
    global resetFrames

    a = int(a) - 1
    b = int(b) - 1
    Mass_functions = [
        "(UK t)",
        "(US t)",
        "(lb)",
        "oz)",
        "(kg)",
        "(g)",
    ]
    if not PerformMass:
        PerformMass = True
        print("truetem")
        ModeMenu_main_convert.grid_remove()
        ModeMenu_main_convert_Mass.grid_remove()
        ModeMenu_main_convert_select_Mass.grid(column=1, row=2)
        label_Mass = customtkinter.CTkLabel(
            master=ModeMenu_main_convert_select_Mass,
            width=(WINW),
            text=str("convert: " + Mass_functions[a] + "to: " + Mass_functions[b]),
            height=(40),
            font=("Roboto", 12),
            corner_radius=0,
        )
        label_Mass.grid(column=1, row=1)
        entry_Mass.grid(column=1, row=2)
        ActiveEntry = entry_Mass
        resetFrames = 1

    else:

        a_str = str(val)
        SpeedData += a_str

        if a_str == "AC":
            his_data.set(SpeedData + " " + str(SpeedAns))
            entry_Mass.delete("0.0", "end")
            entry_Mass.insert("0.0", "")
            SpeedData = ""
        elif a_str == "C":
            entry_Mass.delete("insert-1c")
            SpeedData = entry_Mass.get("0.0", tk.END)

        elif val == "Ans":
            entry_Mass.delete("0.0", "end")
            entry_Mass.insert("0.0", SpeedAns)

        elif val == "=":
            if int(entry_Mass.get("0.0", tk.END)):
                SpeedAns = Convertion_Mass(a, b, entry_Mass.get("0.0", tk.END))
                print(
                    a,
                    b,
                    entry_Mass.get("0.0", tk.END),
                    Convertion_Mass(a, b, entry_Mass.get("0.0", tk.END)),
                    "....",
                )
                entry_Mass.delete("0.0", "end")
                entry_Mass.insert("0.0", str(SpeedAns) + " " + Mass_functions[b])
            else:
                SpeedAns = "Syntax Error"
                entry_Mass.delete("0.0", "end")
                entry_Mass.insert("0.0", SpeedAns)
        else:
            entry_Mass.insert(entry_Mass.index("insert"), val)


def LengthConvertion(a, b, val):
    global ModeMenu_main_convert_select_Length
    global ModeMenu_main_convert
    global PerformLength
    global SpeedData
    global SpeedAns
    global ActiveEntry
    global resetFrames

    a = int(a) - 1
    b = int(b) - 1
    Length_functions = [
        "(mm)",
        "(cm)",
        "(m)",
        "(km)",
        "(in)",
        "(ft)",
        "(yf)",
        "(mi)",
        "(NM)",
        "(mil)",
    ]
    if not PerformLength:
        PerformLength = True
        print("truetem")
        ModeMenu_main_convert.grid_remove()
        ModeMenu_main_convert_Length.grid_remove()
        ModeMenu_main_convert_select_Length.grid(column=1, row=2)
        label_Length = customtkinter.CTkLabel(
            master=ModeMenu_main_convert_select_Length,
            width=(WINW),
            text=str("convert: " + Length_functions[a] + "to: " + Length_functions[b]),
            height=(40),
            font=("Roboto", 12),
            corner_radius=0,
        )
        label_Length.grid(column=1, row=1)
        entry_Length.grid(column=1, row=2)
        ActiveEntry = entry_Length
        resetFrames = 1
    else:

        a_str = str(val)
        SpeedData += a_str

        if a_str == "AC":
            his_data.set(SpeedData + " " + str(SpeedAns))
            entry_Length.delete("0.0", "end")
            entry_Length.insert("0.0", "")
            SpeedData = ""
        elif a_str == "C":

            entry_Length.delete("insert-1c")
            SpeedData = entry_Length.get()

        elif val == "Ans":
            entry_Length.delete("0.0", "end")
            entry_Length.insert("0.0", SpeedAns)

        elif val == "=":
            if int(entry_Length.get("0.0", tk.END)):
                SpeedAns = Convertion_Length(a, b, entry_Length.get("0.0", tk.END))
                print(
                    a,
                    b,
                    entry_Length.get("0.0", tk.END),
                    Convertion_Length(a, b, entry_Length.get("0.0", tk.END)),
                    "....",
                )
                entry_Length.delete("0.0", "end")
                entry_Length.insert("0.0", str(SpeedAns) + " " + Length_functions[b])
            else:
                SpeedAns = "Syntax Error"
                entry_Length.delete("0.0", "end")
                entry_Length.insert("0.0", SpeedAns)
        else:
            entry_Length.insert(entry_Length.index("insert"), val)


def TimeConvertion(a, b, val):
    global ModeMenu_main_convert_select_Time
    global ModeMenu_main_convert
    global PerformTime
    global SpeedData
    global SpeedAns
    global ActiveEntry
    global resetFrames

    a = int(a) - 1
    b = int(b) - 1
    Time_functions = [
        "(ms)",
        "(s)",
        "(min)",
        "(h)",
        "(d)",
        "(wk)",
    ]
    if not PerformTime:
        PerformTime = True
        ModeMenu_main_convert.grid_remove()
        ModeMenu_main_convert_Time.grid_remove()
        ModeMenu_main_convert_select_Time.grid(column=1, row=2)
        label_Time = customtkinter.CTkLabel(
            master=ModeMenu_main_convert_select_Time,
            width=(WINW),
            text=str("convert: " + Time_functions[a] + "to: " + Time_functions[b]),
            height=(40),
            font=("Roboto", 12),
            corner_radius=0,
        )
        label_Time.grid(column=1, row=1)
        entry_Time.grid(column=1, row=2)
        ActiveEntry = entry_Time
        resetFrames = 1

    else:
        a_str = str(val)
        SpeedData += a_str

        if a_str == "AC":
            his_data.set(SpeedData + " " + str(SpeedAns))
            entry_Time.delete("0.0", "end")
            entry_Time.insert("0.0", "")
            SpeedData = ""
        elif a_str == "C":
            entry_Time.delete("insert-1c")
            SpeedData = entry_Time.get("0.0", tk.END)

        elif val == "Ans":
            entry_Time.delete("0.0", "end")
            entry_Time.insert("0.0", SpeedAns)

        elif val == "=":
            if int(entry_Time.get("0.0", tk.END)):
                SpeedAns = Convertion_Time(a, b, entry_Time.get("0.0", tk.END))
                print(
                    a,
                    b,
                    entry_Time.get("0.0", tk.END),
                    Convertion_Time(a, b, entry_Time.get("0.0", tk.END)),
                    "....",
                )
                entry_Time.delete("0.0", "end")
                entry_Time.insert("0.0", str(SpeedAns) + " " + Time_functions[b])
            else:
                SpeedAns = "Syntax Error"
                entry_Time.delete("0.0", "end")
                entry_Time.insert("0.0", SpeedAns)
        else:
            entry_Time.insert(entry_Time.index("insert"), val)


def volumeConvertion(a, b, val):
    global ModeMenu_main_convert_select_volume
    global ModeMenu_main_convert
    global PerformVolume
    global SpeedData
    global SpeedAns
    global ActiveEntry
    global resetFrames

    a = int(a) - 1
    b = int(b) - 1
    volume_functions = [
        "(gal)",
        "(a)",
        "(ha)",
        "(cm)",
        "(in)",
        "(m)",
    ]
    if not PerformVolume:
        PerformVolume = True
        print("truetem")
        ModeMenu_main_convert.grid_remove()
        ModeMenu_main_convert_volume.grid_remove()
        ModeMenu_main_convert_select_volume.grid(column=1, row=2)
        label_volume = customtkinter.CTkLabel(
            master=ModeMenu_main_convert_select_volume,
            width=(WINW),
            text=str("convert: " + volume_functions[a] + "to: " + volume_functions[b]),
            height=(40),
            font=("Roboto", 12),
            corner_radius=0,
        )
        label_volume.grid(column=1, row=1)
        entry_volume.grid(column=1, row=2)
        ActiveEntry = entry_volume
        resetFrames = 1

    else:

        a_str = str(val)
        SpeedData += a_str

        if a_str == "AC":
            his_data.set(SpeedData + " " + str(SpeedAns))
            entry_volume.delete("0.0", "end")
            entry_volume.insert("0.0", "")
            SpeedData = ""
        elif a_str == "C":
            entry_volume.delete("insert-1c")
            SpeedData = entry_volume.get("0.0", tk.END)

        elif val == "Ans":
            entry_volume.delete("0.0", "end")
            entry_volume.insert("0.0", SpeedAns)

        elif val == "=":
            if int(entry_volume.get("0.0", tk.END)):
                SpeedAns = Convertion_volume(a, b, entry_volume.get("0.0", tk.END))
                print(
                    a,
                    b,
                    entry_volume.get("0.0", tk.END),
                    Convertion_volume(a, b, entry_volume.get("0.0", tk.END)),
                    "....",
                )
                entry_volume.delete("0.0", "end")
                entry_volume.insert("0.0", str(SpeedAns) + " " + volume_functions[b])
            else:
                SpeedAns = "Syntax Error"
                entry_volume.delete("0.0", "end")
                entry_volume.insert("0.0", SpeedAns)
        else:
            entry_volume.insert(entry_volume.index("insert"), val)


def Convertor(value):
    global direction
    global speed
    global Time
    global Temperature
    global Mass
    global Area
    global Length
    global Equation
    global Matrix
    global volume
    global mode_menu_convert
    global mode_more

    right = "-->"
    left = "<--"
    value = str(value)

    print("........................mode", mode_more)
    if mode_more:
        if value == "3":
            mode_menu_reset()
            mode_menu("mode_menu_convert")
        elif value == "1":
            mode_more = False
            Equation = True
            ModeMenu_main_modes.grid_remove()
            ModeMenu_main_convert_equation.grid(column=2, row=4)
            equation_functions = [
                "AX = 0",
                "AX" + subscriptValues[2] + "+ AX  = 0",
                "AX" + subscriptValues[3] + "+ AX" + subscriptValues[2] + "+ AX  = 0",
                "AX"
                + subscriptValues[4]
                + "+ AX"
                + subscriptValues[3]
                + "+ AX"
                + subscriptValues[2]
                + "+ AX  = 0",
            ]
            col_val = 1
            row_val = 0
            num = 0
            for equationChar in equation_functions:
                row_val += 1
                num += 1
                label = customtkinter.CTkLabel(
                    master=ModeMenu_main_convert_equation,
                    width=(WINW),
                    text=str(str(num) + " " + equationChar),
                    height=(140 / 3),
                    font=("Calculator", 16, "bold"),
                    justify="left",
                    anchor="w",
                )
                label.grid(column=col_val, row=row_val)
        elif value == "2":
            mode_more = False
            Matrix = True
            ModeMenu_main_modes.grid_remove()
            ModeMenu_main_convert_matrix.grid(column=2, row=4)
            matrix_functions = ["2 × 2", "2 × 3", "3 × 2", "3 × 3 "]
            col_val = 1
            row_val = 0
            num = 0
            for matrixChar in matrix_functions:
                row_val += 1
                num += 1
                label = customtkinter.CTkLabel(
                    master=ModeMenu_main_convert_matrix,
                    width=(WINW / 2),
                    text=str(str(num) + " " + matrixChar),
                    height=(140 / 3),
                    font=("Calculator", 16, "bold"),
                    justify="left",
                    anchor="w",
                )
                label.grid(column=col_val, row=row_val)

                if row_val == 3:
                    row_val = 0
                    col_val += 1

    elif value == "1":
        if direction == right:
            direction = left
        else:
            direction = right
        mode_menu_convert = "In State"
        Area = True
        ModeMenu_main_convert.grid_remove()
        # Arwa Modes functionality
        ModeMenu_main_convert_Area.grid(column=2, row=4)
        Area_functions = [
            "Acres(ac)",
            "Ares(a)",
            "Hectares(ha)",
            "Square centimetre(cm²)",
            "Square feet(ft²)",
            "Square inches(in²)",
            "square metres(m²)",
        ]
        col_val = 1
        row_val = 0
        num = 0
        for AreaChar in Area_functions:
            row_val += 1
            num += 1
            label = customtkinter.CTkLabel(
                master=ModeMenu_main_convert_Area,
                width=(WINW / 2),
                text=str(str(num) + " " + AreaChar + " " + direction),
                height=(140 / 4),
                font=("Calculator", 16, "bold"),
                justify="left",
                anchor="w",
            )
            label.grid(column=col_val, row=row_val)

            if row_val == 4:
                col_val += 1
                row_val = 0

    elif value == "2":
        if direction == right:
            direction = left
        else:
            direction = right
        mode_menu_convert = "In State"
        volume = True
        ModeMenu_main_convert.grid_remove()
        # volume Modes functionality
        ModeMenu_main_convert_volume.grid(column=2, row=4)
        volume_functions = [
            "Uk gallons(gal)",
            "Us gallons(gal)",
            "Litres(l)",
            "Millitres (ml)",
            "cubic centimetres (cc)(cm)",
            "Cubic metres (m)",
            "Cubics metres (in)",
            "Cubic feet (ft)",
        ]
        col_val = 1
        row_val = 0
        num = 0
        for volumeChar in volume_functions:
            row_val += 1
            num += 1
            label = customtkinter.CTkLabel(
                master=ModeMenu_main_convert_volume,
                width=(WINW / 2),
                text=str(str(num) + " " + volumeChar + " " + direction),
                height=(140 / 4),
                font=("Calculator", 16, "bold"),
                justify="left",
                anchor="w",
            )
            label.grid(column=col_val, row=row_val)

            if row_val == 4:
                col_val += 1
                row_val = 0

    elif value == "7":
        if direction == right:
            direction = left
        else:
            direction = right
        mode_menu_convert = "In State"
        Time = True
        ModeMenu_main_convert.grid_remove()
        # speed Modes functionality
        ModeMenu_main_convert_Time.grid(column=2, row=4)
        Time_functions = [
            "Milliseconds (ms)",
            "Seconds (s)",
            "Minutes (min)",
            "Hours (h)",
            "Days (d)",
            "Weeks()",
        ]
        col_val = 1
        row_val = 0
        num = 0
        for TimeChar in Time_functions:
            row_val += 1
            num += 1
            label = customtkinter.CTkLabel(
                master=ModeMenu_main_convert_Time,
                width=(WINW / 2),
                text=str(str(num) + " " + TimeChar + " " + direction),
                height=(140 / 4),
                font=("Calculator", 16, "bold"),
                justify="left",
                anchor="w",
            )
            label.grid(column=col_val, row=row_val)

            if row_val == 3:
                col_val += 1
                row_val = 0
    elif value == "8":
        mode_menu_more()
    elif value == "5":

        if direction == right:
            direction = left
        else:
            direction = right
        mode_menu_convert = "In State"
        Mass = True
        ModeMenu_main_convert.grid_remove()
        # speed Modes functionality
        ModeMenu_main_convert_Mass.grid(column=2, row=4)
        Mass_functions = [
            "Tons (t)",
            "UK tons (t)",
            "US ton (lb)",
            "Pounds (oz)",
            "Ounces (kg)",
            "Kilogrammes (kg)",
            "Grams(g)",
        ]
        col_val = 1
        row_val = 0
        num = 0
        for MassChar in Mass_functions:
            row_val += 1
            num += 1
            label = customtkinter.CTkLabel(
                master=ModeMenu_main_convert_Mass,
                width=(WINW / 2),
                text=str(str(num) + " " + MassChar + " " + direction),
                height=(140 / 4),
                font=("Calculator", 16, "bold"),
                justify="left",
                anchor="w",
            )
            label.grid(column=col_val, row=row_val)

            if row_val == 4:
                col_val += 1
                row_val = 0
    elif value == "6":
        if direction == right:
            direction = left
        else:
            direction = right
        mode_menu_convert = "In State"
        speed = True
        ModeMenu_main_convert.grid_remove()
        # speed Modes functionality
        ModeMenu_main_convert_speed.grid(column=2, row=4)
        Speed_functions = [
            "Meter per second",
            "Metres per hour",
            "Kilometres per second",
            "Kilometres per hour",
            "inches per second",
            "Inches per hour",
            "Miles per second",
            "Miles per hour",
        ]
        col_val = 1
        row_val = 0
        num = 0
        for speedChar in Speed_functions:
            row_val += 1
            num += 1
            label = customtkinter.CTkLabel(
                master=ModeMenu_main_convert_speed,
                width=(WINW / 2),
                text=str(str(num) + " " + speedChar + " " + direction),
                height=(140 / 4),
                font=("Calculator", 16, "bold"),
                justify="left",
                anchor="w",
            )
            label.grid(column=col_val, row=row_val)

            if row_val == 4:
                col_val += 1
                row_val = 0

    elif value == "3":
        if direction == right:
            direction = left
        else:
            direction = right
        mode_menu_convert = "In State"
        Length = True
        ModeMenu_main_convert.grid_remove()
        # speed Modes functionality
        ModeMenu_main_convert_Length.grid(column=2, row=4)
        Length_functions = [
            "Millimetres(mm)",
            "Centimetres(cm)",
            "Metres(m)",
            "Kilometres(km)",
            "Inches(in)",
            "Feet(ft)",
            "Yards(yf)",
            "Miles(mi)",
            "Nautical miles(NM)",
            "Mils(mil)",
        ]
        col_val = 1
        row_val = 0
        num = 0
        for LengthChar in Length_functions:
            row_val += 1
            num += 1
            label = customtkinter.CTkLabel(
                master=ModeMenu_main_convert_Length,
                width=(WINW / 2),
                text=str(str(num) + " " + LengthChar + " " + direction),
                height=(140 / 4),
                font=("Calculator", 14, "bold"),
                justify="left",
                anchor="w",
            )
            label.grid(column=col_val, row=row_val)
            if row_val == 5:
                col_val += 1
                row_val = 0
    elif value == "4":
        if direction == right:
            direction = left
        else:
            direction = right
        mode_menu_convert = "In State"
        Temperature = True
        ModeMenu_main_convert.grid_remove()
        # speed Modes functionality
        ModeMenu_main_convert_Temperature.grid(column=2, row=4)
        Temperature_functions = [
            "Celsius (⁰C)",
            "Fahrenheit (⁰F)",
            "Kelvin (K)",
        ]
        col_val = 1
        row_val = 0
        num = 0
        for TemperatureChar in Temperature_functions:
            row_val += 1
            num += 1
            label = customtkinter.CTkLabel(
                master=ModeMenu_main_convert_Temperature,
                width=(WINW),
                text=str(str(num) + " " + TemperatureChar + " " + direction),
                height=(140 / 3),
                font=("Calculator", 16, "bold"),
                justify="left",
                anchor="w",
            )
            label.grid(column=col_val, row=row_val)


def mode_menu_reset():
    global mode_menu_convert
    global compute
    global PerformSpeed
    global PerformTime
    global PerformLength
    global PerformMass
    global PerformArea
    global PerformTemperature
    global PerformVolume
    global PerformEquation
    global PerformMatrix
    global Equation
    global Matrix
    global SpeedAns
    global SpeedData
    global mode_more
    global compute
    global Temperature
    global Mass
    global Area
    global Length
    global Time
    global volume
    global speed
    global ConvertTo
    global ConvertFrom
    global entry_speed
    global entry_Time
    global entry_Mass
    global direction
    global entry_Temperature
    global ModeMenu_main_convert
    global ModeMenu_main_convert_select
    global ModeMenu_main_convert_select_speed
    global ModeMenu_main_convert_select_Time
    global ModeMenu_main_convert_Temperature
    global ModeMenu_main_convert_select_Mass
    global ModeMenu_main_convert_select_Temperature
    global ModeMenu_main_convert_Time
    global ModeMenu_main_convert_speed
    global ModeMenu_main_convert_Mass
    global ActiveEntry
    global resetFrames

    ActiveEntry = entry
    resetFrames = 0

    mode_menu_convert = False
    PerformArea = False
    direction = False
    compute = True
    ModeMenu_main_convert_select.grid_remove()
    ModeMenu_main_convert_select_speed.grid_remove()
    ModeMenu_main_convert_select_equation.grid_remove()
    ModeMenu_main_convert_select_matrix.grid_remove()
    ModeMenu_main_convert_speed.grid_remove()
    ModeMenu_main_convert_equation.grid_remove()
    ModeMenu_main_convert_matrix.grid_remove()
    ModeMenu_main_convert_Area.grid_remove()
    ModeMenu_main_convert_Length.grid_remove()
    ModeMenu_main_convert_select_Time.grid_remove()
    ModeMenu_main_convert_select_Length.grid_remove()
    ModeMenu_main_convert_Temperature.grid_remove()
    ModeMenu_main_convert_select_Mass.grid_remove()
    ModeMenu_main_convert_select_volume.grid_remove()
    ModeMenu_main_convert_Time.grid_remove()
    ModeMenu_main_convert_volume.grid_remove()
    ModeMenu_main_convert_Mass.grid_remove()
    ModeMenu_main_convert_select_Temperature.grid_remove()
    ModeMenu_main_convert_select_Area.grid_remove()
    ModeMenu_main_modes.grid_remove()
    ModeMenu_main_convert.grid_remove()
    PerformSpeed = False
    PerformTime = False
    PerformArea = False
    PerformLength = False
    PerformTemperature = False
    PerformMass = False
    PerformVolume = False
    PerformEquation = False
    PerformMatrix = False
    SpeedAns = ""
    SpeedData = ""
    SpTime = ""
    compute = True
    speed = False
    Equation = False
    Matrix = False
    mode_more = False
    Time = False
    Area = False
    Mass = False
    Length = False
    volume = False
    Temperature = False
    ConvertTo = 0
    ConvertFrom = 0
    entry.grid(column=1, row=1)
    # empty entry slots
    EntrySlots = [
        entry_speed,
        entry_Time,
        entry_Temperature,
        entry_Mass,
        entry_Area,
        entry_volume,
        entry_Length,
        entry_equation,
        entry_matrix,
    ]
    for entryFrame in EntrySlots:
        entryFrame.delete("0.0", "end")
        entryFrame.insert("0.0", " ")
        entryFrame.grid_remove()


def reset_frame_menu(value):
    global mode_menu_convert
    global compute
    global mode_menu_convert
    global mode_more

    mode_menu_reset()

    mode_menu_convert = True
    compute = False
    entry.grid_remove()
    ModeMenu_main_convert.grid(column=2, row=4)
    if mode_menu_convert != "In State" and mode_menu_convert == True:
        Convertor(value)


def mode_menu(value):
    global mode_menu_convert
    global compute
    global direction
    global speed
    global Time
    global Temperature
    global Mass
    global Area
    global Length
    global Equation
    global Matrix
    global volume
    global mode_menu_convert
    global mode_more
    global resetFrames

    if resetFrames == 1:
        if Area:
            reset_frame_menu("1")
        elif speed:
            reset_frame_menu("6")
        elif Time:
            reset_frame_menu("7")
        elif Temperature:
            reset_frame_menu("4")
        if Mass:
            reset_frame_menu("5")
        elif Length:
            reset_frame_menu("3")
        elif volume:
            reset_frame_menu("2")

        elif Equation:
            mode_more
            reset_frame_menu("8")
            Calc_input_display("1")
        if Matrix:
            mode_more
            reset_frame_menu("8")
            Calc_input_display("2")
    elif value == "mode_menu_convert":
        if mode_menu_convert == "In State" or mode_menu_convert == True:
            mode_menu_reset()
        else:
            mode_menu_convert = True
            compute = False
            entry.grid_remove()
            # speed Modes functionality
            ModeMenu_main_convert.grid(column=2, row=4)
            menu_functions = [
                "Area",
                "Volume",
                "length",
                "Temperature",
                "Mass",
                "Speed",
                "Time",
                "more...",
            ]
            col_val = 1
            row_val = 0
            num = 0
            for speedChar in menu_functions:
                row_val += 1
                num += 1
                label_menu = customtkinter.CTkLabel(
                    master=ModeMenu_main_convert,
                    width=(WINW / 2),
                    text="  " + str(str(num) + "  " + speedChar),
                    height=(140 / 4),
                    font=("Calculator", 22, "bold"),
                    justify="left",
                    anchor="w",
                )
                label_menu.grid(column=col_val, row=row_val)

                if row_val == 4:
                    col_val += 1
                    row_val = 0


def Calc_input_display(value):
    global OriginalData
    global numericObg
    global userInput
    global basicArrays
    global complexArrays
    global ExpFormation
    global Ans
    global PerformSpeed
    global data
    global Equation
    global Matrix
    global Time
    global Area
    global Mass
    global Length
    global volume
    global mode_more
    global PerformTime
    global PerformLength
    global PerformVolume
    global PerformEquation
    global PerformMatrix
    global PerformTemperature
    global PerformMass
    global mode_menu_convert
    global ConvertTo
    global ConvertFrom
    global subscript_move
    global ActiveEntry

    global new
    ActiveEntry.focus_set()

    if mode_menu_convert != "In State" and mode_menu_convert == True:
        Convertor(value)
    elif mode_more:
        Convertor(value)
    elif Equation:
        if (
            value == "="
            or value == "C"
            or value == "Ans"
            or value == "AC"
            or value == "×"
            or value == "+"
            or value == "-"
            or value == "÷"
            or value.isnumeric()
        ):
            if PerformEquation == True:
                EquationConvertion(ConvertTo, value)

            else:
                ConvertTo = value
                EquationConvertion(ConvertTo, value)
    elif Matrix:
        if (
            value == "="
            or value == "C"
            or value == "Ans"
            or value == "AC"
            or value == "×"
            or value == "+"
            or value == "-"
            or value == "÷"
            or value.isnumeric()
        ):
            if PerformMatrix == True:
                MatrixConvertion(ConvertTo, value)

            else:
                ConvertTo = value
                MatrixConvertion(ConvertTo, value)

    elif speed:
        if (
            value == "="
            or value == "C"
            or value == "Ans"
            or value == "AC"
            or value.isnumeric()
        ):

            if PerformSpeed == True:
                SpeedConvertion(ConvertTo, ConvertFrom, value)

            elif ConvertTo != 0:
                ConvertFrom = value
                SpeedConvertion(ConvertTo, ConvertFrom, value)
            else:
                ConvertTo = value
                Convertor("6")
    elif Time:
        if (
            value == "="
            or value == "C"
            or value == "Ans"
            or value == "AC"
            or value.isnumeric()
        ):
            if PerformTime == True:
                TimeConvertion(ConvertTo, ConvertFrom, value)

            elif ConvertTo != 0:
                ConvertFrom = value
                TimeConvertion(ConvertTo, ConvertFrom, value)
            else:
                ConvertTo = value
                Convertor("3")
    elif Temperature:
        if (
            value == "="
            or value == "C"
            or value == "Ans"
            or value == "AC"
            or value.isnumeric()
        ):

            if PerformTemperature == True:

                TemperatureConvertion(ConvertTo, ConvertFrom, value)
            elif ConvertTo != 0:

                ConvertFrom = value
                TemperatureConvertion(ConvertTo, ConvertFrom, value)
            else:

                ConvertTo = value
                Convertor("4")
    elif Mass:
        if (
            value == "="
            or value == "C"
            or value == "Ans"
            or value == "AC"
            or value.isnumeric()
        ):

            if PerformMass == True:
                MassConvertion(ConvertTo, ConvertFrom, value)
            elif ConvertTo != 0:

                ConvertFrom = value
                MassConvertion(ConvertTo, ConvertFrom, value)
            else:

                ConvertTo = value
                Convertor("5")
    elif Area:
        if (
            value == "="
            or value == "C"
            or value == "Ans"
            or value == "AC"
            or value.isnumeric()
        ):

            if PerformArea == True:
                AreaConvertion(ConvertTo, ConvertFrom, value)
            elif ConvertTo != 0:

                ConvertFrom = value
                AreaConvertion(ConvertTo, ConvertFrom, value)
            else:

                ConvertTo = value
                Convertor("1")
    elif volume:
        if (
            value == "="
            or value == "C"
            or value == "Ans"
            or value == "AC"
            or value.isnumeric()
        ):
            if PerformVolume == True:
                volumeConvertion(ConvertTo, ConvertFrom, value)
            elif ConvertTo != 0:
                ConvertFrom = value
                volumeConvertion(ConvertTo, ConvertFrom, value)
            else:
                ConvertTo = value
                Convertor("2")
    elif Length:
        if (
            value == "="
            or value == "C"
            or value == "Ans"
            or value == "AC"
            or value.isnumeric()
        ):
            if PerformLength == True:
                LengthConvertion(ConvertTo, ConvertFrom, value)
            elif ConvertTo != 0:
                ConvertFrom = value
                LengthConvertion(ConvertTo, ConvertFrom, value)
            else:
                ConvertTo = value
                Convertor("3")

    elif compute:
        a = str(value)
        if subscript_move:
            if int(a):
                a = subscriptValues[int(a)]
                subscript_move = False

        if a != "AC" and a != "Ans" and a != "C" and a != "=" and a != "S<=>D":
            if a == "ⁿ":
                a += "^("
            elif a == "\n":
                a = ""
            elif a == "logₓX":
                subscript_move = True
                a = "log"
        if a == "S<=>D":
            if isfloat(Ans):
                Ans = Fraction(Decimal(str(Ans)))
                entry.delete("0.0", "end")
                entry.insert("0.0", Ans)
                OriginalData = str(Ans)
            elif Ans != " ":
                Ans = Fraction(str(Ans))
                entry.delete("0.0", "end")
                entry.insert("0.0", Ans)

        elif a == "AC":
            if ExpFormation != "":
                # find a way to strip white space
                his_data.set(ExpFormation + " = " + str(Ans))
                entry.delete("0.0", "end")
                entry.insert("0.0", "")
                OriginalData = ""
                ExpFormation = ""
        elif a == "C":
            entry.delete("insert-1c")
            OriginalData = entry.get("1.0", tk.END)
            ExpFormation = entry.get("1.0", tk.END)

        elif value == "Ans":
            entry.delete("0.0", "end")
            entry.insert("0.0", Ans)
            OriginalData = str(Ans)
        elif value == "=":
            userInput = []
            userInput.extend(entry.get("1.0", tk.END))
            ExpFormation = entry.get("1.0", tk.END)
            if conditionChecker(userInput) == True:
                Ans = bracket_solu(userInput)
                entry.delete("0.0", "end")
                entry.insert("0.0", Ans)
                OriginalData = str(Ans)
            else:
                Ans = "Syntax Error"
                entry.delete("0.0", "end")
                entry.insert("0.0", Ans)
        else:
            entry.insert(entry.index("insert"), a)


def mode_menu_more():
    global mode_menu_convert
    global mode_more

    mode_menu_convert = "In State"
    mode_more = True
    ModeMenu_main_convert.grid_remove()
    ModeMenu_main_modes.grid(column=2, row=4)
    modes_functions = [
        "Equations (Eq)",
        "Matrix",
        "...prev",
    ]
    col_val = 1
    row_val = 0
    num = 0
    for modeChar in modes_functions:
        row_val += 1
        num += 1
        label = customtkinter.CTkLabel(
            master=ModeMenu_main_modes,
            width=WINW,
            text=str(str(num) + " " + modeChar),
            height=(140 / 4),
            font=("Calculator", 16, "bold"),
            justify="left",
            anchor="w",
        )
        label.grid(column=col_val, row=row_val)
        if row_val == 4:
            col_val += 1
            row_val = 0


def conditionChecker(userInput):
    value = True
    for char in userInput:
        Index = userInput.index(char)

        if Index + 1 != len(userInput):
            if char in basicArrays and userInput[Index + 1] in basicArrays:

                value = False
            if (
                char != "√"
                and char != "π"
                and char in complexArrays
                and userInput[Index + 3] in basicArrays
                or char != "√"
                and char != "π"
                and char in complexArrays
                and userInput[Index + 3] in complexArrays
            ):
                value = False
            if char.isnumeric() and userInput[Index + 1] in complexArrays:

                value = False
            if char == "(" and userInput[Index + 1] == ")":

                value = False

            if (
                char != "√"
                and char != "π"
                and char in complexArrays
                and userInput[Index + 3] == ")"
            ):

                value = False

        else:
            if char in basicArrays or char == "(":
                value = False
    return value


def computeResult(userInput):

    if isinstance(userInput, list):
        value = userInput[0]
    else:
        value = userInput
    index = 0

    multiFactor = 0
    SingleFactor = 0

    if len(userInput) == 0:
        print("Cant Compute")
    else:
        loopCondition = False
        valueCheck = ["t", "S", "c", "R", "D", "√", "l"]
        for valueChar in valueCheck:
            if valueChar in userInput:
                loopCondition = True

        if loopCondition == True:
            for entry in userInput:
                entry = str(entry)
                # solve breakdown complex
                if "t" in entry:
                    multiFactor = 1
                    index = userInput.index(entry)
                    if "⁻" in userInput and userInput[index + 3] == "⁻":
                        SingleFactor = 1
                        number = userInput[index + 5]
                        if isfloat(number):
                            number = float(userInput[index + 5])
                        else:
                            number = int(userInput[index + 5])
                        value = math.atan(number)
                    elif len(userInput) != index + 1 and userInput[index + 3] == "×":
                        number = userInput[index + 2]
                        if isfloat(number):
                            number = float(userInput[index + 2])
                        else:
                            number = int(userInput[index + 2])
                        value = math.atan(number)
                    else:
                        number = userInput[index + 3]
                        if isfloat(number):
                            number = float(userInput[index + 3])
                        else:
                            number = int(userInput[index + 3])
                        value = math.atan(number)

                if "S" in entry:
                    multiFactor = 1
                    index = userInput.index(entry)
                    if "⁻" in userInput and userInput[index + 3] == "⁻":
                        SingleFactor = 1
                        number = userInput[index + 5]
                        if isfloat(number):
                            number = float(userInput[index + 5])
                        else:
                            number = int(userInput[index + 5])

                        value = math.sin(number)
                    elif len(userInput) != index + 1 and userInput[index + 3] == "×":
                        number = userInput[index + 2]
                        if isfloat(number):
                            number = float(userInput[index + 2])
                        else:
                            number = int(userInput[index + 2])
                        value = math.sin(number)

                    else:
                        value = math.sin(float(userInput[index + 3]))

                if "c" in entry:
                    multiFactor = 1
                    index = userInput.index(entry)
                    if "⁻" in userInput and userInput[index + 3] == "⁻":
                        SingleFactor = 1
                        number = userInput[index + 5]
                        if isfloat(number):
                            number = float(userInput[index + 5])
                        else:
                            number = int(userInput[index + 5])

                        value = math.acos(number)
                    elif len(userInput) != index + 1 and userInput[index + 3] == "×":
                        number = userInput[index + 2]
                        if isfloat(number):
                            number = float(userInput[index + 2])
                        else:
                            number = int(userInput[index + 2])

                        value = math.cos(number)

                    else:
                        number = userInput[index + 3]
                        if isfloat(number):
                            number = float(userInput[index + 3])
                        else:
                            number = int(userInput[index + 3])

                        value = math.cos(number)

                if "R" in entry:
                    multiFactor = 1

                    index = userInput.index(entry)

                    if len(userInput) != index + 1 and userInput[index + 3] == "×":
                        number = userInput[index + 2]
                        if isfloat(number):
                            number = float(userInput[index + 2])
                        else:
                            number = int(userInput[index + 2])

                        value = math.rad(number)

                    else:
                        number = userInput[index + 3]
                        if isfloat(number):
                            number = float(userInput[index + 3])
                        else:
                            number = int(userInput[index + 3])

                        value = math.rad(number)

                if "D" in entry:
                    multiFactor = 1

                    index = userInput.index(entry)

                    if len(userInput) != index + 1 and userInput[index + 3] == "×":
                        number = userInput[index + 2]
                        if isfloat(number):
                            number = float(userInput[index + 2])
                        else:
                            number = int(userInput[index + 2])

                        value = math.deg(float(userInput[index + 2]))

                    else:
                        value = math.deg(number)

                if "√" in entry:
                    index = userInput.index(entry)
                    if len(userInput) != index + 1 and userInput[index + 1] == "×":
                        number = userInput[index + 1]
                        if isfloat(number):
                            number = float(userInput[index + 1])
                        else:
                            number = int(userInput[index + 1])

                        value = math.sqrt(number)
                        userInput.pop(index + 1)
                        multiFactor = 1
                    else:
                        number = userInput[index + 1]
                        if isfloat(number):
                            number = float(userInput[index + 1])
                        else:
                            number = int(userInput[index + 1])

                        value = math.sqrt(number)
                        userInput.pop(index + 1)

                if "l" in entry:
                    multiFactor = 1

                    index = userInput.index(entry)

                    if len(userInput) != index + 1 and userInput[index + 3] == ".":
                        if isfloat(userInput[index + 4]):
                            value = "invalid"
                        else:
                            baseVal = int(userInput[index + 4])
                            numVal = int(userInput[index + 5])
                            value = (math.log(baseVal)) * (numVal)
                            userInput.pop(index + 3)

                    elif len(userInput) != index + 1 and userInput[index + 3] == "×":
                        number = userInput[index + 2]
                        if isfloat(number):
                            number = float(userInput[index + 2])
                        else:
                            number = int(userInput[index + 2])

                        value = math.log(number)

                    else:
                        number = userInput[index + 3]
                        valueChr = userInput[index + 3]
                        if userInput[index + 3] in subscriptValues:
                            valueChr = subscriptValues.index(userInput[index + 3]) + 1

                        if isfloat(number):
                            number = float(valueChr)
                        else:
                            number = int(valueChr)
                        value = math.log(number)

                if multiFactor == 1 and SingleFactor == 1:
                    userInput[index] = str(value)
                    for i in range(4):
                        userInput.pop(index + 1)

                elif multiFactor == 1 and SingleFactor == 0:
                    userInput[index] = str(value)
                    for i in range(2):
                        userInput.pop(index + 1)
                else:
                    userInput[index] = str(value)
                    print("val", userInput, userInput[index])

                multiFactor = 0
                SingleFactor = 0

        evaluateChar = ""

        for char in userInput:
            charIndex = userInput.index(char)
            if char in subscriptValues:
                valueChr = subscriptValues.index(char) + 1
            elif char == "×":
                evaluateChar += "*"
            elif char == "π":
                evaluateChar += "22/7"
            elif char == "÷":
                evaluateChar += "/"
            elif char == "²":
                evaluateChar += "**2"
            elif char == "³":
                evaluateChar += "**3"
            elif char == "^":
                evaluateChar += "*1"
            elif (
                charIndex + 1 < len(userInput)
                and (charIndex + 2) <= len(userInput)
                and char not in basicArrays
                and userInput[charIndex + 1] not in basicArrays
                and isinstance(userInput[charIndex + 1], str) == False
            ):

                evaluateChar += str(char) + "*"
            else:
                evaluateChar += str(char)

        try:
            print("userInput-", evaluateChar, index, userInput)
            userInput = eval(evaluateChar)
        except Exception as e:
            userInput = "Invalid syntax"

        return userInput


def bracket_solu(InputData):
    startPosition = 0
    EndPosition = 0
    rangeData = 0
    start = 0
    new_InputData = []
    para_thesis_List = []
    if "(" in InputData:

        startPosition = InputData.index("(")

        EndPosition = InputData.index(")")

        start = startPosition

        # determin end of bracket

        while start > -1:

            if InputData[start] == "(":

                startPosition = start

                rangeData = 0

            elif InputData[start] == ")":

                break

            else:

                rangeData = rangeData + 1

            start += 1

        for i in range(rangeData):

            para_thesis_List.append(InputData[startPosition + i + 1])

        if computeResult(para_thesis_List) != False:
            Ans = computeResult(para_thesis_List)
            InputData.pop(startPosition)

            InputData.pop(EndPosition - 1)

            for i in range(rangeData):

                if rangeData - 1 == i:

                    InputData[startPosition] = Ans

                else:

                    InputData.pop(startPosition)

        if "(" in InputData:
            bracket_solu(InputData)

    print("InputData-we", InputData, new_InputData)
    return computeResult(InputData)


def isfloat(num):
    print(num)
    try:
        float(num)
        return True
    except ValueError:

        return False


Radians = customtkinter.CTkButton(
    master=FunctionFrames_innerFrame,
    text="Rad",
    font=("Roboto", 20),
    width=FunctionFramesBtnWidth,
    height=35,
    fg_color="#1e1e1f",
    hover_color="#0773a4",
    command=lambda: Calc_input_display("Rad("),
)
Radians.grid(column=1, row=1, padx=(0, 0), pady=(2, 5))

Degree = customtkinter.CTkButton(
    master=FunctionFrames_innerFrame,
    text="Deg",
    font=("Roboto", 20),
    width=FunctionFramesBtnWidth,
    fg_color="#1e1e1f",
    hover_color="#0773a4",
    height=35,
    command=lambda: Calc_input_display("Deg("),
)

Degree.grid(column=2, row=1, padx=(0, 0), pady=(2, 5))
SinButton = customtkinter.CTkButton(
    master=FunctionFrames_innerFrame,
    text="sin",
    font=("Roboto", 20),
    width=FunctionFramesBtnWidth,
    height=35,
    fg_color="#1e1e1f",
    hover_color="#0773a4",
    command=lambda: Calc_input_display("Sin("),
)
SinButton.grid(column=3, row=1, padx=(0, 0), pady=(0, 5))
tanButton = customtkinter.CTkButton(
    master=FunctionFrames_innerFrame,
    text="tan",
    font=("Roboto", 20),
    width=FunctionFramesBtnWidth,
    height=35,
    fg_color="#1e1e1f",
    hover_color="#0773a4",
    command=lambda: Calc_input_display("tan("),
)
tanButton.grid(column=4, row=1, padx=(0, 0), pady=(0, 5))
CosButton = customtkinter.CTkButton(
    master=FunctionFrames_innerFrame,
    text="cos",
    font=("Roboto", 20),
    width=FunctionFramesBtnWidth,
    height=35,
    fg_color="#1e1e1f",
    hover_color="#0773a4",
    command=lambda: Calc_input_display("cos("),
)
CosButton.grid(column=5, row=1, padx=(0, 0), pady=(0, 5))

LogButton = customtkinter.CTkButton(
    master=FunctionFrames_innerFrame,
    text="log",
    font=("Roboto", 20),
    width=FunctionFramesBtnWidth,
    height=35,
    fg_color="#1e1e1f",
    hover_color="#0773a4",
    command=lambda: Calc_input_display("log("),
)
LogButton.grid(column=6, row=1, padx=(0, 0), pady=(0, 5))


Xpower_num = customtkinter.CTkButton(
    master=FunctionFrames_innerFrame,
    font=("Roboto", 20),
    width=FunctionFramesBtnWidth,
    text="xⁿ",
    fg_color="#1e1e1f",
    hover_color="#0773a4",
    height=35,
    corner_radius=8,
    command=lambda: Calc_input_display("ⁿ"),
)
Xpower_num.grid(column=2, row=2, padx=(0, 2), pady=(0, 5))

Xpower_cube = customtkinter.CTkButton(
    master=FunctionFrames_innerFrame,
    font=("Roboto", 20),
    width=FunctionFramesBtnWidth,
    text="x³",
    fg_color="#1e1e1f",
    hover_color="#0773a4",
    height=35,
    corner_radius=8,
    command=lambda: Calc_input_display("³"),
)
Xpower_cube.grid(column=1, row=2, padx=(0, 2), pady=(0, 5))


Xsquare = customtkinter.CTkButton(
    master=FunctionFrames_innerFrame,
    font=("Roboto", 20),
    text="x²",
    width=FunctionFramesBtnWidth,
    height=35,
    fg_color="#1e1e1f",
    hover_color="#0773a4",
    command=lambda: Calc_input_display("²"),
)
Xsquare.grid(column=5, row=2, padx=(0, 3), pady=(2, 5))


sinInverseBtn = customtkinter.CTkButton(
    master=FunctionFrames_innerFrame,
    font=("Roboto", 16),
    text="sin⁻¹",
    width=FunctionFramesBtnWidth,
    height=35,
    fg_color="#1e1e1f",
    hover_color="#0773a4",
    command=lambda: Calc_input_display("Sin⁻¹("),
)
sinInverseBtn.grid(column=6, row=2, padx=(0, 3), pady=(2, 5))

tanInverseBtn = customtkinter.CTkButton(
    master=FunctionFrames_innerFrame,
    font=("Roboto", 16),
    text="tan⁻¹",
    width=FunctionFramesBtnWidth,
    height=35,
    fg_color="#1e1e1f",
    hover_color="#0773a4",
    command=lambda: Calc_input_display("tan⁻¹("),
)
tanInverseBtn.grid(column=1, row=3, padx=(0, 3), pady=(2, 5))

cosInverseBtn = customtkinter.CTkButton(
    master=FunctionFrames_innerFrame,
    font=("Roboto", 16),
    text="cos⁻¹",
    width=FunctionFramesBtnWidth,
    height=35,
    fg_color="#1e1e1f",
    hover_color="#0773a4",
    command=lambda: Calc_input_display("cos⁻¹("),
)
cosInverseBtn.grid(column=2, row=3, padx=(0, 3), pady=(2, 5))


logBaseNum = customtkinter.CTkButton(
    master=FunctionFrames_innerFrame,
    font=("Roboto", 16),
    text="logₓX",
    width=FunctionFramesBtnWidth,
    height=35,
    fg_color="#1e1e1f",
    hover_color="#0773a4",
    command=lambda: Calc_input_display("logₓX"),
)
logBaseNum.grid(column=5, row=3, padx=(0, 3), pady=(2, 5))

PieButton = customtkinter.CTkButton(
    master=FunctionFrames_innerFrame,
    text="π",
    font=("Roboto", 20),
    width=FunctionFramesBtnWidth,
    height=35,
    fg_color="#1e1e1f",
    hover_color="#0773a4",
    corner_radius=8,
    command=lambda: Calc_input_display("π"),
)
PieButton.grid(column=6, row=3, padx=(0, 3), pady=(2, 5))

Square_root = customtkinter.CTkButton(
    master=FunctionFrames_innerFrame,
    font=("Roboto", 20),
    width=FunctionFramesBtnWidth,
    text="√ⁿ",
    fg_color="#1e1e1f",
    hover_color="#0773a4",
    height=35,
    corner_radius=8,
    command=lambda: Calc_input_display("√("),
)
Square_root.grid(column=2, row=4, padx=(0, 3), pady=(2, 5))

logInverse = customtkinter.CTkButton(
    master=FunctionFrames_innerFrame,
    font=("Roboto", 16),
    text="log⁻¹",
    width=FunctionFramesBtnWidth,
    height=35,
    fg_color="#1e1e1f",
    hover_color="#0773a4",
    command=lambda: Calc_input_display("log⁻¹"),
)
logInverse.grid(column=1, row=4, padx=(0, 3), pady=(2, 5))

# MAc.grid(column=4, row=4, padx=(0, 3), pady=(2, 5))

fractionConvert = customtkinter.CTkButton(
    master=FunctionFrames_innerFrame,
    font=("Roboto", 18),
    text="S<=>D",
    width=FunctionFramesBtnWidth,
    height=35,
    fg_color="#1e1e1f",
    hover_color="#0773a4",
    command=lambda: Calc_input_display("S<=>D"),
)
fractionConvert.grid(column=5, row=4, padx=(0, 3), pady=(2, 5))

Menu = customtkinter.CTkButton(
    master=FunctionFrames_innerFrame,
    font=("Roboto", 20),
    text="Menu",
    width=FunctionFramesBtnWidth,
    height=35,
    fg_color="#1e1e1f",
    hover_color="#0773a4",
    command=lambda: mode_menu("mode_menu_convert"),
)
Menu.grid(column=6, row=4, padx=(0, 3), pady=(2, 5))
CurlButton = customtkinter.CTkButton(
    master=FunctionFrames_innerFrame,
    text="(",
    font=("Roboto", 20),
    width=FunctionFramesBtnWidth,
    height=35,
    fg_color="#1e1e1f",
    hover_color="#0773a4",
    command=lambda: Calc_input_display("("),
)
CurlButton.grid(column=3, row=4, padx=(0, 0), pady=(2, 5))

CurlyHalf = customtkinter.CTkButton(
    master=FunctionFrames_innerFrame,
    text=")",
    font=("Roboto", 20),
    width=FunctionFramesBtnWidth,
    height=35,
    fg_color="#1e1e1f",
    hover_color="#0773a4",
    corner_radius=8,
    command=lambda: Calc_input_display(")"),
)
CurlyHalf.grid(column=4, row=4, padx=(0, 0), pady=(2, 5))

# convertions

Subtraction_Button = customtkinter.CTkButton(
    master=Btns_innserFrame_innerFrame,
    font=("Roboto", 20),
    text="-",
    width=FramesBtnWidth,
    height=40,
    fg_color="#303031",
    hover_color="#0773a4",
    corner_radius=8,
    command=lambda: Calc_input_display("-"),
)
Subtraction_Button.grid(column=5, row=7, padx=(0, 5), pady=(0, 5))
Addition_Button = customtkinter.CTkButton(
    master=Btns_innserFrame_innerFrame,
    text="+",
    font=("Roboto", 20),
    width=FramesBtnWidth,
    height=40,
    fg_color="#303031",
    hover_color="#0773a4",
    command=lambda: Calc_input_display("+"),
)
Addition_Button.grid(column=4, row=7, padx=(0, 3), pady=(0, 5))


buttonOne = customtkinter.CTkButton(
    master=Btns_innserFrame_innerFrame,
    text="1",
    font=("Roboto", 20),
    width=FramesBtnWidth,
    height=40,
    fg_color="#303031",
    hover_color="#0773a4",
    command=lambda: Calc_input_display("1"),
)
buttonOne.grid(column=1, row=7, padx=(0, 3), pady=(0, 5))

buttonTwo = customtkinter.CTkButton(
    master=Btns_innserFrame_innerFrame,
    text="2",
    font=("Roboto", 20),
    width=FramesBtnWidth,
    height=40,
    fg_color="#303031",
    hover_color="#0773a4",
    command=lambda: Calc_input_display("2"),
)
buttonTwo.grid(column=2, row=7, padx=(0, 3), pady=(0, 5))


ButtonThree = customtkinter.CTkButton(
    master=Btns_innserFrame_innerFrame,
    text="3",
    font=("Roboto", 20),
    width=FramesBtnWidth,
    height=40,
    fg_color="#303031",
    hover_color="#0773a4",
    command=lambda: Calc_input_display("3"),
)
ButtonThree.grid(column=3, row=7, padx=(0, 3), pady=(0, 5))

buttonFour = customtkinter.CTkButton(
    master=Btns_innserFrame_innerFrame,
    text="4",
    font=("Roboto", 20),
    width=FramesBtnWidth,
    height=40,
    fg_color="#303031",
    hover_color="#0773a4",
    command=lambda: Calc_input_display("4"),
)
buttonFour.grid(column=1, row=6, padx=(0, 3), pady=(0, 5))


buttonFive = customtkinter.CTkButton(
    master=Btns_innserFrame_innerFrame,
    text="5",
    font=("Roboto", 20),
    width=FramesBtnWidth,
    height=40,
    fg_color="#303031",
    hover_color="#0773a4",
    command=lambda: Calc_input_display("5"),
)
buttonFive.grid(column=2, row=6, padx=(0, 3), pady=(0, 5))


buttonSix = customtkinter.CTkButton(
    master=Btns_innserFrame_innerFrame,
    text="6",
    font=("Roboto", 20),
    width=FramesBtnWidth,
    height=40,
    fg_color="#303031",
    hover_color="#0773a4",
    command=lambda: Calc_input_display("6"),
)
buttonSix.grid(column=3, row=6, padx=(0, 3), pady=(0, 5))


ClearButton = customtkinter.CTkButton(
    master=Btns_innserFrame_innerFrame,
    text="C",
    font=("Roboto", 20),
    width=FramesBtnWidth,
    height=40,
    fg_color="#303031",
    hover_color="#0773a4",
    command=lambda: Calc_input_display("C"),
)
ClearButton.grid(column=4, row=5, padx=(0, 3), pady=(0, 5))


multiplication = customtkinter.CTkButton(
    master=Btns_innserFrame_innerFrame,
    text="×",
    font=("Roboto", 20),
    width=FramesBtnWidth,
    height=40,
    fg_color="#303031",
    hover_color="#0773a4",
    command=lambda: Calc_input_display("×"),
)
multiplication.grid(column=4, row=6, padx=(0, 3), pady=(0, 5))
DivisionButton = customtkinter.CTkButton(
    master=Btns_innserFrame_innerFrame,
    text="÷",
    font=("Roboto", 20),
    width=FramesBtnWidth,
    height=40,
    fg_color="#303031",
    hover_color="#0773a4",
    command=lambda: Calc_input_display("÷"),
)
DivisionButton.grid(column=5, row=6, padx=(0, 3), pady=(0, 5))


buttonSeven = customtkinter.CTkButton(
    master=Btns_innserFrame_innerFrame,
    text="7",
    font=("Roboto", 20),
    width=FramesBtnWidth,
    height=40,
    fg_color="#303031",
    hover_color="#0773a4",
    command=lambda: Calc_input_display("7"),
)

buttonSeven.grid(column=1, row=5, padx=(0, 3), pady=(0, 5))

buttonEight = customtkinter.CTkButton(
    master=Btns_innserFrame_innerFrame,
    text="8",
    font=("Roboto", 20),
    width=FramesBtnWidth,
    height=40,
    fg_color="#303031",
    hover_color="#0773a4",
    command=lambda: Calc_input_display("8"),
)

buttonEight.grid(column=2, row=5, padx=(0, 3), pady=(0, 5))

buttonNine = customtkinter.CTkButton(
    master=Btns_innserFrame_innerFrame,
    text="9",
    font=("Roboto", 20),
    width=FramesBtnWidth,
    height=40,
    fg_color="#303031",
    hover_color="#0773a4",
    command=lambda: Calc_input_display("9"),
)
buttonNine.grid(column=3, row=5, padx=(0, 3), pady=(0, 5))
Allclear = customtkinter.CTkButton(
    master=Btns_innserFrame_innerFrame,
    text="AC",
    font=("Roboto", 20),
    width=FramesBtnWidth,
    height=40,
    fg_color="#2b8806",
    hover_color="#4ef80b",
    command=lambda: Calc_input_display("AC"),
)
Allclear.grid(column=5, row=5, padx=(0, 3), pady=(0, 5))
ZeroButton = customtkinter.CTkButton(
    master=Btns_innserFrame_innerFrame,
    text="0",
    font=("Roboto", 20),
    width=FramesBtnWidth,
    height=40,
    fg_color="#303031",
    hover_color="#0773a4",
    command=lambda: Calc_input_display("0"),
)

ZeroButton.grid(column=1, row=8, padx=(0, 3), pady=(0, 5))

DotButton = customtkinter.CTkButton(
    master=Btns_innserFrame_innerFrame,
    text="•",
    font=("Roboto", 20),
    width=FramesBtnWidth,
    height=40,
    fg_color="#303031",
    hover_color="#0773a4",
    command=lambda: Calc_input_display("."),
)

DotButton.grid(column=2, row=8, padx=(0, 3), pady=(0, 5))


Equal_Sign = customtkinter.CTkButton(
    master=Btns_innserFrame_innerFrame,
    font=("Roboto", 20),
    text="=",
    width=FramesBtnWidth,
    height=40,
    fg_color="#303031",
    hover_color="#0773a4",
    command=lambda: Calc_input_display("="),
)
Equal_Sign.grid(column=5, row=8, padx=(0, 3), pady=(0, 5))

IOTopower = customtkinter.CTkButton(
    master=Btns_innserFrame_innerFrame,
    font=("Roboto", 20),
    text="ₓ10ᶰ",
    width=FramesBtnWidth,
    height=40,
    fg_color="#303031",
    hover_color="#0773a4",
    command=lambda: Calc_input_display("ₓ10ᶰ"),
)
IOTopower.grid(column=3, row=8, padx=(0, 3), pady=(0, 5))

Answer = customtkinter.CTkButton(
    master=Btns_innserFrame_innerFrame,
    text="Ans",
    font=("Roboto", 20),
    width=FramesBtnWidth,
    height=40,
    command=lambda: Calc_input_display("Ans"),
    fg_color="red",
)
Answer.grid(column=4, row=8, padx=(0, 3), pady=(0, 5))


root.mainloop()
