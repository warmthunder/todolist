import tkinter as tk
class tdlist:
    
    def __init__(self):

    
    
        self.root = tk.Tk()

        heading = tk.Label(self.root, text="TO-DO LIST",font=('Arial',30,'bold'))
        heading.pack()

        self.frame = tk.Frame(self.root)
        self.frame.pack(fill = 'x', anchor = 'w')

        addbtn = tk.Button(self.frame,text="Add New",  
        font=('Arial',8), anchor='w', justify='left',
         command = self.newtaskwindow)
        addbtn.pack(anchor='w' )
        
    
        self.root.geometry("500x500")
        self.root.title("To-Do LIST")

        self.tasks = []

        self.deletebtn = tk.Button(self.frame, 
        text="delete task", 
        command = lambda: (self.removetasks(self.tasks[0]),self.tasks.pop(0)))
        self.deletebtn.pack()
       


        tk.mainloop()
    
    def donetask(self, state, textb1, text):
        st = state.get()
        txt = textb1.get()
        
        if st == 1:
            textb1.set(self.strikethrough(txt))
        else:
            textb1.set(text)
      

    def strikethrough(self, input):
        result = ''
        for i in input:
            result = result + i + '\u0336'
        return result

    def removetasks(self,task):
        task.destroy()

    def newtaskwindow(self):
        addwindow = tk.Toplevel()
        addwindow.geometry('300x200')
        
        textt = tk.Label(addwindow, text="enter name of task", font=('Arial', 16, 'bold'))
        textt.pack()

        entry = tk.Entry(addwindow)
        entry.pack(fill='x')

       

        nextbtn = tk.Button(addwindow, text='add task', font=('Arial', 16), command=lambda: (self.addtask( entry.get()), addwindow.destroy())
        )
        nextbtn.pack()


    def addtask(self, text):
        

        self.newst = tk.IntVar()
        self.text2 = tk.StringVar(value=text)


        nwbtn = tk.Checkbutton(self.frame,textvariable=self.text2, 
         font=('Arial',16), variable = self.newst,command = lambda:( self.donetask(self.newst,self.text2, text)) )
        nwbtn.pack(anchor='w')

        self.tasks.append(nwbtn)
        print(self.tasks)
    


    
tdlist()