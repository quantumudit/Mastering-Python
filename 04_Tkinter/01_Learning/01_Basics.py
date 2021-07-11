import tkinter as tk
from tkinter import ttk

win = tk.Tk()

# adding title:

win.title('My GUI App')

# creating labels:

name_label = ttk.Label(win, text="Enter Your Name: ")
name_label.grid(row=0, column=0, sticky= tk.W)

email_label = ttk.Label(win, text="Enter Your Email: ")
email_label.grid(row=1, column=0, sticky= tk.W)

age_label = ttk.Label(win, text="Enter Your Age: ")
age_label.grid(row=2, column=0, sticky= tk.W)

gender_label = ttk.Label(win, text="Select Your Gender: ")
gender_label.grid(row=3, column=0, sticky= tk.W)

# Creating entry box:

name_var = tk.StringVar()
name_entrybox = ttk.Entry(win, width=16, textvariable=name_var)
name_entrybox.grid(row=0, column=1, sticky= tk.W)
name_entrybox.focus()

email_var = tk.StringVar()
email_entrybox = ttk.Entry(win, width=16, textvariable=email_var)
email_entrybox.grid(row=1, column=1, sticky= tk.W)

age_var = tk.StringVar()
age_entrybox = ttk.Entry(win, width=16, textvariable=age_var)
age_entrybox.grid(row=2, column=1, sticky= tk.W)


# Creating combo box:

gender_var = tk.StringVar()
gender_combobox = ttk.Combobox(win, width=14, textvariable=gender_var, state='readonly')
gender_combobox['values'] = ('Male', 'Female', 'Other')
gender_combobox.current(0)
gender_combobox.grid(row=3, column=1)


# Creating radio buttons:

usertype = tk.StringVar()
radiobtn1 = ttk.Radiobutton(win, text='Student', value='Student', variable=usertype)
radiobtn1.grid(row=4, column=0)

radiobtn2 = ttk.Radiobutton(win, text='Teacher', value='Teacher', variable=usertype)
radiobtn2.grid(row=4, column=1)

# Creating check buttons:

checkbtn_var = tk.IntVar()
checkbtn = ttk.Checkbutton(win, text='Check to Subscribe and get daily updates !', variable=checkbtn_var)
checkbtn.grid(row=5, columnspan=3)


# Creating buttons:

def fxaction():
    username = name_var.get()
    age = age_var.get()
    email = email_var.get()
    gender = gender_var.get()
    user_type = usertype.get()
    if checkbtn_var.get() == 0:
        subscribed = "No"
    else:
        subscribed = "Yes"
    
    with open('file.txt', 'a') as f:
        f.write(f'{username},{age},{email},{gender},{user_type},{subscribed}\n')
    
    print("One Item Appended !")
    

submit_button = ttk.Button(win, text='Submit', command=fxaction)
submit_button.grid(row=8, column=0)


# Clearing filled boxes post submit:

name_entrybox.delete(0, tk.END)
email_entrybox.delete(0, tk.END)
age_entrybox.delete(0, tk.END)


win.mainloop()



"""
NOTES:

> mainloop() : don't let the GUI app to auto-close (Keeps the app open)

> widgets like buttons, radio buttons, labels etc. are available in both 'tk' and 'ttk' module.
But, the widgets from 'ttk' module are more rich and good looking. 'ttk' is a sub-module of 'tk'.

> '.focus()' will take the cursor to the desired position when app opens

> 'pack' and 'grid' method used to place labels in the app. The 'grid' is the choice to go.

> in 'combobox'; 'state=readonly' restricts user to type anything in combo box and just let them choose from option

> gender_combobox.current(0): by default; sets 'Male'

"""