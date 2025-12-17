import tkinter as tk
class tdlist:
    
    def __init__(self):

    
    
        self.root = tk.Tk()

        heading = tk.Label(self.root, text="TO-DO LIST",font=('Arial',30,'bold'))
        heading.pack()

        self.frame = tk.Frame(self.root, bg= 'pink')
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
        self.delphoto = tk.PhotoImage(file='delete.png')
        self.delphoto = self.delphoto.subsample(32,32)

        tk.mainloop()
    

    def quickdel(self, chkbtn):
        parentframe = chkbtn.master
        text = chkbtn.cget("text")
        
        for a in self.tasks:
            if a[2] == text:
                self.tasks.remove(a)
                
        for a in parentframe.winfo_children():
           
            a.destroy()


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
            btn = tk.Checkbutton(deletewindow, textvariable = a[1], font=('Arial',16), command = lambda a=a: self.tasks.remove(a))
            btn.pack()
          
        
       

        confirmbtn = tk.Button(deletewindow, text='confirm', command=lambda:(self.refresh(), deletewindow.destroy()) )
        confirmbtn.pack()

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
            if isinstance(widget, tk.Frame):
                widget.destroy()

        for state, texts, text in self.tasks:
            taskframe = tk.Frame(self.frame)
            taskframe.pack(fill='x')
            nwbtn = tk.Checkbutton(taskframe,textvariable=texts, 
            font=('Arial',16), 
            variable = state,
            command = lambda s=state, t=texts, tx=text: self.donetask(s, t, tx)) 
            nwbtn.pack(anchor='e', side=tk.LEFT)
            delbtn = tk.Button(taskframe, image = self.delphoto, command = lambda nb = nwbtn:self.quickdel(nb))
            delbtn.pack(anchor='e', side=tk.LEFT)
        
    


    
tdlist()