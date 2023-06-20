from tkinter import*
from pytube import YouTube
from tkinter import messagebox, filedialog
root=Tk()
root.title('YT Vedio Downloader')
root.geometry("570x670")
root.configure(bg="black")
root.iconbitmap("favicon.ico")
def browse():
    download_Directory = filedialog.askdirectory(
    initialdir="YOUR DIRECTORY PATH", title="Save Video")
    download_Path.set(download_Directory)
    
def download():
    Youtube_link = video_Link.get()
    download_Folder = download_Path.get()
    getVideo = YouTube(Youtube_link)
    videoStream = getVideo.streams.first()
    videoStream.download(download_Folder)
    messagebox.showinfo("SUCCESSFULLY",
                        "DOWNLOADED AND SAVED IN\n"
                        + download_Folder)
video_Link = StringVar()
download_Path = StringVar()
t1=Entry(root,textvariable=video_Link)
t1.place(x=70,y=50)
t2=Entry(root,textvariable=download_Path)
t2.place(x=70,y=100)
btn=Button(text="Download", height=3, width=20, command=download)
btn1=Button(text="Browse", height=1, width=20,command=browse)
btn.place(x=180,y=150)
btn1.place(x=400,y=98)
lbl=Label(text="Enter link:", fg="white", bg="black")
lbl1=Label(text="Location:", fg="white", bg="black")
lbl.place(x=25,y=50)
lbl1.place(x=25,y=100)

root.mainloop()