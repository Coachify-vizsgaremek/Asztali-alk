# loading_screen.py
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel
from PyQt5.QtCore import Qt, QTimer, QPropertyAnimation
from PyQt5.QtGui import QPixmap

class LoadingScreen(QWidget):
    def __init__(self, message=None, show_logo=False, show_text=False):
        super().__init__()
        self.setWindowTitle("Loading")
        self.showFullScreen()
        self.setStyleSheet("background-color: black;")

        layout = QVBoxLayout()
        
        if show_logo:
            self.logo = QLabel(self)
            self.logo.setAlignment(Qt.AlignCenter)
            self.logo.setPixmap(QPixmap("logo.jpg").scaledToWidth(200))
            layout.addWidget(self.logo)

        if show_text:
            self.label = QLabel("", self)
            self.label.setAlignment(Qt.AlignCenter)
            self.label.setStyleSheet("font-size: 120px; color: orange; font-weight: bold;")
            layout.addWidget(self.label)

            self.slogan_label = QLabel("Edzők, akik érted dolgoznak.", self)
            self.slogan_label.setAlignment(Qt.AlignCenter)
            self.slogan_label.setStyleSheet("font-size: 30px; color: white; margin-top: 20px;")
            layout.addWidget(self.slogan_label)

            self.counter = 0
            QTimer.singleShot(100, self.show_text)

        if message:
            self.message_label = QLabel(message, self)
            self.message_label.setAlignment(Qt.AlignCenter)
            self.message_label.setStyleSheet("font-size: 60px; color: orange; font-weight: bold;")  # Nagyobb betűméret és középre igazítás
            layout.addWidget(self.message_label)

        self.setLayout(layout)

        if message:
            QTimer.singleShot(2000, self.close)

    def show_text(self):
        if self.counter < len("COACHIFY"):
            self.label.setText("COACHIFY"[:self.counter + 1])
            self.counter += 1
            QTimer.singleShot(150, self.show_text)