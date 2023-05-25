import tkinter as tk
from tkinter import ttk

# Function to handle user queries and provide responses
def get_osi_model_info(event=None):
    query = user_input.get().strip().lower()

    if query in osi_model:
        response = osi_model[query]["description"] + "\n\n" + "Examples:\n" + osi_model[query]["examples"]
    else:
        response = "I'm sorry, I don't have information about that specific OSI layer."

    response_text.configure(state='normal')
    response_text.delete('1.0', 'end')
    response_text.insert('1.0', response)
    response_text.configure(state='disabled')

    user_input.delete(0, 'end')

# Function to handle layer-specific questions
def ask_question(layer):
    question = osi_model[layer]["question"]
    response = osi_model[layer]["answer"]

    question_label.configure(text=question)
    response_text.configure(state='normal')
    response_text.delete('1.0', 'end')
    response_text.insert('1.0', response)
    response_text.configure(state='disabled')

# Function to show tooltip
def show_tooltip(event, text):
    tooltip_label.configure(text=text)
    tooltip_label.place(x=event.x_root, y=event.y_root, anchor='nw')

# Function to hide tooltip
def hide_tooltip(event):
    tooltip_label.place_forget()

# Create the main GUI window
window = tk.Tk()
window.title("OSI Model Bot")
window.configure(bg="white")
window.minsize(790, 400)  # Set a minimum window size
window.maxsize(window.winfo_width(), window.winfo_height())  # Set maximum window size

# Create the user input field
user_input = tk.Entry(window, width=50)
user_input.pack(pady=10)
user_input.focus()  # Set focus on the input field
user_input.bind('<Return>', get_osi_model_info)  # Bind the Enter key event

# Create buttons for each layer's question
osi_model = {
    "physical layer": {
        "question": "What is the purpose of the Physical Layer?",
        "answer": "The Physical Layer deals with the physical transmission of data over the network.",
        "description": "The Physical Layer is responsible for the physical transmission of data over the network.",
        "examples": "Examples include Ethernet cables, fiber optic cables, and wireless signals."
    },
    "data link layer": {
        "question": "What is the purpose of the Data Link Layer?",
        "answer": "The Data Link Layer provides error-free transmission of data frames between two nodes.",
        "description": "The Data Link Layer ensures error-free transmission of data frames between two nodes.",
        "examples": "Examples include Ethernet frames, MAC addresses, and switches."
    },
    "network layer": {
        "question": "What is the purpose of the Network Layer?",
        "answer": "The Network Layer handles logical addressing and routing of data packets.",
        "description": "The Network Layer handles logical addressing and routing of data packets.",
        "examples": "Examples include IP addresses, routers, and the Internet Protocol (IP)."
    },
    "transport layer": {
        "question": "What is the purpose of the Transport Layer?",
        "answer": "The Transport Layer ensures reliable delivery of data segments between end systems.",
        "description": "The Transport Layer ensures reliable delivery of data segments between end systems.",
        "examples": "Examples include TCP (Transmission Control Protocol) and UDP (User Datagram Protocol). Well-known ports for common protocols are: HTTP (80), FTP (20, 21), SMTP (25), and DNS (53)."
    },
    "session layer": {
        "question": "What is the purpose of the Session Layer?",
        "answer": "The Session Layer establishes, manages, and terminates sessions between applications.",
        "description": "The Session Layer establishes, manages, and terminates sessions between applications.",
        "examples": "Examples include session management protocols and APIs."
    },
    "presentation layer": {
        "question": "What is the purpose of the Presentation Layer?",
        "answer": "The Presentation Layer deals with data formatting, encryption, and compression.",
        "description": "The Presentation Layer deals with data formatting, encryption, and compression.",
        "examples": "Examples include MIME (Multipurpose Internet Mail Extensions) and SSL/TLS (Secure Sockets Layer/Transport Layer Security)."
    },
    "application layer": {
        "question": "What is the purpose of the Application Layer?",
        "answer": "The Application Layer provides network services to the end-user applications.",
        "description": "The Application Layer provides network services to the end-user applications.",
        "examples": "Examples include HTTP (Hypertext Transfer Protocol), FTP (File Transfer Protocol), and SMTP (Simple Mail Transfer Protocol). Well-known ports for common protocols are: HTTP (80), FTP (20, 21), SMTP (25), and DNS (53)."
    }
}

button_frame = ttk.Frame(window)
button_frame.pack()

for layer in osi_model:
    description = osi_model[layer]["description"]
    button = ttk.Button(button_frame, text=layer.title(), command=lambda l=layer: ask_question(l))
    button.pack(side='left', padx=5)
    button.bind('<Enter>', lambda event, desc=description: show_tooltip(event, desc))
    button.bind('<Leave>', hide_tooltip)

# Create a frame for the response
response_frame = ttk.Frame(window)
response_frame.pack(pady=10)

# Create a label for the current question
question_label = ttk.Label(response_frame, text="", font=("Arial", 12, "bold"))
question_label.pack(pady=5)

# Create a scrollable text widget for the response
response_text = tk.Text(response_frame, bg="white", fg="black", wrap="word", height=10)
response_text.pack(side="left", fill="both", expand=True)

# Create a scrollbar for the response text widget
scrollbar = ttk.Scrollbar(response_frame, command=response_text.yview)
scrollbar.pack(side="right", fill="y")
response_text.configure(yscrollcommand=scrollbar.set)
response_text.configure(state='disabled')  # Set the text widget as read-only

# Create a tooltip label
tooltip_label = ttk.Label(window, text="", background='#FFFFE0', relief='solid', padding=(5, 2))
tooltip_label.lower()  # Lower the tooltip label below other widgets

# Start the GUI event loop
window.mainloop()
