#Lane Moseley, 12/15/2018
from tkinter import *


class gpaCalc:
    def __init__(self, size = 6):
        self.master = Tk()
        self.master.title("GPA Calculator")
        self.size = size
        
        Label(self.master, text="Credits").grid(row=0, column=1)
        Label(self.master, text="Grade (0.0 - 4.0)").grid(row=0, column=2)

        self.gradeArr = []
        self.creditArr = []

        for num in range(self.size):
            Label(self.master, text="Class #" + str(num + 1) + ": ").grid(row=num + 1, column=0, sticky="E")
            c = Entry(self.master)
            g = Entry(self.master)
            self.gradeArr.append(g)
            self.creditArr.append(c)
    
            self.gradeArr[num].grid(row=num + 1, column=2)
            self.creditArr[num].grid(row=num + 1, column=1)
            self.gradeArr[num].insert(1, 0)
            self.creditArr[num].insert(1, 0)

        Label(self.master, text="Current GPA: ").grid(row=(num + 2), sticky="E")
        self.currGPA = Entry(self.master)
        self.currGPA.grid(row=(num + 2), column=1)
        self.currGPA.insert(0, 0.0)

        Label(self.master, text="Current Hours: ").grid(row=(num + 3), sticky="E")
        self.currHours = Entry(self.master)
        self.currHours.grid(row=(num + 3), column=1)
        self.currHours.insert(0, 0)

        Label(self.master, text="Semester GPA: ").grid(row=(num + 4), sticky="E")
        self.semGPA = Entry(self.master)
        self.semGPA.grid(row=(num + 4), column=1)
        self.semGPA.insert(0, 0.0)

        Label(self.master, text="New GPA: ").grid(row=(num + 5), sticky="E")
        self.newGPA = Entry(self.master)
        self.newGPA.grid(row=(num + 5), column=1)
        self.newGPA.insert(0, 0.0)

        #Add Row
        Button(self.master, text='Add Row', command=self.add, width=10).grid(row=1, column=3)

        #Remove Row
        Button(self.master, text='Remove Row', command=self.remove, width=10).grid(row=2, column=3)

        #Reset Form
        Button(self.master, text='Reset Form', command=self.resetForm, width=10).grid(row=3, column=3)

        #Calculate GPA
        Button(self.master, text='Calculate', command=self.calculate, width=10).grid(row=4, column=3)

        #Quit
        Button(self.master, text='Quit', command=self.master.destroy, width=10).grid(row=5, column=3)


    def calculate(self):
        credits = 0
        points = 0
        
        for i in range(self.size):
            try:
                credits += float(self.creditArr[i].get())
            except ValueError:
                self.creditArr[i].delete(0, END)
                self.creditArr[i].insert(0, 0)
        
            try:
                points += float(self.gradeArr[i].get()) * float(self.creditArr[i].get())
            except ValueError:
                self.gradeArr[i].delete(0, END)
                self.gradeArr[i].insert(0, 0)

        
        self.semGPA.delete(0, END)
        self.newGPA.delete(0, END)
    
        if (credits == 0):
            self.semGPA.insert(0, 0.0)
            self.newGPA.insert(0, 0.0)

        else:
            self.semGPA.insert(0, points / credits)
            
            try:
                points += float(self.currGPA.get()) * float(self.currHours.get())
                credits += float(self.currHours.get())
                self.newGPA.insert(0, points / credits)

            except ValueError:
                self.currGPA.delete(0, END)
                self.currHours.delete(0, END)

                self.currGPA.insert(0, 0.0)
                self.currHours.insert(0, 0)

        

    def add(self):
        self.master.destroy()
        gpaCalc(self.size + 1)


    def remove(self):
        if self.size > 6:
            self.master.destroy()
            gpaCalc(self.size - 1)
        

    def resetForm(self):
        self.semGPA.delete(0, END)
        self.newGPA.delete(0, END)
        self.currGPA.delete(0, END)
        self.currHours.delete(0, END)

        for i in range(self.size):
            self.creditArr[i].delete(0, END)
            self.gradeArr[i].delete(0, END)
        
            self.creditArr[i].insert(0, 0)
            self.gradeArr[i].insert(0, 0)

        self.semGPA.insert(0, 0.0)
        self.newGPA.insert(0, 0.0)
        self.currGPA.insert(0, 0.0)
        self.currHours.insert(0, 0)


#Run Program
calc = gpaCalc()
  
mainloop( )



