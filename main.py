import tkinter as tk
class tdlist:
    
    def __init__(self):

    
    
        self.root = tk.Tk()

        heading = tk.Label(self.root, text="TO-DO LIST",font=('Arial',30,'bold'))
        heading.pack()


    

        self.textb1 = tk.StringVar(value="task 1")
        self.state = tk.IntVar()

        self.frame = tk.Frame(self.root)
        self.frame.pack(fill = 'x', anchor = 'w')

        addbtn = tk.Button(self.frame,text="Add New",  
        font=('Arial',8), anchor='w', justify='left',
         command = self.addtask)
        addbtn.pack(anchor='w' )
        
        chkbox = tk.Checkbutton(self.frame, 
        textvariable=self.textb1, font=('Arial',16), 
        anchor='w', justify='left', variable=self.state, 
        command=lambda: self.donetask(self.state,self.textb1))
        chkbox.pack(fill='x')


        self.root.geometry("500x500")
        self.root.title("To-Do LIST")

        


        tk.mainloop()
    
    def donetask(self, state, textb1):
        st = state.get()
        txt = textb1.get()


        
        if st == 1:
            textb1.set(self.strikethrough(txt))
        else:
            textb1.set("task 1")
      

    def strikethrough(self, input):
        result = ''
        for i in input:
            result = result + i + '\u0336'
        return result

        


    def addtask(self):
        self.newst = tk.IntVar()
        self.text2 = tk.StringVar(value="task 2")


        nwbtn = tk.Checkbutton(self.frame,textvariable=self.text2, 
         font=('Arial',16), variable = self.newst, command = lambda: self.donetask(self.newst,self.text2))
        nwbtn.pack(anchor='w')

        
    

       

tdlist()