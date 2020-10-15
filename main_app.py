#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 21 14:55:56 2020

@author: adamswitalski
"""

### location of the Baby Name Generator folder
main_path = 'C:/Users/aswitalski/Desktop/Baby_Name_Generator/'


##### Import #####

import tkinter as Tk
from tkinter import messagebox
from PIL import Image, ImageTk
from baby_name_generator import pick_name, get_names, show_names

##### Functions #####

def set_num(var):
    global intervals
    intervals = names_var.get()

def go():
    get_names()
    set_num(names_var)
    pick_name(intervals, gender_var.get())

def close():
    exit()
    
def about_message():
    messagebox.showinfo('About','Version 0.1 alpha' + 
                        '\nCreator: Adam Switalski')

### create root frame
root = Tk.Tk()
root.geometry('600x500')
root.title('Baby Name Generator')

### add menu dropdowns
menu = Tk.Menu(root)
root.config(menu=menu)
### add file 
file = Tk.Menu(root)
menu.add_cascade(label='File',menu=file)
file.add_command(label='Exit', command=close)

### add options dropdown
options = Tk.Menu(root)
menu.add_cascade(label='Options',menu=options)
options.add_command(label='About', command=about_message)

### create variables on root screen
gender_var = Tk.StringVar()
names_var = Tk.IntVar()
## this sets the default value to 1 for the number of intervals
names_var.set(1)
baby_var = Tk.StringVar()

### import images
boy_img = Image.open(main_path + 'boy_symbol.png')
girl_img = Image.open(main_path + 'girl_symbol.png')
boy_photo = ImageTk.PhotoImage(boy_img)
girl_photo = ImageTk.PhotoImage(girl_img)

### title of root
rt_Label = Tk.Label(root, text='Random Baby Name Generator', font=('Arial', 24))
rt_Label.place(x=75, y=50)

### place images on root
rt_Boy_Img = Tk.Label(image=boy_photo)
rt_Girl_Img = Tk.Label(image=girl_photo)
rt_Boy_Img.place(relx=.2, rely=.2)
rt_Girl_Img.place(relx=.6, rely=.2)

### add sub title on root
rt_Select_Lbl = Tk.Label(root, text='Select gender', font=('Arial', 20))
rt_Select_Lbl.place(relx=.35, y=250)

### add radio buttons for gender
gen_Radio_male = Tk.Radiobutton(root, text='Male', variable=gender_var, 
                                value='Male', font=('Arial', 16))
gen_Radio_female = Tk.Radiobutton(root, text='Female', variable=gender_var, 
                                  value='Female', font=('Arial', 16))
gen_Radio_male.place(relx=.2, rely=.6)
gen_Radio_female.place(relx=.6, rely=.6)

### add number of sample values
sample_Label = Tk.Label(root, text='Number of Names: ', font=('Arial', 16))
sample_Label.place(x=150, y=350)
sample_Entry = Tk.Entry(root, textvar=names_var, width=5, font=('Arial', 16),
                        justify='center')
sample_Entry.place(x=340, y=347)

### add buttons to exit, execute, show names
go_Button = Tk.Button(root, text='Go!', font=('Arial', 16), command=go)
go_Button.config(height=2, width=7, relief='raised')
go_Button.place(relx=.15, rely=.8)

close_Button = Tk.Button(root, text='Close', font=('Arial', 16), command=close)
close_Button.config(height=2, width=7, relief='raised')
close_Button.place(relx=.75, rely=.8)

sn_Button = Tk.Button(root, text='Show names', font=('Arial', 16),
                      command=show_names)
sn_Button.config(height=2, width=12, relief='raised')
sn_Button.place(relx=.4, rely=.8)

root.mainloop()