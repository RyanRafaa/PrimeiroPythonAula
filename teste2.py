import sys
from PySide6.QtWidgets import (QApplication, QMainWindow, QVBoxLayout, QWidget, QLabel)

if __name__ == '__main__':
    app = QApplication (sys.argv)
    janela = QMainWindow ()
    conjunto_widget = QWidget()
    v_layout = QVBoxLayout()
    conjunto_widget.setLayout(v_layout)
    label1= QLabel("Texto aqui ...")
    v_layout.addWidget(label1)
    janela.setCentralWidget(conjunto_widget)
    janela.show()
    app.exec()