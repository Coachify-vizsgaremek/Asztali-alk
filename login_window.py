import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QVBoxLayout, QLineEdit,
                             QPushButton, QLabel, QMessageBox, QSpacerItem,
                             QSizePolicy, QHBoxLayout)
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap, QPalette, QBrush
from mainpage import MainPage  # MainPage importálása

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

        input_container = QWidget(self)
        input_layout = QVBoxLayout()

        self.username_input = QLineEdit(self)
        self.username_input.setPlaceholderText("Felhasználónév")
        self.username_input.setStyleSheet(self._input_style())
        input_layout.addWidget(self.username_input)

        self.password_input = QLineEdit(self)
        self.password_input.setPlaceholderText("Jelszó")
        self.password_input.setEchoMode(QLineEdit.Password)
        self.password_input.setStyleSheet(self._input_style())
        input_layout.addWidget(self.password_input)

        self.login_button = QPushButton("Bejelentkezés", self)
        self.login_button.setStyleSheet(self._button_style())
        self.login_button.clicked.connect(self.login)
        input_layout.addWidget(self.login_button)

        input_container.setLayout(input_layout)
        input_container.setStyleSheet("background-color: rgba(0, 0, 0, 0.5); border-radius: 20px; padding: 40px;")
        layout.addWidget(input_container)

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
        pixmap = QPixmap("elso.jpg").scaled(self.size(), Qt.KeepAspectRatioByExpanding, Qt.SmoothTransformation)
        palette = QPalette()
        palette.setBrush(QPalette.Background, QBrush(pixmap))
        self.setPalette(palette)

    def login(self):
        username = self.username_input.text()
        password = self.password_input.text()

        if username == "admin" and password == "admin":
            print("Bejelentkezés sikeres!")
            self.open_main_page()  # Átirányítás a főoldalra
            self.close()
        else:
            self.show_error_message(username, password)

    def open_main_page(self):
        self.main_page = MainPage()  # MainPage megnyitása
        self.main_page.show()

    def show_error_message(self, username, password):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Critical)
        msg.setWindowTitle("Hiba")
        if username != "admin" and password != "admin":
            msg.setText("Mind a felhasználónév, mind a jelszó hibás!")
        elif username != "admin":
            msg.setText("Hibás felhasználónév!")
        elif password != "admin":
            msg.setText("Hibás jelszó!")
        msg.exec_()

    @staticmethod
    def _input_style():
        return (
            "background-color: rgba(255, 255, 255, 0.8); color: #333; padding: 15px; border-radius: 10px;"
            "font-size: 18px; margin: 10px;"
        )

    @staticmethod
    def _button_style():
        return (
            "QPushButton { background-color: orange; color: white; font-size: 20px; padding: 15px 30px; border-radius: 10px; }"
            "QPushButton:hover { background-color: rgba(255, 69, 0, 0.8); color: white; }"
        )

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = LoginWindow()
    window.show()
    sys.exit(app.exec_())
