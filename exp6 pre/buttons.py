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


def toggle_button(value, button):
    # Check if the same button is clicked again
    if var.get() == value:
        # Deselect
        var.set(0)
        button.config(relief=tk.RAISED, bg="SystemButtonFace")
    else:
        # Deselect all buttons first
        button1.config(relief=tk.RAISED, bg="SystemButtonFace")
        button2.config(relief=tk.RAISED, bg="SystemButtonFace")
        button3.config(relief=tk.RAISED, bg="SystemButtonFace")

        # Select the clicked button
        var.set(value)
        button.config(relief=tk.SUNKEN, bg="#d0d0d0")


# Create main window
root = tk.Tk()
root.title("Button Selection")
root.geometry("400x300")

# Variable to store the selected option
var = tk.IntVar()
var.set(0)  # No selection by default

# Create buttons
button1 = tk.Button(root, text="Option 1", font=("Arial", 12),
                    width=15, height=2,
                    command=lambda: toggle_button(1, button1))
button1.pack(padx=50, pady=5)

button2 = tk.Button(root, text="Option 2", font=("Arial", 12),
                    width=15, height=2,
                    command=lambda: toggle_button(2, button2))
button2.pack(padx=50, pady=5)

button3 = tk.Button(root, text="Option 3", font=("Arial", 12),
                    width=15, height=2,
                    command=lambda: toggle_button(3, button3))
button3.pack(padx=50, pady=5)

# Submit button
submit_button = tk.Button(root, text="Submit", command=show_selection,
                          bg="#4CAF50", fg="white", font=("Arial", 12))
submit_button.pack(pady=20)

# Result label
result_label = tk.Label(root, text="", font=("Arial", 12, "bold"))
result_label.pack(pady=10)

# Run the application
root.mainloop()