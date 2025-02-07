import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QLabel, QSpacerItem, QSizePolicy
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap, QIcon, QColor, QImage
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import matplotlib.pyplot as plt

class MainPage(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Main Page")
        self.setGeometry(100, 100, 1200, 800)
        self.showFullScreen()

        # Fő layout: Horizontális, hogy a bal oldali navigáció és a fő tartalom elférjen
        main_layout = QHBoxLayout()

        # Navigációs sáv létrehozása
        nav_bar_widget = QWidget(self)
        nav_bar_widget.setFixedWidth(300)
        nav_bar_layout = QVBoxLayout()
        nav_bar_widget.setLayout(nav_bar_layout)
        nav_bar_widget.setStyleSheet("background-color: black;")

        # Spacer a logó felett
        nav_bar_layout.addSpacerItem(QSpacerItem(20, 50, QSizePolicy.Minimum, QSizePolicy.Fixed))

        # Logo hozzáadása nagyobb méretben
        self.logo_label = QLabel(self)
        pixmap = QPixmap("logo.jpg")
        self.logo_label.setPixmap(pixmap.scaled(200, 200, Qt.KeepAspectRatio, Qt.SmoothTransformation))
        self.logo_label.setAlignment(Qt.AlignCenter)
        nav_bar_layout.addWidget(self.logo_label)

        # Spacer a logó és menüpontok között (lejjebb tolás)
        nav_bar_layout.addSpacerItem(QSpacerItem(20, 100, QSizePolicy.Minimum, QSizePolicy.Fixed))

        # Menü gombok hozzáadása ikonokkal
        menu_buttons = [
            ("Grafikonok", "icons/chart.png"),
            ("Edzők", "icons/coach.png"),
            ("Felhasználók", "icons/user.png"),
            ("Jogosultságok", "icons/permissions.png"),
            ("Kijelentkezés", "icons/logout.png"),
        ]

        for button_text, icon_path in menu_buttons:
            button = QPushButton(button_text, self)
            colored_icon = self.colorize_icon(icon_path, QColor("orange"))
            button.setIcon(QIcon(colored_icon))
            button.setIconSize(button.sizeHint() / 1.5)
            button.setStyleSheet(""" 
                QPushButton {
                    background-color: transparent;
                    color: orange;
                    font-size: 22px;
                    font-weight: bold;
                    padding: 15px;
                    text-align: left;
                    border-radius: 15px;
                }
                QPushButton:hover {
                    background-color: orange;
                    color: black;
                }
            """)
            button.setFixedHeight(100)
            if button_text == "Kijelentkezés":
                button.clicked.connect(self.logout)
            nav_bar_layout.addWidget(button)

        # Spacer a menüpontok és az alja között
        nav_bar_layout.addSpacerItem(QSpacerItem(20, 100, QSizePolicy.Minimum, QSizePolicy.Expanding))

        # Fő tartalom jobb oldalon
        main_content_layout = QVBoxLayout()
        main_label = QLabel("Regisztrációk", self)
        main_label.setAlignment(Qt.AlignLeft)
        main_label.setStyleSheet("font-size: 40px; color: orange; margin-top: 30px;")
        main_content_layout.addWidget(main_label)

        # Matplotlib grafikonok hozzáadása
        chart_layout = QHBoxLayout()
        chart_layout.addWidget(self.create_chart("Összes ember", 50))  # Példa adatok
        chart_layout.addWidget(self.create_chart("Kliens", 30))
        chart_layout.addWidget(self.create_chart("Tréner", 20))

        main_content_layout.addLayout(chart_layout)

        main_content = QWidget(self)
        main_content.setLayout(main_content_layout)
        main_content.setStyleSheet("background-color: #222;")

        # Fő layout összerakása
        main_layout.addWidget(nav_bar_widget)
        main_layout.addWidget(main_content)

        self.setLayout(main_layout)

    def colorize_icon(self, image_path, color):
        """Színmódosított QPixmap készítése az ikonokból."""
        pixmap = QPixmap(image_path)
        image = pixmap.toImage().convertToFormat(QImage.Format_ARGB32)

        for y in range(image.height()):
            for x in range(image.width()):
                pixel_color = image.pixelColor(x, y)
                if pixel_color.alpha() > 0:  # Csak átlátszatlan pixeleket színezünk
                    image.setPixelColor(x, y, color)

        return QPixmap.fromImage(image)

    def create_chart(self, title, value):
        """Egyszerű matplotlib grafikon generálása."""
        fig = Figure(figsize=(4, 4))
        canvas = FigureCanvas(fig)
        ax = fig.add_subplot(111)

        # Példa grafikon: tortadiagram
        ax.pie([value, 100 - value], labels=[title, "Más"], colors=["orange", "gray"], autopct="%1.1f%%")
        ax.set_title(title, color="orange")

        return canvas

    def logout(self):
        """Kijelentkezés logika - visszadob a login oldalra."""
        self.close()  # Aktuális ablak bezárása
        
        # Késleltetett importálás
        from login_window import LoginWindow  # Késleltetett importálás a körkörös import elkerülésére
        
        self.login_window = LoginWindow()  # Új login ablak megnyitása
        self.login_window.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainPage()
    window.show()
    sys.exit(app.exec_())
