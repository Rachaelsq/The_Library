from tkinter import *

#CREATE THE BASE WINDOW
window=Tk()       

def button_function():
  print(entry1_value.get())
  text1.insert(END, entry1_value.get())
#the above line enters the inputted text and adds it to the end of the existing text


#CREATE A BUTTON
button1=Button(window,text="Execute", command=button_function )
button1.grid(row=0,column=0 )

#CAPTURE USER INPUT
entry1_value=StringVar()
#USER INPUT
entry1=Entry(window, textvariable=entry1_value)
entry1.grid(row=0,column=1)


#TEXT
text1=Text(window, height=1,width=20)
text1.grid(row=0,column=2)

#everything involving the window goes between "window=tk" and "window.mainloop"
window.mainloop()

