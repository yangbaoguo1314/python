from tkinter import *
from tkinter.messagebox import showinfo

def reply(name):
    showinfo(title='404报错页',message='你好:%s!'%name)

top=Tk()
top.title('登陆页')
top.iconbitmap('py-blue-trans-out.ico')

Label(top,text='ENTER YOUR NAME:').pack(side=TOP)
ent = Entry(top)
ent.pack(side=TOP)
btn = Button(top,text='submit',command=(lambda :reply(ent.get())))
btn.pack(side=LEFT)
top.mainloop()
