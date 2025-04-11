# installer PyQt5: pip install PyQt5 PyQtWebEngine
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWebEngineWidgets import QWebEngineView
import sys

# URL cible
URL = "https://arthur-lenoble.github.io/Windows-web"

# Initialisation de l'application Qt
app = QApplication(sys.argv)

# Création de la fenêtre de navigateur
browser = QWebEngineView()
browser.setWindowTitle("WINUX Browser")
browser.resize(1024, 768)  # Taille de la fenêtre
browser.load(URL)  # Chargement de la page web
browser.show()

# Lancement de l'application
sys.exit(app.exec_())
