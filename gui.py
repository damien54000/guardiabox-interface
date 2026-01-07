import sys
from PyQt6.QtWidgets import (
    QApplication, QWidget, QLabel, QLineEdit,
    QPushButton, QGridLayout, QStackedWidget, QFileDialog
)
from PyQt6.QtGui import QIcon
from PyQt6.QtCore import Qt
from db.creation_compte import create_user
from db.connexion_compte import login_user
from db.actions import log_action
from security.chiffrement_secu import chiffrement_message, chiffrement_fichier
from security.dechiffrement_sec import dechiffrement_message, dechiffrement_fichier

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.user_id = None

        self.setWindowTitle("GuardiaBox")
        self.setWindowIcon(QIcon("assets/img/icon.jpeg"))
        self.setContentsMargins(20, 20, 20, 20)
        self.resize(400, 250)

        # parcourir les pages dans une seule fenêtre
        self.stack = QStackedWidget()
        main_layout = QGridLayout()
        main_layout.addWidget(self.stack)
        self.setLayout(main_layout)

        #création des pages
        self.page_login()
        self.page_menu()
        self.page_chiffrement()
        self.page_chiffrement_message()
        self.page_chiffrement_fichier()
        self.page_dechiffrement()
        self.page_dechiffrement_message()
        self.page_dechiffrement_fichier()

        self.stack.setCurrentIndex(0)

    #page créer un compte et se connecter
    def page_login(self):
        page = QWidget()
        layout = QGridLayout()

        title = QLabel("Connexion")
        title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(title, 0, 0, 1, 2)

        layout.addWidget(QLabel("Nom d'utilisateur :"), 1, 0)
        self.input_user = QLineEdit()
        layout.addWidget(self.input_user, 1, 1)

        layout.addWidget(QLabel("Mot de passe :"), 2, 0)
        self.input_password = QLineEdit()
        self.input_password.setEchoMode(QLineEdit.EchoMode.Password)
        layout.addWidget(self.input_password, 2, 1)

        bouton_login = QPushButton("Se connecter")
        bouton_register = QPushButton("Créer un compte")

        layout.addWidget(bouton_login, 3, 0)
        layout.addWidget(bouton_register, 3, 1)

        page.setLayout(layout)
        self.stack.addWidget(page)

        bouton_login.clicked.connect(self.handle_login)
        bouton_register.clicked.connect(self.handle_register)

        self.message_box = QLabel("")
        layout.addWidget(self.message_box, 4, 0, 1, 2)


    #menu principal
    def page_menu(self):
        page = QWidget()
        layout = QGridLayout()

        title = QLabel("Menu principal")
        title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(title, 0, 0, 1, 2)

        bouton_chiffrer = QPushButton("Chiffrer")
        bouton_dechiffrer = QPushButton("Déchiffrer")
        bouton_logout = QPushButton("Déconnexion")

        bouton_chiffrer.clicked.connect(lambda: self.stack.setCurrentIndex(2))
        bouton_dechiffrer.clicked.connect(lambda: self.stack.setCurrentIndex(5))
        bouton_logout.clicked.connect(lambda: self.stack.setCurrentIndex(0))

        layout.addWidget(bouton_chiffrer, 1, 0, 1, 2)
        layout.addWidget(bouton_dechiffrer, 2, 0, 1, 2)
        layout.addWidget(bouton_logout, 3, 0, 1, 2)

        page.setLayout(layout)
        self.stack.addWidget(page)
    
    def handle_login(self):
        username = self.input_user.text()
        password = self.input_password.text()

        user_id = login_user(username, password)

        if user_id is None:
            self.show_error("Identifiants incorrects")
            return

        self.user_id = user_id
        self.stack.setCurrentIndex(1)  # Menu principal

    def handle_register(self):
        username = self.input_user.text()
        password = self.input_password.text()

        try:
            create_user(username, password)
            self.show_info("Compte créé, connectez-vous")
        except Exception as e:
            self.show_error(str(e))

    def show_error(self, message):
        self.message_box.setText(message)

    def show_info(self, message):
        self.message_box.setText(message)


    #page chiffrement
    def page_chiffrement(self):
        page = QWidget()
        layout = QGridLayout()

        title = QLabel("Chiffrement")
        title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(title, 0, 0, 1, 2)

        bouton_message = QPushButton("Chiffrer un message")
        bouton_file = QPushButton("Chiffrer un fichier")
        bouton_back = QPushButton("Retour")

        bouton_back.clicked.connect(lambda: self.stack.setCurrentIndex(1))

        layout.addWidget(bouton_message, 1, 0, 1, 2)
        layout.addWidget(bouton_file, 2, 0, 1, 2)
        layout.addWidget(bouton_back, 3, 0, 1, 2)

        page.setLayout(layout)
        self.stack.addWidget(page)

        bouton_message.clicked.connect(
            lambda: self.stack.setCurrentIndex(3)
        )

        bouton_file.clicked.connect(
            lambda: self.stack.setCurrentIndex(4)
        )


    def page_chiffrement_message(self):
        page = QWidget()
        layout = QGridLayout()

        layout.addWidget(QLabel("Chiffrer un message"), 0, 0, 1, 2)

        layout.addWidget(QLabel("Message :"), 1, 0)
        self.input_chiffrement_message = QLineEdit()
        layout.addWidget(self.input_chiffrement_message, 1, 1)

        layout.addWidget(QLabel("Mot de passe :"), 2, 0)
        self.input_chiffrement_password = QLineEdit()
        self.input_chiffrement_password.setEchoMode(QLineEdit.EchoMode.Password)
        layout.addWidget(self.input_chiffrement_password, 2, 1)

        self.result_box_chiffrement = QLineEdit()
        layout.addWidget(self.result_box_chiffrement, 3, 0, 1, 2)

        bouton_chiffrer = QPushButton("Chiffrer")
        bouton_chiffrer.clicked.connect(self.handle_chiffrement_message)

        bouton_back = QPushButton("Retour")
        bouton_back.clicked.connect(lambda: self.stack.setCurrentIndex(2))  # menu chiffrement

        layout.addWidget(bouton_chiffrer, 4, 0, 1, 2)
        layout.addWidget(bouton_back, 5, 0, 1, 2)

        page.setLayout(layout)
        self.stack.addWidget(page)


    
    def handle_chiffrement_message(self):
        message = self.input_chiffrement_message.text()
        password = self.input_chiffrement_password.text()

        try:
            result = chiffrement_message(message, password)
            self.result_box_chiffrement.setText(result)

            log_action(self.user_id, "CHIFFREMENT_MESSAGE", "message")

        except Exception as e:
            self.show_error(str(e))
        
    
    def page_chiffrement_fichier(self):
        page = QWidget()
        layout = QGridLayout()

        layout.addWidget(QLabel("Chiffrer un fichier"), 0, 0, 1, 2)

        # Champ chemin du fichier
        layout.addWidget(QLabel("Fichier :"), 1, 0)
        self.input_chiffrement_file_path = QLineEdit()
        self.input_chiffrement_file_path.setReadOnly(True)
        layout.addWidget(self.input_chiffrement_file_path, 1, 1)

        bouton_parcourir = QPushButton("Parcourir")
        bouton_parcourir.clicked.connect(self.select_file_to_encrypt)
        layout.addWidget(bouton_parcourir, 2, 1)

        # Champ mot de passe
        layout.addWidget(QLabel("Mot de passe :"), 3, 0)
        self.input_chiffrement_file_password = QLineEdit()
        self.input_chiffrement_file_password.setEchoMode(QLineEdit.EchoMode.Password)
        layout.addWidget(self.input_chiffrement_file_password, 3, 1)

        # Résultat
        self.result_chiffrement_file_box = QLabel("")
        layout.addWidget(self.result_chiffrement_file_box, 4, 0, 1, 2)

        # Boutons
        bouton_chiffrer = QPushButton("Chiffrer le fichier")
        bouton_chiffrer.clicked.connect(self.handle_chiffrement_fichier_gui)

        bouton_back = QPushButton("Retour")
        bouton_back.clicked.connect(lambda: self.stack.setCurrentIndex(2))  # menu chiffrement

        layout.addWidget(bouton_chiffrer, 5, 0, 1, 2)
        layout.addWidget(bouton_back, 6, 0, 1, 2)

        page.setLayout(layout)
        self.stack.addWidget(page)


    def select_file_to_encrypt(self):
        chemin, _ = QFileDialog.getOpenFileName(
            self, "Choisir un fichier", "data/"
        )

        if chemin:
            self.input_chiffrement_file_path.setText(chemin)

    def select_file_to_decrypt(self):
        chemin, _ = QFileDialog.getOpenFileName(
            self, "Choisir un fichier", "data/"
        )

        if chemin:
            self.input_dechiffrement_file_path.setText(chemin)



    def handle_chiffrement_fichier_gui(self):
        chiffrement_chemin = self.input_chiffrement_file_path.text()
        chiffrement_password = self.input_chiffrement_file_password.text()

        if not chiffrement_chemin or not chiffrement_password:
            self.show_error("Veuillez sélectionner un fichier et un mot de passe")
            return

        try:
            resultat = chiffrement_fichier(chiffrement_chemin, chiffrement_password)
            self.result_chiffrement_file_box.setText(f"Fichier chiffré : {resultat}")

            log_action(self.user_id, "CHIFFREMENT_FICHIER", chiffrement_chemin)

        except Exception as e:
            self.show_error(str(e))


    

    #page déchiffrement
    def page_dechiffrement(self):
        page = QWidget()
        layout = QGridLayout()

        title = QLabel("Déchiffrement")
        title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(title, 0, 0, 1, 2)

        bouton_message = QPushButton("Déchiffrer un message")
        bouton_file = QPushButton("Déchiffrer un fichier")
        bouton_back = QPushButton("Retour")

        bouton_back.clicked.connect(lambda: self.stack.setCurrentIndex(1))

        layout.addWidget(bouton_message, 1, 0, 1, 2)
        layout.addWidget(bouton_file, 2, 0, 1, 2)
        layout.addWidget(bouton_back, 3, 0, 1, 2)

        page.setLayout(layout)
        self.stack.addWidget(page)

        bouton_message.clicked.connect(
            lambda: self.stack.setCurrentIndex(6)
        )

        bouton_file.clicked.connect(
            lambda: self.stack.setCurrentIndex(7)
        )

    def page_dechiffrement_message(self):
        page = QWidget()
        layout = QGridLayout()

        layout.addWidget(QLabel("Déchiffrer un message"), 0, 0, 1, 2)

        layout.addWidget(QLabel("Message :"), 1, 0)
        self.input_dechiffrement_message = QLineEdit()
        layout.addWidget(self.input_dechiffrement_message, 1, 1)

        layout.addWidget(QLabel("Mot de passe :"), 2, 0)
        self.input_dechiffrement_password = QLineEdit()
        self.input_dechiffrement_password.setEchoMode(QLineEdit.EchoMode.Password)
        layout.addWidget(self.input_dechiffrement_password, 2, 1)

        self.result_box_dechiffrement = QLineEdit()
        layout.addWidget(self.result_box_dechiffrement, 3, 0, 1, 2)

        bouton_chiffrer = QPushButton("Déchiffrer")
        bouton_chiffrer.clicked.connect(self.handle_dechiffrement_message)

        bouton_back = QPushButton("Retour")
        bouton_back.clicked.connect(lambda: self.stack.setCurrentIndex(5))  # menu chiffrement

        layout.addWidget(bouton_chiffrer, 4, 0, 1, 2)
        layout.addWidget(bouton_back, 5, 0, 1, 2)

        page.setLayout(layout)
        self.stack.addWidget(page)

    def handle_dechiffrement_message(self):
        message = self.input_dechiffrement_message.text()
        password = self.input_dechiffrement_password.text()

        try:
            result = dechiffrement_message(message, password)
            self.result_box_dechiffrement.setText(result)

            log_action(self.user_id, "DECHIFFREMENT_MESSAGE", "message")

        except Exception as e:
            self.show_error(str(e))
    
    def page_dechiffrement_fichier(self):
        page = QWidget()
        layout = QGridLayout()

        layout.addWidget(QLabel("Déchiffrer un fichier"), 0, 0, 1, 2)

        # Champ chemin du fichier
        layout.addWidget(QLabel("Fichier :"), 1, 0)
        self.input_dechiffrement_file_path = QLineEdit()
        self.input_dechiffrement_file_path.setReadOnly(True)
        layout.addWidget(self.input_dechiffrement_file_path, 1, 1)

        bouton_parcourir = QPushButton("Parcourir")
        bouton_parcourir.clicked.connect(self.select_file_to_decrypt)
        layout.addWidget(bouton_parcourir, 2, 1)

        # Champ mot de passe
        layout.addWidget(QLabel("Mot de passe :"), 3, 0)
        self.input_dechiffrement_file_password = QLineEdit()
        self.input_dechiffrement_file_password.setEchoMode(QLineEdit.EchoMode.Password)
        layout.addWidget(self.input_dechiffrement_file_password, 3, 1)

        # Résultat
        self.result_dechiffrement_file_box = QLabel("")
        layout.addWidget(self.result_dechiffrement_file_box, 4, 0, 1, 2)

        # Boutons
        bouton_chiffrer = QPushButton("Déchiffrer le fichier")
        bouton_chiffrer.clicked.connect(self.handle_dechiffrement_fichier_gui)

        bouton_back = QPushButton("Retour")
        bouton_back.clicked.connect(lambda: self.stack.setCurrentIndex(5))  # menu chiffrement

        layout.addWidget(bouton_chiffrer, 5, 0, 1, 2)
        layout.addWidget(bouton_back, 6, 0, 1, 2)

        page.setLayout(layout)
        self.stack.addWidget(page)

    
    def handle_dechiffrement_fichier_gui(self):
        dechiffrement_chemin = self.input_dechiffrement_file_path.text()
        dechiffrement_password = self.input_dechiffrement_file_password.text()

        if not dechiffrement_chemin or not dechiffrement_password:
            self.show_error("Veuillez sélectionner un fichier et un mot de passe")
            return

        try:
            resultat = dechiffrement_fichier(dechiffrement_chemin, dechiffrement_password)
            self.result_chiffrement_file_box.setText(f"Fichier chiffré : {resultat}")

            log_action(self.user_id, "DECHIFFREMENT_FICHIER", dechiffrement_chemin)

        except Exception as e:
            self.show_error(str(e))



#lancement
app = QApplication(sys.argv)
window = Window()
window.show()
sys.exit(app.exec())
