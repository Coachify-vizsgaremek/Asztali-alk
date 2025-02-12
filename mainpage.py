import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QLabel, QSpacerItem, QSizePolicy, QStackedWidget, QScrollArea
from PyQt5.QtCore import Qt, QPropertyAnimation, QRect
from PyQt5.QtGui import QPixmap, QIcon, QColor, QImage
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import numpy as np
import matplotlib.pyplot as plt  # Hozzáadott importálás

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
        self.logo_label.mousePressEvent = self.show_counters  # Logóra kattintás eseménykezelő
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
            elif button_text == "Grafikonok":
                button.clicked.connect(self.show_charts)
            nav_bar_layout.addWidget(button)

        # Spacer a menüpontok és az alja között
        nav_bar_layout.addSpacerItem(QSpacerItem(20, 100, QSizePolicy.Minimum, QSizePolicy.Expanding))

        # Fő tartalom jobb oldalon
        main_content_layout = QVBoxLayout()

        # StackedWidget a számlálóknak és grafikonoknak
        self.stacked_widget = QStackedWidget()

        # 1. Oldal: Számlálók
        counters_widget = QWidget()
        counters_layout = QVBoxLayout()

        main_label = QLabel("Regisztrált felhasználók", self)
        main_label.setAlignment(Qt.AlignCenter)
        main_label.setStyleSheet("font-size: 40px; color: orange; margin-top: 30px;")
        counters_layout.addWidget(main_label)

        self.user_counter = self.create_counter("1430", "Felhasználók")
        self.coach_counter = self.create_counter("865", "Edzők")
        self.client_counter = self.create_counter("565", "Kliensek")

        counters_layout.addWidget(self.user_counter)
        counters_layout.addWidget(self.coach_counter)
        counters_layout.addWidget(self.client_counter)

        counters_widget.setLayout(counters_layout)
        self.stacked_widget.addWidget(counters_widget)

        # 2. Oldal: Grafikonok
        charts_widget = QWidget()
        charts_layout = QVBoxLayout()  # Most már vertikális layoutot használunk

        # Görgethető terület a grafikonok számára
        scroll_area = QScrollArea()
        scroll_area.setWidgetResizable(True)

        # Grafikonok konténerének létrehozása
        charts_container = QWidget()
        charts_container_layout = QVBoxLayout()

        # Többféle grafikon hozzáadása
        charts_container_layout.addWidget(self.create_chart("Felhasználók eloszlása", "pie", [40, 60], ["Kliensek", "Edzők"]))
        charts_container_layout.addWidget(self.create_chart("Aktivitások havi bontásban", "bar", [50, 130, 400, 350, 500], ["Jan", "Feb", "Már", "Ápr", "Máj"]))
        charts_container_layout.addWidget(self.create_chart("Regisztrációk időbeli alakulása", "line", [50, 150, 100, 250, 880], ["Hét 1", "Hét 2", "Hét 3", "Hét 4", "Hét 5"]))
        charts_container_layout.addWidget(self.create_chart("Edzők teljesítménye", "barh", [80, 90, 70, 95, 85], ["Edző 1", "Edző 2", "Edző 3", "Edző 4", "Edző 5"]))
        charts_container_layout.addWidget(self.create_chart("Felhasználói aktivitás szórása", "scatter", np.random.rand(100) * 100, None, np.random.rand(100) * 100))

        charts_container.setLayout(charts_container_layout)
        scroll_area.setWidget(charts_container)

        # A görgethető grafikonok hozzáadása a layouthoz
        charts_layout.addWidget(scroll_area)

        charts_widget.setLayout(charts_layout)
        self.stacked_widget.addWidget(charts_widget)

        # Alapértelmezett oldal: Számlálók
        self.stacked_widget.setCurrentIndex(0)

        main_content_layout.addWidget(self.stacked_widget)

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

    def create_chart(self, title, chart_type, data, labels=None, y_data=None):
        """Grafikon generálása a megadott típus szerint."""
        fig = Figure(figsize=(10, 4))  # Csökkentett magasság a grafikonoknak
        canvas = FigureCanvas(fig)
        ax = fig.add_subplot(111)

        if chart_type == "pie":
            ax.pie(data, labels=labels, autopct="%1.1f%%", colors=["orange", "lightblue", "green", "red", "purple"])
        elif chart_type == "bar":
            ax.bar(labels, data, color="orange")
        elif chart_type == "line":
            ax.plot(labels, data, marker="o", color="orange", linewidth=2)
        elif chart_type == "barh":
            ax.barh(labels, data, color="orange")
        elif chart_type == "scatter":
            ax.scatter(data, y_data, color="orange", s=50)

        ax.set_title(title, color="orange", fontsize=14)  # Kisebb cím betűméret
        ax.set_facecolor("#222")
        fig.patch.set_facecolor("#222")
        ax.tick_params(colors="white")
        ax.grid(color="gray", linestyle="--", linewidth=0.5)

        return canvas

    def create_counter(self, value, label_text):
        widget = QWidget()
        layout = QVBoxLayout()
        layout.setAlignment(Qt.AlignCenter)
        widget.setStyleSheet("background-color: black; border-radius: 20px; padding: 20px;")
        
        label = QLabel(value, self)
        label.setAlignment(Qt.AlignCenter)
        label.setStyleSheet("font-size: 35px; color: orange; font-weight: bold;")
        
        sub_label = QLabel(label_text, self)
        sub_label.setAlignment(Qt.AlignCenter)
        sub_label.setStyleSheet("font-size: 20px; color: white;")
        
        layout.addWidget(label)
        layout.addWidget(sub_label)
        widget.setLayout(layout)
        
        widget.enterEvent = lambda event: self.animate_widget(widget, True)
        widget.leaveEvent = lambda event: self.animate_widget(widget, False)
        return widget

    def animate_widget(self, widget, enter):
        """Animáció a widgetre, amikor az egér belép vagy kilép."""
        animation = QPropertyAnimation(widget, b"geometry")
        animation.setDuration(200)
        rect = widget.geometry()
        if enter:
            animation.setEndValue(QRect(rect.x() - 10, rect.y() - 10, rect.width() + 20, rect.height() + 20))
        else:
            animation.setEndValue(QRect(rect.x() + 10, rect.y() + 10, rect.width() - 20, rect.height() - 20))
        animation.start()

    def show_charts(self):
        """Grafikonok megjelenítése."""
        self.stacked_widget.setCurrentIndex(1)

    def show_counters(self, event):
        """Számlálók megjelenítése."""
        self.stacked_widget.setCurrentIndex(0)

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
