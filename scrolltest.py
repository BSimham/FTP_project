import os
import socket
from tkinter import *
from tkinter import ttk


s = socket.socket()
root = Tk()
root.title('Scroll test')
root.geometry("1400x600")


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

nb=1
def get_files():
    global nb
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
                Button(second_frame, width=50, text=f'{file}', fg='#ff1944', bg='blue').grid(row=nb,column=0,padx=1,pady=1)
                nb=nb+1

                continue

            # if os.path.isdir(os.path.join(locn[5:], file)):
            Button(second_frame, width=50, text=f'{file}',bg='green').grid(row=nb,column=0,padx=1,pady=1) # ,command=btn_clicked(os.path.join(locn, file)))
            nb=nb+1
            #    continue
            # file_btn = tk.Button(frame1, width=300, text=f'{file}')
            # file_btn.pack()
            print(file)

        if t:
            print(nb)
            break


# create a main frame
main_frame = Frame(root)
main_frame.pack(fill=BOTH, expand=1)

# create a canvas
my_canvas = Canvas(main_frame)
my_canvas.pack(side=LEFT, fill=BOTH, expand=1)

# Add a scroll bar to canvas
scroll_bar = Scrollbar(main_frame, orient=VERTICAL, command=my_canvas.yview)
scroll_bar.pack(side=RIGHT, fill=Y)

# configure canvas
my_canvas.configure(yscrollcommand=scroll_bar.set)
my_canvas.bind('<Configure>', lambda e: my_canvas.configure(scrollregion=my_canvas.bbox("all")))

# create another frame in canvas
second_frame = Frame(my_canvas)

# add the new frame to a window in the canvas
my_canvas.create_window((0, 0), window=second_frame, anchor='nw')

Addr_label = Label(second_frame, text="Server Address : ")
Addr_label.grid(row=0, sticky=E, padx=10)

Addr_etr = Entry(second_frame)
Addr_etr.grid(row=0, column=1, sticky=W, padx=10)

port_label = Label(second_frame, text="Port No : ")
port_label.grid(row=0, column=2, sticky=E, padx=10)
port_etr = Entry(second_frame)
port_etr.grid(row=0, column=3, sticky=W, padx=10)
cnt_button = Button(second_frame, text="Connect", width=40, height=5,command=set_connection)
cnt_button.grid(row=0, column=4)
lcn_label = Label(second_frame, text="Enter Location : ")
lcn_label.grid(row=0, column=5, sticky=E)
lcn_etr = Entry(second_frame)
lcn_etr.grid(row=0, column=6, sticky=W)
get_files_btn = Button(second_frame, text="GET files", command=get_files)
get_files_btn.grid(row=0, column=7)

# for thing in range(100):
#    Button(second_frame,text=f'Button {thing} bro').grid(row=thing+1,column=0,pady=10,padx=10)

root.mainloop()