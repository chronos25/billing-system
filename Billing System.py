from Tkinter import *
root=Tk()
root.title("Billing System")

Label(root,text='Select Your Breakfast',font='arial 30 bold',fg='orange').grid(row=0,columnspan=5)
Label(root,text='(Breakfast Calculator)',font='arial 25 underline').grid(row=1,columnspan=5)

    
v1=IntVar()
v2=IntVar()
v3=IntVar()
v4=IntVar()
v5=IntVar()
v6=IntVar()
v7=IntVar()
v8=IntVar()

v9=IntVar()
v10=IntVar()
v11=IntVar()
v12=IntVar()
v13=IntVar()
v14=IntVar()
v15=IntVar()
v16=IntVar()


Checkbutton(root,text='Macroni(105)',variable=v1,onvalue=105,width=10).grid(row=2,column=0)
Checkbutton(root,text='Sandwich(80)',variable=v2,onvalue=80,width=10).grid(row=3,column=0)
Checkbutton(root,text='Aloo Paratha(200)',variable=v3,onvalue=200,width=12).grid(row=4,column=0)
Checkbutton(root,text='Poha(50)',variable=v4,onvalue=50,width=10).grid(row=5,column=0)
Checkbutton(root,text='Noodles(120)',variable=v5,onvalue=120,width=10).grid(row=6,column=0)
Checkbutton(root,text='Egg(20)',variable=v6,onvalue=20,width=10).grid(row=7,column=0)
Checkbutton(root,text='idli(60)',variable=v7,onvalue=60,width=10).grid(row=8,column=0)
Checkbutton(root,text='Upma(70)',variable=v8,onvalue=70,width=15).grid(row=9,column=0)
Checkbutton(root,text='Pav Bhaji(110)',variable=v9,onvalue=110,width=10).grid(row=2,column=1)
Checkbutton(root,text='Pasta(80)',variable=v10,onvalue=80,width=10).grid(row=3,column=1)
Checkbutton(root,text='Omlete(30)',variable=v11,onvalue=30,width=10).grid(row=4,column=1)
Checkbutton(root,text='Fruits(40)',variable=v12,onvalue=40,width=10).grid(row=5,column=1)
Checkbutton(root,text='Bread Butter(20)',variable=v13,onvalue=20,width=10).grid(row=6,column=1)
Checkbutton(root,text='Sprouts(65)',variable=v14,onvalue=65,width=10).grid(row=7,column=1)
Checkbutton(root,text='Porage(55)',variable=v15,onvalue=55,width=10).grid(row=8,column=1)
Checkbutton(root,text='Milk Corn Flakes(25)',variable=v16,onvalue=25,width=15).grid(row=9,column=1)
def fun():
    a=int(v1.get())
    b=int(v2.get())
    c=int(v3.get())
    d=int(v4.get())
    e=int(v5.get())
    f=int(v6.get())
    g=int(v7.get())
    h=int(v8.get())
    i=int(v9.get())
    j=int(v10.get())

    k=int(v11.get())
    l=int(v12.get())
    m=int(v13.get())
    n=int(v14.get())
    o=int(v15.get())
    p=int(v16.get())
    z=a+b+c+d+e+f+g+h+i+j+k+l+m+n+o+p;
    Label(root,text='Total Amount :-   $  '+str(z)+'   ',font='arial 20 bold').grid(row=11)
   

def destroy():
    root.destroy()
    
    
Button(root,text='Check Rs',command=fun,bd=3,font='times 10').grid(row=10,column=0,pady=5)
Button(root,text='Exit',command=destroy,bd=3,font='times 10').grid(row=10,column=1,pady=5)
mainloop()
