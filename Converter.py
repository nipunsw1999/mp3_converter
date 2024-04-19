import tkinter as tk
from tkinter import filedialog
from moviepy.editor import VideoFileClip

def convert_to_mp3():
    file_path = file_entry.get()
    clip = VideoFileClip(file_path)
    audio = clip.audio
    audio.write_audiofile(file_path.replace('.mp4', '.mp3'))
    print(f"Converted {file_path} to mp3.")

root = tk.Tk()
root.title("Video MP3 Converter")

file_label = tk.Label(root, text="File")
file_label.pack()

file_entry = tk.Entry(root)
file_entry.pack()

browse_button = tk.Button(root, text="Browse", command=lambda: file_dialog())
browse_button.pack()

convert_button = tk.Button(root, text="Convert to mp3", command=convert_to_mp3)
convert_button.pack()

def file_dialog():
    file_path = filedialog.askopenfilename()
    file_entry.insert(0, file_path)

root.mainloop()