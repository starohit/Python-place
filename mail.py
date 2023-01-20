import tkinter as tk

root = tk.Tk()
root.title('Registration Form')
root.geometry("500x400")
root.configure(background='light green')
w = tk.Label(root, text='Welcome to Nimbletech', bg='light green')
w.grid(row=0,column=1)
tk.Label(root, text='Name(*)',background='light green').grid(row=1)
tk.Label(root, text='Mailid(*)',background='light green').grid(row=2)
tk.Label(root, text='Mobile No.(*)',background='light green').grid(row=3)
name_filed=tk.Entry(root)
name_filed.grid(row=1,column=1 ,ipadx="100",pady=4)
mail_filed=tk.Entry(root)
mail_filed.grid(row=2,column=1 ,ipadx="100",pady=4)
mob_filed=tk.Entry(root)
mob_filed.grid(row=3,column=1, ipadx="100",pady=4)
v = tk.StringVar()
tk.Label(root, text='Sex',background='light green').grid(row=4)
radio_male=tk.Radiobutton(root, text='Male', 
variable=v, value='Male',bg='light green').grid(row=4,column=1)
radio_female=tk.Radiobutton(root, text='Female', variable=v, value='Female',bg='light green').grid(row=5,column=1)
tk.Label(root, text='Select Subject',background='light green').grid(row=6)
opt=tk.StringVar(root)
opt.set('ML')
sub_optn=tk.OptionMenu(root, opt, "Python", "Java", "Oracle","Android","SQL", "ML","Data Science").grid(row=6,column=1,pady=3)
chk = tk.IntVar()
chk_btn=tk.Checkbutton(root, text='I agree T&C', variable=chk,bg='light green').grid()
data={}
def clicked():
    name=name_filed.get()
    mail=mail_filed.get()
    mob=mob_filed.get()
    tnc=chk.get()
    gend=v.get()
    sub=opt.get()
    global messageVar
    if tnc!=1:
        msg='Please agree T&C!'
        messageVar.config(text=msg,bg='red')
    else:
        if name =='' or mail =='' or mob =='' or gend =='' or sub =='':
            msg = 'All fields are Mandatory'
            messageVar.config(text=msg,bg='red')
        else:
            msg = 'Registered'
            messageVar.config(text=msg,bg=
            'green')
            # name_filed.delete(0, 'end')
            data.update({'name':name,'mail':mail,'mob':mob,'gender':gend,'sub':sub})
            print(data)
button = tk.Button(root, text='Submit',height=1, width=10,bg='green', command=clicked)
button.grid(column=1,pady=10)
button = tk.Button(root, 
text='Cancel',height=1, width=10,bg='red', 
command=root.destroy)
button.grid(column=1,pady=5)
messageVar = tk.Message(root, text='', width=100)
messageVar.config(bg='light green')
messageVar.grid(row=10, column=0)
root.mainloop()