import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QLabel, QSpacerItem, QSizePolicy, QStackedWidget, QFrame
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

        main_layout = QHBoxLayout()
        nav_bar_widget = QWidget(self)
        nav_bar_widget.setFixedWidth(300)
        nav_bar_layout = QVBoxLayout()
        nav_bar_widget.setLayout(nav_bar_layout)
        nav_bar_widget.setStyleSheet("background-color: black;")

        nav_bar_layout.addSpacerItem(QSpacerItem(20, 50, QSizePolicy.Minimum, QSizePolicy.Fixed))
        self.logo_label = QLabel(self)
        pixmap = QPixmap("logo.jpg")
        self.logo_label.setPixmap(pixmap.scaled(200, 200, Qt.KeepAspectRatio, Qt.SmoothTransformation))
        self.logo_label.setAlignment(Qt.AlignCenter)
        self.logo_label.mousePressEvent = self.show_counters
        nav_bar_layout.addWidget(self.logo_label)
        nav_bar_layout.addSpacerItem(QSpacerItem(20, 100, QSizePolicy.Minimum, QSizePolicy.Fixed))

        menu_buttons = [
            ("Grafikonok", "icons/chart.png"),
            ("Edzők", "icons/coach.png"),
            ("Felhasználók", "icons/user.png"),
            ("Jogosultságok", "icons/permissions.png"),
            ("Kijelentkezés", "icons/logout.png"),
        ]

        for button_text, icon_path in menu_buttons:
            button = QPushButton(button_text, self)
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
            elif button_text == "Grafikonok":
                button.clicked.connect(self.show_charts)
            nav_bar_layout.addWidget(button)

        nav_bar_layout.addSpacerItem(QSpacerItem(20, 100, QSizePolicy.Minimum, QSizePolicy.Expanding))

        main_content_layout = QVBoxLayout()
        self.stacked_widget = QStackedWidget()
        counters_widget = QWidget()
        counters_layout = QVBoxLayout()

        main_label = QLabel("Regisztrációk", self)
        main_label.setAlignment(Qt.AlignLeft)
        main_label.setStyleSheet("font-size: 40px; color: orange; margin-top: 30px;")
        counters_layout.addWidget(main_label)

        self.user_counter = self.create_counter_box("Felhasználók: 1430")
        self.coach_counter = self.create_counter_box("Edzők: 865")
        self.client_counter = self.create_counter_box("Kliensek: 565")

        counters_layout.addWidget(self.user_counter)
        counters_layout.addWidget(self.coach_counter)
        counters_layout.addWidget(self.client_counter)

        counters_widget.setLayout(counters_layout)
        self.stacked_widget.addWidget(counters_widget)

        charts_widget = QWidget()
        charts_layout = QHBoxLayout()
        charts_layout.addWidget(self.create_chart("Összes ember", 50))
        charts_layout.addWidget(self.create_chart("Kliens", 30))
        charts_layout.addWidget(self.create_chart("Tréner", 20))
        charts_widget.setLayout(charts_layout)
        self.stacked_widget.addWidget(charts_widget)
        self.stacked_widget.setCurrentIndex(0)

        main_content_layout.addWidget(self.stacked_widget)
        main_content = QWidget(self)
        main_content.setLayout(main_content_layout)
        main_content.setStyleSheet("background-color: #222;")

        main_layout.addWidget(nav_bar_widget)
        main_layout.addWidget(main_content)
        self.setLayout(main_layout)

    def create_counter_box(self, text):
        box = QFrame()
        box.setStyleSheet("""
            QFrame {
                background-color: rgba(0, 0, 0, 150);
                border: 2px solid orange;
                border-radius: 15px;
                padding: 20px;
            }
        """)
        layout = QVBoxLayout()
        label = QLabel(text)
        label.setAlignment(Qt.AlignCenter)
        label.setStyleSheet("font-size: 30px; color: orange;")
        layout.addWidget(label)
        box.setLayout(layout)
        return box

    def create_chart(self, title, value):
        fig = Figure(figsize=(4, 4))
        canvas = FigureCanvas(fig)
        ax = fig.add_subplot(111)
        ax.pie([value, 100 - value], labels=[title, "Más"], colors=["orange", "gray"], autopct="%1.1f%%")
        ax.set_title(title, color="orange")
        return canvas

    def show_charts(self):
        self.stacked_widget.setCurrentIndex(1)

    def show_counters(self, event):
        self.stacked_widget.setCurrentIndex(0)

    def logout(self):
        self.close()
        from login_window import LoginWindow
        self.login_window = LoginWindow()
        self.login_window.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainPage()
    window.show()
    sys.exit(app.exec_())
