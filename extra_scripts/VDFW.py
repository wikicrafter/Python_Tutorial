import tkinter as tk
from tkinter import filedialog
import threading
import youtube_dl

def select_directory():
    directory = filedialog.askdirectory()
    directory_path.set(directory)

def download_video():
    video_url = entry.get()
    download_path = directory_path.get()
    if not download_path:
        status_label.configure(text="Error: Please select a download location.")
        return
    
    # Disable the download button to prevent multiple downloads
    button.config(state=tk.DISABLED)
    
    def perform_download():
        ydl_opts = {
            'outtmpl': f'{download_path}/%(title)s.%(ext)s',
            'progress_hooks': [progress_hook],
        }
        
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            try:
                ydl.download([video_url])
            except:
                status_label.configure(text="Error: Unable to download the video.")
        
        # Re-enable the download button once the download is complete
        button.config(state=tk.NORMAL)

    # Start the download process in a separate thread
    download_thread = threading.Thread(target=perform_download)
    download_thread.start()

def progress_hook(progress):
    if progress['status'] == 'downloading':
        percent = round(progress['downloaded_bytes'] * 100 / progress['total_bytes'], 2)
        status_label.configure(text=f"Downloading: {percent}%")
        window.update()  # Update the GUI to reflect the changes
    elif progress['status'] == 'finished':
        status_label.configure(text="Download completed.")
    elif progress['status'] == 'error':
        status_label.configure(text=f"Error downloading: {progress['error']}")

# Create the main window
window = tk.Tk()
window.title("Video Downloader")

# Create GUI elements
title_label = tk.Label(window, text="Video Downloader", font=("Arial", 16, "bold"))
title_label.pack(pady=10)

url_label = tk.Label(window, text="Enter video URL:")
url_label.pack()

entry = tk.Entry(window, width=50)
entry.pack(pady=5)

directory_label = tk.Label(window, text="Select download directory:")
directory_label.pack()

directory_path = tk.StringVar()
directory_entry = tk.Entry(window, textvariable=directory_path, width=40)
directory_entry.pack(pady=5)

browse_button = tk.Button(window, text="Browse", command=select_directory)
browse_button.pack(pady=5)

button = tk.Button(window, text="Download", command=download_video)
button.pack(pady=10)

status_label = tk.Label(window, text="")
status_label.pack()

# Start the main GUI loop
window.mainloop()
