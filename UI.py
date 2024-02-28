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
complexArrays = ["Rad", "Deg", "tan", "cos", "sin", "log", "π", "√", "%", "x²"]
userInput = []
new = []
ExpFormation = ""
Ans = ""
data = ""

his_data = customtkinter.StringVar()
entry = customtkinter.CTkEntry(
    master=frame,
    width=WINW,
    height=90,
    font=("Roboto", 24),
    fg_color="#2c2c2c",
    corner_radius=0,
)
entry.grid(column=1, row=2)
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


def Calc_input_display(value):

    global OriginalData

    global numericObg

    global userInput

    global basicArrays

    global complexArrays

    global ExpFormation

    global Ans

    global data

    global new

    checker = ""

    checker2 = ""

    a = str(value)

    if a != "AC" and a != "C" and a != "=":

        data += a

        new.append(a)

    OriginalData += a

    if a == "AC":

        his_data.set(data + " = " + Ans)

        numericObg = ""

        ExpFormation = ""

        OriginalData = ""
        data = ""

        userInput = []

    elif a == "C":

        if numericObg != "":

            new = list(numericObg)

            new.pop(len(new) - 1)

            numericObg = "".join(new)

            new = list(data)

            new.pop(len(new) - 1)

            data = "".join(new)

            OriginalData = data

        else:

            his_data.set(data + " = " + Ans)

            numericObg = ""

            ExpFormation = ""

            OriginalData = ""
            data = ""

            userInput = []

    elif a.isnumeric():

        if ExpFormation == "":

            checker += "0"

            checker2 = str(numericObg) + a

            if checker != checker2:

                numericObg += a

        else:

            checker = ExpFormation + "0"

            checker2 = ExpFormation + a

            if checker != checker2:

                ExpFormation += a

        checker = ""

        checker2 = ""

    elif a == ".":

        if ExpFormation == "":

            checker += "0.0"

            checker2 = numericObg + a

            if checker != checker2:

                numericObg += a

        else:

            checker = ExpFormation + "0"

            checker2 = ExpFormation + a

            if checker != checker2:

                ExpFormation += a

        checker = ""

        checker2 = ""

    elif a in basicArrays:

        if numericObg == "" and ExpFormation == "":

            print("No function will be passed")

        elif numericObg != "" and ExpFormation == "":

            userInput.append(numericObg)

            userInput.append(a)

            numericObg = ""

        elif numericObg == "" and ExpFormation != "":

            userInput.append(ExpFormation)

            userInput.append(a)

            ExpFormation = ""

    elif a in complexArrays and ExpFormation == "":

        ExpFormation = a + ","

    elif a == "(":

        if numericObg != "":

            userInput.append(numericObg)

            numericObg = ""

        if ExpFormation != "":

            userInput.append(ExpFormation)

            ExpFormation = ""

        if userInput[len(userInput) - 1] in basicArrays:

            userInput.append("(")

        else:

            userInput.append("×")

            userInput.append("(")

    elif a == ")":

        if numericObg != "":

            userInput.append(numericObg)

            numericObg = ""

        if ExpFormation != "":

            userInput.append(ExpFormation)

            ExpFormation = ""

        userInput.append(")")

    if value == "Ans":

        numericObg = Ans

        OriginalData = Ans

    if value == "=":

        if numericObg != "":

            userInput.append(numericObg)

        if ExpFormation != "":

            userInput.append(ExpFormation)

        InputList = bracket_solu(userInput)

        print(bracket_solu(userInput), InputList)

        if conditionChecker(InputList) == True:

            computeResult(InputList)

        else:

            print(conditionChecker(userInput))

            Ans = "Mathematical Error"

        entry.delete(0, "end")

        entry.insert(0, Ans)

        numericObg = Ans

        OriginalData = Ans

        userInput = []

    else:

        entry.delete(0, "end")

        entry.insert(0, OriginalData)


def computeResult(userInput):

    global Ans

    value = userInput[0]

    index = 0

    multiFactor = 0

    if len(userInput) == 0:

        print("Cant Compute")

    else:

        for entry in userInput:

            entry = str(entry)

            # solve breakdown complex

            if "tan" in entry:

                index = userInput.index(entry)

                if len(userInput) != index + 1 and userInput[index + 1] == "×":

                    value = math.tan(float(userInput[index + 2]))

                    multiFactor = 1

                else:

                    a, b = entry.split(",")

                    value = math.tan(float(b))

            if "sin" in entry:

                index = userInput.index(entry)

                if len(userInput) != index + 1 and userInput[index + 1] == "×":

                    value = math.sin(float(userInput[index + 2]))

                    multiFactor = 1

                else:

                    a, b = entry.split(",")

                    value = math.sin(float(b))

            if "cos" in entry:

                index = userInput.index(entry)

                if len(userInput) != index + 1 and userInput[index + 1] == "×":

                    value = math.cos(float(userInput[index + 2]))

                    multiFactor = 1

                else:

                    a, b = entry.split(",")

                    value = math.cos(float(b))

            if "Rad" in entry:

                index = userInput.index(entry)

                if len(userInput) != index + 1 and userInput[index + 1] == "×":

                    value = math.radians(float(userInput[index + 2]))

                    multiFactor = 1

                else:

                    a, b = entry.split(",")

                    value = math.radians(float(b))

            if "Deg" in entry:

                index = userInput.index(entry)

                if len(userInput) != index + 1 and userInput[index + 1] == "×":

                    value = math.degrees(float(userInput[index + 2]))

                    multiFactor = 1

                else:

                    a, b = entry.split(",")

                    value = math.degrees(float(b))

            if "√" in entry:

                index = userInput.index(entry)

                if len(userInput) != index + 1 and userInput[index + 1] == "×":

                    value = math.sqrt(float(userInput[index + 2]))

                    multiFactor = 1

                else:

                    a, b = entry.split(",")

                    value = math.sqrt(float(b))

            if "log" in entry:

                index = userInput.index(entry)

                if len(userInput) != index + 1 and userInput[index + 1] == "×":

                    value = math.log10(float(userInput[index + 2]))

                    multiFactor = 1

                else:

                    a, b = entry.split(",")

                    value = math.log10(float(b))

            if multiFactor != 1:

                userInput[index] = value

            else:

                userInput[index] = value

                userInput.pop(index + 1)

                userInput.pop(index + 1)

                print("printer here", userInput)

            multiFactor = 0

        print("printer here", userInput)

    PEMDAS(userInput)


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

        Ans = PEMDAS(para_thesis_List)

        if PEMDAS(para_thesis_List) != False:

            InputData.pop(startPosition)

            InputData.pop(EndPosition - 1)

            for i in range(rangeData):

                if rangeData - 1 == i:

                    InputData[startPosition] = Ans

                else:

                    InputData.pop(startPosition)

        if "(" in InputData:

            bracket_solu(InputData)

        else:

            new_InputData = InputData

    else:

        new_InputData = InputData

    return new_InputData


