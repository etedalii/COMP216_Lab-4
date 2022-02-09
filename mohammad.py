from doctest import master
from logging import PlaceHolder
from re import T
from select import select
from textwrap import fill
from tkinter import *
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkinter.ttk import *
import tkinter.ttk as ttk


class App(tk.Frame):
    def __init__(self, master) -> None:
        tk.Frame.__init__(self, master, height=42, width=42)
        #master.resizable(False, False)
        self.radioVar = StringVar()
        self.myColor = '#57D2A9'
        master.title('Centennial College')
        Canvas(width=500, height=350).pack()
        container = Frame(master, relief='groove', padding=(0, 0))
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
        style.configure('TFrame', background=self.myColor)

    def create_ui(self, parent):
        Label(parent, text='ICET Student Survey', font=(
            "arial bold italic", 18), background=self.myColor).place(relx=.3, rely=.05)

        Label(parent, text='Full name:', background=self.myColor).place(
            relx=0.01, rely=0.2)
        Entry(parent, textvariable=self.__fullname).place(relx=.3, rely=.2)

        Label(parent, text='Residency:', background=self.myColor).place(
            relx=0.01, rely=0.3)
        self.radioVar.set('dom')
        Radiobutton(parent, text="Domestic", variable=self.radioVar, value='dom',
                    style='Wild.TRadiobutton').place(relx=0.3, rely=0.3)
        Radiobutton(parent, text="International", variable=self.radioVar, value='intl',
                    style='Wild.TRadiobutton').place(relx=0.3, rely=0.36)

        Label(parent, text='Program:', background=self.myColor).place(
            relx=0.01, rely=0.42)

        # create a combobox ***************
        self.variable = tk.StringVar()
        self.program_cb = ttk.Combobox(
            parent, textvariable=self.variable, state='readonly')
        self.program_cb['values'] = (
            'Health', 'Networking', 'IT Project', 'AI')
        #self.program_cb.grid(column=0, row=5, padx=142, pady=165)
        self.program_cb.current(0)
        self.program_cb.place(x=145, y=160)

        Label(parent, text='Courses:', background=self.myColor).place(
            relx=0.01, rely=0.52)

        # checkbox ****************
        self.var1 = tk.StringVar()
        self.var2 = tk.StringVar()
        self.var3 = tk.StringVar()
        self.var1.set('COMP100')
        self.__checkbox_lst = tuple(['COMP100'])
        tk.Checkbutton(parent, text='Programming I', variable=self.var1, onvalue='COMP100',
                       offvalue='', command=self.checkbox_selection, background=self.myColor).place(relx=0.29, rely=0.52)
        tk.Checkbutton(parent, text='Web Page Design', variable=self.var2, onvalue='COMP213',
                       offvalue='', command=self.checkbox_selection, background=self.myColor).place(relx=0.29, rely=0.61)
        tk.Checkbutton(parent, text='Software Engineering', variable=self.var3, onvalue='COMP120',
                       offvalue='', command=self.checkbox_selection, background=self.myColor).place(relx=0.29, rely=0.70)

        # buttons ************
        Button(parent, text='Reset', command=self.reset).place(
            relx=0.04, rely=.80, width=120)
        Button(parent, text='Ok', command=self.display_info).place(
            relx=0.30, rely=.80, width=160)
        Button(parent, text='Exit', command=self.teminate_app).place(
            relx=0.65, rely=.80, width=120)

    def checkbox_selection(self):
        listx = list(self.__checkbox_lst)
        if (self.var1.get() == 'COMP100'):
            if len(listx) > 0:
                if self.var1.get() not in listx:
                    listx.append(self.var1.get())
            else:
                listx.append(self.var1.get())
        elif (self.var1.get() == ''):
            if len(listx) > 0:
                if 'COMP100' in listx:
                    listx.remove('COMP100')

        if (self.var2.get() == 'COMP213'):
            if len(listx) > 0:
                if self.var2.get() not in listx:
                    listx.append(self.var2.get())
            else:
                listx.append(self.var2.get())
        elif (self.var2.get() == ''):
            if len(listx) > 0:
                if 'COMP213' in listx:
                    listx.remove('COMP213')

        if (self.var3.get() == 'COMP120'):
            if len(listx) > 0:
                if self.var3.get() not in listx:
                    listx.append(self.var3.get())
            else:
                listx.append(self.var3.get())
        elif (self.var3.get() == ''):
            if len(listx) > 0:
                if 'COMP120' in listx:
                    listx.remove('COMP120')

        self.__checkbox_lst = tuple(listx)

    def create_vars(self):
        self.__checkbox_lst = ()
        self.__fullname = StringVar()
        self.__fullname.set('Mohammad Etedali')

    def display_info(self):
        messagebox.showinfo(
            'Information', f'{ self.__fullname.get()}\r\n{self.variable.get()}\r\n{str(self.radioVar.get())}\r\n{self.__checkbox_lst}')

    def teminate_app(self):
        self.quit()

    def reset(self):
        self.__fullname.set('')
        self.program_cb.current(0)
        self.radioVar.set('dom')
        self.var1.set('0')
        self.var2.set('0')
        self.var3.set('0')
        self.__checkbox_lst = ()


def main():
    root = tk.Tk()
    App(root).pack(expand=True, fill='both')
    root.mainloop()


if __name__ == "__main__":
    main()
