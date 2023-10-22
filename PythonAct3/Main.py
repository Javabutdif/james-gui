
from tkinter import *
from tkinter import ttk


class Student:
	
	def __init__ (self):
		
		self.root = Tk()
		self.root.title('Genabio, Anton James')
		self.root.geometry("500x400")
		self.root.resizable(False, False)
		self.root.eval("tk::PlaceWindow  .  center")
		self.frame = Frame(self.root, bd=20)
		self.frame.grid()
		
		self.fontModify = "Arial,30"
		
		# Combobox creation 
		self.n = StringVar() 
		monthchoosen = ttk.Combobox(self.root, width = 27, textvariable = self.n) 
  
		# Adding combobox drop down list 
		monthchoosen['values'] = (' BSIT',  
                          ' BSCS', 
                          ' ACT'
                          ) 
  
		
		
		
		#Label Rows
		self.lb_idNo = Label(self.root, text="Id No: ", font = self.fontModify )
		self.lb_idNo.grid(row=0,column=0)
		self.lb_LastName = Label(self.root, text="Last Name: ", font = self.fontModify )
		self.lb_LastName.grid(row=1,column=0)
		self.lb_FirstName = Label(self.root, text="First Name: ", font = self.fontModify )
		self.lb_FirstName.grid(row=2,column=0)
		self.lb_course = Label(self.root, text="Course: ", font = self.fontModify )
		self.lb_course.grid(row=3,column=0)
		self.lb_year = Label(self.root, text="Year: ", font = self.fontModify )
		self.lb_year.grid(row=4,column=0)
		#TextBox Columns
		self.entry_idNo = Entry(self.root, font = self.fontModify  )
		self.entry_idNo.grid(row=0,column=1)
		self.entry_lastName = Entry(self.root, font = self.fontModify  )
		self.entry_lastName.grid(row=1,column=1)
		self.entry_firstName = Entry(self.root, font = self.fontModify  )
		self.entry_firstName.grid(row=2,column=1)
        
		
		
		
		
		#Execution
		self.root.mainloop()
	


	

def main()->None:
	Student()



if __name__ == "__main__":
	main()