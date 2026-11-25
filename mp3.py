import tkinter as tk

window = tk.Tk()
window.geometry("300x200")

tk.Label(window, text="Top", bg="lightblue").pack(fill="x")
tk.Label(window, text="Middle", bg="lightgreen").pack(fill="both", expand=True)
tk.Label(window, text="Bottom", bg="lightpink").pack(fill="x")

window.mainloop()

button_row = tk.Frame(window)
button_row.pack(pady=10)

tk.Button(button_row, text="OK").pack(side="left", padx=5)
tk.Button(button_row, text="Cancel").pack(side="left", padx=5)

import tkinter as tk

window = tk.Tk()
window.title("Sign Up")

tk.Label(window, text="Name:").grid(row=0, column=0, sticky="e", padx=5, pady=5)
name_entry = tk.Entry(window)
name_entry.grid(row=0, column=1, padx=5, pady=5)

tk.Label(window, text="Email:").grid(row=1, column=0, sticky="e", padx=5, pady=5)
email_entry = tk.Entry(window)
email_entry.grid(row=1, column=1, padx=5, pady=5)

tk.Button(window, text="Submit").grid(row=2, column=0, columnspan=2, pady=10)

window.mainloop()