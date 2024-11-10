# 99DaysWithCPC - Machine Learning
import tkinter as tk
from tkinter import filedialog, messagebox, simpledialog
from tkinter.scrolledtext import ScrolledText
import os


class Notepad:
    def __init__(self, root):
        self.root = root
        self.root.title("Custom Notepad")
        self.root.geometry("800x600")

        # Initialize variables
        self.filename = None
        self.is_private = False
        self.password = None

        # Setup GUI components
        self.setup_menu()
        self.setup_text_widget()
        self.setup_word_counter()

    def setup_menu(self):
        # Create a menu bar
        menubar = tk.Menu(self.root)

        # File Menu
        file_menu = tk.Menu(menubar, tearoff=0)
        file_menu.add_command(label="New", command=self.new_file)
        file_menu.add_command(label="Open", command=self.open_file)
        file_menu.add_command(label="Save", command=self.save_file)
        file_menu.add_command(label="Save As Private", command=self.save_private_file)
        file_menu.add_separator()
        file_menu.add_command(label="Exit", command=self.exit_app)
        menubar.add_cascade(label="File", menu=file_menu)

        # Edit Menu
        edit_menu = tk.Menu(menubar, tearoff=0)
        edit_menu.add_command(
            label="Cut", command=lambda: self.text_area.event_generate("<<Cut>>")
        )
        edit_menu.add_command(
            label="Copy", command=lambda: self.text_area.event_generate("<<Copy>>")
        )
        edit_menu.add_command(
            label="Paste", command=lambda: self.text_area.event_generate("<<Paste>>")
        )
        edit_menu.add_separator()
        edit_menu.add_command(
            label="Undo", command=lambda: self.text_area.event_generate("<<Undo>>")
        )
        edit_menu.add_command(
            label="Redo", command=lambda: self.text_area.event_generate("<<Redo>>")
        )
        menubar.add_cascade(label="Edit", menu=edit_menu)

        # Settings Menu
        settings_menu = tk.Menu(menubar, tearoff=0)
        settings_menu.add_command(label="Font Size", command=self.set_font_size)
        menubar.add_cascade(label="Settings", menu=settings_menu)

        self.root.config(menu=menubar)

    def setup_text_widget(self):
        # Text area with scroll
        self.text_area = ScrolledText(self.root, font=("Arial", 12))
        self.text_area.pack(fill=tk.BOTH, expand=True)
        self.text_area.bind("<<Modified>>", self.update_word_count)

    def setup_word_counter(self):
        # Word counter at the bottom
        self.word_counter_label = tk.Label(self.root, text="Words: 0")
        self.word_counter_label.pack(side=tk.BOTTOM, fill=tk.X)

    def new_file(self):
        if self.confirm_save():
            self.text_area.delete(1.0, tk.END)
            self.filename = None
            self.is_private = False
            self.password = None
            self.update_word_count()

    def open_file(self):
        if self.confirm_save():
            file_path = filedialog.askopenfilename(
                defaultextension=".txt", filetypes=[("Text files", "*.txt")]
            )
            if file_path:
                try:
                    with open(file_path, "r") as file:
                        content = file.read()

                    # Check if the file is private by looking for the password indicator
                    if content.startswith("PRIVATE FILE:"):
                        if not self.unlock_private_file(content):
                            return

                    self.text_area.delete(1.0, tk.END)
                    # Remove password header if file is private
                    self.text_area.insert(
                        tk.END,
                        content if not self.is_private else content.split("\n", 1)[1],
                    )
                    self.filename = file_path
                    self.update_word_count()
                except Exception as e:
                    messagebox.showerror("Error", f"Failed to open file: {e}")

    def save_file(self):
        if self.filename:
            self.write_to_file(self.filename)
        else:
            self.save_file_as()

    def save_file_as(self):
        file_path = filedialog.asksaveasfilename(
            defaultextension=".txt", filetypes=[("Text files", "*.txt")]
        )
        if file_path:
            self.write_to_file(file_path)
            self.filename = file_path

    def save_private_file(self):
        # Ask for password
        password = simpledialog.askstring(
            "Password", "Enter password to secure this file:", show="*"
        )
        if password:
            self.password = password
            self.is_private = True
            self.save_file()

    def write_to_file(self, file_path):
        try:
            content = self.text_area.get(1.0, tk.END)
            if self.is_private and self.password:
                content = (
                    f"PRIVATE FILE:{self.password}\n" + content
                )  # Include password in file header

            with open(file_path, "w") as file:
                file.write(content)
            messagebox.showinfo("Success", "File saved successfully.")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to save file: {e}")

    def confirm_save(self):
        if self.text_area.edit_modified():
            answer = messagebox.askyesnocancel(
                "Unsaved Changes", "Do you want to save changes?"
            )
            if answer:  # Save before proceeding
                self.save_file()
            elif answer is None:  # Cancel the action
                return False
        return True

    def exit_app(self):
        if self.confirm_save():
            self.root.quit()

    def set_font_size(self):
        # Ask user for font size
        font_size = simpledialog.askinteger(
            "Font Size", "Enter font size:", minvalue=8, maxvalue=72
        )
        if font_size:
            self.text_area.config(font=("Arial", font_size))

    def update_word_count(self, event=None):
        content = self.text_area.get(1.0, tk.END).strip()
        words = len(content.split())
        self.word_counter_label.config(text=f"Words: {words}")
        self.text_area.edit_modified(False)

    def unlock_private_file(self, content):
        # Extract the actual password from file header
        header, actual_content = content.split("\n", 1)
        saved_password = header.split(":", 1)[1].strip()

        # Ask for password or bypass code
        entered_password = simpledialog.askstring(
            "Enter Password", "This is a private file. Enter password or bypass code:"
        )
        if entered_password == saved_password or entered_password == "999999":
            self.is_private = True
            self.password = saved_password  # Set the password for the session
            return True
        else:
            messagebox.showerror("Access Denied", "Incorrect password or bypass code.")
            return False


# Run the application
if __name__ == "__main__":
    root = tk.Tk()
    notepad = Notepad(root)
    root.mainloop()
