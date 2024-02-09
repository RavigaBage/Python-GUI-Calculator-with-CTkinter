import customtkinter
import tkinter as tk
import math

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")


root = customtkinter.CTk()
root.geometry("450x420")

frame = customtkinter.CTkFrame(master=root)
frame.grid(column=7, row=10)
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
    width=450,
    height=90,
    font=("Roboto", 24),
    fg_color="#2c2c2c",
    corner_radius=0,
)
entry.grid(columnspan=7, row=2)

label = customtkinter.CTkLabel(
    master=frame,
    width=450,
    textvariable=his_data,
    height=70,
    fg_color="#2c2c2c",
    font=("Roboto", 16),
    corner_radius=0,
)
label.grid(columnspan=7, row=1)


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

        if conditionChecker(userInput) == True:
            computeResult()
        else:
            Ans = "Mathematical Error"

        entry.delete(0, "end")
        entry.insert(0, Ans)
        numericObg = Ans
        OriginalData = Ans
        userInput = []

    else:
        entry.delete(0, "end")
        entry.insert(0, OriginalData)


def computeResult():
    global userInput
    global Ans

    value = userInput[0]
    index = 0

    if len(userInput) == 0:
        return "Cant Compute"
    else:
        for entry in userInput:
            entry = str(entry)
            # solve breakdown complex
            if "tan" in entry:
                index = userInput.index(entry)
                a, b = entry.split(",")
                print(a, b)
                value = math.tan(int(b))
            if "sin" in entry:
                index = userInput.index(entry)
                a, b = entry.split(",")
                print(a, b)
                value = math.sin(int(b))
            if "cos" in entry:
                index = userInput.index(entry)
                a, b = entry.split(",")
                value = math.cos(int(b))
            if "Rad" in entry:
                index = userInput.index(entry)
                a, b = entry.split(",")
                value = math.radians(int(b))
            if "Deg" in entry:
                index = userInput.index(entry)
                a, b = entry.split(",")
                value = math.degrees(int(b))
            if "√" in entry:
                index = userInput.index(entry)
                a, b = entry.split(",")
                value = math.sqrt(int(b))
            if "log" in entry:
                index = userInput.index(entry)
                a, b = entry.split(",")
                value = math.log10(int(b))
            userInput[index] = value
        print("printer here", userInput)

        PEMDAS(userInput)


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
        ):
            splita, splitb = userInput[len(userInput) - 1].split(",")
            if (
                not splitb.isnumeric()
                and splita in complexArrays
                or userInput[len(userInput) - 1] in basicArrays
            ):
                return False
            else:
                print("erw")
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
                                entry not in basicArrays
                                and userInput[index + 1] not in basicArrays
                            ):
                                return False
                                print("197", entry)
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
    moves = 0
    end = 0
    endrange = 0
    start = 0
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
    print(Ans)


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


button = customtkinter.CTkButton(
    master=frame,
    text="Rad",
    font=("Roboto", 20),
    width=70,
    height=45,
    fg_color="#303031",
    hover_color="#0773a4",
    command=lambda: Calc_input_display("Rad"),
)
button.grid(column=1, row=3, padx=(0, 0), pady=(2, 5))

button2 = customtkinter.CTkButton(
    master=frame,
    text="Deg",
    font=("Roboto", 20),
    width=70,
    fg_color="#303031",
    hover_color="#0773a4",
    height=45,
    command=lambda: Calc_input_display("Deg"),
)
button2.grid(column=2, row=3, padx=(0, 3), pady=(2, 5))

button3 = customtkinter.CTkButton(
    master=frame,
    text="π",
    font=("Roboto", 20),
    width=70,
    height=45,
    fg_color="#303031",
    hover_color="#0773a4",
    corner_radius=8,
    command=lambda: Calc_input_display("π"),
)
button3.grid(column=3, row=3, padx=(0, 3), pady=(2, 5))


button4 = customtkinter.CTkButton(
    master=frame,
    text="(",
    font=("Roboto", 20),
    width=70,
    height=45,
    fg_color="#303031",
    hover_color="#0773a4",
    command=lambda: Calc_input_display("("),
)
button4.grid(column=4, row=3, padx=(0, 3), pady=(2, 5))
button5 = customtkinter.CTkButton(
    master=frame,
    text=")",
    font=("Roboto", 20),
    width=70,
    height=45,
    fg_color="#303031",
    hover_color="#0773a4",
    corner_radius=8,
    command=lambda: Calc_input_display(")"),
)
button5.grid(column=5, row=3, padx=(0, 3), pady=(2, 5))

