from tkinter import *
import tkinter as tk
from termcolor import colored

import keyboard as keyboard


def get_users(sys, regex):  # TODO
    f = open(r'C:\Users\oriko\Desktop\test.txt', 'rb')
    data = f.read()
    parts = data.split(regex.encode())  # the simple regex and every two strings is a tuple
    for part in parts:
        sys.users.append(tuple(part))
    f.close()


class Sys(object):
    root = None  # type -> tk

    text = None  # type -> text
    input_text = None  # type -> string

    def __init__(self, root):
        self.root = root
        self.init_texts()
        self.init_buttons()
        self.place_all()
        self.users = [('1', '1')]
        regex = '!@#$%^&*'
        get_users(self, regex)  # ('1', '1')] tuple of user name and password
        print(self.users)

    def init_texts(self):
        self.username = tk.Text(master=self.root, width=60, height=1)
        self.password = tk.Text(master=self.root, width=60, height=1)

    def init_buttons(self):
        self.submit = tk.Button(master=self.root, text="Submit", fg="black", command=self.submit)
        self.sign_up = tk.Button(master=self.root, text="Sign up", fg="black", command=self.sign_up)

    def place_all(self):
        self.username.place(x=0, y=50)
        self.password.place(x=0, y=75)
        self.submit.place(x=30, y=125)
        self.sign_up.place(x=120, y=125)

    def submit(self):
        username = self.username.get('1.0', 'end-1c')
        password = self.password.get('1.0', 'end-1c')
        entry = (username, password)

        is_in = False
        for existing_entry in self.users:
            if entry == existing_entry:
                is_in = True
                print(colored('success', 'green'))
                self.root.destroy()
        if is_in is False:
            print(colored('denied', 'red'))

    def sign_up(self):  # TODO SIGN UP FUNC - make a new windows with other options REMODEL need special regex
        regex = '!@#$%^&*'
        username = self.username.get('1.0', 'end-1c')
        password = self.password.get('1.0', 'end-1c')
        f = open(r'C:\Users\oriko\Desktop\test.txt', 'ab')
        unamereg = username + regex
        passwordreg = password + regex
        f.write(unamereg.encode())
        f.write(passwordreg.encode())
        self.root.destroy()


if __name__ == '__main__':
    root = Tk()
    gui = Sys(root=root)
    root.mainloop()
