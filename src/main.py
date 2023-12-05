import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QLabel, QVBoxLayout
from PyQt6.QtCore import Qt, QMimeData
from PyQt6.QtGui import QPixmap, QDrag


class DraggableLabel(QLabel):
    def __init__(self, pixmap, parent=None):
        super().__init__(parent)
        self.setPixmap(pixmap)

    def mousePressEvent(self, event):
        if event.button() == Qt.MouseButton.LeftButton:
            mimeData = QMimeData()
            mimeData.setText(self.objectName())  # Use object name to identify the module type

            drag = QDrag(self)
            drag.setMimeData(mimeData)
            drag.setPixmap(self.pixmap())

            drag.exec(Qt.DropAction.CopyAction)

class Workspace(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setAcceptDrops(True)

    def dragEnterEvent(self, event):
        event.accept()

    def dropEvent(self, event):
        module_type = event.mimeData().text()
        # Based on the module type, create and add the corresponding module widget to the workspace
        # For example, might create a new label with a specific pixmap depending on the module type

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.centralWidget = QWidget()
        self.setCentralWidget(self.centralWidget)
        layout = QVBoxLayout(self.centralWidget)

        # Create draggable labels (representing your modules)
        analogOutLabel = DraggableLabel(QPixmap(r"C:\Users\rober\Desktop\Programmering\Github\Analog_Digital_IO-simulator\assets\4AO.png"))
        analogOutLabel.setObjectName("AnalogOut")
        layout.addWidget(analogOutLabel)

        digitalInLabel = DraggableLabel(QPixmap(r"C:\Users\rober\Desktop\Programmering\Github\Analog_Digital_IO-simulator\assets\8DI.png"))
        digitalInLabel.setObjectName("DigitalIn")
        layout.addWidget(digitalInLabel)

        digitalOutLabel = DraggableLabel(QPixmap(r"C:\Users\rober\Desktop\Programmering\Github\Analog_Digital_IO-simulator\assets\8DO.png"))
        digitalOutLabel.setObjectName("DigitalOut")
        layout.addWidget(digitalOutLabel)

        self.workspace = Workspace()
        layout.addWidget(self.workspace)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.show()
    sys.exit(app.exec())
