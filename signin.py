from tkinter import *
from PIL import ImageTk

#function part

def signup_page():
    login_window.destroy()
    import signup


def user_enter(event):
    if usernameEntry.get()=='Username':
        usernameEntry.delete(0,END)

def password_enter(event):
    if passwordEntry.get()=='Password':
        passwordEntry.delete(0,END)
#gui part
login_window = Tk()
login_window.geometry('990x660+50+50')
login_window.resizable(False, False)
login_window.title('Login Page')
bgImage = ImageTk.PhotoImage(file='backg.jpg')
bgLabel = Label(login_window,image=bgImage)
bgLabel.place(x=0, y=0)

frame=Frame(login_window, bg='black')
frame.place(x=554, y=10)

heading=Label(frame,text='     LOGIN', font=('Microsoft Yahei UI Light',27, 'bold'), bg='black', fg='firebrick1')
heading.grid(row=0, column=0, padx=10, pady=10)
logo=PhotoImage(file='user.png')
logoLabel=Label(frame, image=logo, bg='black')
logoLabel.grid(row=0, column=0, sticky='w', padx=10, pady=(10, 0))

usernameEntry=Entry(frame, width=25,font=('Microsoft Yahei UI Light', 11, 'bold'), highlightthickness=0,
                    fg='firebrick1', bg='black')
usernameEntry.grid(row=1, column=0, sticky='w', padx=55, pady=(10, 0))
usernameEntry.insert(0, 'Username')

usernameEntry.bind('<FocusIn>', user_enter)


passwordEntry=Entry(frame, width=25,font=('Microsoft Yahei UI Light', 11, 'bold'), fg='firebrick1', bg='black')
passwordEntry.grid(row=2, column=0, sticky='w', padx=55, pady=(10, 0))
passwordEntry.insert(0, 'Password')

passwordEntry.bind('<FocusIn>', password_enter)



forgetButton=Button(frame, text='Forget Password?', borderwidth=0, bg='black', activebackground='black',
                 cursor='hand2', font=('Microsoft Yahei UI Light', 9, 'bold'),fg='firebrick1', activeforeground='firebrick1')
forgetButton.grid(row=3, column=0, sticky='w', padx=55, pady=(10, 0))

loginButton=Button(frame, text='Login', font=('Open Sans', 16, 'bold'), fg='white',
                   bg='firebrick1', activeforeground='white',
                   cursor='hand2', width=15, bd=0, activebackground='black')

loginButton.grid(row=4, column=0, sticky='w', padx=55, pady=(15, 0))

orlabel=Label(frame, text='------------OR--------------', font=('Open Sans', 16), bg='black',
              fg='firebrick1')
orlabel.grid(row=5, column=0, sticky='w', padx=55, pady=(15, 0))

facebook_logo=PhotoImage(file='facebook.png')
fbLabel=Label(frame, image=facebook_logo, bg='black')
fbLabel.grid(row=6, column=0, sticky='w', padx=55, pady=(15, 0))

google_logo=PhotoImage(file='google.png')
googleLabel=Label(frame, image=google_logo, bg='black')
googleLabel.grid(row=6, column=0, sticky='w', padx=100, pady=(15, 0))

twitter_logo=PhotoImage(file='twitter.png')
twitterLabel=Label(frame, image=twitter_logo, bg='black')
twitterLabel.grid(row=6, column=0, sticky='w', padx=150, pady=(15, 0))

signupLabel=Label(frame, text="Don't have an account?" , font=('Open Sans', 9, 'bold'), bg='black'
              , fg='firebrick1')
signupLabel.grid(row=7, column=0, sticky='w', padx=50, pady=(15, 0))

newButton=Button(frame, text='Create New One', font=('Open Sans', 8, 'bold underline'), fg='blue',
                   bg='black', activeforeground='blue', cursor='hand2', bd=0, activebackground='black', command=signup_page)

newButton.grid(row=8, column=0, sticky='w', padx=120, pady=(15, 0))




login_window.mainloop()