import sys
from PyQt5.QtCore import Qt, QUrl
from PyQt5.QtGui import QIcon
from PyQt5.QtWebEngineWidgets import *
from PyQt5.QtWidgets import *

class browser(QWidget):
    def __init__(self):
        super().__init__()
        self.setup()

    def setup(self):
        self.resize(1350, 690)
        self.setWindowTitle('Web Browser')
        self.setWindowIcon(QIcon('Python-Logo.png'))

        self.site = QLineEdit()

        self.go = QPushButton('Go')
        self.go.setFixedWidth(50)
        self.back = QPushButton('Back')
        self.back.setFixedWidth(50)
        self.forw = QPushButton('Forward')
        self.forw.setFixedWidth(50)
        self.relo = QPushButton('Reload')
        self.relo.setFixedWidth(50)

        self.panel = QWebEngineView()
        self.panel.urlChanged.connect(self.adjusturl)
        self.panel.titleChanged.connect(self.adjusttitle)

        layout = QGridLayout()
        layout.addWidget(self.go, 0, 0)
        layout.addWidget(self.site, 0, 1, 1, 4)
        layout.addWidget(self.back, 1, 0)
        layout.addWidget(self.forw, 1, 1)
        layout.addWidget(self.relo, 1, 2)
        layout.addWidget(self.panel, 2, 0, 1, 5)
        self.setLayout(layout)

        self.go.clicked.connect(self.loading)
        self.back.clicked.connect(self.panel.back)
        self.forw.clicked.connect(self.panel.forward)
        self.relo.clicked.connect(self.panel.reload)

    def loading(self):
        self.panel.load(QUrl('https://'+self.site.text()+'.com'))
    def adjusturl(self):
        self.site.setText(QUrl(self.panel.url()).toString())
    def adjusttitle(self):
        self.setWindowTitle('Web Browser : '+self.panel.title())

if __name__ == '__main__':
    a = QApplication(sys.argv)
    b = browser()
    b.show()
    a.exec_()
