import tkinter as tk
from tkinter import simpledialog, messagebox
import json
import os

FILE_NAME = "tasks.json"

# ------------------ DATA ------------------

def load_tasks():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as f:
            return json.load(f)
    return {"todo": [], "progress": [], "done": []}

def save_tasks():
    with open(FILE_NAME, "w") as f:
        json.dump(tasks, f)

def update_data():
    tasks["todo"] = list(todo_list.get(0, tk.END))
    tasks["progress"] = list(progress_list.get(0, tk.END))
    tasks["done"] = list(done_list.get(0, tk.END))
    save_tasks()

# ------------------ HELPERS ------------------

def get_selected():
    for lst in (todo_list, progress_list, done_list):
        if lst.curselection():
            return lst
    return None

# ------------------ ACTIONS ------------------

def add_task():
    task = simpledialog.askstring("Add Task", "Enter task:")
    if task:
        todo_list.insert(tk.END, task)
        update_data()

def edit_task():
    lst = get_selected()
    if not lst:
        messagebox.showwarning("Edit Task", "Select a task first")
        return

    idx = lst.curselection()[0]
    old = lst.get(idx)
    new = simpledialog.askstring("Edit Task", "Edit task:", initialvalue=old)

    if new:
        lst.delete(idx)
        lst.insert(idx, new)
        update_data()

def delete_task():
    lst = get_selected()
    if not lst:
        messagebox.showwarning("Delete Task", "Select a task first")
        return

    lst.delete(lst.curselection()[0])
    update_data()

def delete_all():
    if messagebox.askyesno("Delete All", "Delete ALL tasks?"):
        todo_list.delete(0, tk.END)
        progress_list.delete(0, tk.END)
        done_list.delete(0, tk.END)
        update_data()

def move_right():
    lst = get_selected()
    if not lst or lst == done_list:
        return  # no column to the right

    idx = lst.curselection()[0]
    task = lst.get(idx)
    lst.delete(idx)

    if lst == todo_list:
        progress_list.insert(tk.END, task)
    elif lst == progress_list:
        done_list.insert(tk.END, task)

    update_data()

def move_left():
    lst = get_selected()
    if not lst or lst == todo_list:
        return  # no column to the left

    idx = lst.curselection()[0]
    task = lst.get(idx)
    lst.delete(idx)

    if lst == done_list:
        progress_list.insert(tk.END, task)
    elif lst == progress_list:
        todo_list.insert(tk.END, task)

    update_data()

# ------------------ UI ------------------

root = tk.Tk()
root.title("To-Do App")
root.geometry("1000x480")

tasks = load_tasks()

# Top bar
top = tk.Frame(root)
top.pack(fill="x", padx=10, pady=5)
tk.Button(top, text="Delete All", fg="red", command=delete_all).pack(side="right")

# Main layout
main = tk.Frame(root)
main.pack(fill="both", expand=True)

# To Do
todo_frame = tk.LabelFrame(main, text="To Do", padx=10, pady=10)
todo_frame.pack(side="left", fill="both", expand=True, padx=5)
todo_list = tk.Listbox(todo_frame)
todo_list.pack(fill="both", expand=True)

# Arrows (To Do ↔ In Progress)
arrow1 = tk.Frame(main)
arrow1.pack(side="left", padx=5)
tk.Button(arrow1, text="➡", width=4, command=move_right).pack(pady=5)
tk.Button(arrow1, text="⬅", width=4, command=move_left).pack(pady=5)

# In Progress
progress_frame = tk.LabelFrame(main, text="In Progress", padx=10, pady=10)
progress_frame.pack(side="left", fill="both", expand=True, padx=5)
progress_list = tk.Listbox(progress_frame)
progress_list.pack(fill="both", expand=True)

# Arrows (In Progress ↔ Completed)
arrow2 = tk.Frame(main)
arrow2.pack(side="left", padx=5)
tk.Button(arrow2, text="➡", width=4, command=move_right).pack(pady=5)
tk.Button(arrow2, text="⬅", width=4, command=move_left).pack(pady=5)

# Completed
done_frame = tk.LabelFrame(main, text="Completed", padx=10, pady=10)
done_frame.pack(side="left", fill="both", expand=True, padx=5)
done_list = tk.Listbox(done_frame)
done_list.pack(fill="both", expand=True)

# Bottom controls
bottom = tk.Frame(root)
bottom.pack(pady=10)
tk.Button(bottom, text="Add", width=10, command=add_task).pack(side="left", padx=5)
tk.Button(bottom, text="Edit", width=10, command=edit_task).pack(side="left", padx=5)
tk.Button(bottom, text="Delete", width=10, command=delete_task).pack(side="left", padx=5)

# Load saved tasks
for t in tasks["todo"]:
    todo_list.insert(tk.END, t)
for t in tasks["progress"]:
    progress_list.insert(tk.END, t)
for t in tasks["done"]:
    done_list.insert(tk.END, t)

root.mainloop()