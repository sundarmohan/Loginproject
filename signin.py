import tkinter
from tkinter import *

import PIL
from PIL import ImageTk



#Functionality part
def register():
    login_window.destroy()
    import signup


def user_click(event):
    if usernameEntry.get().lower()=='username':
        usernameEntry.delete(0,END)

def pswd_click(event):
    if passwordEntry.get().lower()=='password':
        passwordEntry.delete(0,END)

def hide():
    openeye.config(file=r"C:\Users\sunda\PycharmProjects\Loginproject\venv\bg\closeeye.png")
    passwordEntry.config(show='*')
    eyebutton.config(command=show)

def show():
    openeye.config(file=r"C:\Users\sunda\PycharmProjects\Loginproject\venv\bg\openeye.png")
    passwordEntry.config(show='')
    eyebutton.config(command=hide)


#GUPart
login_window= Tk()
login_window.geometry('900x600+50+50')
login_window.resizable(0,0)

login_window.title("Login page")

bgimage=ImageTk.PhotoImage(file=r"C:\Users\sunda\PycharmProjects\Loginproject\venv\bg\bgp.jpg")

bglabel=Label(login_window,image=bgimage)
bglabel.place(x=0,y=0)

heading = Label(login_window,text='USER LOGIN', font=('ariel',25,'bold'),fg='red')
heading.place(x=210,y=200)

usernameEntry=Entry(login_window,width=40,font='ariel',fg= 'red')
usernameEntry.place(x=180,y=255)
usernameEntry.insert(0,'username')
usernameEntry.bind('<FocusIn>', user_click)

Frame(login_window,width=360,height=2, bg='blue').place (x=180,y=275)

passwordEntry=Entry(login_window,width=40,font='ariel',fg= 'red')
passwordEntry.place(x=180,y=300)
passwordEntry.insert(0,'password')
passwordEntry.bind('<FocusIn>', pswd_click)


openeye=PhotoImage(file=r'C:\Users\sunda\PycharmProjects\Loginproject\venv\bg\openeye.png')
eyebutton=Button(login_window,image=openeye,bg='white',width=15,height=15,bd=0, cursor='hand2',
                 command=hide)
eyebutton.place(x=500, y=300)

forgetbutton=Button(login_window,text='forgot password?', font=('ariel', 9, ),activebackground='white',bd=0, cursor='hand2' )
forgetbutton.place(x=400,y=340)

loginbutton=Button(login_window, text= 'Login', font=('ariel', 16, 'bold'), activebackground='white',fg='red', activeforeground='grey', bd=0, cursor='hand2')
loginbutton.place(x=300,y=400)



orlabel=Label(login_window,text ='---------------------OR------------------', font=('arial',19 ), fg= 'red', bg='white')
orlabel.place(x=150,y=450)


signuplabel=Label(login_window,text ="Don't have an account?", font=('arial',10 ), fg= 'red', bg='white')
signuplabel.place(x=150,y=500)

createlabel=Button(login_window,text='create an account', font=('ariel', 10, UNDERLINE ),fg='blue',
                   activebackground='white',bd=0, cursor='hand2', command=register)
createlabel.place(x=330,y=500)




login_window.mainloop()