button6 = customtkinter.CTkButton(
    master=frame,
    font=("Roboto", 20),
    text="x!",
    width=70,
    height=45,
    fg_color="#303031",
    hover_color="#0773a4",
    command=lambda: Calc_input_display("x!"),
)
button6.grid(column=6, row=3, padx=(0, 3), pady=(2, 5))

button7 = customtkinter.CTkButton(
    master=frame,
    font=("Roboto", 20),
    width=70,
    text="√x",
    fg_color="#303031",
    hover_color="#0773a4",
    height=45,
    corner_radius=8,
    command=lambda: Calc_input_display("√"),
)
button7.grid(column=1, row=4, padx=(0, 2), pady=(0, 5))
button8 = customtkinter.CTkButton(
    master=frame,
    text="sin",
    font=("Roboto", 20),
    width=70,
    height=45,
    fg_color="#303031",
    hover_color="#0773a4",
    command=lambda: Calc_input_display("sin"),
)
button8.grid(column=2, row=4, padx=(0, 3), pady=(0, 5))
button9 = customtkinter.CTkButton(
    master=frame,
    font=("Roboto", 20),
    width=70,
    text="-",
    height=45,
    fg_color="#303031",
    hover_color="#0773a4",
    corner_radius=8,
    command=lambda: Calc_input_display("-"),
)
button9.grid(column=3, row=4, padx=(0, 3), pady=(0, 5))

button10 = customtkinter.CTkButton(
    master=frame,
    text="1",
    font=("Roboto", 20),
    width=70,
    height=45,
    fg_color="#303031",
    hover_color="#0773a4",
    command=lambda: Calc_input_display("1"),
)
button10.grid(column=4, row=4, padx=(0, 3), pady=(0, 5))

button11 = customtkinter.CTkButton(
    master=frame,
    text="2",
    font=("Roboto", 20),
    width=70,
    height=45,
    fg_color="#303031",
    hover_color="#0773a4",
    command=lambda: Calc_input_display("2"),
)
button11.grid(column=5, row=4, padx=(0, 3), pady=(0, 5))

button12 = customtkinter.CTkButton(
    master=frame,
    text="3",
    font=("Roboto", 20),
    width=70,
    height=45,
    fg_color="#303031",
    hover_color="#0773a4",
    command=lambda: Calc_input_display("3"),
)
button12.grid(column=6, row=4, padx=(0, 3), pady=(0, 5))

button13 = customtkinter.CTkButton(
    master=frame,
    text="log",
    font=("Roboto", 20),
    width=70,
    height=45,
    fg_color="#303031",
    hover_color="#0773a4",
    command=lambda: Calc_input_display("log"),
)
button13.grid(column=1, row=5, padx=(0, 3), pady=(0, 5))

button14 = customtkinter.CTkButton(
    master=frame,
    text="tan",
    font=("Roboto", 20),
    width=70,
    height=45,
    fg_color="#303031",
    hover_color="#0773a4",
    command=lambda: Calc_input_display("tan"),
)
button14.grid(column=2, row=5, padx=(0, 3), pady=(0, 5))
button15 = customtkinter.CTkButton(
    master=frame,
    text="+",
    font=("Roboto", 20),
    width=70,
    height=45,
    fg_color="#303031",
    hover_color="#0773a4",
    command=lambda: Calc_input_display("+"),
)
button15.grid(column=3, row=5, padx=(0, 3), pady=(0, 5))

button16 = customtkinter.CTkButton(
    master=frame,
    text="4",
    font=("Roboto", 20),
    width=70,
    height=45,
    fg_color="#303031",
    hover_color="#0773a4",
    command=lambda: Calc_input_display("4"),
)
button16.grid(column=4, row=5, padx=(0, 3), pady=(0, 5))


button17 = customtkinter.CTkButton(
    master=frame,
    text="5",
    font=("Roboto", 20),
    width=70,
    height=45,
    fg_color="#303031",
    hover_color="#0773a4",
    command=lambda: Calc_input_display("5"),
)
button17.grid(column=5, row=5, padx=(0, 3), pady=(0, 5))

