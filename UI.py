import customtkinter

import tkinter as tk

import math


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

OriginalData = ""
numericObg = ""
basicArrays = ["+", "-", "÷", "×"]
complexArrays = ["R", "D", "t", "c", "S", "l", "π", "√", "%", "x²"]
userInput = []
new = []
ExpFormation = ""
Ans = ""
data = ""
# modes
PerformSpeed = False
mode_menu_convert = False
SpeedAns = ""
SpeedData = ""
compute = True
speed = False
ConvertTo = 0
ConvertFrom = 0

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
MenuFrame.grid(column=1, row=2)
entry = customtkinter.CTkEntry(
    master=MenuFrame,
    width=WINW,
    height=140,
    font=("Roboto", 24),
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
entry_speed = customtkinter.CTkEntry(
    master=ModeMenu_main_convert_select,
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


def SpeedConvertion(a, b, val):
    global PerformSpeed
    global SpeedData
    global SpeedAns

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
        ModeMenu_main_convert_speed.grid_remove()
        ModeMenu_main_convert_select.grid(column=1, row=2)
        label_speed = customtkinter.CTkLabel(
            master=ModeMenu_main_convert_select,
            width=(WINW),
            text=str("convert: " + Speed_functions[a] + "to: " + Speed_functions[b]),
            height=(40),
            font=("Roboto", 12),
            corner_radius=0,
        )
        label_speed.grid(column=1, row=1)
        entry_speed.grid(column=1, row=2)

    else:
        a_str = str(val)
        SpeedData += a_str

        if a_str == "AC":
            his_data.set(SpeedData + " " + str(SpeedAns))
            entry_speed.delete(0, "end")
            entry_speed.insert(0, "")
            SpeedData = ""
        elif a_str == "C":
            CurrentVal = entry_speed.index("insert")
            entry_speed.delete(CurrentVal - 1)
            SpeedData = entry_speed.get()

        elif val == "Ans":
            entry_speed.delete(0, "end")
            entry_speed.insert(0, SpeedAns)

        elif val == "=":
            print(entry_speed.get(), SpeedData)
            if entry_speed.get().isnumeric():
                SpeedAns = Convertion_speed(a, b, entry_speed.get())
                entry_speed.delete(0, "end")
                entry_speed.insert(0, str(SpeedAns) + " " + Speed_functions[b])
            else:
                SpeedAns = "Syntax Error"
                entry_speed.delete(0, "end")
                entry_speed.insert(0, SpeedAns)
        else:
            entry_speed.delete(0, "end")
            entry_speed.insert(0, SpeedData)


def Convertor(value):
    global direction
    global speed
    global mode_menu_convert

    right = "-->"
    left = "<--"
    value = str(value)
    if value == "1":
        print("1")
    if value == "2":
        print("2")
    if value == "3":
        print("3")
    if value == "4":
        print("4")
    if value == "5":
        print("5")
    if value == "6":
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
            "Meter per second (m/s)",
            "Metres per hour (m/h)",
            "Kilometres per second (km/s)",
            "Kilometres per hour(km/h)",
            "inches per second (in/s)",
            "Inches per hour(in/h)",
            "Miles per second(mi/s)",
            "Miles per hour(mi/h)",
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
                font=("Roboto", 12),
                corner_radius=0,
            )
            label.grid(column=col_val, row=row_val)

            if row_val == 4:
                col_val += 1
                row_val = 0


def mode_menu_reset():
    global mode_menu_convert
    global compute
    global PerformSpeed
    global mode_menu_convert
    global SpeedAns
    global SpeedData
    global compute
    global speed
    global ConvertTo
    global ConvertFrom
    global entry_speed

    print("clear")
    mode_menu_convert = False
    compute = True
    ModeMenu_main_convert.grid_remove()
    ModeMenu_main_convert_select.grid_remove()
    ModeMenu_main_convert_speed.grid_remove()
    entry_speed.grid_remove()
    ModeMenu_main_convert.grid_remove()
    PerformSpeed = False
    SpeedAns = ""
    SpeedData = ""
    compute = True
    speed = False
    ConvertTo = 0
    ConvertFrom = 0
    entry.grid(column=1, row=1)

    print("reset")


def mode_menu(value):
    global mode_menu_convert

    print(mode_menu_convert)
    if value == "mode_menu_convert":
        if mode_menu_convert == "In State":
            mode_menu_reset()
        else:
            mode_menu_convert = True
            compute = False
            entry.grid_remove()
            # speed Modes functionality
            ModeMenu_main_convert.grid(column=2, row=4)
            menu_functions = [
                "Area",
                "Distance",
                "Data",
                "knots",
                "Mass",
                "Speed",
                "Time",
                "Temperature",
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
                    text=str(str(num) + " " + speedChar),
                    height=(140 / 4),
                    font=("Roboto", 12),
                    corner_radius=0,
                )
                label_menu.grid(column=col_val, row=row_val)

                if row_val == 4:
                    col_val += 1
                    row_val = 0
                print(row_val, col_val)


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
    global mode_menu_convert
    global ConvertTo
    global ConvertFrom

    global new

    if mode_menu_convert != "In State" and mode_menu_convert == True:
        Convertor(value)
        print("speed value", speed, mode_menu_convert)
    elif speed:
        if (
            value == "="
            or value == "C"
            or value == "Ans"
            or value == "AC"
            or value.isnumeric()
            and int(value) < 9
        ):
            if PerformSpeed == True:
                SpeedConvertion(ConvertTo, ConvertFrom, value)

            elif ConvertTo != 0:
                ConvertFrom = value
                SpeedConvertion(ConvertTo, ConvertFrom, value)
            else:
                ConvertTo = value
                Convertor("6")

    elif compute:
        a = str(value)
        if a != "AC" and a != "Ans" and a != "C" and a != "=":
            OriginalData += a
            ExpFormation += a

        if a == "AC":
            his_data.set(ExpFormation + " = " + str(Ans))
            entry.delete(0, "end")
            entry.insert(0, "")
            OriginalData = ""
            ExpFormation = ""
        elif a == "C":
            CurrentVal = entry.index("insert")
            entry.delete(CurrentVal - 1)
            OriginalData = entry.get()
            ExpFormation = entry.get()

        elif value == "Ans":
            entry.delete(0, "end")
            entry.insert(0, Ans)
            OriginalData = str(Ans)

        elif value == "=":
            userInput = []
            userInput.extend(entry.get())
            print(userInput)
            if conditionChecker(userInput) == True:
                Ans = bracket_solu(userInput)
                entry.delete(0, "end")
                entry.insert(0, Ans)
                OriginalData = str(Ans)
            else:
                Ans = "Syntax Error"
                entry.delete(0, "end")
                entry.insert(0, Ans)
        else:
            entry.delete(0, "end")
            entry.insert(0, OriginalData)


def conditionChecker(userInput):
    value = True
    for char in userInput:
        Index = userInput.index(char)

        if Index + 1 != len(userInput):
            if char in basicArrays and userInput[Index + 1] in basicArrays:
                print("288")
                value = False

            if (
                char in complexArrays
                and userInput[Index + 3] in basicArrays
                or char in complexArrays
                and userInput[Index + 3] in complexArrays
            ):

                value = False
            if char.isnumeric() and userInput[Index + 1] in complexArrays:
                print("296")
                value = False
            if char == "(" and userInput[Index + 1] == ")":
                print("302")
                value = False

            if char in complexArrays and userInput[Index + 3] == ")":
                print("306")
                value = False

        else:
            if char in basicArrays or char == "(":
                print("309")
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

        for entry in userInput:

            entry = str(entry)

            # solve breakdown complex

            if "t" in entry:
                multiFactor = 1
                index = userInput.index(entry)
                if "⁻" in userInput and userInput[index + 3] == "⁻":
                    SingleFactor = 1
                    print("valeues", userInput[index + 5])
                    value = math.atan(float(userInput[index + 5]))
                elif len(userInput) != index + 1 and userInput[index + 3] == "×":
                    value = math.tan(float(userInput[index + 2]))

                else:
                    value = math.tan(float(userInput[index + 3]))

            if "S" in entry:
                multiFactor = 1
                index = userInput.index(entry)
                if "⁻" in userInput and userInput[index + 3] == "⁻":
                    SingleFactor = 1
                    print(userInput[index + 5])
                    value = math.sin(float(userInput[index + 5]))
                elif len(userInput) != index + 1 and userInput[index + 3] == "×":

                    value = math.sin(float(userInput[index + 2]))

                else:
                    value = math.sin(float(userInput[index + 3]))

            if "c" in entry:
                multiFactor = 1
                index = userInput.index(entry)
                if "⁻" in userInput and userInput[index + 3] == "⁻":
                    SingleFactor = 1
                    value = math.acos(float(userInput[index + 5]))
                elif len(userInput) != index + 1 and userInput[index + 3] == "×":

                    value = math.tan(float(userInput[index + 2]))

                else:
                    value = math.tan(float(userInput[index + 3]))

            if "R" in entry:
                multiFactor = 1

                index = userInput.index(entry)

                if len(userInput) != index + 1 and userInput[index + 3] == "×":

                    value = math.tan(float(userInput[index + 2]))

                else:
                    value = math.tan(float(userInput[index + 3]))

            if "D" in entry:
                multiFactor = 1

                index = userInput.index(entry)

                if len(userInput) != index + 1 and userInput[index + 3] == "×":

                    value = math.tan(float(userInput[index + 2]))

                else:
                    value = math.tan(float(userInput[index + 3]))

            if "√" in entry:

                index = userInput.index(entry)

                if len(userInput) != index + 1 and userInput[index + 1] == "×":

                    value = math.sqrt(float(userInput[index + 2]))

                    multiFactor = 1

                else:

                    a, b = entry.split(",")

                    value = math.sqrt(float(b))

            if "l" in entry:
                multiFactor = 1

                index = userInput.index(entry)

                if len(userInput) != index + 1 and userInput[index + 3] == "×":

                    value = math.log(float(userInput[index + 2]))

                else:
                    value = math.log(float(userInput[index + 3]))

            if multiFactor == 1 and SingleFactor == 1:
                userInput[index] = str(value)
                for i in range(4):
                    userInput.pop(index + 1)

            elif multiFactor == 1 and SingleFactor == 0:
                for i in range(2):
                    userInput.pop(index + 1)
            else:
                userInput[index] = str(value)

            multiFactor = 0
            SingleFactor = 0
        evaluateChar = ""
        for char in userInput:
            charIndex = userInput.index(char)
            print(charIndex + 1, len(userInput))
            if (
                charIndex + 1 < len(userInput)
                and (charIndex + 2) <= len(userInput)
                and char not in basicArrays
                and userInput[charIndex + 1] not in basicArrays
                and isinstance(userInput[charIndex + 1], str) == False
            ):
                evaluateChar += str(char + "*")
                print(evaluateChar)
            elif char == "×":
                evaluateChar += "*"
            elif char == "²":
                evaluateChar += "**2"
            else:
                evaluateChar += str(char)
        try:
            print("inputdata", evaluateChar)
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


def PEMDAS(inputData):

    # checked for paranthesis and

    global Ans

    pre = ""

    preIndex = ""
    post = ""

    postIndex = ""

    symbolIndex = ""

    negations = False

    value = ""

    newInputData = inputData

    para_thesis_List = []

    if ")" in inputData:

        end = inputData.index(")")

        endrange = inputData.index(")")

        # determin end of bracket

        while end > 0:

            if inputData[end - 1] == "(":

                start = end - 1

                break

            else:

                end = end - 1

        rangeData = endrange - start

        for i in range(rangeData):

            if start + i != start:

                para_thesis_List.append(inputData[start + i])

        print("para before solve", rangeData, para_thesis_List, start)

        Result = solvepara(para_thesis_List)

        print("Result val: ", Result)

        inputData[start] = Result

        print("new ifnor", newInputData)

        newInputData.pop(endrange)

        for i in range(rangeData):

            if start + i != start:

                newInputData.pop((start + 1))

        print(newInputData)

        PEMDAS(newInputData)

    elif "×" in inputData:

        print(newInputData, inputData)

        symbolIndex = inputData.index("×")

        preIndex = symbolIndex - 1

        postIndex = symbolIndex + 1

        if inputData[preIndex - 1] == "-":

            negations = True

            moves = 4

        else:

            negations = False

            moves = 3

        if not negations:

            pre = float(inputData[preIndex])

        else:

            pre = float(inputData[preIndex]) * -1

        post = float(inputData[postIndex])

        value = pre * post

        inputData[preIndex] = value

        newInputData.pop(postIndex)

        newInputData.pop(symbolIndex)

        if negations:

            newInputData.pop((preIndex - 1))

        PEMDAS(newInputData)

    elif "÷" in inputData:

        symbolIndex = inputData.index("÷")

        preIndex = symbolIndex - 1

        postIndex = symbolIndex + 1

        if inputData[preIndex - 1] == "-":

            negations = True

            moves = 4

        else:

            negations = False

            moves = 3

        if not negations:

            pre = float(inputData[preIndex])

        else:

            pre = float(inputData[preIndex]) * -1

        post = float(inputData[postIndex])

        value = pre / post

        inputData[preIndex] = value

        newInputData.pop(postIndex)

        newInputData.pop(symbolIndex)

        if negations:

            newInputData.pop((preIndex - 1))

        PEMDAS(newInputData)

    elif "+" in inputData:

        symbolIndex = inputData.index("+")

        preIndex = symbolIndex - 1

        postIndex = symbolIndex + 1

        if inputData[preIndex - 1] == "-":

            negations = True

            moves = 4

        else:

            negations = False

            moves = 3

        if not negations:

            pre = float(inputData[preIndex])

        else:

            pre = float(inputData[preIndex]) * -1

        print(pre, post, inputData[postIndex])

        post = float(inputData[postIndex])

        value = pre + post

        inputData[preIndex] = value

        newInputData.pop(postIndex)

        newInputData.pop(symbolIndex)

        if negations:

            newInputData.pop((preIndex - 1))

        PEMDAS(newInputData)

    elif "-" in inputData:

        symbolIndex = inputData.index("-")

        preIndex = symbolIndex - 1

        postIndex = symbolIndex + 1

        if inputData[preIndex - 1] == "-":

            negations = True

            moves = 4

        else:

            negations = False

            moves = 3

        if not negations:

            pre = float(inputData[preIndex])

        else:

            pre = float(inputData[preIndex]) * -1

        post = float(inputData[postIndex])

        value = pre - post

        inputData[preIndex] = value

        newInputData.pop(postIndex)

        newInputData.pop(symbolIndex)

        if negations:

            newInputData.pop((preIndex - 1))

        PEMDAS(newInputData)

    Ans = str(newInputData[0])

    entry.delete(0, "end")

    entry.insert(0, Ans)

    return Ans


def solvepara(inputData):

    # checked for paranthesis and

    global Ans
    pre = ""

    preIndex = ""
    post = ""

    postIndex = ""

    symbolIndex = ""

    negations = False

    value = ""

    newInputData = inputData

    moves = 0

    print("para result entry", newInputData)

    if "×" in inputData:

        symbolIndex = inputData.index("×")

        preIndex = symbolIndex - 1

        postIndex = symbolIndex + 1

        if not negations:

            pre = float(inputData[preIndex])

        else:

            pre = float(inputData[preIndex]) * -1

        post = float(inputData[postIndex])

        value = pre * post

        inputData[preIndex] = value

        newInputData.pop(postIndex)

        newInputData.pop(symbolIndex)

        newInputData = inputData

        if len(newInputData) == 1:

            print("resultgf 423: ", newInputData)

            return newInputData[0]

        else:

            solvepara(newInputData)

    elif "÷" in inputData:

        symbolIndex = inputData.index("÷")

        preIndex = symbolIndex - 1

        postIndex = symbolIndex + 1

        if inputData[preIndex - 1] == "-":

            negations = True

            moves = 4

        else:

            negations = False

            moves = 3

        if not negations:

            pre = float(inputData[preIndex])

        else:

            pre = float(inputData[preIndex]) * -1

        post = float(inputData[postIndex])

        value = pre / post

        inputData[preIndex] = value

        newInputData.pop(postIndex)

        newInputData.pop(symbolIndex)

        newInputData = inputData

        if len(newInputData) == 1:

            print("resultgf 455 : ", newInputData)

            return 8

        else:

            solvepara(newInputData)

    elif "+" in inputData:

        symbolIndex = inputData.index("+")

        preIndex = symbolIndex - 1

        postIndex = symbolIndex + 1

        if inputData[preIndex - 1] == "-":

            negations = True

            moves = 4

        else:

            negations = False

            moves = 3

        if not negations:

            pre = float(inputData[preIndex])

        else:

            pre = float(inputData[preIndex]) * -1

        post = float(inputData[postIndex])

        value = pre + post

        inputData[preIndex] = value

        newInputData.pop(postIndex)

        newInputData.pop(symbolIndex)

        newInputData = inputData

        if len(newInputData) == 1:

            print("resultgf 486: ", newInputData)

            return newInputData[0]

        else:

            solvepara(newInputData)

    elif "-" in inputData:

        symbolIndex = inputData.index("-")

        preIndex = symbolIndex - 1

        postIndex = symbolIndex + 1

        if inputData[preIndex - 1] == "-":

            negations = True

            moves = 4

        else:

            negations = False

            moves = 3

        if not negations:

            pre = float(inputData[preIndex])

        else:

            pre = float(inputData[preIndex]) * -1

        post = float(inputData[postIndex])

        value = pre - post

        inputData[preIndex] = value

        newInputData.pop(postIndex)

        newInputData.pop(symbolIndex)

        newInputData = inputData

        if len(newInputData) == 1:

            print("resultgf 517: ", newInputData)

            return newInputData[0]

        else:

            solvepara(newInputData)

    print("para result", newInputData[0])

    return str(newInputData[0])


def isfloat(num):

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
CurlButton.grid(column=1, row=2, padx=(0, 0), pady=(2, 5))

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
CurlyHalf.grid(column=2, row=2, padx=(0, 0), pady=(2, 5))

SquareRoot = customtkinter.CTkButton(
    master=FunctionFrames_innerFrame,
    font=("Roboto", 20),
    width=FunctionFramesBtnWidth,
    text="√x",
    fg_color="#1e1e1f",
    hover_color="#0773a4",
    height=35,
    corner_radius=8,
    command=lambda: Calc_input_display("√"),
)
SquareRoot.grid(column=3, row=2, padx=(0, 2), pady=(0, 5))
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
PieButton.grid(column=3, row=2, padx=(0, 0), pady=(2, 5))

AbsoluteX = customtkinter.CTkButton(
    master=FunctionFrames_innerFrame,
    font=("Roboto", 20),
    text="|x|",
    width=FunctionFramesBtnWidth,
    height=35,
    fg_color="#1e1e1f",
    hover_color="#0773a4",
    command=lambda: Calc_input_display("|x|"),
)
AbsoluteX.grid(column=4, row=2, padx=(0, 0), pady=(2, 5))

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
sinInverseBtn.grid(column=1, row=3, padx=(0, 3), pady=(2, 5))

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
tanInverseBtn.grid(column=2, row=3, padx=(0, 3), pady=(2, 5))

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
cosInverseBtn.grid(column=3, row=3, padx=(0, 3), pady=(2, 5))

logInverseBtn = customtkinter.CTkButton(
    master=FunctionFrames_innerFrame,
    font=("Roboto", 16),
    text="log⁻¹",
    width=FunctionFramesBtnWidth,
    height=35,
    fg_color="#1e1e1f",
    hover_color="#0773a4",
    command=lambda: Calc_input_display("log⁻¹"),
)
logInverseBtn.grid(column=4, row=3, padx=(0, 3), pady=(2, 5))

SeHr = customtkinter.CTkButton(
    master=FunctionFrames_innerFrame,
    font=("Roboto", 16),
    text="Time",
    width=FunctionFramesBtnWidth,
    height=35,
    fg_color="#1e1e1f",
    hover_color="#0773a4",
    command=lambda: Calc_input_display("Time"),
)
SeHr.grid(column=5, row=3, padx=(0, 3), pady=(2, 5))

KilobyteMega = customtkinter.CTkButton(
    master=FunctionFrames_innerFrame,
    font=("Roboto", 16),
    text="Data",
    width=FunctionFramesBtnWidth,
    height=35,
    fg_color="#1e1e1f",
    hover_color="#0773a4",
    command=lambda: Calc_input_display("Data"),
)
KilobyteMega.grid(column=5, row=3, padx=(0, 3), pady=(2, 5))

Temp = customtkinter.CTkButton(
    master=FunctionFrames_innerFrame,
    font=("Roboto", 13),
    text="Tmp",
    width=FunctionFramesBtnWidth,
    height=35,
    fg_color="#1e1e1f",
    hover_color="#0773a4",
    command=lambda: Calc_input_display("Tmp"),
)
Temp.grid(column=6, row=3, padx=(0, 3), pady=(2, 5))

Volume = customtkinter.CTkButton(
    master=FunctionFrames_innerFrame,
    font=("Roboto", 20),
    text="Mass",
    width=FunctionFramesBtnWidth,
    height=35,
    fg_color="#1e1e1f",
    hover_color="#0773a4",
    command=lambda: Calc_input_display("Kg->lb"),
)
Volume.grid(column=2, row=4, padx=(0, 3), pady=(2, 5))

eConvert = customtkinter.CTkButton(
    master=FunctionFrames_innerFrame,
    font=("Roboto", 20),
    text="e",
    width=FunctionFramesBtnWidth,
    height=35,
    fg_color="#1e1e1f",
    hover_color="#0773a4",
    command=lambda: Calc_input_display("e"),
)
eConvert.grid(column=3, row=4, padx=(0, 3), pady=(2, 5))

MAc = customtkinter.CTkButton(
    master=FunctionFrames_innerFrame,
    font=("Roboto", 20),
    text="Area",
    width=FunctionFramesBtnWidth,
    height=35,
    fg_color="#1e1e1f",
    hover_color="#0773a4",
    command=lambda: Calc_input_display("Area"),
)
MAc.grid(column=4, row=4, padx=(0, 3), pady=(2, 5))

SeHr = customtkinter.CTkButton(
    master=FunctionFrames_innerFrame,
    font=("Roboto", 20),
    text="Time",
    width=FunctionFramesBtnWidth,
    height=35,
    fg_color="#1e1e1f",
    hover_color="#0773a4",
    command=lambda: Calc_input_display("Time"),
)
SeHr.grid(column=5, row=4, padx=(0, 3), pady=(2, 5))

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


SquareCustomise = customtkinter.CTkButton(
    master=FunctionFrames_innerFrame,
    font=("Roboto", 20),
    text="X^()",
    width=FunctionFramesBtnWidth,
    height=35,
    fg_color="#1e1e1f",
    hover_color="#0773a4",
    command=lambda: Calc_input_display("X^()"),
)
SquareCustomise.grid(column=6, row=2, padx=(0, 3), pady=(2, 5))
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
    text=".",
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
Ans = customtkinter.CTkButton(
    master=Btns_innserFrame_innerFrame,
    text="Ans",
    font=("Roboto", 20),
    width=FramesBtnWidth,
    height=40,
    command=lambda: Calc_input_display("Ans"),
    fg_color="red",
)
Ans.grid(column=4, row=8, padx=(0, 3), pady=(0, 5))


root.mainloop()
