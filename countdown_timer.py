import time
from tkinter import *
from tkinter import messagebox

root = Tk()
root.geometry("300x250")
root.title("Countdown Timer App")
root.configure(bg="#5B5B5B")

hour = StringVar()
minute = StringVar()
second = StringVar()

hour.set("  0")
minute.set("  0")
second.set("  0")

hour_place = Entry(root, text="hours", width=3, font=("Arial", 18, "bold"),
                   textvariable=hour)
hour_place.place(x=80, y=20)
hour_place.configure(background="#7F7F7F", foreground="#060D0D")

minute_place = Entry(root, text="Minute", width=3, font=("Arial", 18, "bold"),
                     textvariable=minute)
minute_place.place(x=130, y=20)
minute_place.configure(background="#7F7F7F", foreground="#060D0D")

second_place = Entry(root, text="second", width=3, font=("Arial", 18, "bold"),
                     textvariable=second)
second_place.place(x=180, y=20)
second_place.configure(background="#7F7F7F", foreground="#060D0D")


def submit():
    try:

        temp = int(hour.get())*3600 + int(minute.get())*60 + int(second.get())
    except:
        print("Set the value ")
    while temp > -1:

        mins, secs = divmod(temp, 60)

        hours = 0
        if mins > 60:

            hours, mins = divmod(mins, 60)

        hour.set("{0:2d}".format(hours))
        minute.set("{0:2d}".format(mins))
        second.set("{0:2d}".format(secs))

        root.update()
        time.sleep(1)

        if (temp == 0):
            messagebox.showinfo("Alert", "Time's up ")

        temp -= 1


# option
btn2 = Button(root, text='Set Time Countdown', bd='0',
              width=19, bg="#B6B6B6", fg="#5B5B5B")
btn2.place(x=80, y=98)

btn = Button(root, text='Start', bd='5',
             bg="#B6B6B6", fg="#060D0D", width=15, command=submit)
btn.place(x=89, y=190)
root.mainloop()
