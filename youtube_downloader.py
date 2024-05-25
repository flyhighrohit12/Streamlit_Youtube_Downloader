import tkinter as tk
from pytube import YouTube
from tkinter import messagebox, simpledialog

def download_video():
    url = simpledialog.askstring("Input", "Enter the YouTube URL:")
    if url:
        yt = YouTube(url)
        stream = yt.streams.filter(progressive=True, file_extension='mp4').first()
        if stream:
            # Set filename
            filename = yt.title.replace('/', '-').replace('\\', '-').replace(':', '-').replace('|', '-').replace('*', '-').replace('?', '-').replace('"', '-').replace('<', '-').replace('>', '-') + ".mp4"
            # Download
            stream.download(filename=filename)
            messagebox.showinfo("Success", f"Video downloaded: {filename}")
        else:
            messagebox.showerror("Error", "Video could not be downloaded.")
    else:
        messagebox.showinfo("Cancelled", "No URL provided.")

root = tk.Tk()
root.title("YouTube Downloader")

download_button = tk.Button(root, text="Download Video", command=download_video)
download_button.pack(pady=20)

root.mainloop()
