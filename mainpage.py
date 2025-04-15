# mainpage.py
import sys
from PyQt5.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QLabel, QSpacerItem,
    QSizePolicy, QStackedWidget, QScrollArea, QTableWidget, QTableWidgetItem, QHeaderView, 
    QMessageBox, QLineEdit, QDialog, QFrame
)
from PyQt5.QtCore import Qt, QPropertyAnimation, QRect, QTimer
from PyQt5.QtGui import QPixmap, QIcon, QColor, QImage
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import numpy as np
import matplotlib.pyplot as plt
from api_client import APIClient
from loading_screen import LoadingScreen

class StatsPage(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Grafikonok")
        layout = QVBoxLayout(self)
        layout.setContentsMargins(10, 10, 10, 10)

        scroll_area = QScrollArea()
        scroll_area.setWidgetResizable(True)

        self.scroll_content = QWidget()
        self.scroll_layout = QVBoxLayout(self.scroll_content)
        self.scroll_layout.setAlignment(Qt.AlignTop)
        self.scroll_layout.setSpacing(30)

        self.scroll_content.setMinimumSize(1000, 2500)

        self.timer = QTimer()
        self.timer.timeout.connect(self.update_charts)
        self.timer.start(3000)

        self.update_charts()

        scroll_area.setWidget(self.scroll_content)
        layout.addWidget(scroll_area)

    def update_charts(self):
        for i in reversed(range(self.scroll_layout.count())):
            self.scroll_layout.itemAt(i).widget().setParent(None)

        users = APIClient.get_users()
        trainers = APIClient.get_trainers()

        if not users or not trainers:
            QMessageBox.warning(self, "Hiba", "Nincsenek adatok a grafikonok megjelenítéséhez.")
            return

        ages = [user['age'] for user in users]
        self.add_histogram(self.scroll_layout, ages, "Felhasználók életkora")

        specializations = {}
        for trainer in trainers:
            spec = trainer.get('specialization', 'Nincs megadva')
            specializations[spec] = specializations.get(spec, 0) + 1
        self.add_bar_chart(self.scroll_layout, list(specializations.keys()), list(specializations.values()), "Edzők specializációja")

        price_ranges = {}
        for trainer in trainers:
            price = trainer.get('price_range', 'Nincs megadva')
            price_ranges[price] = price_ranges.get(price, 0) + 1
        self.add_bar_chart(self.scroll_layout, list(price_ranges.keys()), list(price_ranges.values()), "Edzők árkategóriái")

        locations = {}
        for trainer in trainers:
            location = trainer.get('location', 'Nincs megadva')
            locations[location] = locations.get(location, 0) + 1
        self.add_bar_chart(self.scroll_layout, list(locations.keys()), list(locations.values()), "Edzők elhelyezkedése")

    def add_histogram(self, layout, data, title):
        fig, ax = plt.subplots(figsize=(10, 6))
        ax.hist(data, bins=10, color='orange', edgecolor='black')
        ax.set_title(title, color="orange", fontsize=16, pad=20)
        ax.set_facecolor("#222")
        fig.patch.set_facecolor("#222")
        ax.tick_params(colors="white")
        ax.grid(color="gray", linestyle="--", linewidth=0.5)
        ax.set_ylabel("Darabszám", color="white", fontsize=14)

        canvas = FigureCanvas(fig)
        layout.addWidget(canvas)

    def add_bar_chart(self, layout, labels, values, title):
        fig, ax = plt.subplots(figsize=(10, 6))
        fig.subplots_adjust(bottom=0.4)

        bars = ax.bar(labels, values, color='orange')
        ax.set_title(title, color="orange", fontsize=16, pad=20)
        ax.set_xticks(range(len(labels)))
        ax.set_xticklabels(labels, rotation=45, ha='right', color='white', fontsize=12)
        ax.set_facecolor("#222")
        fig.patch.set_facecolor("#222")
        ax.tick_params(colors="white")
        ax.grid(color="gray", linestyle="--", linewidth=0.5)
        ax.set_ylabel("Darabszám", color="white", fontsize=14)

        canvas = FigureCanvas(fig)
        layout.addWidget(canvas)

class MainPage(QWidget):
    def __init__(self, admin_name):
        super().__init__()
        self.admin_name = admin_name
        self.setWindowTitle("Main Page")
        self.setGeometry(100, 100, 1200, 800)
        self.showFullScreen()

        self.profiles_data = {
            "Magda Ágoston": {
                "image": "profilkepek/Agoston.jpg",
                "phone": "+36 30 123 4567",
                "email": "agoston@example.com",
                "working_hours": "9:00 - 17:00",
                "motivation": "Magda Ágoston, a Coachify weboldal fejlesztője, azért alapította a céget, hogy segítsen az embereknek egyszerűen és gyorsan megtalálni a számukra megfelelő személyi edzőt.",
                "role": "Weboldal fejlesztő",
                "age": 35,
                "gender": "Férfi",
                "nationality": "Magyar",
                "income": "*** HUF",
                "username": "admin1",
                "code": "***"
            },
            "Kaiser Móric": {
                "image": "profilkepek/Moric.jpg",
                "phone": "+36 30 234 5678",
                "email": "moric@example.com",
                "working_hours": "10:00 - 18:00",
                "motivation": "Kaiser Móric, a Coachify mobilalkalmazás fejlesztője, azért jött létre a cég, hogy az emberek bárhol és bármikor hozzáférhessenek a személyi edzőikhez.",
                "role": "Mobilalkalmazás fejlesztő",
                "age": 30,
                "gender": "Férfi",
                "nationality": "Magyar",
                "income": "*** HUF",
                "username": "admin2",
                "code": "***"
            },
            "Podhorányi Donát": {
                "image": "profilkepek/Donat.jpg",
                "phone": "+36 30 345 6789",
                "email": "donat@example.com",
                "working_hours": "8:00 - 16:00",
                "motivation": "Podhorányi Donát, a Coachify asztali alkalmazás fejlesztője, azért alapította a céget, hogy az emberek számára professzionális eszközöket biztosítson az edzésprogramok követésére.",
                "role": "Asztali alkalmazás fejlesztő",
                "age": 28,
                "gender": "Férfi",
                "nationality": "Magyar",
                "income": "*** HUF",
                "username": "admin3",
                "code": "***"
            }
        }

        main_layout = QHBoxLayout()

        # Navigációs sáv
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
        self.logo_label.mousePressEvent = lambda event: self.show_counters(event)
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
            elif button_text == "Edzők":
                button.clicked.connect(self.show_trainers)
            elif button_text == "Felhasználók":
                button.clicked.connect(self.show_users)
            elif button_text == "Jogosultságok":
                button.clicked.connect(self.show_permissions)
            nav_bar_layout.addWidget(button)

        nav_bar_layout.addSpacerItem(QSpacerItem(20, 100, QSizePolicy.Minimum, QSizePolicy.Expanding))

        # Fő tartalom
        main_content_layout = QVBoxLayout()
        self.stacked_widget = QStackedWidget()

        # 1. Oldal: Számlálók
        counters_widget = QWidget()
        counters_layout = QVBoxLayout()

        main_label = QLabel("Regisztrált felhasználók", self)
        main_label.setAlignment(Qt.AlignCenter)
        main_label.setStyleSheet("font-size: 40px; color: orange; margin-top: 30px;")
        counters_layout.addWidget(main_label)

        self.user_counter = self.create_counter("0", "Felhasználók")
        self.coach_counter = self.create_counter("0", "Edzők")
        self.client_counter = self.create_counter("0", "Kliensek")

        counters_layout.addWidget(self.user_counter)
        counters_layout.addWidget(self.coach_counter)
        counters_layout.addWidget(self.client_counter)

        counters_widget.setLayout(counters_layout)
        self.stacked_widget.addWidget(counters_widget)

        # 2. Oldal: Grafikonok
        self.stats_page = StatsPage()
        self.stacked_widget.addWidget(self.stats_page)

        # 3. Oldal: Jogosultságok / Profilok
        self.permissions_widget = QWidget()
        self.build_permissions_page()
        self.stacked_widget.addWidget(self.permissions_widget)

        # 4. Oldal: Edzők listája
        self.trainers_widget = QWidget()
        self.trainers_layout = QVBoxLayout()
        self.trainers_widget.setLayout(self.trainers_layout)
        self.stacked_widget.addWidget(self.trainers_widget)

        # 5. Oldal: Felhasználók listája
        self.users_widget = QWidget()
        self.users_layout = QVBoxLayout()
        self.users_widget.setLayout(self.users_layout)
        self.stacked_widget.addWidget(self.users_widget)

        self.stacked_widget.setCurrentIndex(0)
        main_content_layout.addWidget(self.stacked_widget)

        main_content = QWidget(self)
        main_content.setLayout(main_content_layout)
        main_content.setStyleSheet("background-color: #222;")

        main_layout.addWidget(nav_bar_widget)
        main_layout.addWidget(main_content)
        self.setLayout(main_layout)

        self.timer = QTimer()
        self.timer.timeout.connect(self.update_counters)
        self.timer.start(300)

    def update_counters(self):
        """Számlálók frissítése valós adatokkal."""
        users = APIClient.get_users()
        trainers = APIClient.get_trainers()

        num_users = len(users) if users else 0
        num_trainers = len(trainers) if trainers else 0

        self.user_counter.findChild(QLabel).setText(str(num_users + num_trainers))
        self.coach_counter.findChild(QLabel).setText(str(num_trainers))
        self.client_counter.findChild(QLabel).setText(str(num_users))

    def show_charts(self):
        """Grafikonok megjelenítése."""
        self.stacked_widget.setCurrentWidget(self.stats_page)

    def show_counters(self, event=None):
        """Számlálók megjelenítése."""
        self.stacked_widget.setCurrentIndex(0)

    def show_trainers(self):
        """Edzők listájának megjelenítése."""
        self.stacked_widget.setCurrentWidget(self.trainers_widget)
        self.load_trainers()

    def show_users(self):
        """Felhasználók listájának megjelenítése."""
        self.stacked_widget.setCurrentWidget(self.users_widget)
        self.load_users()

    def load_trainers(self):
        """Edzők adatainak betöltése és megjelenítése."""
        trainers = APIClient.get_trainers()
        if trainers:
            self.display_data_in_table(trainers, self.trainers_layout, 
                                     ["ID", "Név", "Település", "Specializáció", "Árkategória"], 
                                     "trainer")
        else:
            QMessageBox.warning(self, "Hiba", "Nem sikerült betölteni az edzők adatait.")

    def load_users(self):
        """Felhasználók adatainak betöltése és megjelenítése."""
        users = APIClient.get_users()
        if users:
            self.display_data_in_table(users, self.users_layout, 
                                     ["ID", "Név", "Életkor", "E-mail"], 
                                     "user")
        else:
            QMessageBox.warning(self, "Hiba", "Nem sikerült betölteni a felhasználók adatait.")

    def filter_table(self, text, data, layout, headers, item_type):
        """Táblázat szűrése név alapján."""
        try:
            filtered_data = []
            for item in data:
                if 'full_name' in item and text.lower() in item['full_name'].lower():
                    filtered_data.append(item)
            
            if not filtered_data and text:
                no_results_label = QLabel("Nincs találat a keresésre.")
                no_results_label.setStyleSheet("font-size: 20px; color: orange;")
                no_results_label.setAlignment(Qt.AlignCenter)
                
                while layout.count():
                    item = layout.takeAt(0)
                    widget = item.widget()
                    if widget:
                        widget.deleteLater()
                
                layout.addWidget(no_results_label)
                return
            
            self.display_data_in_table(filtered_data, layout, headers, item_type)
        except Exception as e:
            print(f"Hiba a szűrés során: {e}")
            QMessageBox.warning(self, "Hiba", "Hiba történt a keresés során.")

    def sort_table(self, data, layout, headers, sort_by, order, item_type):
        """Táblázat rendezése."""
        try:
            if sort_by == "id":
                sorted_data = sorted(data, key=lambda x: x.get("id", 0), reverse=(order == "desc"))
            elif sort_by == "name":
                sorted_data = sorted(data, key=lambda x: x.get("full_name", "").lower(), reverse=(order == "desc"))
            elif sort_by == "price":
                sorted_data = sorted(data, key=lambda x: float(x.get("price_range", "0").replace(' HUF', '').strip()), reverse=(order == "desc"))
            
            self.display_data_in_table(sorted_data, layout, headers, item_type)
        except Exception as e:
            print(f"Hiba a rendezés során: {e}")
            QMessageBox.warning(self, "Hiba", "Hiba történt a rendezés során.")

    def display_data_in_table(self, data, layout, headers, item_type):
        """Adatok megjelenítése táblázatban."""
        while layout.count():
            item = layout.takeAt(0)
            widget = item.widget()
            if widget:
                widget.deleteLater()

        search_layout = QHBoxLayout()
        search_field = QLineEdit()
        search_field.setPlaceholderText("Keresés név alapján...")
        search_field.setStyleSheet("""
            QLineEdit {
                font-size: 16px;
                padding: 8px;
                border: 2px solid orange;
                border-radius: 10px;
                background-color: #333;
                color: white;
            }
            QLineEdit:focus {
                border: 2px solid #ffb84d;
            }
        """)
        search_field.textChanged.connect(lambda text, data=data, layout=layout, headers=headers, item_type=item_type: 
                                     self.filter_table(text, data, layout, headers, item_type))
        search_layout.addWidget(search_field)

        if item_type == "user":
            sort_buttons = [
                ("ID ↑", "id", "asc"),
                ("ID ↓", "id", "desc"),
                ("Név A-Z", "name", "asc"),
                ("Név Z-A", "name", "desc")
            ]
        else:
            sort_buttons = [
                ("ID ↑", "id", "asc"),
                ("ID ↓", "id", "desc"),
                ("Név A-Z", "name", "asc"),
                ("Név Z-A", "name", "desc"),
                ("Ár ↑", "price", "asc"),
                ("Ár ↓", "price", "desc")
            ]

        for text, sort_by, order in sort_buttons:
            button = QPushButton(text)
            button.setStyleSheet("""
                QPushButton {
                    background-color: orange;
                    color: black;
                    font-size: 14px;
                    font-weight: bold;
                    padding: 8px;
                    border-radius: 8px;
                    margin-left: 5px;
                }
                QPushButton:hover {
                    background-color: #ffb84d;
                }
            """)
            button.clicked.connect(lambda _, data=data, layout=layout, headers=headers, 
                                 item_type=item_type, sort_by=sort_by, order=order: 
                                 self.sort_table(data, layout, headers, sort_by, order, item_type))
            search_layout.addWidget(button)

        layout.addLayout(search_layout)

        table = QTableWidget()
        table.setRowCount(len(data))
        table.setColumnCount(len(headers) + 2)
        table.setHorizontalHeaderLabels(headers + ["Törlés", "Módosítás"])

        for row_idx, row_data in enumerate(data):
            item_id = row_data.get('id')
            
            for col_idx, header in enumerate(headers):
                key = header.lower()
                if key == "név":
                    key = "full_name"
                elif key == "életkor":
                    key = "age"
                elif key == "e-mail":
                    key = "email"
                elif key == "település":
                    key = "location"
                elif key == "specializáció":
                    key = "specialization"
                elif key == "árkategória":
                    key = "price_range"
                
                item = QTableWidgetItem(str(row_data.get(key, "")))
                table.setItem(row_idx, col_idx, item)

            delete_button = QPushButton("Törlés")
            delete_button.setStyleSheet("""
                QPushButton {
                    background-color: red;
                    color: white;
                    font-size: 14px;
                    padding: 5px;
                    border-radius: 5px;
                }
                QPushButton:hover {
                    background-color: darkred;
                }
            """)
            delete_button.clicked.connect(lambda _, id=item_id, type=item_type: self.delete_item(id, type))
            table.setCellWidget(row_idx, len(headers), delete_button)

            edit_button = QPushButton("Módosítás")
            edit_button.setStyleSheet("""
                QPushButton {
                    background-color: orange;
                    color: black;
                    font-size: 14px;
                    padding: 5px;
                    border-radius: 5px;
                }
                QPushButton:hover {
                    background-color: #ffb84d;
                }
            """)
            edit_button.clicked.connect(lambda _, id=item_id, type=item_type: self.edit_item(id, type))
            table.setCellWidget(row_idx, len(headers) + 1, edit_button)

        table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        table.setStyleSheet("""
            QTableWidget {
                background-color: #222;
                color: white;
                font-size: 16px;
                border: 1px solid orange;
            }
            QHeaderView::section {
                background-color: orange;
                color: black;
                font-weight: bold;
                padding: 10px;
            }
        """)

        layout.addWidget(table)

    def edit_item(self, item_id, item_type):
        """Elem szerkesztése."""
        try:
            if item_type == "trainer":
                trainer_data = APIClient.get_trainer(item_id)
                if trainer_data:
                    self.open_edit_window(trainer_data, "trainer")
                else:
                    QMessageBox.warning(self, "Hiba", "Nem sikerült betölteni az edző adatait.")
            elif item_type == "user":
                user_data = APIClient.get_user(item_id)
                if user_data:
                    self.open_edit_window(user_data, "user")
                else:
                    QMessageBox.warning(self, "Hiba", "Nem sikerült betölteni a felhasználó adatait.")
        except Exception as e:
            print(f"Hiba a szerkesztés során: {e}")
            QMessageBox.warning(self, "Hiba", "Hiba történt a szerkesztés során.")

    def delete_item(self, item_id, item_type):
        """Elem törlése."""
        reply = QMessageBox.question(
            self,
            'Megerősítés',
            'Biztosan törölni szeretnéd ezt az elemet?',
            QMessageBox.Yes | QMessageBox.No,
            QMessageBox.No
        )
        
        if reply == QMessageBox.Yes:
            try:
                if item_type == "trainer":
                    success = APIClient.delete_trainer(item_id)
                    if success:
                        self.load_trainers()
                    else:
                        QMessageBox.warning(self, "Hiba", "Nem sikerült törölni az edzőt.")
                elif item_type == "user":
                    success = APIClient.delete_user(item_id)
                    if success:
                        self.load_users()
                    else:
                        QMessageBox.warning(self, "Hiba", "Nem sikerült törölni a felhasználót.")
                
                QMessageBox.information(self, "Siker", "Elem sikeresen törölve.")
            except Exception as e:
                print(f"Hiba a törlés során: {e}")
                QMessageBox.warning(self, "Hiba", "Hiba történt a törlés során.")

    def open_edit_window(self, data, item_type):
        """Szerkesztő ablak megnyitása."""
        edit_dialog = QDialog(self)
        edit_dialog.setWindowTitle("Szerkesztés")
        edit_dialog.resize(600, 400)
        layout = QVBoxLayout()

        self.edit_fields = {}
        for key, value in data.items():
            if key == "id":
                continue
                
            label = QLabel(key.capitalize())
            label.setStyleSheet("font-size: 16px; color: white;")
            layout.addWidget(label)

            edit_field = QLineEdit(str(value))
            edit_field.setStyleSheet("font-size: 16px; color: black; background-color: white;")
            layout.addWidget(edit_field)
            self.edit_fields[key] = edit_field

        button_layout = QHBoxLayout()
        
        save_button = QPushButton("Mentés")
        save_button.setStyleSheet("""
            QPushButton {
                background-color: orange;
                color: black;
                font-size: 16px;
                font-weight: bold;
                padding: 8px 16px;
                border-radius: 8px;
            }
            QPushButton:hover {
                background-color: #ffb84d;
            }
        """)
        save_button.clicked.connect(lambda: self.save_item(data["id"], item_type, self.get_edited_data()))
        button_layout.addWidget(save_button)

        cancel_button = QPushButton("Mégse")
        cancel_button.setStyleSheet("""
            QPushButton {
                background-color: red;
                color: white;
                font-size: 16px;
                font-weight: bold;
                padding: 8px 16px;
                border-radius: 8px;
            }
            QPushButton:hover {
                background-color: darkred;
            }
        """)
        cancel_button.clicked.connect(edit_dialog.close)
        button_layout.addWidget(cancel_button)

        layout.addLayout(button_layout)
        edit_dialog.setLayout(layout)
        edit_dialog.exec_()

    def get_edited_data(self):
        """Szerkesztett adatok összegyűjtése."""
        edited_data = {}
        for key, edit_field in self.edit_fields.items():
            edited_data[key] = edit_field.text()
        return edited_data

    def save_item(self, item_id, item_type, new_data):
        """Elem mentése."""
        try:
            if item_type == "trainer":
                success = APIClient.update_trainer(item_id, new_data)
            else:
                success = APIClient.update_user(item_id, new_data)

            if success:
                QMessageBox.information(self, "Siker", "Elem sikeresen frissítve.")
                if item_type == "trainer":
                    self.load_trainers()
                else:
                    self.load_users()
            else:
                QMessageBox.warning(self, "Hiba", "Nem sikerült frissíteni az elemet.")
        except Exception as e:
            print(f"Hiba a mentés során: {e}")
            QMessageBox.warning(self, "Hiba", "Hiba történt a mentés során.")

    def build_permissions_page(self):
        """Jogosultságok oldal felépítése."""
        self.permissions_widget = QWidget()
        permissions_layout = QHBoxLayout()

        profiles = [
            ("Magda Ágoston", "profilkepek/Agoston.jpg"),
            ("Kaiser Móric", "profilkepek/Moric.jpg"),
            ("Podhorányi Donát", "profilkepek/Donat.jpg"),
        ]

        for name, image_path in profiles:
            profile_widget = QWidget()
            profile_layout = QVBoxLayout()
            profile_widget.setStyleSheet("background-color: black; border-radius: 20px; padding: 20px;")

            profile_pic = QLabel()
            pic = QPixmap(image_path).scaled(450, 450, Qt.KeepAspectRatio, Qt.SmoothTransformation)
            profile_pic.setPixmap(pic)
            profile_pic.setAlignment(Qt.AlignCenter)
            profile_pic.setStyleSheet("border: 2px solid orange; border-radius: 10px; margin-bottom: 10px;")

            profile_pic.enterEvent = lambda event, widget=profile_pic: self.animate_profile_pic(widget, True)
            profile_pic.leaveEvent = lambda event, widget=profile_pic: self.animate_profile_pic(widget, False)

            name_label = QLabel(name)
            name_label.setAlignment(Qt.AlignCenter)
            name_label.setStyleSheet("font-size: 22px; font-weight: bold; color: orange;")

            details_button = QPushButton("Részletek")
            details_button.setStyleSheet("""
                QPushButton {
                    background-color: orange;
                    color: black;
                    font-size: 16px;
                    font-weight: bold;
                    padding: 8px 16px;
                    border-radius: 8px;
                }
                QPushButton:hover {
                    background-color: #ffb84d;
                }
            """)
            details_button.clicked.connect(lambda checked, name=name: self.show_profile_details(name))

            profile_layout.addWidget(profile_pic)
            profile_layout.addWidget(name_label)
            profile_layout.addWidget(details_button)
            profile_widget.setLayout(profile_layout)
            permissions_layout.addWidget(profile_widget)

        self.permissions_widget.setLayout(permissions_layout)

    def show_permissions(self):
        """Jogosultságok oldal megjelenítése."""
        self.stacked_widget.setCurrentWidget(self.permissions_widget)

    def show_profile_details(self, profile_name):
        """Profil részletek megjelenítése."""
        details_widget = QWidget()
        main_layout = QVBoxLayout()
        main_layout.setAlignment(Qt.AlignTop)
        
        data = self.profiles_data.get(profile_name, {})
        if not data:
            return
        
        content_layout = QVBoxLayout()
        content_layout.setSpacing(30)
        
        top_layout = QHBoxLayout()
        
        profile_pic = QLabel()
        pic = QPixmap(data["image"]).scaled(250, 250, Qt.KeepAspectRatioByExpanding, Qt.SmoothTransformation)
        profile_pic.setPixmap(pic)
        profile_pic.setStyleSheet("border: 5px solid orange; border-radius: 15px;")
        
        name_role_layout = QVBoxLayout()
        name_label = QLabel(f"{profile_name}")
        name_label.setStyleSheet("font-size: 32px; font-weight: bold; color: orange;")
        role_label = QLabel(f"<i>{data['role']}</i>")
        role_label.setStyleSheet("font-size: 22px; color: lightgray;")
        
        name_role_layout.addWidget(name_label)
        name_role_layout.addWidget(role_label)
        
        top_layout.addWidget(profile_pic)
        top_layout.addLayout(name_role_layout)
        top_layout.addStretch()
        
        middle_layout = QHBoxLayout()
        left_data_layout = QVBoxLayout()
        right_data_layout = QVBoxLayout()
        
        data_fields = {
            "Kor": data["age"],
            "Nem": data["gender"],
            "Nemzetiség": data["nationality"],
            "Jövedelem": data["income"],
            "E-mail": data["email"],
            "Telefonszám": data["phone"],
            "Felhasználónév": data["username"],
            "Kód": data["code"]
        }
        
        for index, (key, value) in enumerate(data_fields.items()):
            label = QLabel(f"<b>{key}:</b> {value}")
            label.setStyleSheet("font-size: 20px; color: white;")
            if index % 2 == 0:
                left_data_layout.addWidget(label)
            else:
                right_data_layout.addWidget(label)
        
        middle_layout.addLayout(left_data_layout)
        middle_layout.addLayout(right_data_layout)
        
        motivation_label = QLabel(data["motivation"])
        motivation_label.setWordWrap(True)
        motivation_label.setStyleSheet(
            "font-size: 20px; color: white; background-color: rgba(255,255,255,0.2);"
            "padding: 15px; border-radius: 10px; font-style: italic;"
        )
        
        back_button = QPushButton("Vissza")
        back_button.setStyleSheet(
            "background-color: orange; font-size: 18px; padding: 12px; border-radius: 10px;"
            "transition: background-color 0.3s ease-in-out;"
        )
        back_button.setCursor(Qt.PointingHandCursor)
        back_button.clicked.connect(self.back_to_permissions)
        
        content_layout.addLayout(top_layout)
        content_layout.addLayout(middle_layout)
        content_layout.addWidget(motivation_label)
        content_layout.addWidget(back_button, alignment=Qt.AlignCenter)
        
        main_layout.addLayout(content_layout)
        details_widget.setLayout(main_layout)
        
        self.stacked_widget.addWidget(details_widget)
        self.stacked_widget.setCurrentWidget(details_widget)

    def back_to_permissions(self):
        """Vissza a jogosultságok oldalra."""
        self.stacked_widget.setCurrentWidget(self.permissions_widget)

    def animate_profile_pic(self, widget, enter):
        """Profilkép animáció."""
        animation = QPropertyAnimation(widget, b"geometry")
        animation.setDuration(200)
        rect = widget.geometry()
        if enter:
            animation.setEndValue(QRect(rect.x() - 5, rect.y() - 5, rect.width() + 10, rect.height() + 10))
        else:
            animation.setEndValue(QRect(rect.x() + 5, rect.y() + 5, rect.width() - 10, rect.height() - 10))
        animation.start()

    def create_counter(self, value, label_text):
        """Számláló widget létrehozása."""
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
        """Widget animáció."""
        animation = QPropertyAnimation(widget, b"geometry")
        animation.setDuration(200)
        rect = widget.geometry()
        if enter:
            animation.setEndValue(QRect(rect.x() - 10, rect.y() - 10, rect.width() + 20, rect.height() + 20))
        else:
            animation.setEndValue(QRect(rect.x() + 10, rect.y() + 10, rect.width() - 20, rect.height() - 20))
        animation.start()

    def colorize_icon(self, image_path, color):
        """Ikon színezése."""
        pixmap = QPixmap(image_path)
        image = pixmap.toImage().convertToFormat(QImage.Format_ARGB32)

        for y in range(image.height()):
            for x in range(image.width()):
                pixel_color = image.pixelColor(x, y)
                if pixel_color.alpha() > 0:
                    image.setPixelColor(x, y, color)

        return QPixmap.fromImage(image)

    def logout(self):
        """Kijelentkezés."""
        self.close()

        self.loading_screen = LoadingScreen("Kijelentkezés...")
        self.loading_screen.show()

        QTimer.singleShot(500, self.show_login_window)

    def show_login_window(self):
        """Bejelentkező ablak megjelenítése."""
        from login_window import LoginWindow
        self.login_window = LoginWindow(initial_load=False)
        self.login_window.show()
        self.loading_screen.close()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainPage("Magda Ágoston")
    window.show()
    sys.exit(app.exec_())