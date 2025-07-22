from tkinter import *
import os

window=Tk()
window.title('Dashboard')
window.geometry('1270x668+0+0')
window.config(bg='white')
window.resizable(0,0)
image_path = os.path.join(os.path.dirname(__file__), 'images', 'icon.png')
bg_Image = PhotoImage(file=image_path)
titleLabel=Label(window, image=bg_Image,compound=LEFT,text=' Inventory Management System', font=('times new roman',40,'bold'),bg='black', fg='white', anchor='w', padx=20)
titleLabel.place(x=0,y=0,relwidth=1)

logoutButton=Button(window,text='Logout', font=('times new roman',20,'bold'),fg='black')
logoutButton.place(x=1100, y=10,)

subLabel=Label(window, text= 'Welcome Admin\t\t Date: 07/22/2025\t\t Time: 12:45:00 PM', font=('times new roman',15), bg="#4d636d", fg ='white')
subLabel.place(x=0,y=70,relwidth=1)

leftFrame=Frame(window)
leftFrame.place(x=0,y=102,width=200,height=555)

logoimage_path = os.path.join(os.path.dirname(__file__), 'images', 'image.png')
logoImage=PhotoImage(file=logoimage_path)
imageLabel=Label(leftFrame,image=logoImage)
imageLabel.grid(row=0,column=0)

window.mainloop()