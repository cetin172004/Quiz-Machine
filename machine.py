""" QUIZ MACHINE """

# created by cetin172004
# memorize foreign words easily

from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

import random
import sys
import os

class MachineWindow(QWidget):
	def __init__(self):
		super().__init__()
		self.MachineGUI()
	def MachineGUI(self):
		
		# Layouts
		main_layout = QVBoxLayout()
		
		# Items
		question_label = QLabel('Press To Start Button')
		question_label.setAlignment(Qt.AlignCenter)
		question_label.setFont(QFont('Coruier New',24))
		question_label.setStyleSheet('color: white;')
		
		mode_button = QPushButton(' Mode: Endless')
		mode_button.setFont(QFont('Courier New',16))
		mode_button.resize(200,200)
		
		# Item & SubLayout Management
		main_layout.addWidget(question_label)
		main_layout.addStretch()	
		main_layout.addWidget(mode_button)
		main_layout.addStretch()
		
		# General Properties
		self.setLayout(main_layout)
		self.setGeometry(0,0,500,700)
		self.setStyleSheet('background-color: #373737;')
		self.setWindowTitle('Quiz Machine')
		self.setWindowIcon(QIcon('resources/icon.png'))
		self.show()

def main():
	app = QApplication(sys.argv)
	window = MachineWindow()
	sys.exit(app.exec())
	
if __name__ == "__main__":
	main()
	
	
"""
hunter mode = tamam hayir butonu ekler
			tamam dedikce kelimeler bidaha gelmez
			en son kelime bitince durur
endless mode = tamam / hayir butonlari kalkar surekli devam eder

"""