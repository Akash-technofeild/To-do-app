# tasks=[]
# def show_menu():
#     print("\n------To Do List Menu-----")
#     print("1. Add Task")
#     print("2. View Task")
#     print("3. Mark Task As Done")
#     print("4. Delete Task ")
#     print("5. Exit")

# def add_task():
#     task=input("Enter Your Task: ")
#     tasks.append({"task":task,"done":False})
#     print(f" ✅ Task '{task}' added.")
# def view_tasks():
#     if not tasks:
#         print("No Tasks No Found.")
#         return

#     print("-----Your Tasks----\n")
#     for i,t in enumerate(tasks):
#         status= "✔️" if t['done'] else "❌"
#         print(f"{i+1}.[{status}] {t['task']}")
# def mark_done():
#     view_tasks()
#     try:
#         task_no=int(input("Enter task number to be marked as done"))
#         if 0<task_no<=len(tasks):
#             tasks[task_no-1]["done"] =True
#             print(f"✅ Task '{tasks[task_no-1]['task']}' marked as done ")
#         else:
#             print("❌ Invalid task number.")
#     except ValueError:
#         print("❌ Please enter a number.")

# def delete_task():
#     view_tasks()
#     try:
#         task_no=int(input("Enter task "))
#         if 0< task_no <=len(tasks):
#             deleted=tasks.pop(task_no-1)
#             print(f"🗑️ Task '{deleted['task']}' deleted.")
#         else:
#             print("❌ Invalid task number.")
#     except ValueError:
#         print("❌ Please enter a number.")
# while True:
#     show_menu()
#     choice=input("Choose an option (1-5): ")

#     if choice == '1':
#         add_task()
#     elif choice == '2':
#         view_tasks()
#     elif choice == '3':
#         mark_done()
#     elif choice =="4":
#         delete_task()
#     elif choice == "5":
#         print(" 👋 Exiting To DO List BYE BYE ")
#         break
#     else:
#         print("❌ Invalid option. Please choose 1–5.")

# GUI for todo
# import tkinter as tk
# from tkinter import messagebox

# # to create a window
# root=tk.Tk()
# root.title("To DO List ")
# root.geometry("400*400")

# # to take input
# entry=tk.Entry(root,width=40)
# entry.pack()

# # to create buttons
# btn_add=tk.Button(root,text="Add Task", command=add_task)
# btn_add.pack()

# # to show the task list 
# listbox=tk.Listbox(root,width=50)
# listbox.pack()

# # to run the app
# root.mainloop()

import tkinter as tk
from tkinter import messagebox

tasks=[]

def add_task():
    task_text=entry.get().strip()
    if task_text:
        tasks.append({"task":task_text,"done":False})
        # print(f"✅ Task '{task_text}' added.")
        entry.delete(0,tk.END)
        update_listbox()
    else:
        messagebox.showwarning("Input error","❌ Please enter a task.")

def update_listbox():
    listbox.delete(0,tk.END)
    for i,task in enumerate(tasks,start=1):
        status="✔️" if task["done"] else "❌"
        listbox.insert(tk.END,f"{i}.[{status} {task['task']}")

# 
def mark_done():
    try:
        index=listbox.curselection()[0]
        tasks[index]["done"] =True
        update_listbox()
        messagebox.showinfo("Success", f"✅ Task '{tasks[index]['task']}' marked as done." )
    except IndexError:
        messagebox.showwarning("Selection Error","❌ Please select a task to mark as done.")


def delete_task():
    try:
        index=listbox.curselection()[0]
        deleted=tasks.pop(index)
        update_listbox()
        messagebox.showinfo("Deleted",f"🗑️ Task '{deleted['task']}' deleted.")
    
    except IndexError:
        messagebox.showwarning("Selection Error","❌ Please select a task to delete.")
    


# to create a window
root=tk.Tk()
root.title("To DO List ")
root.geometry("600x400")

entry=tk.Entry(root,width=40,font=('Arial',12))
entry.pack(pady=10)

# to add button
btn_add=tk.Button(root,text="Add Task" , command=add_task,bg="#4CAF50",fg="white",font=("Arial",10,"bold"))
btn_add.pack(pady=5)

# to add listbox too show list in window
listbox=tk.Listbox(root,width=50, font=("Arial", 12), height=10)
listbox.pack(pady=10)

# mark as done button
btn_done = tk.Button(root, text="Mark as Done", command=mark_done,bg="#2196F3", fg="white", font=("Arial", 10, "bold"))
btn_done.pack(pady=5)

btn_delete = tk.Button(root,text="Delete Task", command=delete_task, bg="#f44336", fg="white", font=("Arial", 10, "bold"))
btn_delete.pack(pady=5)

frame=tk.Frame(root)
frame.pack(pady=10)

scrollbar =tk.Scrollbar(frame)
scrollbar.pack(side=tk.RIGHT,fill=tk.Y)

root.mainloop()