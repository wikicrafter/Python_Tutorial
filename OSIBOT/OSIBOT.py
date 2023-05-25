import tkinter as tk

# Function to handle user queries and provide responses
def get_osi_model_info():
    query = user_input.get().strip().lower()

    osi_model = {
        "physical layer": {
            "description": "The Physical Layer deals with the physical transmission of data over the network.",
            "examples": "Examples include Ethernet cables, fiber optic cables, and wireless signals."
        },
        "data link layer": {
            "description": "The Data Link Layer provides error-free transmission of data frames between two nodes.",
            "examples": "Examples include Ethernet frames, MAC addresses, and switches."
        },
        "network layer": {
            "description": "The Network Layer handles logical addressing and routing of data packets.",
            "examples": "Examples include IP addresses, routers, and the Internet Protocol (IP)."
        },
        "transport layer": {
            "description": "The Transport Layer ensures reliable delivery of data segments between end systems.",
            "examples": "Examples include TCP (Transmission Control Protocol) and UDP (User Datagram Protocol). Well-known ports for common protocols are: HTTP (80), FTP (20, 21), SMTP (25), and DNS (53)."
        },
        "session layer": {
            "description": "The Session Layer establishes, manages, and terminates sessions between applications.",
            "examples": "Examples include session management protocols and APIs."
        },
        "presentation layer": {
            "description": "The Presentation Layer deals with data formatting, encryption, and compression.",
            "examples": "Examples include MIME (Multipurpose Internet Mail Extensions) and SSL/TLS (Secure Sockets Layer/Transport Layer Security)."
        },
        "application layer": {
            "description": "The Application Layer provides network services to the end-user applications.",
            "examples": "Examples include HTTP (Hypertext Transfer Protocol), FTP (File Transfer Protocol), and SMTP (Simple Mail Transfer Protocol). Well-known ports for common protocols are: HTTP (80), FTP (20, 21), SMTP (25), and DNS (53)."
        }
    }

    if query in osi_model:
        response = osi_model[query]["description"] + "\n\n" + "Examples:\n" + osi_model[query]["examples"]
    else:
        response = "I'm sorry, I don't have information about that specific OSI layer."

    response_label.config(text="ChatBot: " + response)

# Create the main GUI window
window = tk.Tk()
window.title("OSI Model Bot")
window.configure(bg="black")



# Create the user input field
user_input = tk.Entry(window, width=50)
user_input.pack()

# Create the submit button
submit_button = tk.Button(window, text="Submit", command=get_osi_model_info)
submit_button.pack()

# Create the response label
response_label = tk.Label(window, text="Bot: ", bg="black", fg="white")
response_label.pack()

# Start the GUI event loop
window.mainloop()
