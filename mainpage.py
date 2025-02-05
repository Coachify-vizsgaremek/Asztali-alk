import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QLabel, QSpacerItem, QSizePolicy
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap

class MainPage(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Main Page")
        self.setWindowState(Qt.WindowMaximized)

        # Fő layout: Horizontális, hogy a bal oldali navigáció és a fő tartalom elférjen
        main_layout = QHBoxLayout()

        # Bal oldali navigációs sáv
        nav_bar_layout = QVBoxLayout()
        nav_bar_layout.setContentsMargins(0, 0, 0, 0)  # Ne legyenek margók

        # Kép a navigáció tetején (helyet foglal)
        self.profile_image = QLabel(self)
        pixmap = QPixmap("default_profile_image.jpg")  # Kép helye, amit később cserélünk
        self.profile_image.setPixmap(pixmap.scaled(150, 150, Qt.KeepAspectRatio))  # Kép méretezés
        self.profile_image.setAlignment(Qt.AlignCenter)
        nav_bar_layout.addWidget(self.profile_image)

        # Menü gombok
        menu_buttons = ["Dashboard", "Edzők", "Felhasználók", "Beállítások", "Kijelentkezés"]
        for button_text in menu_buttons:
            button = QPushButton(button_text, self)
            button.setStyleSheet("""
                background-color: rgba(0, 0, 0, 0.5);
                color: white;
                font-size: 18px;
                padding: 15px;
                border: none;
                border-radius: 5px;
                margin: 10px;
            """)
            nav_bar_layout.addWidget(button)

        # A bal oldali navigációs sáv (barna háttér)
        nav_bar = QWidget(self)
        nav_bar.setLayout(nav_bar_layout)
        nav_bar.setStyleSheet("""
            background-color: #333;  # Sötét háttér
            width: 25%;  # Az oldal 1/4-ét fogja elfoglalni
        """)

        # Fő tartalom jobb oldalon
        main_content_layout = QVBoxLayout()

        # Fő cím a jobb oldalon
        main_label = QLabel("Főoldal", self)
        main_label.setAlignment(Qt.AlignCenter)
        main_label.setStyleSheet("font-size: 30px; color: white; margin-top: 30px;")
        main_content_layout.addWidget(main_label)

        # A fő tartalom widget
        main_content = QWidget(self)
        main_content.setLayout(main_content_layout)
        main_content.setStyleSheet("""
            background-color: #222;  # Sötét háttér a jobb oldalon
            width: 75%;  # Az oldal 3/4-ét fogja elfoglalni
        """)

        # A teljes layout összerakása
        main_layout.addWidget(nav_bar)
        main_layout.addWidget(main_content)

        # A teljes ablak layout beállítása
        self.setLayout(main_layout)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainPage()
    window.show()
    sys.exit(app.exec_())
