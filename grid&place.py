import tkinter as franz

window = franz.Tk()
# window.title("Daddy Rob")
# window.geometry("100x100")
# window.config(bg="light pink")
# window.resizable(True, True)

#place
# label = franz.Label(window, text="Welcome User").place(x=20,y=7)
# user_lbl = franz.Label(window, text="Username").place(x=10,y=30)
# user_entry=franz.Label(window).place(x=35,y=25)


#grid
welcome = franz.Label(window, text="Welcome").grid(column=0,row=0)

label = franz.Label(window, text="User Form")
label.grid(column=3, row= 0, columnspan= 3)

#Username
user_lbl = franz.Label(window, text="Username")
user_lbl.grid(column=2, row= 1, columnspan=1)
#User_entry
u_entry = franz.Entry(window)
u_entry.grid(column=3, row=1)
#password
pass_lbl = franz.Label(window, text="Password")
pass_lbl.grid(column=2, row=2, columnspan=1)
#pass_entry
pass_entry = franz.Entry(window)
pass_entry.grid(column=3, row=2)
#buttown
button = franz.Button(window, text= "Log In")
button.grid(column=3, row=3, columnspan=1)

def on_enter(event):
    button ['bg'] = 'pink'
    
def on_leave(event):
    button["bg"] = 'blue'

button.bind("<Enter>", on_enter)
button.bind("<Leave>", on_leave)

window.mainloop()