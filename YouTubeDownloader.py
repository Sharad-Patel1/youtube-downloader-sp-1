import tkinter
import customtkinter
from pytube import YouTube


# Download video Function
def downloadVideo():
    try:
        ytLink = link.get()
        yt = YouTube(ytLink, on_progress_callback=onProgress)
        video = yt.streams.get_highest_resolution()
        title.configure(text=f"Downloading... {yt.title}", text_color="white")
        finLabel.configure(text="")
        video.download()
        # print("Download Complete!")
        finLabel.configure(text="Download Complete!")
    except:
        finLabel.configure(text="Error fetching URL.", text_color="red")


def onProgress(stream, chunk, bytes_remaining):
    totalSize = stream.filesize
    bytesDownloaded = totalSize - bytes_remaining
    percentageCompletion = (bytesDownloaded/totalSize) * 100
    percent = str(int(percentageCompletion))
    # Update Num
    progressNum.configure(text=percent+'%')
    progressNum.update()
    # Update Bar
    progressBar.set(percentageCompletion/100)

    # print(percentageCompletion)


# Design UI -- System Settings
customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue")

# Defaults -- App Frame
app = customtkinter.CTk()
app.geometry("720x480")
app.title("YouTube Video Downloader")

# UI Elements
# Title
title = customtkinter.CTkLabel(app, text="Insert a YouTube Link: ")
title.pack(padx=10, pady=20)

# Link input
userInput = tkinter.StringVar()
link = customtkinter.CTkEntry(
    app, width=350, height=40, textvariable=userInput)
link.pack()

# Finished Downloading
finLabel = customtkinter.CTkLabel(app, text="")
finLabel.pack()

# Download Button
download = customtkinter.CTkButton(app, text="Download", command=downloadVideo)
download.pack(padx=10, pady=20)


# Progress Bar & Number
progressNum = customtkinter.CTkLabel(app, text="0%")
progressNum.pack()

progressBar = customtkinter.CTkProgressBar(app, width=500)
progressBar.set(0)
progressBar.pack(padx=10, pady=20)

# Run app -- keep app open
app.mainloop()
