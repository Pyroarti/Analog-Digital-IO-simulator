from time import sleep

from widgetlords.pi_spi import *

"""680 is 4mA and 3446 is 20mA"""

outputs = Mod2AO()

def sim_higher():
    t = 0
    while True:
        value1 = 680 + t
        value2 = 680 + t
        outputs.write_single(0, int(value1))
        outputs.write_single(1, int(value2))
        print(value1)
        print(value2)
        t += 15
        sleep(0.1)

        if value1 >= 3446 or value2 >= 3446:
            sim_lower()
            break


def sim_lower():
    t = 0
    while True:
        value1 = 680 - t
        value2 = 680 - t
        outputs.write_single(0, int(value1))
        outputs.write_single(1, int(value2))
        print(value1)
        print(value2)
        t += 15
        sleep(0.1)

        if value1 <= 680 or value2 <= 680:
            break


def main():
    init()
    sim_higher()


if __name__ == "__main__":
    main()
