from tkinter import *
from tkinter.scrolledtext import ScrolledText
import paramiko
import time
import os
import sys
from openpyxl.styles.borders import Side

fields = 'IP Address :','Login :', 'Password :', 'Command :'
def Login(entries,root):
    text=[]
    for entry in entries:
        text.append(entry[1].get())
    print(text)
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(text[0], username=text[1], password=text[2])
    stdin, stdout, stderr = ssh.exec_command(text[3])
    u=stdout.readlines()
    output = ''.join(u)
    sc=ScrolledText(root)
    sc.pack(side=LEFT)
    sc.insert(END, output)
    
    
def makeform(root, fields):
    entries = []
    for field in fields:
        row = Frame(root)
        lab = Label(row, width=15, text=field, anchor='w')
        ent = Entry(row)
        row.pack(side=TOP, fill=X, padx=5, pady=5)
        lab.pack(side=LEFT)
        ent.pack(side=LEFT, expand=NO, fill=X)
        entries.append((field, ent))
    la = Label(root, width=15, text="Output :", anchor='w')
    la.pack(side=LEFT)
    return entries

if __name__ == '__main__':
    root = Tk()
    root.title("SSH Login Application")
    ents = makeform(root, fields)
    root.bind('<Return>', (lambda event, e=ents: Login(e))) 
    b1 = Button(root, text='Login',command=(lambda e=ents:Login(e,root)))
    b1.pack(side=LEFT, padx=5, pady=5)
    b2 = Button(root, text='Quit', command=root.quit)
    b2.pack(side=LEFT, padx=5, pady=5)
    root.mainloop()