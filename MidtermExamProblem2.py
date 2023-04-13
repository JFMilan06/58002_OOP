from tkinter import *
class MyWindow:
    def __init__(self,win):

        self.lbl5 = Label(win, text="My Full Name",fg="Red",font = "Verdana")
        self.lbl5.place(x=200,y=25)
        self.lbl1 = Label(win,text="Enter Given Name:",fg="Red")
        self.lbl1.place(x=80,y=50)
        self.lbl2 = Label(win, text= "Enter Middle Name:",fg="Red")
        self.lbl2.place(x=80,y=100)
        self.lbl3 = Label(win, text="Enter Last Name:",fg="Red")
        self.lbl3.place(x=80, y=150)
        self.lbl4 = Label(win, text="My Full Name is:",fg="Red")
        self.lbl4.place(x=80,y=200)
        self.txt1 = Entry(win,bd=3)
        self.txt1.place(x=300,y=50)
        self.txt2 = Entry(win,bd=3)
        self.txt2.place(x=300,y=100)
        self.txt3 = Entry(win,bd=3)
        self.txt3.place(x=300,y=150)
        self.txt4 = Entry(win, bd=3,fg="Red")
        self.txt4.place(x=300, y=200)


        self.btnSFN = Button(win,text="Show Full Name")
        self.btnSFN.place(x=200,y=250)
        self.btnSFN.bind('<Button-1>',self.SFN)

        self.btnclr = Button(win, text="Clear All",command = self.clr)
        self.btnclr.place(x=220,y=280)

    def SFN(self,SFN):
        self.txt4.delete(0, 'end')
        num1 = (self.txt1.get()) +" "
        num2 = (self.txt2.get()) +" "
        num3 = (self.txt3.get()) +","
        result =  num3 + num1 + num2
        self.txt4.insert(END,str(result))

    def clr(self):
        self.txt1.delete(0, 'end')
        self.txt2.delete(0, 'end')
        self.txt3.delete(0, 'end')
        self.txt4.delete(0, 'end')

window = Tk()
mywin = MyWindow(window)
window.geometry("600x400+10+10")
window.title("Midterm Exam Problem 2")
window.mainloop()