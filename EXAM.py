import tkinter as tk

window = tk.Tk()
window.title('Maningas HO Exam')
window.configure(bg='white')

data = {"username": "", "password": ""}

# REGISTER BUTTON -----------------------------------------------------------------------------
def register():
    t = tk.Toplevel(window)
    t.config(bg='white')

    s_lbl = tk.Label(t, text='', font=('arial', 9, 'bold'), fg='white', bg='white')
    s_lbl.grid(row=0, column=0, columnspan=2)

    header = tk.Label(t, text='Register', font=('arial', 13, 'bold'), bg='white')
    header.grid(row=1, column=0, columnspan=2)

    u_lbl = tk.Label(t, text='Username:', font=('arial', 9, 'bold'), bg='white')
    u_lbl.grid(row=2, column=0)

    u_entry = tk.Entry(t, width=20)
    u_entry.grid(row=2, column=1)

    p_lbl = tk.Label(t, text='Password:', font=('arial', 9, 'bold'), bg='white')
    p_lbl.grid(row=3, column=0)

    p_entry = tk.Entry(t, width=20, show='*')
    p_entry.grid(row=3, column=1)


    show_var = tk.IntVar()
    def show():
        if show_var.get() == 1:
            p_entry.config(show='')
        else:
            p_entry.config(show='*')

    sp_btn = tk.Checkbutton(t, text='See Password', variable=show_var, bg='white', command=show)
    sp_btn.grid(row=4, column=1)


    def reg():
        username = u_entry.get()
        password = p_entry.get()

        if len(password) >= 8:
            data["username"] = username
            data["password"] = password


            s_lbl.config(text='You have succesfully registered!', bg='green')
            t.config(bg='green')
            header.config(bg='green')
            u_lbl.config(bg='green')
            p_lbl.config(bg='green')
        else:
            s_lbl.config(text='Password must be 8+ characters!', bg='red')
            t.config(bg='red')
            header.config(bg='red')
            u_lbl.config(bg='red')
            p_lbl.config(bg='red')

    reg_btn = tk.Button(t, text='Register', bg='blue', width=15, height=1, command=reg)
    reg_btn.grid(row=5, column=0, columnspan=2)



# LOG IN BUTTON -------------------------------------------------------------------------------------
def login():
    t = tk.Toplevel(window)
    t.config(bg='white')

    s_lbl = tk.Label(t, text='', font=('arial', 9, 'bold'), fg='white', bg='white')
    s_lbl.grid(row=0, column=0, columnspan=2)

    header = tk.Label(t, text='Log In', font=('arial', 13, 'bold'), bg='white')
    header.grid(row=1, column=0, columnspan=2)

    u_lbl = tk.Label(t, text='Username:', font=('arial', 9, 'bold'), bg='white')
    u_lbl.grid(row=2, column=0)

    u_entry = tk.Entry(t, width=20)
    u_entry.grid(row=2, column=1)

    p_lbl = tk.Label(t, text='Password:', font=('arial', 9, 'bold'), bg='white')
    p_lbl.grid(row=3, column=0)

    p_entry = tk.Entry(t, width=20, show='*')
    p_entry.grid(row=3, column=1)


    show_var = tk.IntVar()
    def show():
        if show_var.get() == 1:
            p_entry.config(show='')
        else:
            p_entry.config(show='*')

    sp_btn = tk.Checkbutton(t, text='See Password', variable=show_var, bg='white', command=show)
    sp_btn.grid(row=4, column=1)
    
    def log():
        current_user = u_entry.get()
        current_pass = p_entry.get()
        
        # Check if it matches our dictionary and ensures it's not empty!
        if current_user == data["username"] and current_pass == data["password"] and data["username"] != "":
            s_lbl.config(text='Log in successful!', bg='green')
            t.config(bg='green')
            header.config(bg='green')
            u_lbl.config(bg='green')
            p_lbl.config(bg='green')
        else:
            s_lbl.config(text='Incorrect Username or Password!', bg='red')
            t.config(bg='red')
            header.config(bg='red')
            u_lbl.config(bg='red')
            p_lbl.config(bg='red')

    log_btn = tk.Button(t, text='Log In', bg='green', width=15, height=1, command=log)
    log_btn.grid(row=5, column=0, columnspan=2)


# MAIN WINDOW ---------------------------------------------------------------------------------------
w_lbl = tk.Label(window, text='Welcome!', font=('arial', 16, 'bold'), bg='white')
w_lbl.grid(row=0, column=0, columnspan=3)

r_btn = tk.Button(window, text='Register', font=('arial', 16, 'bold'), bg='blue', width=20, command=register)
r_btn.grid(row=1, column=0, columnspan=3, pady=5)

l_btn = tk.Button(window, text='Log In', font=('arial', 16, 'bold'), bg='green', width=20, command=login)
l_btn.grid(row=2, column=0, columnspan=3, pady=5)




window.mainloop()