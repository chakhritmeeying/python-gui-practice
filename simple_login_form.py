import tkinter as tk
from tkinter import messagebox


class LoginForm:
    def __init__(self, root):
        self.root = root
        self.root.title("Login Form")
        self.root.geometry("400x300")

        self.create_widgets()

        self.users = [
            {
                "username": "user",
                "password": "password"
            },
            {
                "username": "bella",
                "password": "acb123"
            }
        ]

    def create_widgets(self):
        tk.Label(
            self.root,
            text="Enter username and password",
            font=("Arial", 14, "bold")
        ).pack(pady=10)
        frame_user_password = tk.Frame(self.root)
        frame_user_password.pack(pady=10)
        # Username field
        tk.Label(
            frame_user_password,
            text="Username: "
        ).grid()
        self.entry_username = tk.Entry(
            frame_user_password,
            width=20
        )
        self.entry_username.grid(row=0, column=1, padx=5)
        # Password field
        tk.Label(
            frame_user_password,
            text="Password: "
        ).grid(row=1, column=0)
        self.entry_password = tk.Entry(
            frame_user_password,
            show="*",
            width=20
        )
        self.entry_password.grid(row=1, column=1, padx=5)

        # Button frame
        frame_button = tk.Frame(
            self.root
        )
        frame_button.pack(pady=10)
        # Login button
        tk.Button(
            frame_button,
            text="Login",
            command=self.login_check
        ).pack(side="left")
        tk.Button(
            frame_button,
            text="Register",
            command=self.register_page
        ).pack(side="left", padx=5)

        self.login_success = tk.StringVar()
        tk.Label(
            self.root,
            textvariable=self.login_success,
            font=("Arial", 16, "bold")
        ).pack(pady=10)

    def login_check(self):
        entry_username = self.entry_username.get()
        entry_password = self.entry_password.get()
        if not entry_username or not entry_password:
            messagebox.showwarning(
                "Login failed", "Please enter username and password")
            return
        for info in self.users:
            if entry_username == info["username"]:
                if entry_password == info["password"]:
                    messagebox.showinfo("Login success", "Login success")
                    self.login_success.set(f"Welcome {info['username']}")
                    return
                else:
                    messagebox.showwarning(
                        "Login failed", "Password incorrect\nPlease try again.")
                    return
        messagebox.showwarning(
            "Login failed", "User not found\nPlease try again.")

    def register_page(self):
        self.open_register_window()
    # Register Form

    def open_register_window(self):
        register_window = tk.Toplevel(self.root)
        register_window.title("Register")
        register_window.geometry("400x300")

        tk.Label(
            register_window,
            text="Register new user",
            font=("Arial", 14, "bold")
        ).pack(pady=10)
        frame_info = tk.Frame(register_window)
        frame_info.pack(pady=10)
        tk.Label(
            frame_info,
            text="username: "
        ).grid()
        entry_register_user = tk.Entry(
            frame_info,
            width=20
        )
        entry_register_user.grid(row=0, column=1, padx=5)
        tk.Label(
            frame_info,
            text="password: "
        ).grid(row=1, column=0)
        entry_register_password = tk.Entry(
            frame_info,
            show="*",
            width=20
        )
        entry_register_password.grid(row=1, column=1, padx=5)
        tk.Label(
            frame_info,
            text="confirm-password: "
        ).grid(row=2, column=0)
        entry_confirm_password = tk.Entry(
            frame_info,
            show="*",
            width=20
        )
        entry_confirm_password.grid(
            row=2, column=1, padx=5)
        frame_register_button = tk.Frame(register_window)
        frame_register_button.pack(pady=10)
        tk.Button(
            frame_register_button,
            text="Submit",
            command=lambda: self.register_new_user(
                entry_register_user,
                entry_register_password,
                entry_confirm_password,
                register_window
            )
        ).pack(side="left")
        tk.Button(
            frame_register_button,
            text="Close",
            command=register_window.destroy
        ).pack(side="left", padx=5)

    def register_new_user(self, entry_user, entry_pass, entry_confirm, window):
        username = entry_user.get()
        password = entry_pass.get()
        confirm_password = entry_confirm.get()
        if not username or not password or not confirm_password:
            messagebox.showwarning(
                "Error",
                "Please enter username password and confirm password."
            )
            entry_user.focus()
            return
        if self.check_user(username):
            messagebox.showwarning(
                "Error",
                "Username has used please try another username"
            )
            entry_user.focus()
            return
        if password != confirm_password:
            messagebox.showinfo(
                "Error",
                "Password not match"
            )
            return
        self.users.append({
            "username": username,
            "password": password
        })
        messagebox.showinfo("Success", "Register success.")
        window.destroy()

    def check_user(self, username):
        for user in self.users:
            if username == user['username']:
                return True
        return False


if __name__ == "__main__":
    root = tk.Tk()
    app = LoginForm(root)
    root.mainloop()
