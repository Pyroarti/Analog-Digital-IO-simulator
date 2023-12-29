import sys
from PyQt6.QtCore import Qt, QMimeData
from PyQt6.QtGui import QPixmap, QDrag
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QLabel, QVBoxLayout, QHBoxLayout, QPushButton

from simulator_page import ControlWindow

class DraggableLabel(QLabel):
    def __init__(self, pixmap, parent=None):
        super().__init__(parent)
        self.setPixmap(pixmap)
        self.setScaledContents(True)  # Add this line if you want to scale the image to label size

    def mousePressEvent(self, event):
        if event.button() == Qt.MouseButton.LeftButton:
            drag = QDrag(self)
            mimeData = QMimeData()
            mimeData.setText(self.objectName())  # Use object name to identify the module type

            drag.setMimeData(mimeData)
            pixmap = self.pixmap().scaled(100, 100, Qt.AspectRatioMode.KeepAspectRatio)  # Optional: Scale pixmap for the drag
            drag.setPixmap(pixmap)

            drag.exec(Qt.DropAction.CopyAction)

class Workspace(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setAcceptDrops(True)
        self.slot_layouts = []  # To store layouts for each slot
        layout = QHBoxLayout(self)

        for _ in range(7):
            # Create a QVBoxLayout for each slot
            slot_layout = QVBoxLayout()

            # Create and configure the name label
            name_label = QLabel("Drop module here")
            name_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
            slot_layout.addWidget(name_label)

            # Create and configure the image label
            image_label = QLabel()
            image_label.setFixedSize(150, 150)
            image_label.setStyleSheet("border: 1px solid black;")
            image_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
            slot_layout.addWidget(image_label)

            # Add the slot layout to the main layout
            layout.addLayout(slot_layout)
            self.slot_layouts.append((name_label, image_label))  # Store the labels

    def dragEnterEvent(self, event):
        event.accept()

    def dropEvent(self, event):
        position = event.position()
        for name_label, image_label in self.slot_layouts:
            if image_label.geometry().contains(position.toPoint()):
                module_type = event.mimeData().text()
                image_path = f'assets/{module_type}.png'
                print(f"Attempting to load image from: {image_path}")  # Debug print
                pixmap = QPixmap(image_path)
                if pixmap.isNull():
                    print(f"Failed to load image: {image_path}")
                    return
                name_label.setText(module_type)  # Set the module name
                image_label.setPixmap(pixmap.scaled(image_label.size(), Qt.AspectRatioMode.KeepAspectRatio))
                break

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Main widget and layout
        self.centralWidget = QWidget()
        self.setCentralWidget(self.centralWidget)
        mainLayout = QVBoxLayout(self.centralWidget)

        # Workspace where modules are dragged to
        self.workspace = Workspace()
        mainLayout.addWidget(self.workspace)

        # Bottom row for draggable labels with names
        bottomRowLayout = QHBoxLayout()

        self.buildSetButton = QPushButton("Build Set", self)
        self.buildSetButton.clicked.connect(self.buildSet)
        mainLayout.addWidget(self.buildSetButton)

        # Function to create a draggable label with a name
        def createDraggableItem(image_path, name):
            itemLayout = QVBoxLayout()  # Vertical layout for each item (name + image)

            nameLabel = QLabel(name)  # Label for the name
            nameLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)
            itemLayout.addWidget(nameLabel)

            draggableLabel = DraggableLabel(QPixmap(image_path))
            draggableLabel.setObjectName(name)
            draggableLabel.setFixedSize(200, 200)  # Set a fixed size for the image
            itemLayout.addWidget(draggableLabel)

            return itemLayout

        # Add items to the bottom row layout
        bottomRowLayout.addLayout(createDraggableItem("assets/4AO.png", "4AO"))
        bottomRowLayout.addLayout(createDraggableItem("assets/8DI.png", "8DI"))
        bottomRowLayout.addLayout(createDraggableItem("assets/8DO.png", "8DO"))

        # Add bottom row layout to the main layout
        mainLayout.addLayout(bottomRowLayout)

    def buildSet(self):
        # Get the list of selected modules
        selected_modules = [name_label.text() for name_label, _ in self.workspace.slot_layouts if name_label.text() != "Drop module here"]
        # Open the ControlWindow with the selected modules
        if selected_modules:
            self.controlWindow = ControlWindow(selected_modules)
            self.controlWindow.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.show()
    sys.exit(app.exec())
