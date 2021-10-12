from tkinter import *
#Drawing the main window here
root = Tk()
root.title('Temperature Converter')
root.geometry('400x250')

#C to F class/window/etc.
class open_celFar:
    def __init__(self):
        celFar = Toplevel()
        celFar.title('Celsius to Fahrenheit')
        celFar.geometry('400x250')
        img = PhotoImage(file='celFar.png')
        Label(celFar, image=img).pack()
        self.label1 = Label(celFar, text='Temperature')
        self.label1.place(x=100, y=100)
        self.label2 = Label(celFar, text='Converted temp')
        self.label2.place(x=100, y=150)
        self.button1 = Button(celFar, text='Convert', command=self.fahrenheit)
        self.button1.place(x=100, y=200)
        self.button2 = Button(celFar, text="Exit", command=celFar.destroy)
        self.button2.place(x=200, y=200)
        self.text1 = Entry(celFar, bd=5)
        self.text1.place(x=200, y=100)
        self.text2 = Entry(celFar, bd=3)
        self.text2.place(x=200, y=150)
        celFar.mainloop()
#this is where the C to F math happens.
    def fahrenheit(self):
        self.text2.delete(0, 'end')
        num1 = float(self.text1.get())
        result = ((float(num1) * 1.8) + 32)
        self.text2.insert(END, str(result))

#F to C code lives here.
class open_farCel:
    def __init__(self):
        farCel = Toplevel()
        farCel.title('Fahrenheit to Celsius')
        farCel.geometry('400x250')
        img = PhotoImage(file='farCel.png')
        Label(farCel, image=img).pack()
        self.label1 = Label(farCel, text='Temperature')
        self.label1.place(x=100, y=100)
        self.label2 = Label(farCel, text='Converted temp')
        self.label2.place(x=100, y=150)
        self.button1 = Button(farCel, text='Convert', command=self.celsius)
        self.button1.place(x=100, y=200)
        self.button2 = Button(farCel, text="Exit", command=farCel.destroy)
        self.button2.place(x=200, y=200)
        self.text1 = Entry(farCel, bd=5)
        self.text1.place(x=200, y=100)
        self.text2 = Entry(farCel, bd=3)
        self.text2.place(x=200, y=150)
        farCel.mainloop()
#actual math for F to C.
    def celsius(self):
        self.text2.delete(0, 'end')
        num1 = float(self.text1.get())
        result = ((float(num1) - 32) / 1.8)
        self.text2.insert(END, str(result))

#all the buttons and graphics and such for the main window
img = PhotoImage(file='mm.png')
Label(root, image=img).pack()
button1 = Button(root, text='Fahrenheit to Celsius', command=open_farCel)
button1.place(x=155, y=100)
button2 = Button(root, text='Celsius to Fahrenheit', command=open_celFar)
button2.place(x=155, y=150)
button3 = Button(root, text='Exit', command=root.destroy)
button3.place(x=155, y=200)
#make the actual main window work
root.mainloop()
