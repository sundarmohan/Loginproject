from tkinter import *
from PIL import ImageTk
from tkinter import messagebox
import pymysql

def connect_database():
    if emailEntry.get() == "" or userEntry.get() =="" or passEntry.get()=="" or confirm_passlabelEntry.get()=="":
        messagebox.showerror('Error','All the fields must be entered')

    elif passEntry.get()!=confirm_passlabelEntry.get():
        messagebox.showerror('Error', 'Password Mismatch')

    elif check.get()==0:
        messagebox.showerror('Error','Accept the Terms & conditions')





def login_page():
    signup_window.destroy()
    import signin

signup_window=Tk()
signup_window.title('Signup Page')
signup_window.minsize ()
signup_window.geometry()


background=ImageTk.PhotoImage(file=r"C:\Users\sunda\PycharmProjects\Loginproject\venv\bg\bgp.jpg")


bglabel=Label(signup_window, image=background)
bglabel.grid()

frame = Frame(signup_window)
frame.place(x=600,y=100)

heading = Label(frame,text='CREATE AN ACCOUNT', font=('ariel',20,'bold'),fg='red')
heading.grid(row=0,column=0,padx=10,pady=10)

emaillabel=Label(frame,text='Email',font=('ariel',10),fg='red')
emaillabel.grid(row=1,column=0,padx=10,pady=2, sticky='w')

emailEntry=Entry(frame,width=40,font=('ariel',9),fg='red' )
emailEntry.grid(row=2,column=0, padx=10,pady=2, sticky='w')


userlabel=Label(frame,text='Username',font=('ariel',10),fg='red')
userlabel.grid(row=3,column=0,padx=10,pady=2, sticky='w')

userEntry=Entry(frame,width=40,font=('ariel',9),fg='red' )
userEntry.grid(row=4,column=0, padx=10,pady=2, sticky='w')


passlabel=Label(frame,text='Password',font=('ariel',10),fg='red')
passlabel.grid(row=5,column=0,padx=10,pady=2, sticky='w')

passEntry=Entry(frame,width=40,font=('ariel',9),fg='red' )
passEntry.grid(row=6,column=0, padx=10,pady=2, sticky='w')


confirm_passlabel=Label(frame,text='Confirm Password',font=('ariel',10),fg='red')
confirm_passlabel.grid(row=7,column=0,padx=10,pady=2, sticky='w')

confirm_passlabelEntry=Entry(frame,width=40,font=('ariel',9),fg='red' )
confirm_passlabelEntry.grid(row=8,column=0, padx=10,pady=2, sticky='w')

check=IntVar()
checkbox=Checkbutton(frame,text='I accept to the terms & conditions', font=('ariel',9),fg='blue'
                     , activebackground='white', activeforeground='blue', cursor='hand2', variable=check)
checkbox.grid(row=9,column=0, padx=10,pady=2, sticky='w')

signup=Button(frame, text= 'SignUp', font=('ariel', 16, 'bold'), activebackground='white',fg='red',
              activeforeground='grey', bd=1, cursor='hand2', command=connect_database)
signup.grid(row=10,column=0, padx=10,pady=10)

existacc=Label(frame, text='Already have an account', font=('arial',7),fg= 'red')
existacc.grid(row=11, column=0, padx=5,pady=5)

signin=Button(frame,text= 'Sign-in',font=('ariel',7,UNDERLINE),fg='blue', bd=0, cursor='hand2', command=login_page)
signin.place(x=220, y=347)


signup_window.mainloop()
