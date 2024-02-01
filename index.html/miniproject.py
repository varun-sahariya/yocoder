from tkinter import ttk  # Import ttk module
import speedtest

root = Tk()
root.title("Internet Speed Test")
root.geometry("720x720")
root.resizable(False, False)
root.configure(bg="#1a212d")

def Check():
    test = speedtest.Speedtest()
    test.get_best_server()  # Optionally, choose the best server before testing
    Uploading = round(test.upload() / (1024 * 1024), 2)
    downloading = round(test.download() / (1024 * 1024), 2)
    ping_value = test.results.ping

    upload.config(text=Uploading)
    download.config(text=downloading)
    Download.config(text=downloading)
    ping.config(text=ping_value)

# Your existing code...
# icon
image_icon = PhotoImage(file="logo.png")
root.iconphoto(False, image_icon)

# Images
Top = PhotoImage(file="top.png")
Label(root, image=Top, bg="#1a212d").pack()

Main = PhotoImage(file="main.png")
Label(root, image=Main, bg="#1a212d").pack(pady=(40, 0))

button = PhotoImage(file="button.png")
Button = Button(root, image=button, bg="#1a212d", bd=0, activebackground="#1a212d", cursor="hand2", command=Check)
Button.pack(pady=10)

# Labels
Label(root, text="Ping", font="arial 10 bold", bg="#384056").place(x=235, y=0)
Label(root, text="Download", font="arial 10 bold", bg="#384056").place(x=325, y=0)
Label(root, text="Upload", font="arial 10 bold", bg="#384056").place(x=445, y=0)

Label(root, text="MS", font="arial 7 bold", bg="#384056", fg="white").place(x=245, y=80)
Label(root, text="MBPS", font="arial 7 bold", bg="#384056", fg="white").place(x=345, y=80)
Label(root, text="MBPS", font="arial 7 bold", bg="#384056", fg="white").place(x=455, y=80)

Label(root, text="Download", font="arial 15 bold", bg="#384056", fg="white").place(x=320, y=280)
Label(root, text="MBPS", font="arial 15 bold", bg="#384056", fg="white").place(x=335, y=380)

ping = Label(root, text="00", font="arial 13 bold", bg="#384056", fg="white")
ping.place(x=250, y=60, anchor="center")

download = Label(root, text="00", font="arial 13 bold", bg="#384056", fg="white")
download.place(x=360, y=60, anchor="center")

upload = Label(root, text="00", font="arial 13 bold", bg="#384056", fg="white")
upload.place(x=470, y=60, anchor="center")

Download = Label(root, text="00", font="arial 40 bold", bg="#384056")
Download.place(x=365, y=350, anchor="center")

# Your existing code...
# icon
image_icon = PhotoImage(file="logo.png")
root.iconphoto(False, image_icon)

# Images
Top = PhotoImage(file="top.png")
Label(root, image=Top, bg="#1a212d").pack()

Main = PhotoImage(file="main.png")
Label(root, image=Main, bg="#1a212d").pack(pady=(40, 0))

button = PhotoImage(file="button.png")
Button = Button(root, image=button, bg="#1a212d", bd=0, activebackground="#1a212d", cursor="hand2", command=Check)
Button.pack(pady=10)

# Labels
Label(root, text="Ping", font="arial 10 bold", bg="#384056").place(x=235, y=0)
Label(root, text="Download", font="arial 10 bold", bg="#384056").place(x=325, y=0)
Label(root, text="Upload", font="arial 10 bold", bg="#384056").place(x=445, y=0)

Label(root, text="MS", font="arial 7 bold", bg="#384056", fg="white").place(x=245, y=80)
Label(root, text="MBPS", font="arial 7 bold", bg="#384056", fg="white").place(x=345, y=80)
Label(root, text="MBPS", font="arial 7 bold", bg="#384056", fg="white").place(x=455, y=80)

Label(root, text="Download", font="arial 15 bold", bg="#384056", fg="white").place(x=320, y=280)
Label(root, text="MBPS", font="arial 15 bold", bg="#384056", fg="white").place(x=335, y=380)

ping = Label(root, text="00", font="arial 13 bold", bg="#384056", fg="white")
ping.place(x=250, y=60, anchor="center")

download = Label(root, text="00", font="arial 13 bold", bg="#384056", fg="white")
download.place(x=360, y=60, anchor="center")

upload = Label(root, text="00", font="arial 13 bold", bg="#384056", fg="white")
upload.place(x=470, y=60, anchor="center")

Download = Label(root, text="00", font="arial 40 bold", bg="#384056")
Download.place(x=365, y=350, anchor="center")

root.mainloop()