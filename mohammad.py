from logging import PlaceHolder
from re import T
from tkinter import *
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkinter.ttk import *
import tkinter.ttk as ttk

from click import command


class App(Tk):
    def __init__(self) -> None:
        Tk.__init__(self)
        self.resizable(False, False)
        self.radioVar = IntVar()
        self.myColor = '#57D2A9'
        self.title('Centennial College')
        Canvas(width=500, height=350).pack()
        container = Frame(self, relief='groove', padding=(0, 0))
        container.place(
            relx=0.02,
            rely=0.03,
            relheight=0.95,
            relwidth=0.96)
        self.create_styles()
        self.create_vars()
        self.create_ui(container)

        self.s = ttk.Style()
        self.s.configure('Wild.TRadiobutton',
                         background=self.myColor, foreground='black')

    def create_styles(self):
        style = Style()
        style.configure('TFrame', background='#57D2A9')

    def create_ui(self, parent):
        Label(parent, text='ICET Student Survey', font=(
            "arial bold italic", 18), background=self.myColor).place(relx=.3, rely=.05)

        Label(parent, text='Full name:', background=self.myColor).place(
            relx=0.01, rely=0.2)
        Entry(parent, textvariable=self.__fullname).place(relx=.3, rely=.2)

        Label(parent, text='Residency:', background=self.myColor).place(
            relx=0.01, rely=0.3)
        self.radioVar.set(1)
        Radiobutton(parent, text="Domestic", variable=self.radioVar, value='dom',
                         command=self.sel, style='Wild.TRadiobutton').place(relx=0.3, rely=0.3)
        Radiobutton(parent, text="International", variable=self.radioVar, value='intl',
                         command=self.sel, style='Wild.TRadiobutton').place(relx=0.3, rely=0.36)

        Label(parent, text='Program:', background=self.myColor).place(
            relx=0.01, rely=0.42)
        # create a combobox
        self.variable = tk.StringVar()
        program_cb = ttk.Combobox(
            parent, textvariable=self.variable, state='readonly')
        program_cb['values'] = ('Health', 'Networking', 'IT Project')
        program_cb.grid(column=0, row=5, padx=142, pady=145)
        program_cb.current(0)
        program_cb.bind('<<ComboboxSelected>>', self.comboSel)

        Label(parent, text='Courses:', background=self.myColor).place(
            relx=0.01, rely=0.52)

        # checkbox
        self.var1 = tk.IntVar()
        self.var2 = tk.IntVar()
        self.var3 = tk.IntVar()
        self.var1.set('COMP100')
        tk.Checkbutton(parent, text='Programming I', variable=self.var1, onvalue='COMP100',
                       offvalue=0, command=self.checkbox_selection, background=self.myColor).place(relx=0.29, rely=0.52)
        tk.Checkbutton(parent, text='Web Page Design', variable=self.var2, onvalue='COMP213',
                       offvalue=0, command=self.checkbox_selection, background=self.myColor).place(relx=0.29, rely=0.61)
        tk.Checkbutton(parent, text='Software Engineering', variable=self.var3, onvalue='COMP120',
                       offvalue=0, command=self.checkbox_selection, background=self.myColor).place(relx=0.29, rely=0.70)

        Button(parent, text='Reset', command=self.display_info).place(
            relx=0.04, rely=.80, width=120)
        Button(parent, text='Ok', command=self.display_info).place(
            relx=0.30, rely=.80, width=160)
        Button(parent, text='Exit', command=self.display_info).place(
            relx=0.65, rely=.80, width=120)

    def checkbox_selection(self):
        pass
        # if (self.var1.get() == 1) & (self.var2.get() == 0):
        # self.
        # elif (self.var1.get() == 0) & (self.var2.get() == 1):
        #     l.config(text='I love C++')
        # elif (var1.get() == 0) & (var2.get() == 0):
        #     l.config(text='I do not anything')
        # else:
        #     l.config(text='I love both')

    def sel(self):
        selection = "You selected the option " + str(self.radioVar.get())
        #label.config(text = selection)

    def comboSel(self, event):
        print(event.get())

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
