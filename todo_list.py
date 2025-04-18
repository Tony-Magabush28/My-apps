import tkinter as tk
from tkinter import messagebox

# Create main window
root = tk.Tk()
root.title("To-Do List App")
root.geometry("300x400")

# Task list
tasks = []

# Functions
def add_task():
    task = entry.get()
    if task != "":
        tasks.append(task)
        update_listbox()
        entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "Task cannot be empty!")

def delete_task():
    selected = listbox.curselection()
    if selected:
        tasks.pop(selected[0])
        update_listbox()
    else:
        messagebox.showwarning("Warning", "No task selected!")

def update_listbox():
    listbox.delete(0, tk.END)
    for task in tasks:
        listbox.insert(tk.END, task)

# Widgets
entry = tk.Entry(root, width=25)
entry.pack(pady=10)

add_button = tk.Button(root, text="Add Task", command=add_task)
add_button.pack(pady=5)

listbox = tk.Listbox(root, width=30, height=10)
listbox.pack(pady=10)

delete_button = tk.Button(root, text="Delete Task", command=delete_task)
delete_button.pack(pady=5)

# Start the app
root.mainloop()

                    

