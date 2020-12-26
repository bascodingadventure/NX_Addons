import tkinter as tk

# Create the master object
master = tk.Tk()
master.title('Settings')

# Create the labels
tk.Label(text = 'Set Up New Iso View').grid(row=0, column=1)
tk.Label(text = 'Enter Scale here : ' ).grid(row=2, column=0)
tk.Label(text = 'Plot Scale Label : ' ).grid(row=3, column=0)

# Create input list
scl = tk.StringVar(master)
OPTIONS = ["5:1", "2:1", "1:1", "1:2", "1:5"] 
scl.set(OPTIONS[2]) # default value
tk.OptionMenu(master, scl, *OPTIONS).grid(row=2, column=1)

scale_label = tk.IntVar()
checkbox1 = tk.Checkbutton(master, variable=scale_label).grid(row=3, column=1)


def func_1():
    print('var:' , scale_label.get(), 'scale:' , scl.get())
    scale= scl.get()
    if scale == '1:1':
        denominator = 1.0
        numerator = 1.0
    elif scale == '1:2':
        denominator = 2.0
        numerator = 1.0
    elif scale == '1:5':
        denominator = 5.0
        numerator = 1.0
    elif scale == '2:1':    
        denominator = 1.0
        numerator = 2.0
    elif scale ==  '5:1':    
        denominator = 1.0
        numerator = 5.0

    print(numerator,':',denominator)
    master.destroy()

button = tk.Button(master, text="Place View", command=func_1).grid(row=4,column=1)

tk.mainloop()