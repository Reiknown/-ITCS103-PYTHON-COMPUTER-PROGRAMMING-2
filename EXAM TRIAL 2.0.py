import tkinter as tk


def register():
    t = tk.Toplevel(window)
    t.title('Maningas HO Exam')
    t.config(bg='white')
    
    s_lbl = tk.Label(t, text='Register', font=('arial', 9, 'bold'), bg='white')
    s_lbl.grid(row=0, column=0, columnspan=2)

    u_lbl = tk.Label(t, text='Username:', font=('arial', 9, 'bold'), bg='white')
    u_lbl.grid(row=1, column=0)

    u_ent = tk.Entry(t, width=20)
    u_ent.grid(row=1, column=1)

    p_lbl = tk.Label(t, text='Password:', font=('arial', 9, 'bold'), bg='white')
    p_lbl.grid(row=2, column=0)

    p_ent = tk.Entry(t, width=20, show='*')
    p_ent.grid(row=2, column=1)

    show_var = tk.IntVar()

    def show():
        if show_var.get() == 1:
            p_ent.config(show='')
        else:
            p_ent.config(show='*')

    sp_cbt = tk.Checkbutton(t, text='See Password', bg='white', variable=show_var, command=show)
    sp_cbt.grid(row=3, column=1)

    
    def reg():
        username = u_ent.get()
        password = p_ent.get()
        if len(password) >= 8:
            s_lbl.config(text='You have succesfully registered!', fg='white', bg='green')
            t.config(bg='green')
            u_lbl.config(bg='green')
            p_lbl.config(bg='green')
        else:
            s_lbl.config(text='Password must be 8+ characters!', fg='white', bg='red')
            t.config(bg='red')
            u_lbl.config(bg='red')
            p_lbl.config(bg='red')


    r_btn = tk.Button(t, text='Register', bg='blue', width=20, command=reg)
    r_btn.grid(row=4, column=0, columnspan=2)



def login():
    t2 = tk.Toplevel(window)
    t2.title('Maningas HO Exam')
    t2.config(bg='white')
    
    s2_lbl = tk.Label(t2, text='', font=('arial', 9, 'bold'), bg='white')
    s2_lbl.grid(row=0, column=0, columnspan=2)

    log_lbl = tk.Label(t2, text='Log In', font=('arial', 13, 'bold'), bg='white')
    log_lbl.grid(row=1, column=0, columnspan=2)

    u2_lbl = tk.Label(t2, text='Username:', font=('arial', 9, 'bold'), bg='white')
    u2_lbl.grid(row=2, column=0)

    u2_ent = tk.Entry(t2, width=20)
    u2_ent.grid(row=2, column=1)

    p2_lbl = tk.Label(t2, text='Password:', font=('arial', 9, 'bold'), bg='white')
    p2_lbl.grid(row=3, column=0)

    p2_ent = tk.Entry(t2, width=20, show='*')
    p2_ent.grid(row=3, column=1)


    show_var = tk.IntVar()
    def show2():
        if show_var.get() == 1:
            p2_ent.config(show='')
        else:
            p2_ent.config(show='*')

    sp2_cbt = tk.Checkbutton(t2, text='See Password', bg='white', variable=show_var, command=show2)
    sp2_cbt.grid(row=4, column=1)


    log_btn = tk.Button(t2, text='Log In', bg='green', width=20)
    log_btn.grid(row=5, column=0, columnspan=2)












window = tk.Tk()
window.title('Maningas HO Exam')
window.config(bg='white')

w_lbl = tk.Label(text='Welcome!', font=('arial', 16, 'bold'), bg='white')
w_lbl.grid(row=0, column=0, columnspan=3)

r_btn = tk.Button(text='Register', font=('arial', 16, 'bold'), bg='blue', width=20, command=register)
r_btn.grid(row=1, column=0, columnspan=3, pady=5)

l_btn = tk.Button(text='Log In', font=('arial', 16, 'bold'), bg='green', width=20, command=login)
l_btn.grid(row=2, column=0, columnspan=3, pady=5)

window.mainloop()