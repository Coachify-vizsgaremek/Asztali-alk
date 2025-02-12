import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QVBoxLayout, QLabel, QSpacerItem,
                             QSizePolicy, QHBoxLayout, QLineEdit, QPushButton, QMessageBox)
from PyQt5.QtCore import Qt, QTimer, QPropertyAnimation
from PyQt5.QtGui import QPixmap, QPalette, QBrush
from mainpage import MainPage  # MainPage importálása

class LoadingScreen(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Loading")
        self.showFullScreen()
        self.setStyleSheet("background-color: black;")

        layout = QVBoxLayout()
        self.label = QLabel("", self)
        self.label.setAlignment(Qt.AlignCenter)
        self.label.setStyleSheet("font-size: 120px; color: orange; font-weight: bold;")
        layout.addWidget(self.label)

        self.logo = QLabel(self)
        self.logo.setAlignment(Qt.AlignCenter)
        self.logo.setPixmap(QPixmap("logo.jpg").scaledToWidth(200))
        self.logo.setVisible(False)
        layout.addWidget(self.logo)

        self.slogan_label = QLabel("Edzők, akik érted dolgoznak.", self)
        self.slogan_label.setAlignment(Qt.AlignCenter)
        self.slogan_label.setStyleSheet("font-size: 30px; color: white; margin-top: 20px;")
        self.slogan_label.setVisible(False)
        layout.addWidget(self.slogan_label)

        self.setLayout(layout)
        self.counter = 0
        self.logo_animation = None
        self.login_animation = None

        QTimer.singleShot(100, self.show_text)

    def show_text(self):
        if self.counter < len("COACHIFY"):
            self.label.setText("COACHIFY"[:self.counter + 1])
            self.counter += 1
            QTimer.singleShot(150, self.show_text)
        else:
            self.show_logo()

    def show_logo(self):
        self.logo.setVisible(True)
        self.logo_animation = QPropertyAnimation(self.logo, b"windowOpacity")
        self.logo_animation.setDuration(1000)
        self.logo_animation.setStartValue(0)
        self.logo_animation.setEndValue(1)
        self.logo_animation.start()
        QTimer.singleShot(500, self.show_slogan)

    def show_slogan(self):
        self.slogan_label.setVisible(True)
        QTimer.singleShot(1500, self.open_login)

    def open_login(self):
        self.login_window = LoginWindow()
        self.login_window.setWindowOpacity(0)
        self.login_window.show()

        self.login_animation = QPropertyAnimation(self.login_window, b"windowOpacity")
        self.login_animation.setDuration(1000)
        self.login_animation.setStartValue(0)
        self.login_animation.setEndValue(1)
        self.login_animation.start()

        self.close()

class LoginWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("COACHIFY - Admin Login")
        self.showFullScreen()

        layout = QVBoxLayout()
        self.label = QLabel("COACHIFY", self)
        self.label.setAlignment(Qt.AlignCenter)
        self.label.setStyleSheet("font-size: 120px; color: orange; font-weight: bold;")
        layout.addWidget(self.label)

        self.admin_label = QLabel("(ADMIN felület)", self)
        self.admin_label.setAlignment(Qt.AlignCenter)
        self.admin_label.setStyleSheet("font-size: 20px; color: white;")
        layout.addWidget(self.admin_label)

        self.slogan = QLabel("Edzők, akik érted dolgoznak.", self)
        self.slogan.setAlignment(Qt.AlignCenter)
        self.slogan.setStyleSheet("font-size: 40px; color: white; margin-bottom: 40px;")
        layout.addWidget(self.slogan)

        layout.addSpacerItem(QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding))

        self.username_input = QLineEdit(self)
        self.username_input.setPlaceholderText("Felhasználónév")
        self.username_input.setStyleSheet(self._input_style())
        layout.addWidget(self.username_input)

        self.password_input = QLineEdit(self)
        self.password_input.setPlaceholderText("Jelszó")
        self.password_input.setEchoMode(QLineEdit.Password)
        self.password_input.setStyleSheet(self._input_style())
        layout.addWidget(self.password_input)

        self.login_button = QPushButton("Bejelentkezés", self)
        self.login_button.setStyleSheet(self._button_style())
        self.login_button.clicked.connect(self.login)
        layout.addWidget(self.login_button)

        layout.addSpacerItem(QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding))

        close_button_container = QHBoxLayout()
        self.close_button = QPushButton("X", self)
        self.close_button.setStyleSheet("background-color: rgba(255, 69, 0, 0.5); color: white; font-size: 18px; border: none; border-radius: 5px;")
        self.close_button.setFixedSize(40, 40)
        self.close_button.clicked.connect(self.close)
        close_button_container.addWidget(self.close_button, alignment=Qt.AlignLeft)
        layout.addLayout(close_button_container)

        self.setLayout(layout)
        self.set_background_image()

    def set_background_image(self):
        self.setAutoFillBackground(True)
        pixmap = QPixmap("elso.jpg").scaled(self.size(), Qt.KeepAspectRatioByExpanding, Qt.SmoothTransformation)
        palette = self.palette()
        palette.setBrush(QPalette.Background, QBrush(pixmap))
        self.setPalette(palette)

    def login(self):
        username = self.username_input.text()
        password = self.password_input.text()

        if username == "admin" and password == "admin":
            print("Bejelentkezés sikeres!")
            self.open_main_page()
            self.close()
        else:
            self.show_error_message(username, password)

    def open_main_page(self):
        self.main_page = MainPage()
        self.main_page.show()

    def show_error_message(self, username, password):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Critical)
        msg.setWindowTitle("Hiba")
        msg.setText("Hibás felhasználónév vagy jelszó!")
        msg.exec_()

    @staticmethod
    def _input_style():
        return "background-color: rgba(255, 255, 255, 0.8); color: #333; padding: 15px; border-radius: 10px; font-size: 18px; margin: 10px; width: 300px;"

    @staticmethod
    def _button_style():
        return "QPushButton { background-color: orange; color: white; font-size: 20px; padding: 15px 30px; border-radius: 10px; } QPushButton:hover { background-color: rgba(255, 69, 0, 0.8); }"

if __name__ == '__main__':
    app = QApplication(sys.argv)
    loading_screen = LoadingScreen()
    loading_screen.show()
    sys.exit(app.exec_())
