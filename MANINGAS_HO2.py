import tkinter as tk

window = tk.Tk()

window.title("Hanniel Rei's Profile")
window.geometry("600x600")
window.resizable(False, True)
window.config(bg="#2C3E50")


label_title = tk.Label(window, text="Student Profile", 
                 font=("Arial", 50, "bold"),
                 fg="#F39C12", bg="#2C3E50")
label_title.pack(pady=20)


label_name = tk.Label(window, text="NAME: Hanniel Rei L. Maningas\n", 
                       font=("Arial", 14), fg="#ECF0F1", bg="#2C3E50",)
label_name.pack(anchor="w", padx=15)


label_age = tk.Label(window, text="AGE: 19 Years Old\n", 
                       font=("Arial", 14), fg="#ECF0F1", bg="#2C3E50")
label_age.pack(anchor="w", padx=15)


label_course = tk.Label(window, text="COURSE: BSIT-1A\n", 
                       font=("Arial", 14), fg="#ECF0F1", bg="#2C3E50")
label_course.pack(anchor="w", padx=15)


label_date = tk.Label(window, text="BIRTHDAY: July 12, 2006\n", 
                       font=("Arial", 14), fg="#ECF0F1", bg="#2C3E50")
label_date.pack(anchor="w", padx=15)


label_quote = tk.Label(window, text="MOTTO: 'Right mindset turn your weakness into a strength'", 
                       font=("Arial", 14), fg="#ECF0F1", bg="#2C3E50")
label_quote.pack(anchor="w", padx=15)

window.mainloop()