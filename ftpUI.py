# Huseyin Emre INAN
import tkinter as tk
from tkinterdnd2 import DND_FILES, TkinterDnD
import ftpClient as fc


def drop(event, entry_sv):
    entry_sv.set(event.data)

def listDirectories(listbox):
    listbox.delete(0, tk.END)
    file_list = fc.listFiles()
    print("AAAAA", file_list)
    for files in file_list:
        listbox.insert(tk.END, files)
    print(file_list)

def button_click3(entry, entry2, info):
    info['text'] = fc.changeFName(entry.get(), entry2.get())

def button_click2(entry, action_type, info):

    if action_type == "upload":
        fc.filenameUpload
        info["text"] = fc.uploadFile(entry.get())

    elif action_type == "download":
        info["text"] = fc.downloadFile(entry.get())

    elif action_type == "create":
        info["text"] = fc.createDir(entry.get())
    elif action_type == "delete":
        info["text"] = fc.deleteDir(entry.get())
    elif action_type == "changename":
        info['text'] = fc.changeFName()
    # elif action_type == "list":

    else:
        print("ERROR")


def button_click(entry1, entry2, entry3, info):
    input_text1 = entry1.get()
    input_text2 = entry2.get()
    input_text3 = entry3.get()
    print("Girilen host:", input_text1)
    print("Girilen user:", input_text2)
    print("Girilen passwd:", input_text3)
    info['text'] = res = fc.login(input_text1, input_text2, input_text3)
    #res = fc.login(input_text1, input_text2, input_text3)
    print(res[0:3])
    if (res[0:3] == "220"):
        info['foreground'] = "green"
    elif (res[0:3] == "400"):
        info['foreground'] = "red"
    else:
        info['foreground'] = "black"


def UIStart():
    root = TkinterDnD.Tk()
    root.title("FTP Processes")

    window_width = 800
    window_height = 300
    root.geometry(f"{window_width}x{window_height}")
    root.resizable(False, False)


    hostLabel = tk.Label(root, text="HOSTNAME:")
    userLabel = tk.Label(root, text="USERNAME:")
    passwdLabel = tk.Label(root, text="PASSWORD:")
    hostLabel.pack()
    userLabel.pack()
    passwdLabel.pack()
    hostLabel.place(x=10, y=30)
    userLabel.place(x=10, y=60)
    passwdLabel.place(x=10, y=90)

    entry0 = tk.Entry(root)
    entry0.pack()
    entry0.place(x=90, y=30)

    entry = tk.Entry(root)
    entry.pack()
    entry.place(x=90, y=60)

    entry2 = tk.Entry(root, show="*")
    entry2.pack()
    entry2.place(x=90, y=90)

    buttonAuth = tk.Button(root, text="Login", command=lambda: button_click(entry0, entry, entry2, info))
    buttonAuth.pack()
    buttonAuth.place(x=230, y=30, width=120, height=80)


    # drag & drop
    entry_sv = tk.StringVar()
    dragUpload = tk.Entry(root, textvar=entry_sv, width=80)

    dragUpload.insert(0, 'Upload file: path/drag')
    dragUpload.bind("<FocusIn>", lambda args: dragUpload.delete('0', 'end'))

    dragUpload.pack(fill=tk.X)
    dragUpload.drop_target_register(DND_FILES)
    dragUpload.dnd_bind('<<Drop>>', lambda event: drop(event, entry_sv))
    dragUpload.get
    dragUpload.place(x=10, y=120, width=200)

    buttonDragUpload = tk.Button(root, text="Upload", command=lambda: button_click2(dragUpload, "upload", info))
    buttonDragUpload.pack()
    buttonDragUpload.place(x=230, y=120, width=120, height=20)


    entryDownload = tk.Entry(root)
    entryDownload.insert(0, "Download file")
    entryDownload.bind("<FocusIn>", lambda args: entryDownload.delete('0', 'end'))
    entryDownload.pack()
    entryDownload.place(x=10, y=150, width=200)

    buttonDownload = tk.Button(root, text="Download", command=lambda: button_click2(entryDownload, "download", info))
    buttonDownload.pack()
    buttonDownload.place(x=230, y=150, width=120, height=20)


    entryCreateDir = tk.Entry(root)
    entryCreateDir.pack()
    entryCreateDir.insert(0, "Create directory")
    entryCreateDir.bind("<FocusIn>", lambda args: entryCreateDir.delete('0', 'end'))
    entryCreateDir.place(x=10, y=180, width=200)

    buttonCreateDir = tk.Button(root, text="CrDir", command=lambda: button_click2(entryCreateDir, "create",info))
    buttonCreateDir.pack()
    buttonCreateDir.place(x=230, y=180, width=120, height=20)


    entryDeleteDir = tk.Entry(root)
    entryDeleteDir.pack()
    entryDeleteDir.insert(0, "Delete directory")
    entryDeleteDir.bind("<FocusIn>", lambda args: entryDeleteDir.delete('0', 'end'))
    entryDeleteDir.place(x=10, y=210, width=200)

    buttonDeleteDir = tk.Button(root, text="Del Directory", command=lambda: button_click2(entryDeleteDir,"delete",info))
    buttonDeleteDir.pack()
    buttonDeleteDir.place(x=230, y=210, width=120, height=20)


    entryChangeFName = tk.Entry(root)
    entryChangeFName.pack()
    entryChangeFName.insert(0, "Chane file name")

    entryChanged = tk.Entry(root)
    entryChanged.pack()
    entryChanged.insert(0, "New name")

    entryChangeFName.bind("<FocusIn>", lambda args: entryChangeFName.delete('0', 'end'))
    entryChangeFName.place(x=10, y=240, width=100)

    entryChanged.bind("<FocusIn>", lambda args: entryChanged.delete('0', 'end'))
    entryChanged.place(x=120, y=240, width=100)

    #changed var bi de buna özel function lazım
    buttonChangeFName = tk.Button(root, text="Change File Name", command=lambda: button_click3(entryChangeFName, entryChanged, info))
    buttonChangeFName.pack()
    buttonChangeFName.place(x=230, y=240, width=120, height=20)

    listbox = tk.Listbox(root, width=66, height=13)
    listbox.pack()
    listbox.place(x=380, y=60)

    buttonList = tk.Button(root, text="List Server Files/Directories", command=lambda: listDirectories(listbox), bg="black",
                           fg="white", border=1)
    buttonList.pack()
    buttonList.place(x=380, y=30, width=400, height=20)


    info = tk.Label(root, text='')
    info.pack()
    info.place(x=10, y=270)


    root.mainloop()
