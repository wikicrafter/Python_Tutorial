import tkinter as tk
from tkinter import filedialog, messagebox
from tkinter.ttk import *
import subprocess
import pdb
from pygments import lex
from pygments.lexers import PythonLexer
from pygments.styles import get_style_by_name

# Function to open a file
def open_file():
    filepath = filedialog.askopenfilename(
        filetypes=[("Python Files", "*.py"), ("Text Files", "*.txt"), ("All Files", "*.*")]
    )
    if filepath:
        with open(filepath, "r") as file:
            code_editor.delete("1.0", tk.END)
            code_editor.insert(tk.END, file.read())
            code_editor.highlight_syntax()

# Function to save a file
def save_file():
    filepath = filedialog.asksaveasfilename(
        defaultextension=".txt",
        filetypes=[("Python Files", "*.py"), ("Text Files", "*.txt"), ("All Files", "*.*")]
    )
    if filepath:
        with open(filepath, "w") as file:
            file.write(code_editor.get("1.0", tk.END))

# Function to run the code
def run_code():
    code = code_editor.get("1.0", tk.END)
    process = subprocess.Popen(["python", "-c", code], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    output, error = process.communicate()
    if output:
        messagebox.showinfo("Output", output.decode())
    if error:
        messagebox.showerror("Error", error.decode())

# Function to start debugging
def start_debugging():
    code = code_editor.get("1.0", tk.END)
    pdb.run(code)

# Custom Text widget for code editor with syntax highlighting and auto-suggestions
class CodeEditor(tk.Text):
    def __init__(self, master, *args, **kwargs):
        super().__init__(master, *args, **kwargs)
        self.style = get_style_by_name("default")
        self.configure(
            font=("Courier New", 12),
            undo=True,
            wrap="word",
            autoseparators=True,
            maxundo=-1,
        )
        self.bind("<KeyRelease>", self.highlight_syntax)

    def highlight_syntax(self, event=None):
        code = self.get("1.0", tk.END)
        tokens = lex(code, PythonLexer())
        self.mark_set("range_start", "1.0")
        self.mark_set("range_end", "1.0")
        self.start_styling()
        for token, text in tokens:
            self.insert(tk.END, text, self.style.token)
        self.stop_styling()

    def start_styling(self):
        self.style.token = self.style.Token

    def stop_styling(self):
        self.tag_remove("Token", "1.0", tk.END)

# Create the main window
window = tk.Tk()
window.title("Python IDE")

# Configure the window to expand with the available space
window.rowconfigure(0, weight=1)
window.columnconfigure(0, weight=1)

# Text widget for code editor
code_editor = CodeEditor(window)
code_editor.grid(row=0, column=0, sticky="nsew")

# Create a scrollbar for the code editor
scrollbar = Scrollbar(window, command=code_editor.yview)
scrollbar.grid(row=0, column=1, sticky="ns")
code_editor.configure(yscrollcommand=scrollbar.set)

# Add menu options
menu_bar = tk.Menu(window)
file_menu = tk.Menu(menu_bar, tearoff=0)
edit_menu = tk.Menu(menu_bar, tearoff=0)
run_menu = tk.Menu(menu_bar, tearoff=0)
debug_menu = tk.Menu(menu_bar, tearoff=0)
options_menu = tk.Menu(menu_bar, tearoff=0)
help_menu = tk.Menu(menu_bar, tearoff=0)

# Add menu items to the File menu
file_menu.add_command(label="New File")
file_menu.add_command(label="Open File", command=open_file)
file_menu.add_command(label="Save File", command=save_file)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=window.quit)

# Add menu items to the Edit menu
edit_menu.add_command(label="Cut", command=lambda: code_editor.event_generate("<<Cut>>"))
edit_menu.add_command(label="Copy", command=lambda: code_editor.event_generate("<<Copy>>"))
edit_menu.add_command(label="Paste", command=lambda: code_editor.event_generate("<<Paste>>"))
edit_menu.add_command(label="Undo", command=lambda: code_editor.event_generate("<<Undo>>"))
edit_menu.add_command(label="Redo", command=lambda: code_editor.event_generate("<<Redo>>"))

# Add menu items to the Run menu
run_menu.add_command(label="Run", command=run_code)

# Add menu items to the Debug menu
debug_menu.add_command(label="Start Debugging", command=start_debugging)
debug_menu.add_command(label="Step Into")
debug_menu.add_command(label="Step Over")
debug_menu.add_command(label="Step Out")

# Add menu items to the Options menu
options_menu.add_command(label="Preferences")

# Add menu items to the Help menu
help_menu.add_command(label="About")

# Add the menus to the menu bar
menu_bar.add_cascade(label="File", menu=file_menu)
menu_bar.add_cascade(label="Edit", menu=edit_menu)
menu_bar.add_cascade(label="Run", menu=run_menu)
menu_bar.add_cascade(label="Debug", menu=debug_menu)
menu_bar.add_cascade(label="Options", menu=options_menu)
menu_bar.add_cascade(label="Help", menu=help_menu)

# Configure the window to use the menu bar
window.config(menu=menu_bar)

# Run IDE
window.mainloop()
