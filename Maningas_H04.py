import tkinter as tk

window = tk.Tk()
window.title("Profile Builder")
# window.geometry("600x300")
window.configure(bg="light blue")

title_label = tk.Label(window, text="Profile Builder",font=("Arial", 15, "bold"), bg="lightblue")
title_label.grid(row=0)

frame = tk.Frame(window, bg="light green", bd=5)
frame.grid(row=1)

first_name = tk.Entry(frame, width=20)
first_name.grid(row=0, column=0, padx=15)
first = tk.Label(frame, text="First Name", font=("Arial", 11, "italic"), bg="lightgreen")
first.grid(row=1, column=0)

middle_name = tk.Entry(frame, width=20)
middle_name.grid(row=0, column=1, padx=15)
middle = tk.Label(frame, text="Middle Name", font=("Arial", 11, "italic"), bg="lightgreen")
middle.grid(row=1, column=1)

last_name = tk.Entry(frame, width=20)
last_name.grid(row=0, column=2, padx=15)
last = tk.Label(frame, text="Last Name", font=("Arial", 11, "italic"), bg="lightgreen")
last.grid(row=1, column=2)

birth_year = tk.Entry(frame, width=20)
birth_year.grid(row=2, column=0, padx=15)
birth = tk.Label(frame, text="Birth Year", font=("Arial", 11, "italic"), bg="lightgreen")
birth.grid(row=3, column=0)

result_age = tk.Label(frame, text="Calculating Age.......",font=("Arial", 11, "bold"), bg="lightgreen")
result_age.grid(row=3, column =1)

gender = tk.Label(frame, text="Gender", font=("Arial", 11, "italic"), bg="lightgreen")
gender.grid(row=4, column=0)

female = tk.Radiobutton(frame, text="Female", value=0)
female.grid(row=4, column=1)

male = tk.Radiobutton(frame, text="Male", value=1)
male.grid(row=4, column=2)

button = tk.Button(window, text="Submit", font=("Arial", 11), bg="lightgreen")
button.grid(row=7)

new_window = tk.Toplevel()

window.mainloop()

