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

        self.g_field = Entry(frame)
        self.g_field.grid(row=0, column=1)
        self.g_field.insert(0, 0.0)

        self.c_field = Entry(frame)
        self.c_field.grid(row=1, column=1)
        self.c_field.insert(0, 0)

    def getCredits(self):
        try:
            credits = int(self.c_field.get())
            return credits
        except ValueError:
            return 0
    
    def getPoints(self):
        try:
            points = float(self.c_field.get()) * float(self.g_field.get())
            return points
        except ValueError:
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

        self.c_field = Entry(frame)
        self.c_field.grid(row=num, column=1)
        self.c_field.insert(1, 0)

        self.g_field = Entry(frame)
        self.g_field.grid(row=num, column=2)
        self.g_field.insert(1, 0)

    def getCredits(self):
        try:
            credits = int(self.c_field.get())
            return credits
        except ValueError:
            return 0
    
    def getPoints(self):
        try:
            points = float(self.c_field.get()) * float(self.g_field.get())
            return points
        except ValueError:
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
master.geometry("600x300")
master.configure(bg="#234C67")

#Top Frame
top_frame = Frame(master)
top_frame.grid(row=0, columnspan=2)

Label(top_frame, text="Credits").grid(row=1, column=1)
Label(top_frame, text="Grade (0.0 - 4.0)").grid(row=1, column=2)

for i in range(num):
    class_data.append(classData(top_frame, i + 2))

#Bottom Left Frame
bottom_left = Frame(master)
bottom_left.grid(row=num+1, column=0)

curr = currentGPA(bottom_left)

#Bottom Right Frame
bottom_right = Frame(master)
bottom_right.grid(row=num+1, column=1)

Label(bottom_right, text="Semester GPA: ").grid(row=0, column=0, sticky="E")
sem_gpa = Entry(bottom_right)
sem_gpa.grid(row=0, column=1)
sem_gpa.insert(0, 0.0)

Label(bottom_right, text="New GPA: ").grid(row=1, column=0, sticky="E")
new_gpa = Entry(bottom_right)
new_gpa.grid(row=1, column=1)
new_gpa.insert(0, 0.0)

#Button Frame
buttons = Frame(master)
buttons.grid(row=num+2, columnspan=2)

Button(buttons, text='Add Row', command=add, width=10).grid(row=0, column=0)
Button(buttons, text='Remove Row', command=remove, width=10).grid(row=0, column=1)
Button(buttons, text='Reset Form', command=lambda: resetForm(curr, sem_gpa, new_gpa, class_data, num), width=10).grid(row=0, column=2)
Button(buttons, text='Calculate', command=lambda: calculate(curr, class_data, num, sem_gpa, new_gpa), width=10).grid(row=0, column=3)
Button(buttons, text='Quit', command=master.destroy, width=10).grid(row=0, column=4)


 
mainloop( )



