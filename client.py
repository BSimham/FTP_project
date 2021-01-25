import socket
import tkinter as tk
import os
from tkinter import ttk

s = socket.socket()
window = tk.Tk()


class ScrollableFrame(ttk.Frame):
    def __init__(self, container, *args, **kwargs):
        super().__init__(container, *args, **kwargs)
        canvas = tk.Canvas(self)
        scrollbar = ttk.Scrollbar(self, orient="vertical", command=canvas.yview)
        self.scrollable_frame = ttk.Frame(canvas)

        self.scrollable_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(
                scrollregion=canvas.bbox("all")
            )
        )

        canvas.create_window((0,0), window=self.scrollable_frame, anchor="nw")

        canvas.configure(yscrollcommand=scrollbar.set)

        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")


frame1 = ScrollableFrame(window)


# frame3=tk.Frame(window,width=300,height=400)
# frame3.place(x=10,y=10)
# canvas = tk.Canvas(frame3)
# scroller = tk.Scrollbar(frame3, command=canvas.yview)
# canvas.configure(yscrollcommand=scroller.set)
# canvas.pack(side=tk.LEFT)
# canvas.create_window((0, 0), window=frame1, anchor='nw')

# scroller.pack(side=tk.RIGHT, fill=tk.Y)
# scroller.config(command=frame1)


# def myfunction(event):
#    canvas.configure(scrollregion=canvas.bbox("all"))


# frame1.bind("<Configure>", myfunction)


def set_connection():
    print(Addr_etr.get())

    adr = (Addr_etr.get())
    pn = (port_etr.get())
    print(type(pn))
    s.connect((adr, int(pn)))
    # c.connect(('localhost', 9999))
    # name=input('Enter your name')
    # c.send(name.encode())
    # print(c.recv(1024).decode())
    print("Connected to server")


def get_files():
    locn = 'locn:' + lcn_etr.get()
    s.sendall(locn.encode())
    # con=0
    while True:
        data = s.recv(1024).decode()
        # con+=1
        # print(con)
        if data == 'endlast':
            break
        t = 0
        for file in data.split('&'):
            if file == 'endlast':
                t = 1
                break
            if file == '':
                continue
            if '$' in file:
                continue

            if os.path.isfile(os.path.join(locn[5:], file)):
                file_btn = tk.Button(frame1.scrollable_frame, width=500, text=f'{file}', fg='#ff1944', bg='blue')
                file_btn.pack()
                continue

            # if os.path.isdir(os.path.join(locn[5:], file)):
            file_btn = tk.Button(frame1.scrollable_frame, width=500, text=f'{file}',bg='green')  # ,command=btn_clicked(os.path.join(locn, file)))
            file_btn.pack()
            #    continue
            # file_btn = tk.Button(frame1, width=300, text=f'{file}')
            # file_btn.pack()
            print(file)
        if t:
            break
    # print(s.recv(1024).decode())


"""
def btn_clicked(x):
    for widget in frame1.winfo_children():
        widget.destroy()
    s.sendall(x.encode())

    while True:
        data = s.recv(1024).decode()
        # con+=1
        # print(con)
        if data == 'endlast':
            break
        t = 0
        for file in data.split('&'):
            if file == 'endlast':
                t = 1
                break
            if file == '':
                continue
            if '$' in file:
                print(file+'2')
                continue

            if os.path.isfile(os.path.join(x[5:], file)):
                file_btn = tk.Button(frame1, width=300, text=f'{file}', fg='#ff1944', bg='blue')
                file_btn.pack()
                continue
            print(file)
            if os.path.isdir(os.path.join(x[5:], file)):
                file_btn = tk.Button(frame1, width=300, text=f'{file}',bg='green',command=btn_clicked(os.path.join(x,file)))
                file_btn.pack()
                continue
            file_btn = tk.Button(frame1, width=300, text=f'{file}')
            file_btn.pack()
        if t:
            break
"""

window.title("FTP Protocol connection")
# window.columnconfigure([0,1],minsize=50,weight=1)
# window.rowconfigure([0,1,2],minsize=50,weight=1)
frame = tk.Frame(window)
Addr_label = tk.Label(frame, text="Server Address : ")
Addr_label.grid(row=0, sticky=tk.E, padx=10)

Addr_etr = tk.Entry(frame)
Addr_etr.grid(row=0, column=1, sticky=tk.W, padx=10)

port_label = tk.Label(frame, text="Port No : ")
port_label.grid(row=0, column=2, sticky=tk.E, padx=10)
port_etr = tk.Entry(frame)
port_etr.grid(row=0, column=3, sticky=tk.W, padx=10)
cnt_button = tk.Button(frame, text="Connect", width=40, height=5, command=set_connection)
cnt_button.grid(row=0, column=4)
lcn_label = tk.Label(frame, text="Enter Location : ")
lcn_label.grid(row=0, column=5, sticky=tk.E)
lcn_etr = tk.Entry(frame)
lcn_etr.grid(row=0, column=6, sticky=tk.W)
get_files_btn = tk.Button(frame, text="GET files", command=get_files)
get_files_btn.grid(row=0, column=7)

frame.pack(fill=tk.X)

sp = tk.Button(frame1)
frame1.pack(fill=tk.Y)

window.mainloop()
