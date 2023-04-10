from time import sleep
import tkinter as tk
from PIL import Image, ImageTk

try:
    from widgetlords.pi_spi import *
except ImportError as error:
    print(error, "You need to run this code on a raspberry pi")

BACKGROUND_IMAGE = "backround.jpg"




class App(tk.Tk):
    """Class for the main app and main window"""
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.geometry("500x600")
        self.title("4-20 analog simulator")
        self.resizable(False, False)

        self.t_value = 0

        self.bg_image = ImageTk.PhotoImage(Image.open(BACKGROUND_IMAGE).resize((500, 880)))

        self.bg_image_label = tk.Label(self, image=self.bg_image)
        self.bg_image_label.place(x=0, y=0, relwidth=1, relheight=1)

        self.frame_1 = tk.Frame(master=self)
        self.frame_1.place(relx=0.5, rely=0.5, anchor="center")
        

        self.frame_1 = tk.Frame(master=self)
        self.frame_1.pack(pady=20, padx=40, fill="both", expand=True)
        

        main_label = tk.Label(master=self.frame_1, text="4-20 analog simulator",
                              font=("Helvetica", 20, "bold")
                              )
        main_label.pack(pady=10, padx=10)

        button_sim_high_low = tk.Button(master=self.frame_1,
                                   command=lambda: sim_higher(self),
                                   text="4-20mA then 20-4mA",
                                   width=18)
        button_sim_high_low.pack(pady=10, padx=10)

        button_set_value_4ma = tk.Button(master=self.frame_1,
                                   command=set_value_4ma,
                                   text="Set value to 4mA",
                                   width=18)
        button_set_value_4ma.pack(pady=10, padx=10)

        button_set_value_12ma = tk.Button(master=self.frame_1,
                                   command=set_value_12ma,
                                   text="Set value to 12mA",
                                   width=18)
        button_set_value_12ma.pack(pady=10, padx=10)

        button_set_value_20ma = tk.Button(master=self.frame_1,
                                   command=set_value_20ma,
                                   text="Set value to 20mA",
                                   width=18)
        button_set_value_20ma.pack(pady=10, padx=10)

        entry_box_label = tk.Label(master=self.frame_1, text="Set the time how fast it goes from 4-20 then 20-4 mA",
                              font=("Helvetica", 10)
                              )
        entry_box_label.pack(pady=5, padx=5)

        entry_box_label_tip = tk.Label(master=self.frame_1, text="Around 10 to 15 is pretty good values to use",
                              font=("Helvetica", 10)
                              )
        entry_box_label_tip.pack(pady=1, padx=1)

        def on_change(_):
            entered_value = time_entry_box.get()
            try:
                self.t_value = int(entered_value)
            except ValueError:
                print("Invalid input, please enter an integer value.")

        time_entry_box = tk.Entry(master=self.frame_1)
        time_entry_box.pack(pady=5, padx=5)
        time_entry_box.bind("<Return>", on_change)

        

try:
    outputs = Mod2AO()
except NameError as error:
    print(error, "You need to run this code on a raspberry pi")

""" 680 is 4mA and 3446 is 20mA """
def sim_higher(app):
    while True:
        value1 = 680 + app.t_value
        value2 = 680 + app.t_value
        outputs.write_single(0, int(value1))
        outputs.write_single(1, int(value2))
        print(value1, value2)
        t_value += 15
        sleep(0.1)

        if value1 >= 3446 or value2 >= 3446:
            sim_lower()
            break

def sim_lower(app):
    while True:
        value1 = 3446 - app.t_value
        value2 = 3446 - app.t_value
        outputs.write_single(0, int(value1))
        outputs.write_single(1, int(value2))
        print(value1, value2)
        t_value += 15
        sleep(0.1)

        if value1 <= 680 or value2 <= 680:
            break


def set_value_4ma():
    outputs.write_single(0, 680)


def set_value_12ma():
    outputs.write_single(0, 2063)


def set_value_20ma():
    outputs.write_single(0, 3446)

def main():
    try:
        init()
    except NameError as error:
        print(error, "You need to run this code on a raspberry pi")
    app = App()
    app.mainloop()

if __name__ == "__main__":
    main()
