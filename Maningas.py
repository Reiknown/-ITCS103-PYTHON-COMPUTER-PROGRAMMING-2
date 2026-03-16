import tkinter as tk

window = tk.Tk()
window.title("Profile Builder")
window.geometry("600x300")
window.configure(bg="light green")

title_label = tk.Label(window, text="Profile Builder", font=("Arial", 16, "bold"), bg="light green")
title_label.pack(pady=(10, 5))

frame = tk.Frame(window, bg="light green")
frame.pack(padx=10, pady=5)


first_entry = tk.Entry(frame, width=20)
first_entry.grid(row=0, column=0, padx=15, pady=(15, 0))
tk.Label(frame, text="First Name", font=("Arial", 10, "italic"), bg="light green").grid(row=1, column=0)

middle_entry = tk.Entry(frame, width=20)
middle_entry.grid(row=0, column=1, padx=15, pady=(15, 0))
tk.Label(frame, text="Middle Name", font=("Arial", 10, "italic"), bg="light green").grid(row=1, column=1)

last_entry = tk.Entry(frame, width=20)
last_entry.grid(row=0, column=2, padx=15, pady=(15, 0))
tk.Label(frame, text="Last Name", font=("Arial", 10, "italic"), bg="light green").grid(row=1, column=2)

year_entry = tk.Entry(frame, width=20)
year_entry.grid(row=2, column=0, padx=15, pady=(20, 0))
tk.Label(frame, text="Birth Year", font=("Arial", 10, "italic"), bg="light green").grid(row=3, column=0)

age_label = tk.Label(frame, text="Computing Age...", font=("Arial", 13, "italic",), bg="light green")
age_label.grid(row=2, column=1, columnspan=2, pady=(20, 0), padx=20)



tk.Label(frame, text="Gender", font=("Arial", 10, "italic"), bg="light green").grid(row=4, column=0, pady=(15, 15))
gender_var = tk.StringVar(value="None")

male_radio = tk.Radiobutton(frame, text="Male", variable=gender_var, value="Male", bg="light green")
male_radio.grid(row=4, column=1, sticky="w", padx=15, pady=(15, 15))

female_radio = tk.Radiobutton(frame, text="Female", variable=gender_var, value="Female", bg="light green")
female_radio.grid(row=4, column=1, sticky="e", padx=15, pady=(15, 15))

submit_btn = tk.Button(window, text="Submit", bg="light green", font=("Arial", 10, "bold"))
submit_btn.pack(pady=10)





def calculate_age(event):
    birth_year = int(year_entry.get())
    age = 2026 - birth_year
    age_label['text'] = f"Age: {age} years old"

def change_bg():
    selected_gender = gender_var.get()
    if selected_gender == "Female":
        new_color = "pink"
    elif selected_gender == "Male":
        new_color = "light blue"
    else:
        new_color = "light green"
        
    window.configure(bg=new_color)
    title_label.configure(bg=new_color)
    frame.configure(bg=new_color)
    
    for widget in frame.winfo_children():
        if isinstance(widget, (tk.Label, tk.Radiobutton)):
            widget.configure(bg=new_color)

def on_enter(event):
    submit_btn['background'] = 'lime green'

def on_leave(event):
    submit_btn['background'] = window.cget("bg") 

def generate_id():
    popup = tk.Toplevel(window)
    popup.title("Student ID")
    popup.geometry("300x400")
    
    bg_color = window.cget("bg")
    popup.configure(bg=bg_color)
    popup.grab_set() 

    tk.Label(popup, text="Student ID", font=("Arial", 16, "bold"), bg=bg_color).pack(pady=15)

    card_frame = tk.Frame(popup, bg="alice blue", bd=1, relief="solid")
    card_frame.pack(padx=20, pady=5, fill="both", expand=True)

    img = tk.PhotoImage(file="profileicon.png").subsample(2, 2)
    img_label = tk.Label(card_frame, image=img, bg="alice blue")
    img_label.image = img 
    img_label.pack(pady=15)

    full_name = f"{first_entry.get()} {middle_entry.get()} {last_entry.get()}"
    age_text = age_label['text'].replace("Age: ", "")
    gender_text = gender_var.get()

    tk.Label(card_frame, text=f"Name:  {full_name}", bg="alice blue", font=("Arial", 11)).pack(pady=5, anchor="w", padx=20)
    tk.Label(card_frame, text=f"Age:      {age_text}", bg="alice blue", font=("Arial", 11)).pack(pady=5, anchor="w", padx=20)
    tk.Label(card_frame, text=f"Gender: {gender_text}", bg="alice blue", font=("Arial", 11)).pack(pady=5, anchor="w", padx=20)


year_entry.bind('<Return>', calculate_age)

female_radio.config(command=change_bg)
male_radio.config(command=change_bg)

submit_btn.config(command=generate_id)
submit_btn.bind("<Enter>", on_enter)
submit_btn.bind("<Leave>", on_leave)


window.mainloop()
