from logging import PlaceHolder
from tkinter import *
from tkinter import messagebox
from tkinter.ttk import *
from turtle import bgcolor
from typing import Container

class App(Tk):
    

    def __init__(self) -> None:
        Tk.__init__(self)
        self.var = IntVar()
        self.title('Centennial College')
        Canvas(width=600, height=400).pack()
        container = Frame(self, relief='groove', padding=(0, 0))
        container.place(
            relx=0.02,
            rely=0.03,
            relheight=0.95,
            relwidth=0.96)
        self.create_styles()
        self.create_vars()
        self.create_ui(container)


    def create_styles(self):
        style = Style()
        style.configure('TFrame', #TButton-> TLable
         background='#57D2A9')

    def create_ui(self, parent):
        Label(parent, text='ICET Student Survey',font=("arial bold italic", 18), background=('#57D2A9')).place(relx=.3, rely=.05)

        Label(parent, text='Full name:', background=('#57D2A9')).place(relx=0.01, rely=0.2)
        Entry(parent, textvariable=self.__fullname).place(relx=.3, rely=.2)

        Label(parent, text='Residency:', background=('#57D2A9')).place(relx=0.01, rely=0.2)
        R1 = Radiobutton(parent, text="Domestic", variable=self.var, value=1,command=self.sel).place(relx=0.3, rely=0.3)        
        R2 = Radiobutton(parent, text="International", variable=self.var, value=2,command=self.sel).place(relx=0.3, rely=0.36)

        
        #Button(parent, text='Click me', command=self.display_info).place(relx=.2,rely=.25)
        #Button(parent, text='another button me', command=self.display_info).place(relx=.4,rely=.25)
        #Entry(parent, textvariable=self.__fullname).place(relx=.2, rely=.4)

    def sel(self):
        selection = "You selected the option " + str(self.var.get())
        #label.config(text = selection)

    def create_vars(self):
        '''
        create all the text variables
        '''
        self.__from_title = StringVar()
        self.__fullname = StringVar()
        self.__fullname.set('Mohammad Etedali')

    def display_info(self):
        messagebox.showinfo('an important message', self.__fullname.get())






# test harness
app = App()
app.mainloop()        