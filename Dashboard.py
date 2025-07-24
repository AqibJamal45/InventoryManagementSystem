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
imageLabel.pack()

menuLabel=Label(leftFrame,text='Menu', font=('times new roman',20), bg = '#4d636d')
menuLabel.pack(fill=X)

manimage_path = os.path.join(os.path.dirname(__file__), 'images', 'man.png')
manImage=PhotoImage(file=manimage_path)
manButton=Button(leftFrame,image=manImage,compound=LEFT,text=' Employees',font=('times new roman',20,'bold'), anchor='w', padx=10)
manButton.pack(fill=X)

supplierImage_path = os.path.join(os.path.dirname(__file__), 'images', 'supplier.png')
supplierImage=PhotoImage(file=supplierImage_path)
supplierButton=Button(leftFrame,image=supplierImage,compound=LEFT,text=' Suppliers',font=('times new roman',20,'bold'), anchor='w', padx=10)
supplierButton.pack(fill=X)

categoryImage_path = os.path.join(os.path.dirname(__file__), 'images', 'category.png')
categoryImage=PhotoImage(file=categoryImage_path)
categoryButton=Button(leftFrame,image=categoryImage,compound=LEFT,text=' Category',font=('times new roman',20,'bold'), anchor='w', padx=10)
categoryButton.pack(fill=X)

productImage_path = os.path.join(os.path.dirname(__file__), 'images', 'box.png')
productImage=PhotoImage(file=productImage_path)
productButton=Button(leftFrame,image=productImage,compound=LEFT,text=' Products',font=('times new roman',20,'bold'), anchor='w', padx=10)
productButton.pack(fill=X)

salesImage_path = os.path.join(os.path.dirname(__file__), 'images', 'funds.png')
salesImage=PhotoImage(file=salesImage_path)
salesButton=Button(leftFrame,image=salesImage,compound=LEFT,text=' Sales',font=('times new roman',20,'bold'), anchor='w', padx=10)
salesButton.pack(fill=X)

exitImage_path = os.path.join(os.path.dirname(__file__), 'images', 'exit.png')
exitImage=PhotoImage(file=exitImage_path)
exitButton=Button(leftFrame,image=exitImage,compound=LEFT,text=' Exit',font=('times new roman',20,'bold'), anchor='w', padx=10)
exitButton.pack(fill=X)

empFrame=Frame(window,bg="#2C3E50",bd=3,relief=RIDGE)
empFrame.place(x=400,y=125,height=170,width=280)
empImage_path = os.path.join(os.path.dirname(__file__), 'images', 'teamwork.png')
empImage=PhotoImage(file=empImage_path)
empImageLabel=Label(empFrame,image=empImage,bg="#2C3E50")
empImageLabel.pack(pady=10)

empLabel=Label(empFrame,text='Total Employees',bg="#2C3E50",fg='white',font=('times new roman', 15,'bold'))
empLabel.pack()

empCountLabel=Label(empFrame,text='0',bg="#2C3E50",fg='white',font=('times new roman', 30,'bold'))
empCountLabel.pack()

supFrame=Frame(window,bg="#68205C",bd=3,relief=RIDGE)
supFrame.place(x=800,y=125,height=170,width=280)
supImage_path = os.path.join(os.path.dirname(__file__), 'images', 'sup.png')
supImage=PhotoImage(file=supImage_path)
supImageLabel=Label(supFrame,image=supImage,bg="#68205C")
supImageLabel.pack(pady=10)

supLabel=Label(supFrame,text='Total Suppliers',bg="#68205C",fg='white',font=('times new roman', 15,'bold'))
supLabel.pack()

supCountLabel=Label(supFrame,text='0',bg="#68205C",fg='white',font=('times new roman', 30,'bold'))
supCountLabel.pack()

catFrame=Frame(window,bg="#758619",bd=3,relief=RIDGE)
catFrame.place(x=400,y=310,height=170,width=280)
catImage_path = os.path.join(os.path.dirname(__file__), 'images', 'menu.png')
catImage=PhotoImage(file=catImage_path)
catImageLabel=Label(catFrame,image=catImage,bg="#758619")
catImageLabel.pack(pady=10)

catLabel=Label(catFrame,text='Total Categories',bg="#758619",fg='white',font=('times new roman', 15,'bold'))
catLabel.pack()

catCountLabel=Label(catFrame,text='0',bg="#758619",fg='white',font=('times new roman', 30,'bold'))
catCountLabel.pack()

prodFrame=Frame(window,bg="#B77615",bd=3,relief=RIDGE)
prodFrame.place(x=800,y=310,height=170,width=280)
prodImage_path = os.path.join(os.path.dirname(__file__), 'images', 'cubes.png')
prodImage=PhotoImage(file=prodImage_path)
prodImageLabel=Label(prodFrame,image=prodImage,bg="#B77615")
prodImageLabel.pack(pady=10)

prodLabel=Label(prodFrame,text='Total Products',bg="#B77615",fg='white',font=('times new roman', 15,'bold'))
prodLabel.pack()

prodCountLabel=Label(prodFrame,text='0',bg="#B77615",fg='white',font=('times new roman', 30,'bold'))
prodCountLabel.pack()

salFrame=Frame(window,bg="#BC2727",bd=3,relief=RIDGE)
salFrame.place(x=600,y=495,height=170,width=280)
salImage_path = os.path.join(os.path.dirname(__file__), 'images', 'trend.png')
salImage=PhotoImage(file=salImage_path)
salImageLabel=Label(salFrame,image=salImage,bg="#BC2727")
salImageLabel.pack(pady=10)

salLabel=Label(salFrame,text='Total Sales',bg="#BC2727",fg='white',font=('times new roman', 15,'bold'))
salLabel.pack()

salCountLabel=Label(salFrame,text='0',bg="#BC2727",fg='white',font=('times new roman', 30,'bold'))
salCountLabel.pack()

window.mainloop()