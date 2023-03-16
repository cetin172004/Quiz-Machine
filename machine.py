""" QUIZ MACHINE """

# created by cetin172004
# memorize foreign words easily

from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

import random
import sys
import os

def TurnOffMachine():
	sys.exit()

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
		question_label.setFont(QFont('Sans Serif',24))
		question_label.setStyleSheet('color: white;')
		
		mode_button = QPushButton('Mode: Endless')
		mode_button.setFont(QFont('Sans Serif',16))
		mode_button.setStyleSheet('color: white;')
		
		get_button = QPushButton('Get Question')
		get_button.setFont(QFont('Sans Serif',16))
		get_button.setStyleSheet('color: white;')
		
		show_button = QPushButton('Show Answer')
		show_button.setFont(QFont('Sans Serif',16))
		show_button.setStyleSheet('color: white;')
		
		exit_button = QPushButton('Exit')
		exit_button.setFont(QFont('Sans Serif',16))
		exit_button.setStyleSheet('color: white;')
		
		# Actions
		exit_button.clicked.connect(TurnOffMachine)
		
		# Item & SubLayout Management
		main_layout.addStretch()
		main_layout.addWidget(question_label)
		main_layout.addStretch()	
		main_layout.addWidget(mode_button)
		main_layout.addWidget(get_button)
		main_layout.addWidget(show_button)
		main_layout.addWidget(exit_button)
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