button18 = customtkinter.CTkButton(
    master=frame,
    text="6",
    font=("Roboto", 20),
    width=70,
    height=45,
    fg_color="#303031",
    hover_color="#0773a4",
    command=lambda: Calc_input_display("6"),
)
button18.grid(column=6, row=5, padx=(0, 3), pady=(0, 5))


button19 = customtkinter.CTkButton(
    master=frame,
    text="C",
    font=("Roboto", 20),
    width=70,
    height=45,
    fg_color="#303031",
    hover_color="#0773a4",
    command=lambda: Calc_input_display("C"),
)
button19.grid(column=1, row=6, padx=(0, 3), pady=(0, 5))

button20 = customtkinter.CTkButton(
    master=frame,
    text="cos",
    font=("Roboto", 20),
    width=70,
    height=45,
    fg_color="#303031",
    hover_color="#0773a4",
    command=lambda: Calc_input_display("cos"),
)
button20.grid(column=2, row=6, padx=(0, 3), pady=(0, 5))

button21 = customtkinter.CTkButton(
    master=frame,
    text="×",
    font=("Roboto", 20),
    width=70,
    height=45,
    fg_color="#303031",
    hover_color="#0773a4",
    command=lambda: Calc_input_display("×"),
)
button21.grid(column=3, row=6, padx=(0, 3), pady=(0, 5))


button22 = customtkinter.CTkButton(
    master=frame,
    text="7",
    font=("Roboto", 20),
    width=70,
    height=45,
    fg_color="#303031",
    hover_color="#0773a4",
    command=lambda: Calc_input_display("7"),
)
button22.grid(column=4, row=6, padx=(0, 3), pady=(0, 5))

button24 = customtkinter.CTkButton(
    master=frame,
    text="8",
    font=("Roboto", 20),
    width=70,
    height=45,
    fg_color="#303031",
    hover_color="#0773a4",
    command=lambda: Calc_input_display("8"),
)
button24.grid(column=5, row=6, padx=(0, 3), pady=(0, 5))

button25 = customtkinter.CTkButton(
    master=frame,
    text="9",
    font=("Roboto", 20),
    width=70,
    height=45,
    fg_color="#303031",
    hover_color="#0773a4",
    command=lambda: Calc_input_display("9"),
)
button25.grid(column=6, row=6, padx=(0, 3), pady=(0, 5))


button26 = customtkinter.CTkButton(
    master=frame,
    text="AC",
    font=("Roboto", 20),
    width=70,
    height=45,
    fg_color="#2b8806",
    hover_color="#4ef80b",
    command=lambda: Calc_input_display("AC"),
)
button26.grid(column=1, row=7, padx=(0, 3), pady=(0, 5))

button27 = customtkinter.CTkButton(
    master=frame,
    text=".",
    font=("Roboto", 20),
    width=70,
    height=45,
    fg_color="#303031",
    hover_color="#0773a4",
    command=lambda: Calc_input_display("."),
)
button27.grid(column=2, row=7, padx=(0, 3), pady=(0, 5))

button29 = customtkinter.CTkButton(
    master=frame,
    text="÷",
    font=("Roboto", 20),
    width=70,
    height=45,
    fg_color="#303031",
    hover_color="#0773a4",
    command=lambda: Calc_input_display("÷"),
)
button29.grid(column=3, row=7, padx=(0, 3), pady=(0, 5))

button30 = customtkinter.CTkButton(
    master=frame,
    text="0",
    font=("Roboto", 20),
    width=70,
    height=45,
    fg_color="#303031",
    hover_color="#0773a4",
    command=lambda: Calc_input_display("0"),
)
button30.grid(column=4, row=7, padx=(0, 3), pady=(0, 5))

button31 = customtkinter.CTkButton(
    master=frame,
    font=("Roboto", 20),
    text="=",
    width=70,
    height=45,
    fg_color="#303031",
    hover_color="#0773a4",
    command=lambda: Calc_input_display("="),
)
button31.grid(column=5, row=7, padx=(0, 3), pady=(0, 5))

button32 = customtkinter.CTkButton(
    master=frame,
    text="Ans",
    font=("Roboto", 20),
    width=70,
    height=45,
    command=lambda: Calc_input_display("Ans"),
    fg_color="red",
)

button32.grid(column=6, row=7, padx=(0, 3), pady=(0, 5))

root.mainloop()
