import tkinter as tk

window = tk.Tk()
window.title("Student ID")
window.configure(bg="white")


frame = tk.Frame(window, bg="white")
frame.pack(pady=20, padx=20)


tk.Label(frame, text="First Name:", font=("Arial", 10, "bold"), bg="white").pack(anchor="w")
first_entry = tk.Entry(frame, width=40)
first_entry.pack(pady=(0, 10))

tk.Label(frame, text="Middle Name:", font=("Arial", 10, "bold"), bg="white").pack(anchor="w")
middle_entry = tk.Entry(frame, width=40)
middle_entry.pack(pady=(0, 10))

tk.Label(frame, text="Last Name:", font=("Arial", 10, "bold"), bg="white").pack(anchor="w")
last_entry = tk.Entry(frame, width=40)
last_entry.pack(pady=(0, 10))

# Birth Year & Age
tk.Label(frame, text="Birth Year (Press Enter to compute):", font=("Arial", 10, "bold"), bg="white").pack(anchor="w")
year_entry = tk.Entry(frame, width=40)
year_entry.pack(pady=(0, 5))

age_label = tk.Label(frame, text="Computed Age: --", font=("Arial", 10, "italic"), fg="gray", bg="white")
age_label.pack(anchor="w", pady=(0, 10))

# Gender
tk.Label(frame, text="Gender:", font=("Arial", 10, "bold"), bg="white").pack(anchor="w")
gender_var = tk.StringVar(value="None")

female_radio = tk.Radiobutton(frame, text="Female", variable=gender_var, value="Female", bg="white")
female_radio.pack(anchor="w")


male_radio = tk.Radiobutton(frame, text="Male", variable=gender_var, value="Male", bg="white")
male_radio.pack(anchor="w")

# Submit Button
submit_btn = tk.Button(window, text="Submit", bg="green", fg="white", font=("Arial", 11, "bold"), width=15)
submit_btn.pack(pady=20)

def on_enter(event):
    submit_btn['background'] = 'dark green'

def on_leave(event):
    submit_btn['background'] = 'green'


def change_bg():
    selected_gender = gender_var.get()
    if selected_gender == "Female":
        new_color = "pink"
    elif selected_gender == "Male":
        new_color = "light blue"
    else:
        new_color = "white"
        
    window.configure(bg=new_color)
    frame.configure(bg=new_color)
    for widget in frame.winfo_children():
        if isinstance(widget, (tk.Label, tk.Radiobutton)):
            widget.configure(bg=new_color)

female_radio.config(command=change_bg)
male_radio.config(command=change_bg)

window.mainloop()