from tkinter import *
import speedtest
import threading


def speedcheck():
    lab_down.config(text="Testing...")
    lab_up.config(text="Testing...")

    def run_speed_test():
        sp = speedtest.Speedtest()
        sp.get_best_server()
        down = str(round(sp.download() / (1024 * 1024), 2)) + " Mbps"
        up = str(round(sp.upload() / (1024 * 1024), 2)) + " Mbps"
        lab_down.config(text=down)
        lab_up.config(text=up)

    thread = threading.Thread(target=run_speed_test)
    thread.start()


sp = Tk()
sp.title("Internet Speed Test")
sp.geometry('500x600')
sp.config(bg='blue')

Label(sp, text="Internet Speed Test", font=('Times New Roman', 30, 'bold'), bg='blue', fg='white').place(x=40, y=40,
                                                                                                         height=50,
                                                                                                         width=380)

Label(sp, text="Download Speed", font=('Times New Roman', 20, 'bold'), bg='white', fg='black').place(x=40, y=130,
                                                                                                     height=40,
                                                                                                     width=380)
lab_down = Label(sp, text="00 Mbps", font=('Times New Roman', 25, 'bold'), bg='black', fg='white')
lab_down.place(x=40, y=180, height=50, width=380)

Label(sp, text="Upload Speed", font=('Times New Roman', 20, 'bold'), bg='white', fg='black').place(x=40, y=260,
                                                                                                   height=40, width=380)
lab_up = Label(sp, text="00 Mbps", font=('Times New Roman', 25, 'bold'), bg='black', fg='white')
lab_up.place(x=40, y=310, height=50, width=380)

button = Button(sp, text="Check Speed", font=('Times New Roman', 20, 'bold'), relief=RAISED, bg='red', fg='white',
                command=speedcheck)
button.place(x=40, y=400, height=50, width=380)

sp.mainloop()
