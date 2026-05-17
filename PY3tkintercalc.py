import tkinter as tk

# ---------------------------
# SIGN-UP WINDOW
# ---------------------------

def start_app():
    name = name_entry.get().strip()
    age = age_entry.get().strip()

    if name == "" or age == "":
        signup_error.config(text="Please fill in all fields.")
        return

    signup_root.destroy()
    open_calculator(name, age)


signup_root = tk.Tk()
signup_root.title("Sign Up")

tk.Label(signup_root, text="Enter your details", font=("Monospace", 16)).pack(pady=10)

tk.Label(signup_root, text="Name:").pack()
name_entry = tk.Entry(signup_root)
name_entry.pack(pady=5)

tk.Label(signup_root, text="Age:").pack()
age_entry = tk.Entry(signup_root)
age_entry.pack(pady=5)

signup_error = tk.Label(signup_root, text="", fg="red")
signup_error.pack()

tk.Button(signup_root, text="Continue", command=start_app).pack(pady=10)


# ---------------------------
# MAIN APP
# ---------------------------

def open_calculator(user_name, user_age):
    root = tk.Tk()
    root.title("Tkinter Calculator")
    root.config(bg="lightblue")  # Challenge 2

    # Make columns stretch
    for c in range(4):
        root.grid_columnconfigure(c, weight=1)

    tk.Label(root, text=f"Welcome {user_name}!", font=("Monospace", 14), bg="lightblue").grid(row=0, column=0, columnspan=4, pady=10)

    tk.Label(root, text="No. 1:", bg="lightblue").grid(row=1, column=0, sticky="e")
    entry_a = tk.Entry(root)
    entry_a.grid(row=1, column=1)
    entry_a.insert(0, "0")  # Challenge 1

    tk.Label(root, text="No. 2:", bg="lightblue").grid(row=1, column=2, sticky="e")
    entry_b = tk.Entry(root)
    entry_b.grid(row=1, column=3)
    entry_b.insert(0, "0")  # Challenge 1

    tk.Label(root, text="Decimals:", bg="lightblue").grid(row=2, column=0)
    entry_round = tk.Entry(root, width=5)
    entry_round.grid(row=2, column=1)
    entry_round.insert(0, "2")

    result_label = tk.Label(root, text="Result: --", font=("Monospace", 16), fg="green", bg="lightblue")
    result_label.grid(row=3, column=0, columnspan=4)

    error_label = tk.Label(root, text="", fg="red", bg="lightblue")
    error_label.grid(row=4, column=0, columnspan=4)

    # History panel
    history = tk.Listbox(root, height=6)
    history.grid(row=0, column=4, rowspan=6, padx=10)

    def shake():
        for i in range(10):
            root.geometry(f"+{100 + i*5}+100")
            root.update()
            root.after(20)
            root.geometry(f"+{100 - i*5}+100")
            root.update()

    def parse_inputs():
        try:
            a = float(entry_a.get())
            b = float(entry_b.get())
            n = int(entry_round.get())
            return a, b, n
        except:
            raise ValueError("Invalid input")

    def show_result(value, text):
        _, _, n = parse_inputs()
        value = round(value, n)  # Challenge 6
        result_label.config(text=f"Result: {value}")
        error_label.config(text="")
        history.insert(tk.END, f"{text} = {value}")  # Challenge 8

    def show_error(msg):
        error_label.config(text=msg)
        result_label.config(text="Result: --")
        shake()  # Challenge 10

    def op_add():
        try:
            a, b, _ = parse_inputs()
            show_result(a + b, f"{a} + {b}")
        except Exception as e:
            show_error(str(e))

    def op_sub():
        try:
            a, b, _ = parse_inputs()
            show_result(a - b, f"{a} - {b}")
        except Exception as e:
            show_error(str(e))

    def op_mul():
        try:
            a, b, _ = parse_inputs()
            show_result(a * b, f"{a} × {b}")
        except Exception as e:
            show_error(str(e))

    def op_div():
        try:
            a, b, _ = parse_inputs()
            if b == 0:
                raise ValueError("Cannot divide by zero")
            show_result(a / b, f"{a} ÷ {b}")
        except Exception as e:
            show_error(str(e))

    def op_percent():
        try:
            a, b, _ = parse_inputs()
            show_result(a * b / 100, f"{b}% of {a}")
        except Exception as e:
            show_error(str(e))

    def clear_all():
        entry_a.delete(0, tk.END)
        entry_b.delete(0, tk.END)
        result_label.config(text="Result: --")
        error_label.config(text="")

    # Buttons
    tk.Button(root, text="+", command=op_add).grid(row=5, column=0)
    tk.Button(root, text="-", command=op_sub).grid(row=5, column=1)
    tk.Button(root, text="×", command=op_mul).grid(row=5, column=2)
    tk.Button(root, text="÷", command=op_div).grid(row=5, column=3)

    tk.Button(root, text="%", command=op_percent).grid(row=6, column=0)

    tk.Button(root, text="Clear", command=clear_all).grid(row=6, column=1, columnspan=2)
    tk.Button(root, text="Quit", command=root.destroy).grid(row=6, column=3)

    # Step 9 bindings
    root.bind("<Return>", lambda e: op_add())

    # Advanced keyboard shortcuts
    root.bind("+", lambda e: op_add())
    root.bind("-", lambda e: op_sub())
    root.bind("*", lambda e: op_mul())
    root.bind("/", lambda e: op_div())

    root.mainloop()


signup_root.mainloop()