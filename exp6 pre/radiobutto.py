import tkinter as tk
from tkinter import messagebox


def show_selection():
    selection = var.get()

    if selection == 1:
        result_label.config(text="You selected: Option 1", fg="#3776ab")
    elif selection == 2:
        result_label.config(text="You selected: Option 2", fg="#f89820")
    elif selection == 3:
        result_label.config(text="You selected: Option 3", fg="#00599c")
    else:
        messagebox.showwarning("No Selection", "Please select an option first!")


def toggle_selection(value):
    # Check the previous value before tkinter updates it
    if last_selected.get() == value:
        # Same button clicked twice - deselect
        var.set(0)
        last_selected.set(0)
    else:
        # Different button clicked - select it
        last_selected.set(value)


# Create main window
root = tk.Tk()
root.title("Radiobutton Selection")
root.geometry("400x250")

# Variable to store the selected option
var = tk.IntVar()
var.set(0)  # No selection by default

# Variable to track the last selected option
last_selected = tk.IntVar()
last_selected.set(0)

# Create radiobuttons with command parameter
radio1 = tk.Radiobutton(root, text="Option 1", variable=var, value=1,
                        font=("Arial", 12), command=lambda: toggle_selection(1))
radio1.pack(anchor=tk.W, padx=50, pady=5)

radio2 = tk.Radiobutton(root, text="Option 2", variable=var, value=2,
                        font=("Arial", 12), command=lambda: toggle_selection(2))
radio2.pack(anchor=tk.W, padx=50, pady=5)

radio3 = tk.Radiobutton(root, text="Option 3", variable=var, value=3,
                        font=("Arial", 12), command=lambda: toggle_selection(3))
radio3.pack(anchor=tk.W, padx=50, pady=5)

# Submit button
submit_button = tk.Button(root, text="Submit", command=show_selection,
                          bg="#4CAF50", fg="white", font=("Arial", 12))
submit_button.pack(pady=20)

# Result label
result_label = tk.Label(root, text="", font=("Arial", 12, "bold"))
result_label.pack(pady=10)

# Run the application
root.mainloop()