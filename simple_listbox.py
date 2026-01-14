import tkinter as tk
from tkinter import messagebox, Listbox, MULTIPLE

# Create the main window
root = tk.Tk()
root.title("Simple Listbox")
root.geometry("700x550")


def check_selection(selected_indices):
    if not selected_indices:
        messagebox.showwarning(
            "Warning", "Please select at least one item."
        )
        return False
    return True


def create_text_info(selected_indices):
    text = []
    for i in selected_indices:
        text.append(f"index :  {i} - {list_items.get(i)}\n")
    return text


def show_selection():

    selected_indices = list_items.curselection()
    if not check_selection(selected_indices):
        return

    text_show_selection = create_text_info(selected_indices)
    label_var.set(f"You selected: \n {''.join(text_show_selection)}")


def delete_selection():
    selected_indices = list_items.curselection()
    if not check_selection(selected_indices):
        return
    text_delete_selection = create_text_info(selected_indices)
    for i in reversed(selected_indices):
        list_items.delete(i)
    messagebox.showinfo(
        "Deleted Items", f"Deleted:\n{''.join(text_delete_selection)}")


# Create a Listbox widget
list_items = Listbox(root,
                     selectmode=MULTIPLE,
                     selectbackground="blue",
                     font=("Arial", 16)
                     )


# Insert items into the listbox
list_items.insert(tk.END, "Miyuki")
list_items.insert(tk.END, "Bella")
list_items.insert(tk.END, "Eri")
list_items.insert(tk.END, "Rin")
list_items.insert(tk.END, "Pixel")

list_items.pack()

# Create a button to show the selected item
Button_frame = tk.Frame(root)
Button_frame.pack(pady=10)
tk.Button(
    Button_frame,
    text="show selection",
    command=show_selection
).grid()
tk.Button(
    Button_frame,
    text="delete selection",
    command=delete_selection
).grid(row=0, column=1, padx=10)

label_var = tk.StringVar()
tk.Label(
    root,
    textvariable=label_var,
    font=("Arial", 16, "bold")
).pack(pady=10)
root.mainloop()
