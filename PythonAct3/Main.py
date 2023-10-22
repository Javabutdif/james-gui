from tkinter import *
from tkinter import ttk
from tkinter import messagebox  # Import messagebox

from dvhelp import *

# Method for database

class Student:
    def __init__(self):
        self.root = Tk()
        self.root.title('Genabio, Anton James')
        self.root.geometry("500x500")
        self.root.resizable(False, False)
        self.root.eval("tk::PlaceWindow  .  center")
        self.frame = Frame(self.root, bd=20)
        self.frame.grid()

        self.fontModify = "Arial, 12"

        n = StringVar()
        self.course = ttk.Combobox(self.root, width=27, textvariable=n)
        self.course['values'] = ('BSIT', 'BSCS', 'ACT', 'BSIS')

        y = StringVar()
        self.year = ttk.Combobox(self.root, width=27, textvariable=y)
        self.year['values'] = ('1', '2', '3', '4')

        self.lb_idNo = Label(self.root, text="Id No: ", font=self.fontModify)
        self.lb_idNo.grid(row=0, column=0)
        self.lb_LastName = Label(self.root, text="Last Name: ", font=self.fontModify)
        self.lb_LastName.grid(row=1, column=0)
        self.lb_FirstName = Label(self.root, text="First Name: ", font=self.fontModify)
        self.lb_FirstName.grid(row=2, column=0)
        self.lb_course = Label(self.root, text="Course: ", font=self.fontModify)
        self.lb_course.grid(row=3, column=0)
        self.lb_year = Label(self.root, text="Year: ", font=self.fontModify)
        self.lb_year.grid(row=4, column=0)

        # TextBox Columns
        self.entry_idNo = Entry(self.root, font=self.fontModify)
        self.entry_idNo.grid(row=0, column=1)
        self.entry_lastName = Entry(self.root, font=self.fontModify)
        self.entry_lastName.grid(row=1, column=1)
        self.entry_firstName = Entry(self.root, font=self.fontModify)
        self.entry_firstName.grid(row=2, column=1)
        self.course.current(0)
        self.course.grid(row=3, column=1)
        self.year.current(0)
        self.year.grid(row=4, column=1)
        self.find_button = Button(self.root, text="Find", command=self.findStud)
        self.find_button.grid(row=0, column=2)

        self.new_button = Button(self.root, text="New", command=self.newStud)
        self.new_button.grid(row=5, column=0)
        self.save_button = Button(self.root, text="Save", command=self.saveStud)
        self.save_button.grid(row=5, column=1)
        self.delete_button = Button(self.root, text="Delete", command=self.deleteStud)
        self.delete_button.grid(row=5, column=2)
        self.update_button = Button(self.root, text="Update", command=self.updateStud)
        self.update_button.grid(row=5, column=3)

        self.root.mainloop()

    def findStud(self):
        id_no = self.entry_idNo.get()
        records = getrecord("student", idno=id_no)
        if records:
            student = records[0]
            self.entry_lastName.delete(0, END)
            self.entry_firstName.delete(0, END)
            self.entry_lastName.insert(0, student['lastname'])
            self.entry_firstName.insert(0, student['firstname'])
            self.course.set(student['course'])
            self.year.set(student['year'])
        else:
            messagebox.showinfo("Not Found", "Record not found")

    def newStud(self):
        self.entry_idNo.delete(0, END)
        self.entry_lastName.delete(0, END)
        self.entry_firstName.delete(0, END)
        self.course.set('')
        self.year.set('')

    def saveStud(self):
        id_no = self.entry_idNo.get()
        last_name = self.entry_lastName.get()
        first_name = self.entry_firstName.get()
        course_value = self.course.get()
        year_value = self.year.get()

        if addrecord("student", idno=id_no, lastname=last_name, firstname=first_name, course=course_value, year=year_value):
            messagebox.showinfo("Success", "Record saved successfully")
        else:
            messagebox.showerror("Error", "Failed to save record")

    def deleteStud(self):
        id_no = self.entry_idNo.get()
        if deleterecord("student", idno=id_no):
            messagebox.showinfo("Success", "Record deleted successfully")
            self.newStud()
        else:
            messagebox.showerror("Error", "Failed to delete record")

    def updateStud(self):
        id_no = self.entry_idNo.get()
        last_name = self.entry_lastName.get()
        first_name = self.entry_firstName.get()
        course_value = self.course.get()
        year_value = self.year.get()

        if updaterecord("student", idno=id_no, lastname=last_name, firstname=first_name, course=course_value, year=year_value):
            messagebox.showinfo("Success", "Record updated successfully")
        else:
            messagebox.showerror("Error", "Failed to update record")

def main():
    global student
    student = Student()

if __name__ == "__main__":
    main()
