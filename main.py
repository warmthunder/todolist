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
        text="delete task", font=('Arial',8),
        command = self.selectdelete)
        self.deletebtn.pack(anchor='w')
       
        self.delete = []


        tk.mainloop()
    
    def donetask(self, state, textb1, text):
        st = state.get()
        txt = textb1.get()
        
        if st == 1:
            textb1.set(self.strikethrough(txt))
        else:
            textb1.set(text)
      
    def selectdelete(self):

        deletewindow = tk.Toplevel()
        deletewindow.geometry('500x300')

        head = tk.Label(deletewindow, text="Select which task to delete",font=('Arial',25,'bold'))
        head.pack()

        for a in self.tasks:
            btn = tk.Checkbutton(deletewindow, textvariable = a[1], font=('Arial',16),variable = a[0], command = lambda a=a: self.delete.append(a))
            btn.pack()
            print(a)
        
       

        confirmbtn = tk.Button(deletewindow, text='confirm', command=lambda:(self.refreshdata(),self.refresh(), deletewindow.destroy()) )
        confirmbtn.pack()

        
        
    def refreshdata(self):
         for t1 in self.tasks:
            if t1 in self.delete:
                self.tasks.remove(t1)


    def strikethrough(self, input):
        result = ''
        for i in input:
            result = result + i + '\u0336'
        return result

   

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
        

        newst = tk.IntVar()
        text2 = tk.StringVar(value=text)

        self.tasks.append((newst,text2,text))
        self.refresh()

    def refresh(self):
        for widget in self.frame.winfo_children():
            if isinstance(widget, tk.Checkbutton):
                widget.destroy()

        for state, texts, text in self.tasks:
            nwbtn = tk.Checkbutton(self.frame,textvariable=texts, 
            font=('Arial',16), 
            variable = state,
            command = lambda:( self.donetask(state,texts, text)) )
            nwbtn.pack(anchor='w')
       
    


    
tdlist()