def conditionChecker(userInput):

    if (
        userInput[len(userInput) - 1] == "("
        or userInput[len(userInput) - 1] in basicArrays
    ):

        return False

    else:

        if (
            not userInput[len(userInput) - 1].isnumeric()
            and userInput[len(userInput) - 1] not in basicArrays
            and userInput[len(userInput) - 1] != ")"
            and isfloat(userInput[len(userInput) - 1]) != True
        ):

            splita, splitb = userInput[len(userInput) - 1].split(",")

            if (
                not splitb.isnumeric()
                and splita in complexArrays
                or userInput[len(userInput) - 1] in basicArrays
            ):

                return False

            else:

                for entry in userInput:

                    index = userInput.index(entry)

                    if (index + 1) < len(userInput):

                        if (
                            entry != "("
                            and entry != ")"
                            and userInput[index + 1] != "("
                            and userInput[index + 1] != ")"
                        ):

                            if (
                                entry in basicArrays
                                and userInput[index + 1] in basicArrays
                            ):

                                if entry == userInput[index + 1]:

                                    print(entry, userInput[index + 1])

                                    userInput.pop(index + 1)

                                else:

                                    print("185", entry)

                                    return False

                            elif (
                                entry in basicArrays
                                and not userInput[index + 1].isnumeric()
                                and userInput[index + 1] == ")"
                            ):

                                print("191", entry)

                                return False

                            elif (
                                not userInput[index + 1].isnumeric()
                                and entry not in basicArrays
                                and userInput[index + 1] not in basicArrays
                            ):

                                print("197", entry)

                                return False

                        else:

                            if entry == "" or entry == " ":

                                print("208", entry)

                                return False

                            else:

                                return True

                    else:

                        return True

        else:

            return True


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
    command=lambda: Calc_input_display("Rad"),
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
    command=lambda: Calc_input_display("Deg"),
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
    command=lambda: Calc_input_display("sin"),
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
    command=lambda: Calc_input_display("tan"),
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
    command=lambda: Calc_input_display("cos"),
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
    command=lambda: Calc_input_display("log"),
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
    text="X²",
    width=FunctionFramesBtnWidth,
    height=35,
    fg_color="#1e1e1f",
    hover_color="#0773a4",
    command=lambda: Calc_input_display("X²"),
)
Xsquare.grid(column=5, row=2, padx=(0, 3), pady=(2, 5))


KHM = customtkinter.CTkButton(
    master=FunctionFrames_innerFrame,
    font=("Roboto", 16),
    text="Speed",
    width=FunctionFramesBtnWidth,
    height=35,
    fg_color="#1e1e1f",
    hover_color="#0773a4",
    command=lambda: Calc_input_display("Speed"),
)
KHM.grid(column=1, row=3, padx=(0, 3), pady=(2, 5))

KmLb = customtkinter.CTkButton(
    master=FunctionFrames_innerFrame,
    font=("Roboto", 16),
    text="Mass",
    width=FunctionFramesBtnWidth,
    height=35,
    fg_color="#1e1e1f",
    hover_color="#0773a4",
    command=lambda: Calc_input_display("Kg->lb"),
)
KmLb.grid(column=2, row=3, padx=(0, 3), pady=(2, 5))

KmM = customtkinter.CTkButton(
    master=FunctionFrames_innerFrame,
    font=("Roboto", 16),
    text="Length",
    width=FunctionFramesBtnWidth,
    height=35,
    fg_color="#1e1e1f",
    hover_color="#0773a4",
    command=lambda: Calc_input_display("Length"),
)
KmM.grid(column=3, row=3, padx=(0, 3), pady=(2, 5))

MAc = customtkinter.CTkButton(
    master=FunctionFrames_innerFrame,
    font=("Roboto", 16),
    text="Area",
    width=FunctionFramesBtnWidth,
    height=35,
    fg_color="#1e1e1f",
    hover_color="#0773a4",
    command=lambda: Calc_input_display("Area"),
)
MAc.grid(column=4, row=3, padx=(0, 3), pady=(2, 5))

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

KilobyteMega = customtkinter.CTkButton(
    master=FunctionFrames_innerFrame,
    font=("Roboto", 20),
    text="Data",
    width=FunctionFramesBtnWidth,
    height=35,
    fg_color="#1e1e1f",
    hover_color="#0773a4",
    command=lambda: Calc_input_display("Data"),
)
KilobyteMega.grid(column=5, row=4, padx=(0, 3), pady=(2, 5))


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
