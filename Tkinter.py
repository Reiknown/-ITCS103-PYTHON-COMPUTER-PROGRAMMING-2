import tkinter as tk

window = tk.Tk()
window.title("TESTINGS")
window.resizable(True, True)
window.configure(bg="light blue", cursor="heart")

menu_bar = tk.Menu(window)
window.config(menu=menu_bar)

# 1. File Menu
file_menu = tk.Menu(menu_bar, tearoff=0)
file_menu.add_command(label="New")
file_menu.add_command(label="Open")
file_menu.add_command(label="Exit", command=window.quit)
menu_bar.add_cascade(label="File", menu=file_menu)

# 2. View Menu
view_menu = tk.Menu(menu_bar, tearoff=1)
view_menu.add_separator()
view_menu.add_command(label="Zoom")
view_menu.add_command(label="Resize")
menu_bar.add_cascade(label="View", menu=view_menu)

# 3. Edit Menu
edit_menu = tk.Menu(menu_bar, tearoff=1)
edit_menu.add_separator()
edit_menu.add_command(label="front")
edit_menu.add_command(label="back")
menu_bar.add_cascade(label="Edit", menu=edit_menu)



header = tk.Label(window, text="Profile Builder", font=("Poppins", 21, "bold"), bg="lightblue")
header.grid(row=0, column=0, columnspan=3)


user_lbl = tk.Label(window, text="Username", font=("Poppins", 11), bg="lightblue")
user_lbl.grid(row=1,column=0, columnspan=3)

user_entry = tk.Entry(window, width=20)
user_entry.grid(row=2,column=0, columnspan=3)


pass_lbl = tk.Label(window, text="Password", font=("Poppins", 11), bg="lightblue")
pass_lbl.grid(row=3, column=0, columnspan=3)

pass_entry = tk.Entry(window, width=20, show="*")
pass_entry.grid(row=4, column=0, columnspan=3)

# Main Frame
frame = tk.Frame(window, bg="lightblue", relief="solid", bd=1)
frame.grid(row=5, column=0, columnspan=3, padx=10, pady=10)

# First Name
f_entry=tk.Entry(frame, width=25, )
f_entry.grid(row=0, column=0, padx=5, pady=5)

f_label=tk.Label(frame, text="First Name", font=("Poppins", 11, "italic"), bg="light blue")
f_label.grid(row=1, column=0)

# Middle Name
m_entry=tk.Entry(frame, width=25, )
m_entry.grid(row=0, column=1, padx=5, pady=5)

m_label=tk.Label(frame, text="Middle Name", font=("Poppins", 11, "italic"), bg="lightblue")
m_label.grid(row=1, column=1)

# Last Name
l_entry=tk.Entry(frame, width=25, )
l_entry.grid(row=0, column=2, padx=5, pady=5)

l_label=tk.Label(frame, text="Last Name", font=("Poppins", 11, "italic"), bg="lightblue")
l_label.grid(row=1, column=2)


def compute_age(event):
    birth_year = b_entry.get()
    age = 2026 - int(birth_year)
    c_label['text'] = f"Age: {age}"
    
    
# Birth Year
b_entry=tk.Entry(frame, width=25)
b_entry.grid(row=2, column=0, padx=5, pady=5)
b_entry.bind("<Return>", compute_age)

b_label=tk.Label(frame, text="Birth Year", font=("Poppins", 11, "italic"), bg="lightblue")
b_label.grid(row=3, column=0)

# Computing Age
c_label = tk.Label(frame, text="Computing Age...", font=("Poppins", 16, "italic"), bg="lightblue")
c_label.grid(row=2, column=1, rowspan=2, columnspan=2)

# Gender
g_label=tk.Label(frame, text="Gender", font=("Poppins", 11, "italic"), bg="lightblue")
g_label.grid(row=4, column=0)

# RButton
gender_button = tk.IntVar()
male_button = tk.Radiobutton(frame, text= "Male", bg="lightblue", variable=gender_button, value=1)
male_button.grid(row=4, column=1)

fmale_button = tk.Radiobutton(frame, text= "Female", bg="lightblue", variable=gender_button, value=0)
fmale_button.grid(row=4, column=2)

# List Box
list_label = tk.Label(frame, text="Languages", font=("Poppins", 11, "italic"), bg="white")
list_label.grid(row=5, column=0, columnspan=3)

v_scroll = tk.Scrollbar(frame)
h_scroll = tk.Scrollbar(frame, orient="horizontal")

listbox = tk.Listbox(frame, selectmode="multiple", yscrollcommand=v_scroll.set, xscrollcommand=h_scroll.set)
listbox.grid(row=6, column=0, columnspan=3, pady=5, sticky="n")

v_scroll.grid(row=6, column=3, sticky="ns")
v_scroll['command'] = listbox.yview

h_scroll.grid(row=7, column=0, columnspan=3, sticky="we")
h_scroll['command'] = listbox.xview

listbox.insert(0, "Python")
listbox.insert(1, "Java")
listbox.insert(2, "JavaScript")
listbox.insert(3, "C")
listbox.insert(4, "C++")
listbox.insert(5, "C#")
listbox.insert(6, "TypeScript")
listbox.insert(7, "Go")
listbox.insert(8, "PHP")
listbox.insert(9, "SQL")
listbox.insert(10, "Kotlin")
listbox.insert(11, "Swift")
listbox.insert(12, "Rust")
listbox.insert(13, "Dart")
listbox.insert(14, "Ruby")
listbox.insert(15, "Common Lisp Object System")


# CButton
c_button = tk.IntVar()
remember = tk.Checkbutton(window, text= "Remember Me", bg="lightblue", variable=c_button, onvalue=1)
remember.grid(row=8, column=0, columnspan=3)

# Button
button = tk.Button(window, text="Submit", font=("Poppins", 13, "bold"), width=10, activebackground="green")
button.grid(row = 9, column=0, columnspan=3, pady=5)


window.mainloop()
