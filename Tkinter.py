import tkinter as tk

window = tk.Tk()
window.title("TESTINGS")
window.resizable(True, True)
window.configure(bg="light blue", cursor="heart")

header = tk.Label(window, text="Profile Builder", font=("Poppins", 21, "bold"), bg="lightblue")
header.grid(row=0, column=0, columnspan=3)

# Main Frame
frame = tk.Frame(window, bg="lightblue", relief="solid", bd=1)
frame.grid(row=1, column=0, padx=10, pady=10)

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

# Birth Year
b_entry=tk.Entry(frame, width=25)
b_entry.grid(row=2, column=0, padx=5, pady=5)

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

# CButton
c_button = tk.IntVar()
rem = tk.Checkbutton(window, text= "Remember Me", bg="lightblue", variable=c_button, onvalue=1)
rem.grid(row=5, column=0, columnspan=3)

# Button
button = tk.Button(window, text="Submit", font=("Poppins", 13, "bold"), width=10, activebackground="green")
button.grid(row = 6, column=0, columnspan=3, pady=5)


window.mainloop()