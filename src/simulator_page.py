from PyQt6.QtWidgets import QWidget, QLabel, QVBoxLayout, QPushButton, QSpinBox
from io_classes import AnalogOut, DigitalIn, DigitalOut, ModuleManager
import time
import sys

class ControlWindow(QWidget):
    def __init__(self, module_types, parent=None):
        super().__init__(parent)
        self.layout = QVBoxLayout(self)
        self.module_manager = ModuleManager()

        for module_type in module_types:
            if module_type == "4AO":  # Analog Out
                self.createAnalogOutControls()
            elif module_type == "8DI":  # Digital In
                self.createDigitalInControls()
            elif module_type == "8DO":  # Digital Out
                self.createDigitalOutControls()

        self.setLayout(self.layout)

    def createAnalogOutControls(self):
        ao = self.module_manager.create_analog_out()
        self.layout.addWidget(QLabel("Analog Output"))
        value_spinbox = QSpinBox()
        value_spinbox.setMaximum(20)  # Assuming 4-20 mA range
        value_spinbox.valueChanged.connect(lambda value, ao=ao: ao.set_current_output(0, value))  # Assuming channel 0 for simplicity
        self.layout.addWidget(value_spinbox)

    def createDigitalInControls(self):
        di = self.module_manager.create_digital_in()
        self.layout.addWidget(QLabel("Digital Input"))
        # Here, you can add controls to display the state of the digital inputs

    def createDigitalOutControls(self):
        do = self.module_manager.create_digital_out()
        self.layout.addWidget(QLabel("Digital Outputs"))

        # Example: Create a button for each digital output
        for i in range(8):  # Assuming 8 digital outputs
            button = QPushButton(f"Set Output {i}")
            button.clicked.connect(lambda checked, index=i, do=do: self.setDigitalOutput(do, index))
            self.layout.addWidget(button)

    def setDigitalOutput(self, do, index):
        # Placeholder for setting digital output
        # In a real scenario, you would call do.set_output(index, state) with the desired state
        print(f"Setting digital output {index}...")

        # Convert the index to the appropriate bitmask (1 << index)
        bitmask = 1 << index

        # Write the bitmask to the 8DO module
        do.write(bitmask)

        # Sleep for a moment (optional)
        time.sleep(1)
