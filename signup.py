from tkinter import *
from tkinter import messagebox
from PIL import ImageTk
import mysql.connector

def clear():
    emailEntry.delete(0,END)
    usernameEntry.delete(0,END)
    passwordEntry.delete(0,END)
    conf_passwordEntry.delete(0,END)
    check.set(0)


def connect_database():
    if emailEntry.get()=='' or usernameEntry.get()=='' or passwordEntry.get()=='' or conf_passwordEntry.get()=='':
        messagebox.showerror('Error', 'All Fields Are Required')
    elif passwordEntry.get() != conf_passwordEntry.get():
        messagebox.showerror('Error', 'Wrong Password')
    elif check.get()==0:
        messagebox.showerror('Error', 'Please Accept Terms & Conditions')
    else:
        try:
            mydb = mysql.connector.connect(host='localhost', user='root', password='1234')
            print(mydb.connection_id)
            mycursor = mydb.cursor()
        except:
            messagebox.showerror('Error', 'Database Connectivity Issue, Please Try Again')
            return
        try:
            query='create database userdata'
            mycursor.execute(query)
            query='use userdata'
            mycursor.execute(query)
            query= 'create table data(id int auto_increment primary key not null, email varchar(50),username varchar(100), password varchar(20))'
            mycursor.execute(query)
        except:
            mycursor.execute('user userdata')

        query='insert into data(email,username,password)values(%s,%s,%s)'
        mycursor.execute(query,(emailEntry.get(),usernameEntry.get(),passwordEntry.get()))
        mydb.commit()
        mysql.close()
        messagebox.showinfo('Success', 'Registration is successful')
        clear()
        signup_window.destroy()
        import signin


def login_page():
    signup_window.destroy()
    import signin
signup_window=Tk()
signup_window.title('SignUp Page')
signup_window.resizable(False, False)

background=PhotoImage(file='background1.png')

bgLabel=Label(signup_window, image=background)
bgLabel.grid()

frame=Frame(signup_window, bg='grey')
frame.place(x=554, y=10)

heading=Label(frame,text='CREATE AN ACCOUNT', font=('Microsoft Yahei UI Light',17, 'bold')
              , bg='grey', fg='black')
heading.grid(row=0, column=0, padx=10, pady=10)

emailLabel=Label(frame,text='Email', font=('Microsoft Yahei UI Light',15, 'bold'), bg='grey', fg='black')
emailLabel.grid(row=1, column=0, sticky='w', padx=25, pady=(10, 0))

emailEntry=Entry(frame,width=30, font=('Microsoft Yahei UI Light', 10, 'bold')
                 , fg='black', bg='white')
emailEntry.grid(row=2, column=0, sticky='w', padx=25, pady=(10, 0))


usernameLabel=Label(frame,text='Username', font=('Microsoft Yahei UI Light',15, 'bold'), bg='grey', fg='black')
usernameLabel.grid(row=3, column=0, sticky='w', padx=25, pady=(10, 0))

usernameEntry=Entry(frame,width=30, font=('Microsoft Yahei UI Light', 10, 'bold')
                 , fg='black', bg='white')
usernameEntry.grid(row=4, column=0, sticky='w', padx=25, pady=(10, 0))


passwordLabel=Label(frame,text='Password', font=('Microsoft Yahei UI Light',15, 'bold'), bg='grey', fg='black')
passwordLabel.grid(row=5, column=0, sticky='w', padx=25, pady=(10, 0))

passwordEntry=Entry(frame,width=30, font=('Microsoft Yahei UI Light', 10, 'bold')
                 , fg='black', bg='white')
passwordEntry.grid(row=6, column=0, sticky='w', padx=25, pady=(10, 0))


conf_passwordLabel=Label(frame,text='Confirm Password', font=('Microsoft Yahei UI Light',15, 'bold'), bg='grey', fg='black')
conf_passwordLabel.grid(row=7, column=0, sticky='w', padx=25, pady=(10, 0))

conf_passwordEntry=Entry(frame,width=30, font=('Microsoft Yahei UI Light', 10, 'bold')
                 , fg='black', bg='white')
conf_passwordEntry.grid(row=8, column=0, sticky='w', padx=25, pady=(10, 0))

check=IntVar()

terms_conditions=Checkbutton(frame, text='I agree to the Terms & Conditions', font=('Microsoft Yahei UI Light', 8,'bold')
                                , fg='black', bg='grey', activeforeground='black', activebackground='grey'
                             , cursor='hand2', variable=check)
terms_conditions.grid(row=9, column=0, padx=15, pady=10)

signupButton=Button(frame, text='SignUp', font=('Open Sans', 16,'bold'), bd=0, bg='black'
                    , fg='white', activeforeground='white', activebackground='blue', width=17, command=connect_database)
signupButton.grid(row=10, column=0, pady=10)

alreadyaccount=Label(frame, text="Don't have an account?" , font=('Open Sans', 9, 'bold'), bg='grey'
              , fg='black')
alreadyaccount.grid(row=11, column=0, sticky='w', padx=25, pady=10)

loginButton=Button(frame, text='Log in', font=('Open Sans', 9, 'bold underline'), fg='black',
                   bg='grey', activeforeground='blue', cursor='hand2', bd=0, activebackground='white'
                   , command=login_page)

loginButton.place(x=190, y=438)

signup_window.mainloop()