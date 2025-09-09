import tkinter as tk
from tkinter import messagebox
import json

# File for saving tasks
FILE_NAME = "tasks.json"

# Load tasks from file
def load_tasks():
    try:
        with open(FILE_NAME, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return []   # If no file exists, start with empty list
    except json.JSONDecodeError:
        return []   # If file is empty/corrupt, reset to empty list

# Save tasks to file
def save_tasks():
    with open(FILE_NAME, "w") as f:
        json.dump(tasks, f)

# Functions
def add_task():
    task = entry.get()
    if task.strip() != "":
        tasks.append(task)
        entry.delete(0, tk.END)
        save_tasks()
        messagebox.showinfo("Success", "Task added successfully!")
    else:
        messagebox.showwarning("Warning", "Task cannot be empty")

def update_task():
    try:
        selected_index = task_listbox.curselection()[0]
        new_task = entry.get()
        if new_task.strip() != "":
            tasks[selected_index] = new_task
            entry.delete(0, tk.END)
            save_tasks()
            view_tasks()
            messagebox.showinfo("Success", "Task updated successfully!")
        else:
            messagebox.showwarning("Warning", "Task cannot be empty")
    except IndexError:
        messagebox.showwarning("Warning", "Select a task to update")

def delete_task():
    try:
        selected_index = task_listbox.curselection()[0]
        tasks.pop(selected_index)
        save_tasks()
        view_tasks()
        messagebox.showinfo("Success", "Task deleted successfully!")
    except IndexError:
        messagebox.showwarning("Warning", "Select a task to delete")

def clear_all_tasks():
    if tasks:
        confirm = messagebox.askyesno("Confirm", "Are you sure you want to clear all tasks?")
        if confirm:
            tasks.clear()
            save_tasks()
            task_listbox.delete(0, tk.END)
            messagebox.showinfo("Success", "All tasks cleared!")
    else:
        messagebox.showinfo("Info", "No tasks to clear.")

def view_tasks():
    task_listbox.delete(0, tk.END)  # Clear old list
    if not tasks:
        messagebox.showinfo("Info", "No tasks available.")
    else:
        for task in tasks:
            task_listbox.insert(tk.END, task)

# ---------------- GUI SETUP ----------------
root = tk.Tk()
root.title("To-Do List Application")
root.geometry("450x420")

# Title
title_label = tk.Label(root, text=" To-Do List", font=("Arial", 16, "bold"))
title_label.pack(pady=10)

# Input field
entry = tk.Entry(root, width=30, font=("Arial", 12))
entry.pack(pady=10)

# Buttons frame
btn_frame = tk.Frame(root)
btn_frame.pack(pady=5)

add_btn = tk.Button(btn_frame, text="Add Task", width=12, command=add_task)
add_btn.grid(row=0, column=0, padx=5)

update_btn = tk.Button(btn_frame, text="Update Task", width=12, command=update_task)
update_btn.grid(row=0, column=1, padx=5)

delete_btn = tk.Button(btn_frame, text="Delete Task", width=12, command=delete_task)
delete_btn.grid(row=0, column=2, padx=5)

view_btn = tk.Button(btn_frame, text="View Tasks", width=12, command=view_tasks)
view_btn.grid(row=0, column=3, padx=5)

clear_btn = tk.Button(root, text="Clear All Tasks", width=20, command=clear_all_tasks, bg="red", fg="white")
clear_btn.pack(pady=10)

# Task Listbox
task_listbox = tk.Listbox(root, width=50, height=12, selectmode=tk.SINGLE)
task_listbox.pack(pady=10)

# Load tasks (but don’t show until "View Tasks" clicked)
tasks = load_tasks()

# Run GUI
root.mainloop()
