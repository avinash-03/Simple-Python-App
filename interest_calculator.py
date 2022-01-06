from tkinter import *

# screen
window = Tk()
#title
window.title('Interest Calculator')
# size
window.geometry('400x450')
# fix size
window.resizable(False,False)

# function
def calculate():
    principal_info= int(entry1.get())
    interest_rate = int(entry2.get())
    time_info = int(entry3.get())
    amount = (principal_info*interest_rate*time_info)/100
    Label(window,text='Interest',font='impack 15 bold').place(x=30,y=210)
    Label(window,text=amount,font='impack 15 bold').place(x=175,y=210)

# heading
Label(window,text='Simple Interest Calculator',font='impack 20 bold',bg='orange').pack(fill=X)  # fill the orage color horizontal

Label(window,text='Principal Amount',font='20').place(x=30,y=80)
Label(window,text='Interest Rate(%)',font='20').place(x=30,y=120)
Label(window,text='Time(yerar)',font='20').place(x=30,y=160)

# entry box
entry1=Entry(window,font='15',width=15,bd=3)
entry1.place(x=180,y=80)

entry2=Entry(window,font='15',width=15,bd=3)
entry2.place(x=180,y=120)

entry3=Entry(window,font='15',width=15,bd=3)
entry3.place(x=180,y=160)

# button
Button(window,text='Calculate',font=25,bg='green',fg='white',command=calculate).place(x=50,y=280)

Button(window,text='Exit',font=25,bg='red',fg='white',width=8,command=lambda:exit()).place(x=250,y=280)



mainloop()
