from io_classes import AnalogOut, DigitalIn, DigitalOut


class ModuleManager:
    def __init__(self):
        self.analog_outputs = []
        self.digital_inputs = []
        self.digital_outputs = []

    def create_analog_out(self):
        ao = AnalogOut()
        self.analog_outputs.append(ao)
        return ao

    def create_digital_in(self):
        di = DigitalIn()
        self.digital_inputs.append(di)
        return di

    def create_digital_out(self):
        do = DigitalOut()
        self.digital_outputs.append(do)
        return do