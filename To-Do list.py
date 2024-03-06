import tkinter as tk

tasks = []

def add_task():
    task = entry_task.get()
    if task:
        tasks.append(task)
        listbox_tasks.insert(tk.END, task)
        entry_task.delete(0, tk.END)

def remove_task():
    try:
        selected_index = listbox_tasks.curselection()[0]
        tasks.pop(selected_index)
        listbox_tasks.delete(selected_index)
    except IndexError:
        pass

window = tk.Tk()
window.title("To-Do List")

label_task = tk.Label(window, text="Enter Task:")
label_task.pack()

entry_task = tk.Entry(window)
entry_task.pack()

button_add_task = tk.Button(window, text="Add Task", command=add_task)
button_add_task.pack()

listbox_tasks = tk.Listbox(window)
listbox_tasks.pack()

button_remove_task = tk.Button(window, text="Remove Task", command=remove_task)
button_remove_task.pack()

window.mainloop()
