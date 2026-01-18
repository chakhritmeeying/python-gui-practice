import tkinter as tk
from tkinter import messagebox


class LoginForm:
    def __init__(self, root):
        self.root = root
        self.root.title("Login Form")
        self.root.geometry("400x300")

        self.create_widgets()
        # self.userid = "user"
        # self.userpassword = "password"

        self.userid = [
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
        userid = self.userid
        for idx, info in enumerate(userid, start=1):
            if entry_username == info["username"]:
                if entry_password == info["password"]:
                    messagebox.showinfo("Login success", "Login success")
                    self.login_success.set(f"Welcom {info['username']}")
                    return
                else:
                    messagebox.showwarning(
                        "Login failed", "Password incorrect\nPlease try again.")
                    return
        messagebox.showwarning(
            "Login failed", "User not found\nPlease try again.")

    def register_page(self):
        messagebox.showinfo("Information", "This function will be soon.")


if __name__ == "__main__":
    root = tk.Tk()
    app = LoginForm(root)
    root.mainloop()
