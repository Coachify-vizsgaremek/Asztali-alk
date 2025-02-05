import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLineEdit, QPushButton, QLabel, QSpacerItem, QSizePolicy, QMessageBox
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap, QPalette, QBrush

class MainPage(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Main Page")
        self.setWindowState(Qt.WindowMaximized)

        layout = QVBoxLayout()
        main_label = QLabel("Main Page", self)
        main_label.setAlignment(Qt.AlignCenter)
        layout.addWidget(main_label)

        self.setLayout(layout)

class LoginWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("COACHIFY - Admin Login")
        
        # Beállítjuk az ablakot úgy, hogy teljes képernyős legyen
        self.setWindowState(Qt.WindowMaximized)

        # Layout
        layout = QVBoxLayout()

        # COACHIFY label
        self.label = QLabel("COACHIFY", self)
        self.label.setAlignment(Qt.AlignCenter)
        self.label.setStyleSheet("font-size: 60px; color: orange; font-weight: bold;")
        layout.addWidget(self.label)

        # ADMIN felület aláírás
        self.admin_label = QLabel("(ADMIN felület)", self)
        self.admin_label.setAlignment(Qt.AlignCenter)
        self.admin_label.setStyleSheet("font-size: 16px; color: orange; font-weight: normal; margin-top: 10px;")
        layout.addWidget(self.admin_label)

        # Slogan
        self.slogan = QLabel("Edzők, akik érted dolgoznak.", self)
        self.slogan.setAlignment(Qt.AlignCenter)
        self.slogan.setStyleSheet("font-size: 25px; color: white; margin-bottom: 30px;")
        layout.addWidget(self.slogan)

        # Spacer between slogan and input fields
        layout.addSpacerItem(QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding))

        # Create a container for inputs and button, centered
        input_container = QWidget(self)
        input_layout = QVBoxLayout()

        # Username input
        self.username_input = QLineEdit(self)
        self.username_input.setPlaceholderText("Felhasználónév")
        self.username_input.setStyleSheet("""
            background-color: rgba(255, 255, 255, 0.3);
            color: white;
            padding: 15px;
            border-radius: 10px;
            font-size: 18px;
            margin: 10px;
        """)
        input_layout.addWidget(self.username_input)

        # Password input
        self.password_input = QLineEdit(self)
        self.password_input.setPlaceholderText("Jelszó")
        self.password_input.setEchoMode(QLineEdit.Password)  # Jelszó rejtése
        self.password_input.setStyleSheet("""
            background-color: rgba(255, 255, 255, 0.3);
            color: white;
            padding: 15px;
            border-radius: 10px;
            font-size: 18px;
            margin: 10px;
        """)
        input_layout.addWidget(self.password_input)

        # Login button (átlátszó háttér hover effekttel)
        self.login_button = QPushButton("Bejelentkezés", self)
        self.login_button.setStyleSheet("""
            QPushButton {
                background-color: rgba(0, 0, 0, 0.2);  # Áttetsző háttér
                color: orange;
                font-size: 20px;
                padding: 15px 30px;
                border-radius: 10px;
                margin-top: 20px;
                width: fit-content;
                align-self: center;
            }
            QPushButton:hover {
                background-color: rgba(255, 69, 0, 0.6);  # Hover effekt (Narancssárga)
                color: white;
            }
        """)
        self.login_button.clicked.connect(self.login)
        input_layout.addWidget(self.login_button)

        # Create a surrounding box for the input fields
        input_container.setLayout(input_layout)
        input_container.setStyleSheet("""
            background-color: rgba(0, 0, 0, 0.6); 
            border-radius: 20px; 
            padding: 40px;
            width: 400px;  # A box szélessége
            height: 300px;  # A box magassága
        """)
        
        # Add the input container to the main layout
        layout.addWidget(input_container)

        # Spacer before the input fields
        layout.addSpacerItem(QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding))

        # Close button (X) at the top right corner
        self.close_button = QPushButton("X", self)
        self.close_button.setStyleSheet("""
            QPushButton {
                background-color: rgba(0, 0, 0, 0.3);  # Áttetsző háttér
                color: white;
                font-size: 25px;
                padding: 10px;
                border-radius: 10px;
                border: none;
                position: absolute;
                top: 20px;
                right: 20px;
                transition: background-color 0.3s ease;
            }
            QPushButton:hover {
                background-color: rgba(255, 69, 0, 0.5);  # Hover szín
            }
        """)
        self.close_button.setFixedSize(40, 40)
        self.close_button.clicked.connect(self.close)  # Bezárja az ablakot
        layout.addWidget(self.close_button)

        # Set layout to the window
        self.setLayout(layout)

        # Háttérkép beállítása
        self.set_background_image()

    def set_background_image(self):
        # Háttérkép beállítása a QPalette segítségével
        pixmap = QPixmap("elso.jpg")  # Beállítjuk a háttérképet
        palette = QPalette()
        palette.setBrush(QPalette.Background, QBrush(pixmap))  # A háttérre beállítjuk a pixmap-ot
        self.setPalette(palette)

    def login(self):
        # Log-in hitelesítés
        username = self.username_input.text()
        password = self.password_input.text()

        # Az admin felhasználó hitelesítése
        if username == "admin" and password == "admin":
            print("Bejelentkezés sikeres!")
            self.close()  # Bezárjuk a log-in ablakot
            self.open_main_page()  # Átirányítjuk a főoldalra
        else:
            print("Hibás felhasználónév vagy jelszó!")
            self.show_error_message(username, password)

    def open_main_page(self):
        self.main_page = MainPage()  # MainPage ablak megnyitása
        self.main_page.show()  # Az új ablakot láthatóvá tesszük

    def show_error_message(self, username, password):
        # Hibaüzenet létrehozása
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

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = LoginWindow()
    window.show()
    sys.exit(app.exec_())
