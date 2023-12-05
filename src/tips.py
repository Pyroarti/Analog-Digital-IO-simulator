
""" 680 is 4mA and 3446 is 20mA """
def sim_higher(app):
    t = 0
    while True:
        value1 = 680 + t
        value2 = 680 + t
        outputs.write_single(0, int(value1))
        outputs.write_single(1, int(value2))
        print(value1, value2)
        t += app.t_value
        sleep(0.1)

        if value1 >= 3446 or value2 >= 3446:
            sim_lower(app)
            break

def sim_lower(app):
    t = 0
    while True:
        value1 = 3446 - t
        value2 = 3446 - t
        outputs.write_single(0, int(value1))
        outputs.write_single(1, int(value2))
        print(value1, value2)
        t += app.t_value
        sleep(0.1)

        if value1 <= 680 or value2 <= 680:
            break


def set_value_4ma():
    outputs.write_single(0, 680)


def set_value_12ma():
    outputs.write_single(0, 2063)


def set_value_20ma():
    outputs.write_single(0, 3446)



