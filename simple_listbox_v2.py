import tkinter as tk
from tkinter import messagebox


class SimpleListbox:
    def __init__(self, root):
        self.root = root
        self.root.title("Simple Listbox")
        self.root.geometry("700x550")

        self.create_widgets()

    def create_widgets(self):
        tk.Label(
            self.root,
            text="Contact List",
            font=("Arial", 16, "bold"),
            fg="white",
            background="black"
        ).pack(pady=20)
        self.listbox_name = tk.Listbox(
            self.root,
            selectmode=tk.MULTIPLE,
            selectbackground="blue",
            font=("Arial", 14)
        )
        list_name = [
            "Miyuki",
            "Bella",
            "Eri",
            "Rin",
            "Kaede"
        ]
        for name in list_name:
            self.listbox_name.insert(tk.END, name)
        self.listbox_name.pack(pady=10)

        button_frame = tk.Frame(self.root)
        button_frame.pack(pady=10)
        tk.Button(
            button_frame,
            text="Show",
            command=self.show_selection
        ).grid()
        tk.Button(
            button_frame,
            text="Delete",
            command=self.delete_selection

        ).grid(row=0, column=1, padx=10)

        self.label_var = tk.StringVar()
        tk.Label(
            self.root,
            textvariable=self.label_var,
            font=("Arial", 14, "bold")
        ).pack(pady=10)

    def create_text_info(self, selected_indices):
        return "".join(
            f"index: {i+1} - {self.listbox_name.get(i)}\n"
            for i in selected_indices
        )

    def check_selection(self, selected_indices):
        if not selected_indices:
            messagebox.showwarning(
                "Warning", "Please select at least one item."
            )
            return False
        return True

    def show_selection(self):
        selected_indices = self.listbox_name.curselection()
        if not self.check_selection(selected_indices):
            return
        text_show_selection = self.create_text_info(selected_indices)
        self.label_var.set(f"You selected\n {text_show_selection}")

    def confirm_delete(self):
        return messagebox.askyesno(
            "Confirm Delete", "Please confirm."
        )

    def delete_selection(self):
        selected_indices = self.listbox_name.curselection()
        if not self.check_selection(selected_indices):
            return
        if not self.confirm_delete():
            return
        text_delete_selection = self.create_text_info(selected_indices)
        for i in reversed(selected_indices):
            self.listbox_name.delete(i)
        self.label_var.set(f"Deleted\n {text_delete_selection}")


if __name__ == "__main__":
    root = tk.Tk()
    app = SimpleListbox(root)
    root.mainloop()
