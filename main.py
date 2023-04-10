from time import sleep

import customtkinter
from PIL import Image

try:
    from widgetlords.pi_spi import *
except ImportError as error:
    print(error, "You need to run this code on a raspberry pi")



BACKGROUND_IMAGE = "backround.jpg"

class App(customtkinter.CTk):
    """Class for the main app and main window"""
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


        self.geometry("400x500")
        self.title("4-20 analog simulator")

        self.resizable(False, False)

        self.bg_image = customtkinter.CTkImage(Image.open(BACKGROUND_IMAGE),
                                               size=(400, 780))
        
        self.bg_image_label = customtkinter.CTkLabel(self, image=self.bg_image)
        self.bg_image_label.place(x=0, y=0, relwidth=1, relheight=1)

        self.frame_1 = customtkinter.CTkFrame(master=self, bg_color="transparent")
        self.frame_1.place(relx=0.5, rely=0.5, anchor="center")

        self.frame_1 = customtkinter.CTkFrame(master=self)
        self.frame_1.pack(pady=20, padx=40, fill="both", expand=True)

        main_label = customtkinter.CTkLabel(master=self.frame_1, justify=customtkinter.LEFT,
                                            text="4-20 analog simulator",
                                            font=customtkinter.CTkFont(size=20, weight="bold"),
                                            bg_color="transparent")
        main_label.pack(pady=10, padx=10)

        button_explore = customtkinter.CTkButton(master=self.frame_1,
                                                 command=lambda: sim_higher(self),
                                                 text="4-20mA then 20-4mA")
        button_explore.pack(pady=10, padx=10)

try:
    outputs = Mod2AO()
except NameError as error:
    print(error, "You need to run this code on a raspberry pi")

""" 680 is 4mA and 3446 is 20mA """
def sim_higher():
    t = 0
    while True:
        value1 = 680 + t
        value2 = 680 + t
        outputs.write_single(0, int(value1))
        outputs.write_single(1, int(value2))
        print(value1, value2)
        t += 15
        sleep(0.1)

        if value1 >= 3446 or value2 >= 3446:
            sim_lower()
            break


def sim_lower():
    t = 0
    while True:
        value1 = 3446 - t
        value2 = 3446 - t
        outputs.write_single(0, int(value1))
        outputs.write_single(1, int(value2))
        print(value1, value2)
        t += 15
        sleep(0.1)

        if value1 <= 680 or value2 <= 680:
            break


def main():
    try:
        init()
    except NameError as error:
        print(error, "You need to run this code on a raspberry pi")
    app = App()
    app.mainloop()



if __name__ == "__main__":
    main()
