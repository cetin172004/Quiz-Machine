""" QUIZ MACHINE """

# created by cetin172004
# memorize foreign words easily

from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

import random
import sys
import os

""" EXTERNAL FUNCTIONS """

def deletePNG(text):
	edited_word = ""
	counter = 0
	for character in text:	
		if counter == len(text) - 4:
			break
		edited_word += character
		counter += 1
	return edited_word

def deleteScoreText(text):
	edited_score = ""
	counter = 0
	for character in text:
		if counter > 6:
			edited_score += character
			counter += 1
		else:
			counter += 1
	
	return edited_score

""" BUTTON ACTIONS """

def TurnOffMachine():
	sys.exit()

def GetQuestion(mode_controller,label,score):
	old_score = deleteScoreText(score.text())
	new_score = int(old_score) + 1
	score.setText('Score: ' + str(new_score))
	
	# mode check
	if mode_controller.text() == 'Mode: Endless':
		words = os.listdir('words')
		word = random.choice(words)
		
		# choose another one if they are same
		if label.text() == deletePNG(word):
			words.remove(word)
			alternative_word = random.choice(words)
			words.append(word)
			label.setText(deletePNG(alternative_word))	
		else:
			label.setText(deletePNG(word))

""" WINDOW SECTION """

class MachineWindow(QWidget):
	def __init__(self):
		super().__init__()
		self.MachineGUI()
	def MachineGUI(self):
		
		# Layouts
		main_layout = QVBoxLayout()
		info_panel = QHBoxLayout()
		
		# Items
		score_label = QLabel('Score: 0')
		score_label.setFont(QFont('Sans Serif',16))
		score_label.setStyleSheet('color: white;')
		
		total_label = QLabel('Total: ' + str(len(os.listdir('words'))))
		total_label.setFont(QFont('Sans Serif',16))
		total_label.setStyleSheet('color: white;')
		
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
		get_button.clicked.connect(lambda: GetQuestion(mode_button,question_label,score_label))
		
		# Item & SubLayout Management
		info_panel.addWidget(score_label)
		info_panel.addWidget(total_label)
		info_panel.setAlignment(Qt.AlignCenter)
		
		main_layout.addLayout(info_panel)
		main_layout.addStretch()
		main_layout.addWidget(question_label)
		main_layout.addStretch()	
		main_layout.addWidget(mode_button)
		main_layout.addWidget(get_button)
		main_layout.addWidget(show_button)
		main_layout.addWidget(exit_button)
		
		# General Properties
		self.setLayout(main_layout)
		self.setGeometry(0,0,400,500)
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
500 700
exit_button.setEnabled(False)
hunter mode = tamam hayir butonu ekler
			tamam dedikce kelimeler bidaha gelmez
			en son kelime bitince durur
endless mode = tamam / hayir butonlari kalkar surekli devam eder

size fix
mode name and infos should make colorful

"""