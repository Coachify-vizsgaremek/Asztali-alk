# login_window.py
import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QVBoxLayout, QLabel, QSpacerItem,
                             QSizePolicy, QHBoxLayout, QLineEdit, QPushButton, QMessageBox)
from PyQt5.QtCore import Qt, QTimer
from PyQt5.QtGui import QPixmap, QPalette, QBrush
from mainpage import MainPage  # MainPage importálása
from loading_screen import LoadingScreen  # LoadingScreen importálása

class LoginWindow(QWidget):
    def __init__(self, initial_load=True):  # Új paraméter: initial_load
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

        # Kezdő Loading Screen megjelenítése csak akkor, ha a program indul (initial_load=True)
        if initial_load:
            self.initial_loading_screen = LoadingScreen(show_logo=True, show_text=True)
            self.initial_loading_screen.show()
            QTimer.singleShot(3000, self.show_login_window)
        else:
            self.show()  # Ha kijelentkezés után jelenik meg, akkor azonnal megjelenik a login ablak

    def show_login_window(self):
        """Login ablak megjelenítése a kezdő loading screen után."""
        if hasattr(self, 'initial_loading_screen'):
            self.initial_loading_screen.close()
        self.show()
                
    def set_background_image(self):
        self.setAutoFillBackground(True)
        pixmap = QPixmap("elso.jpg").scaled(self.size(), Qt.KeepAspectRatioByExpanding, Qt.SmoothTransformation)
        palette = self.palette()
        palette.setBrush(QPalette.Background, QBrush(pixmap))
        self.setPalette(palette)

    def login(self):
        username = self.username_input.text()
        password = self.password_input.text()

        # Ellenőrizzük a felhasználónevet és a jelszót
        if (username == "admin1" and password == "admin1") or \
           (username == "admin2" and password == "admin2") or \
           (username == "admin3" and password == "admin3"):
            print("Bejelentkezés sikeres!")
            
            # Bejelentkezett admin nevének meghatározása
            admin_name = "Magda Ágoston" if username == "admin1" else \
                         "Kaiser Móric" if username == "admin2" else \
                         "Podhorányi Donát"
            
            # Bejelentkezés utáni loading screen megjelenítése
            self.post_login_loading_screen = LoadingScreen(f"Üdv, {admin_name}", show_logo=True)
            self.post_login_loading_screen.show()
            self.close()

            # Főoldal megnyitása
            QTimer.singleShot(2000, lambda: self.open_main_page(admin_name))
        else:
            self.show_error_message(username, password)

    def open_main_page(self, admin_name):
        self.main_page = MainPage(admin_name)
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
    login_window = LoginWindow()  # A program indulásakor a kezdő loading screen jelenik meg
    sys.exit(app.exec_())