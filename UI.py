import tkinter as tk
from tkinterdnd2 import DND_FILES, TkinterDnD
import scanner as sc
import serverBL as sv
import clientBL as cl
import server_mac_address as sv_mac

nameDevice = None


def listDevices(listbox):
    listbox.delete(0, tk.END)
    devices = sc.search_devices()
    for addr, name in devices:
        print(" %s - %s" % (addr, name))
    for addr, name in devices:
        listbox.insert(tk.END, f"{addr} - {name}")


def on_list_click(event):
    global nameDevice
    # Listbox'ta tıklanan öğenin değerini al
    selected_item = listbox.get(listbox.curselection())
    # Entry kutusuna tıklanan öğenin değerini yerleştir
    macEntry.delete(0, tk.END)
    macEntry.insert(0, selected_item.split()[0])
    nameDevice = selected_item.split("-")[1]


def open_client_window():
    global txt
    root.withdraw()  # Ana pencereyi gizle
    chatWindow = tk.Toplevel(root)
    window_width = 665
    window_height = 610
    ws = chatWindow.winfo_screenwidth()  # width of the screen
    hs = chatWindow.winfo_screenheight()  # height of the screen
    # calculate x and y coordinates for the Tk root window
    x = (ws / 2) - (window_width / 2)
    y = (hs / 2) - (window_height / 2)
    chatWindow.geometry('%dx%d+%d+%d' % (window_width, window_height, x, y))
    chatWindow.resizable(False, False)
    chatWindow.title("Client")
    chatWindow.protocol("WM_DELETE_WINDOW", lambda: close_window(chatWindow))

    cl.threaded(macEntry.get())
    BG_GRAY = "#ABB2B9"
    BG_COLOR = "#17202A"
    TEXT_COLOR = "#EAECEE"

    FONT = "Helvetica 14"
    FONT_BOLD = "Helvetica 13 bold"

    # Send function
    def send(event=None):
        get = "You(Client) -> " + e.get()
        txtController(1)
        txt.insert(tk.END, "\n" + get)
        txtController(0)
        word = e.get()
        e.delete(0, tk.END)
        cl.sendMessage(word)
        # get = e.get().lower()a


    lable1 = tk.Label(chatWindow, bg=BG_COLOR, fg=TEXT_COLOR, text="Welcome", font=FONT_BOLD, pady=10, width=20,
                      height=1).grid(
        row=0)

    txt = tk.Text(chatWindow, bg=BG_COLOR, fg=TEXT_COLOR, font=FONT, width=60, state=tk.DISABLED)
    txt.grid(row=1, column=0, columnspan=2)
    txt.config(state=tk.DISABLED)

    scrollbar = tk.Scrollbar(txt)
    scrollbar.place(relheight=1, relx=0.974)

    e = tk.Entry(chatWindow, bg="#2C3E50", fg=TEXT_COLOR, font=FONT, width=55)
    e.grid(row=2, column=0)
    e.bind('<Return>', send)

    sendButton = tk.Button(chatWindow, text="Send", font=FONT_BOLD, bg=BG_GRAY,
                     command=send).grid(row=2, column=1)

def txtController(integer):
    if integer == 1:
        txt.config(state=tk.NORMAL)
    else:
        txt.config(state=tk.DISABLED)

def open_server_window():
    global txt
    root.withdraw()  # Ana pencereyi gizle
    chatWindow = tk.Toplevel(root)
    window_width = 665
    window_height = 610
    ws = chatWindow.winfo_screenwidth()  # width of the screen
    hs = chatWindow.winfo_screenheight()  # height of the screen
    # calculate x and y coordinates for the Tk root window
    x = (ws / 2) - (window_width / 2)
    y = (hs / 2) - (window_height / 2)
    chatWindow.geometry('%dx%d+%d+%d' % (window_width, window_height, x, y))
    chatWindow.resizable(False, False)
    chatWindow.title("Server")
    chatWindow.protocol("WM_DELETE_WINDOW", lambda: close_window(chatWindow))
    serverMac = sv_mac.get_bluetooth_mac_windows()
    print(serverMac)
    sv.threaded(serverMac)
    BG_GRAY = "#ABB2B9"
    BG_COLOR = "#17202A"
    TEXT_COLOR = "#EAECEE"

    FONT = "Helvetica 14"
    FONT_BOLD = "Helvetica 13 bold"

    # Send function
    def send(event=None):
        get = "You(Server) -> " + e.get()
        txtController(1)
        txt.insert(tk.END, "\n" + get)
        txtController(0)
        word = e.get()
        e.delete(0, tk.END)
        sv.sendMessage(word)
        # get = e.get().lower()

    lable1 = tk.Label(chatWindow, bg=BG_COLOR, fg=TEXT_COLOR, text="Welcome", font=FONT_BOLD, pady=10, width=20,
                      height=1).grid(
        row=0)

    txt = tk.Text(chatWindow, bg=BG_COLOR, fg=TEXT_COLOR, font=FONT, width=60)
    txt.grid(row=1, column=0, columnspan=2)
    txt.config(state=tk.DISABLED)

    scrollbar = tk.Scrollbar(txt)
    scrollbar.place(relheight=1, relx=0.974)

    e = tk.Entry(chatWindow, bg="#2C3E50", fg=TEXT_COLOR, font=FONT, width=55)
    e.grid(row=2, column=0)
    e.bind('<Return>', send)
    sendButton = tk.Button(chatWindow, text="Send", font=FONT_BOLD, bg=BG_GRAY,
                     command=send).grid(row=2, column=1)


def setTxt(message):
    global nameDevice
    txt.insert(tk.END, "\n" + "Friend: " + message)


def close_window(window):
    window.destroy()  # Yeni pencereyi kapatir
    if sv.returnCheck() == True:
        sv.stop()
        sv.resetChange()
    window.destroy()
    root.deiconify()  # Ana pencereyi tekrar göster


# init
def init():
    global root, macEntry, listbox
    root = TkinterDnD.Tk()
    root.title("Device Selection")
    window_width = 300
    window_height = 300
    ws = root.winfo_screenwidth()  # width of the screen
    hs = root.winfo_screenheight()  # height of the screen
    # calculate x and y coordinates for the Tk root window
    x = (ws / 2) - (window_width / 2)
    y = (hs / 2) - (window_height / 2)
    root.geometry('%dx%d+%d+%d' % (window_width, window_height, x, y))
    root.resizable(False, False)

    # mac entry
    macEntry = tk.Entry(root)
    macEntry.pack()
    macEntry.place(x=10, y=30)

    buttonMac = tk.Button(root, text="Bağlan", command=open_client_window)
    buttonMac.pack()
    buttonMac.place(x=140, y=30, height=20)

    buttonServer = tk.Button(root, text="Create Chat Server", command=open_server_window)
    buttonServer.pack()
    buttonServer.place(x=190, y=30, width=100, height=20),

    # Listbox
    listbox = tk.Listbox(root, width=45, height=11)
    listbox.pack()
    listbox.place(x=10, y=100)
    listbox.bind('<<ListboxSelect>>', on_list_click)

    buttonListDevices = tk.Button(root, text="List Devices", command=lambda: listDevices(listbox), bg="black",
                                  fg="white", border=1)
    buttonListDevices.pack()
    buttonListDevices.place(x=10, y=60, width=280, height=20)

    root.mainloop()
