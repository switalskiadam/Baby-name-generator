#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 18 15:07:24 2020

@author: adamswitalski
"""
###### Import ######

import random
import tkinter as Tk


###### Functions #######

def get_names():
    from pandas import read_csv
    ### location of file folder
    filename = 'C:/Users/aswitalski/Desktop/Baby_Name_Generator/NationalNames.csv'
    global boys
    global girls
    df = read_csv(filename)
    ## Show names from 1990 or later
    name_list = df[(df['Year'] >= 1980) & (df['Year'] <= 2000)]
    ## Show names with at least x count
    name_list = name_list[name_list['Count'] > 1000]
    boys = list(name_list['Name'][name_list['Gender'] == 'M'])
    girls = list(name_list['Name'][name_list['Gender'] == 'F'])
    ## Dedupe names
    boys = list(dict.fromkeys(boys))
    girls = list(dict.fromkeys(girls))

def show_names():
    keep_window = Tk.Tk()
    keep_window.geometry('250x200')
    keep_window.title('Saved Names')
    scrollbar = Tk.Scrollbar(keep_window)
    scrollbar.pack( side = Tk.RIGHT, fill=Tk.Y)

    mylist = Tk.Listbox(keep_window, yscrollcommand = scrollbar.set,
                        borderwidth=0, highlightthickness=0)

    for name in keep_names:
       mylist.insert(Tk.END, name)

    mylist.pack( side = Tk.LEFT, fill = Tk.BOTH )
    scrollbar.config( command = mylist.yview )
    keep_window.wait_window()

def pick_name(number=1, gender='Male'):
    """Create loop to pick number of names"""
    global keep_names
    keep_names = []

    def add_name():
        global keep_names
        keep_names.append(baby_var)
        name_window.destroy()
    def reject():
        name_window.destroy()

    if gender == 'Male':
        random.shuffle(boys)
    else:
        random.shuffle(girls)

    if number > 200:
        loops = 200
    else:
        loops = number

    for i in range(0,loops):
        if gender == 'Male':
            name = boys[i]
        else:
            name = girls[i]

        baby_var = name

        name_window = Tk.Tk()
        name_window.geometry('250x200+100+100')
        name_window.title('Baby Name')
        nw_sub = Tk.Label(name_window, text='Do you like the name', font=('Arial', 14))
        nw_sub.place(relx=.5, rely=.2, anchor='center')

        name_Label = Tk.Label(name_window, text=baby_var, font=('Arial', 20))
        name_Label.place(relx=.5, rely=.4, anchor='center')

        yes_Button = Tk.Button(name_window, text='Yes', font=('Arial', 14),
                               command=add_name)
        yes_Button.config(height=2, width=7, relief='raised')
        yes_Button.place(relx=.15, rely=.6)

        no_Button = Tk.Button(name_window, text='No', font=('Arial', 14),
                              command=reject)
        no_Button.config(height=2, width=7, relief='raised')
        no_Button.place(relx=.6, rely=.6)

        name_window.wait_window()
