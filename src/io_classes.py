

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

class AnalogIn:
    """The Pi-SPi-8AI+ has 8 channel 4-20 mA input module"""
    # Dont have this one so it will wait
    pass


class AnalogOut:
    """The Pi-SPi-2AO provides 2 channels of 4-20 mA output and 
    simultaneous 2 channels of 0 to 10 VDC output."""

    def __init__(self):
        #self.module = Mod2AO()
        pass


    def set_current_output(self, channel, value):
        scaled_value = int((value - 4) * (4095 / 16))
        #self.module.write_single(channel, scaled_value)


    def set_voltage_output(self, channel, value):
        # Similar to set_current_output, but for voltage
        pass  # Implement voltage scaling and writing


class DigitalIn:
    """The Pi-SPi-8DI has 8 inputs that can either be DC or AC 
    (Max 24 V) and are optically isolated."""

    def __init__(self):
        #self.module = Mod8DI()
        pass

    def read_inputs(self):
        return self.module.read()
        # This will return the state of all 8 inputs


class DigitalOut:
    """The Pi-SPi-8KO has 2 SPDT relays and 6 relay signal outputs."""

    def __init__(self):
        #self.module = Mod8KO()
        pass

    def set_output(self, output_number, state):
  
        # convert the output_number and state to the appropriate format
        # that can be written to the module
        pass  # Implement the logic to set a specific output

    def read_outputs(self):
        # This method should read the current state of the outputs
        pass  # Implement the logic to read the outputs

