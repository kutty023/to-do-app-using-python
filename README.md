# To-do App

A simple desktop-based Kanban-style To-Do application built using Python and Tkinter. The app allows users to manage tasks across three stages — To Do, In Progress, and Completed — with persistent storage.

----
# ✨ Features
- ➕ Add new tasks
- ✏️ Edit existing tasks
- 🗑 Delete individual tasks
- 🧹 Delete all tasks at once
- ⬅ ➡ Move tasks between columns using arrow buttons
- 💾 Persistent storage using JSON
- 🖥 Simple and intuitive GUI

----
# 🧱 Application Layout
```
        To Do   ⬅ ➡   In Progress   ⬅ ➡   Completed
```

----
# 🛠 Tech Stack
- Language: Python
- GUI Framework: Tkinter
- Data Storage: JSON
- Platform: Cross-platform (Windows / macOS / Linux)

----
# 📂 Project Structure
```
        📁 todo-app/
        │── todo_app.py
        │── tasks.json       
        │── README.md
```

----
# ▶ How to Run
1. Ensure Python is installed:
```
        $python --version
```
2. Run the application:
```
        $python todo_app.py
```
 
No external libraries required. Tkinter comes bundled with Python.

----
# Usage Guide
1. Click Add to create a task
2. Select a task and use:
    - ➡ to move forward
    - ⬅ to move backward
3. Use Edit to update task text
4. Use Delete to remove a selected task
5. Use Delete All to clear all tasks

All changes are saved automatically.

----
# 📜 License
This project is open-source and free to use for learning and personal projects.