from tkinter import *

def us():
    value = valueEntry.get()
    resultTextUS.configure(text = float(value) * 0.018)

def eu():
    value = valueEntry.get()
    resultTextEU.configure(text = float(value) * 0.017)
    
def yen():
    value = valueEntry.get()
    resultTextYEN.configure(text = float(value) * 2.35)
    
def riy():
    value = valueEntry.get()
    resultTextRIY.configure(text = float(value) * 0.069)

def pound():
    value = valueEntry.get()
    resultTextPOUND.configure(text = float(value) * 0.015)
    
def allcon():
    us()
    eu()
    yen()
    riy()
    pound()
    
tkWindow = Tk()
tkWindow.geometry("600x300")
tkWindow.title("KC Currency Conversion")

showTxt = Label(tkWindow, text= "Currency Conversion", fg="Steel Blue", bd = 2, font=("Arial Black", 30))
showTxt.grid(row=0, column= 0, columnspan=4)

valueLabel = Label(tkWindow, text = "Enter Denomination(Php): ", font=('Arial Black', 10))
value = IntVar()
valueLabel.grid(row=1,column=0)

valueEntry = Entry(tkWindow, textvariable=value) 
valueEntry.grid(row=1,column=1)

convertBtn = Button(tkWindow, text = "Convert", command = allcon)
convertBtn.grid(row=5, column=1)

resultLabel1 = Label(tkWindow, text = "US DOLLARS", font=('Arial', 10))
resultLabel1.grid(row=6, column=0)

resultTextUS = Label(tkWindow)
resultTextUS.grid(row=6, column=1)

resultLabel2 = Label(tkWindow, text = "EURO", font=('Arial ', 10))
resultLabel2.grid(row=7, column=0)

resultTextEU = Label(tkWindow)
resultTextEU.grid(row=7, column=1)

resultLabel3 = Label(tkWindow, text = "JAPANESE YEN", font=('Arial', 10))
resultLabel3.grid(row=8, column=0)

resultTextYEN = Label(tkWindow)
resultTextYEN.grid(row=8, column=1)

resultLabel4 = Label(tkWindow, text = "SAUDI RIYALS", font=('Arial ', 10))
resultLabel4.grid(row=9, column=0)

resultTextRIY = Label(tkWindow)
resultTextRIY.grid(row=9, column=1)

resultLabel5 = Label(tkWindow, text = "BRITISH POUND", font=('Arial', 10))
resultLabel5.grid(row=10, column=0)

resultTextPOUND = Label(tkWindow)
resultTextPOUND.grid(row=10, column=1)



tkWindow.mainloop()