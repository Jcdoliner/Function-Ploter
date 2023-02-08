from tkinter import *
from numpy import *

import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg as FC

main_window=Tk()
main_window.title("Function Plotter")


x1=DoubleVar()
x2=DoubleVar()
p=IntVar()



fx_Entry=Entry(main_window)
fx_Entry.grid(row=2,column=0,pady=10,padx=10,sticky=W)


summarylabel=Label(main_window,bg="LightBlue",text="Function Grapher")
summarylabel.grid(row=0,column=1)


fxlabel=Label(main_window,bg="LightBlue",text="Equation f(x)")
fxlabel.grid(row=1,column=0)

x1_label=Label(main_window,bg='LightBlue',text="Start Point")
x1_label.grid(row=3,column=0,pady=10)

x1_Entry=Entry(main_window,textvariable=x1)
x1_Entry.grid(row=4,column=0,pady=10,padx=10,sticky=W)


x2_label=Label(main_window,bg='LightBlue',text="End Point")
x2_label.grid(row=3,column=1,pady=10)

x2_Entry=Entry(main_window,textvariable=x2)
x2_Entry.grid(row=4,column=1,pady=10,padx=10)

p_label=Label(main_window,bg='LightBlue',text="# of points")
p_label.grid(row=3,column=2,pady=10,padx=10)

p_Entry=Entry(main_window,textvariable=p)
p_Entry.grid(row=4,column=2,pady=10,padx=10)


def fx_Plot():

#get starting,ending and number of points
    sp=x1.get()
    ep=x2.get()
    np=p.get()
#sets up the x array
    x=linspace(sp,ep,np)
#evaluates function elements (cos,pi...etc) that are strings to the values of the x array 
    fx=(eval(fx_Entry.get()))
 
    fig=plt.figure(figsize=(5,5),layout="constrained") #layout argument allows to show the complete plot
    plt.plot(x,fx)
    plt.title(fx_Entry.get())
    plt.ylabel("F(x)",fontsize=10)
    plt.xlabel("x",fontsize=10)
    plt.grid(True)
    canvas=FC(fig,master=main_window)
    canvas.get_tk_widget().grid(row=6,column=1,padx=10,pady=20,sticky=W+E+S)

plotbutton=Button(main_window,bg='LightBlue',text='Plot response',fg="black",command=fx_Plot)
plotbutton.grid(row=5,column=1,padx=10,pady=10)
mainloop()
