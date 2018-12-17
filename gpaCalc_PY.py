#Lane Moseley, 12/15/2018
from tkinter import *

#Global Variable for Initial Number of Data Rows
num = 6

#Global Array for holding class data
class_data = []


#Helper Classes and Functions
class currentGPA:
    def __init__(self, frame):
        Label(frame, text="Current GPA: ").grid(row=0, column=0, sticky="E")
        Label(frame, text="Current Hours: ").grid(row=1, column=0, sticky="E")

        self.g_field = Entry(frame, width=6)
        self.g_field.grid(row=0, column=1)
        self.g_field.insert(0, 0.0)

        self.c_field = Entry(frame, width=6)
        self.c_field.grid(row=1, column=1)
        self.c_field.insert(0, 0)

    def getCredits(self):
        try:
            credits = int(float(self.c_field.get()))

            #Ensuring that no negative values are returned
            if credits > 0:
                return credits
            else:
                self.clear()
                return 0

        except ValueError:
            self.clear()
            return 0
    
    def getPoints(self):
        try:
            points = int(float(self.c_field.get())) * float(self.g_field.get())
            
            #Ensuring that no negative values are returned
            if points > 0.0:
                return points
            else:
                self.clear()
                return 0.0

        except ValueError:
            self.clear()
            return 0.0

    def clear(self):
        self.g_field.delete(0, END)
        self.c_field.delete(0, END)
        
        self.c_field.insert(0, 0)
        self.g_field.insert(0, 0.0)
    
        

class classData:
    def __init__(self, frame, num=1):
        self.l = Label(frame, text="Class #" + str(num-1) + ": ")
        self.l.grid(row=num, column=0, sticky="E")

        self.c_field = Entry(frame, width=16)
        self.c_field.grid(row=num, column=1)
        self.c_field.insert(1, 0)

        self.g_field = Entry(frame, width=17)
        self.g_field.grid(row=num, column=2)
        self.g_field.insert(1, 0)

    def getCredits(self):
        try:
            credits = int(float(self.c_field.get()))
            
            #Ensuring that no negative values are returned
            if credits > 0:
                return credits
            else:
                self.clear()
                return 0

        except ValueError:
            self.clear()
            return 0
    
    def getPoints(self):
        try:
            points = int(float(self.c_field.get())) * float(self.g_field.get())
            
            #Ensuring that no negative values are returned
            if points > 0.0:
                return points
            else:
                self.clear()
                return 0.0

        except ValueError:
            self.clear()
            return 0.0

    def clear(self):
        self.g_field.delete(0, END)
        self.c_field.delete(0, END)
        
        self.c_field.insert(0, 0)
        self.g_field.insert(0, 0)


def calculate(current, entered, size, semester, cummulative):
    credits = 0
    points = 0

    for i in range(size):
        credits += entered[i].getCredits()
        points += entered[i].getPoints()

    semester.delete(0, END)
    cummulative.delete(0, END)

    if credits != 0:
        semester.insert(0, round(points / credits, 3))

        credits += current.getCredits()
        points += current.getPoints()

        cummulative.insert(0, round(points / credits, 3))
    else:
        semester.insert(0, 0.0)
        cummulative.insert(0, 0.0)



def resetForm(current, sem_gpa, new_gpa, entered, size):
    current.clear()

    sem_gpa.delete(0, END)
    sem_gpa.insert(0, 0.0)

    new_gpa.delete(0, END)
    new_gpa.insert(0, 0.0)

    for i in range(size):
        entered[i].clear()



def add():
    global num, class_data
    class_data.append(classData(top_frame, num + 2))
    num += 1



def remove():
    global num, class_data
    if num > 6:
        class_data[num - 1].l.grid_forget()
        class_data[num - 1].c_field.grid_forget()
        class_data[num - 1].g_field.grid_forget()
        
        class_data.pop()
        num -= 1



# Beginning of Program
master = Tk()

# Window Title and Geometry
master.title("GPA Calculator")
master.configure(bg="#234C67")

#Title Frame
title_frame = Frame(master, border=4, relief=RIDGE)
title_frame.grid(row=0, sticky=E+W)
title_frame.columnconfigure(0, weight=1)

Label(title_frame, text="GPA Calculator", font="bold").grid(row=0)

#Top Frame
top_frame = Frame(master, border=4, relief=RIDGE)
top_frame.grid(row=1, sticky=E+W)
top_frame.columnconfigure(0, weight=1)

Label(top_frame, text="Credits").grid(row=1, column=1)
Label(top_frame, text="Grade (0.0 - 4.0)").grid(row=1, column=2)

for i in range(num):
    class_data.append(classData(top_frame, i + 2))

#Bottom Frame
bot_frame = Frame(master, border=4, relief=RIDGE)
bot_frame.grid(row=2, sticky=E+W)
bot_frame.columnconfigure(0, weight=1)

curr = currentGPA(bot_frame)

Label(bot_frame, text="Semester GPA: ").grid(row=0, column=2, sticky="E")
sem_gpa = Entry(bot_frame, width=7)
sem_gpa.grid(row=0, column=3)
sem_gpa.insert(0, 0.0)

Label(bot_frame, text="New GPA: ").grid(row=1, column=2, sticky="E")
new_gpa = Entry(bot_frame, width=6)
new_gpa.grid(row=1, column=3)
new_gpa.insert(0, 0.0)

#Button Frame
buttons = Frame(master, border=4, relief=RIDGE)
buttons.grid(row=3, sticky=E+W)
buttons.columnconfigure(0, weight=1)

Button(buttons, text='+', command=add, width=3).grid(row=0, column=0)
Button(buttons, text='-', command=remove, width=3).grid(row=0, column=1)
Button(buttons, text='Reset', command=lambda: resetForm(curr, sem_gpa, new_gpa, class_data, num), width=8).grid(row=0, column=2)
Button(buttons, text='Calculate', command=lambda: calculate(curr, class_data, num, sem_gpa, new_gpa), width=8).grid(row=0, column=3)
Button(buttons, text='Quit', command=master.destroy, width=8).grid(row=0, column=4)


 
mainloop( )



