""" QUIZ MACHINE """

# created by cetin172004
# memorize foreign words easily

from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

import random
import sys
import os

""" VARIABLES """

error1_message = "Firstly you must to get a question"
endless_message = " You are in endless mode \n You can read documentation"
hunter_message = "You are in hunter mode \n You can read documentation"

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
	# refresh score
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

def ShowAnswer(label,error_window):
	if label.text() == ' Press To Start Button ':
		error_window.show()
	else:
		file_name = label.text() + '.png'
		os.system('eog words/' + file_name)

def ChangeMode(button,mode1_window,mode2_window):
	if button.text() == 'Mode: Endless':
		button.setText('Mode: Hunter')
		mode2_window.show()
	else:
		button.setText('Mode: Endless')
		mode1_window.show()

""" WINDOW SECTION """

class MachineWindow(QWidget):
	def __init__(self):
		super().__init__()
		self.MachineGUI()
	def MachineGUI(self):
		
		# Layouts
		main_layout = QVBoxLayout()
		info_panel = QHBoxLayout()
		question_box = QHBoxLayout()
		
		# Items
		error1_window = Error1()
		endless_window = EndlessModeInfo()
		hunter_window = HunterModeInfo()
		
		score_label = QLabel('Score: 0')
		score_label.setFont(QFont('Sans Serif',16))
		score_label.setStyleSheet('color: white;')
		
		info_seperator = QLabel('  ')
		
		total_label = QLabel('Total: ' + str(len(os.listdir('words'))))
		total_label.setFont(QFont('Sans Serif',16))
		total_label.setStyleSheet('color: white;')
		
		question_label = QLabel(' Press To Start Button ')
		question_label.setAlignment(Qt.AlignCenter)
		question_label.setFont(QFont('Sans Serif',24))
		question_label.setStyleSheet('color: white;')
		
		right_label = QLabel()
		right_label.setPixmap(QPixmap('resources/right.png'))
		
		left_label = QLabel()
		left_label.setPixmap(QPixmap('resources/left.png'))
		
		mode_button = QPushButton('Mode: Endless')
		mode_button.setFont(QFont('Sans Serif',16))
		mode_button.setStyleSheet('color: white;')
		
		get_button = QPushButton('Get Question')
		get_button.setFont(QFont('Sans Serif',16))
		get_button.setStyleSheet('color: white;')
		
		show_button = QPushButton('Show Answer')
		show_button.setFont(QFont('Sans Serif',16))
		show_button.setStyleSheet('color: white;')
		
		documentation_button = QPushButton('Documentation')
		documentation_button.setFont(QFont('Sans Serif',16))
		documentation_button.setStyleSheet('color: white;')
		
		exit_button = QPushButton('Exit')
		exit_button.setFont(QFont('Sans Serif',16))
		exit_button.setStyleSheet('color: white;')
		
		# Actions
		exit_button.clicked.connect(TurnOffMachine)
		get_button.clicked.connect(lambda: GetQuestion(mode_button,question_label,score_label))
		show_button.clicked.connect(lambda: ShowAnswer(question_label,error1_window))
		mode_button.clicked.connect(lambda: ChangeMode(mode_button,endless_window,hunter_window))
		
		# Item & SubLayout Management
		info_panel.addWidget(score_label)
		info_panel.addWidget(info_seperator)
		info_panel.addWidget(total_label)
		info_panel.setAlignment(Qt.AlignCenter)
		main_layout.addLayout(info_panel)
		
		main_layout.addStretch()
		
		question_box.addWidget(right_label)
		question_box.addWidget(question_label)
		question_box.addWidget(left_label)
		main_layout.addLayout(question_box)
		question_box.setAlignment(Qt.AlignCenter)
		
		main_layout.addStretch()	
		
		main_layout.addWidget(documentation_button)
		main_layout.addWidget(mode_button)
		main_layout.addWidget(get_button)
		main_layout.addWidget(show_button)
		main_layout.addWidget(exit_button)
		
		# General Properties
		self.setLayout(main_layout)
		self.setGeometry(0,0,400,550)
		self.setStyleSheet('background-color: #373737;')
		self.setWindowTitle('Quiz Machine')
		self.setWindowIcon(QIcon('resources/icon.png'))
		self.show()

class Error1(QWidget):
	def __init__(self):
		super().__init__()
		self.Error1GUI()
	def Error1GUI(self):
		error1_layout = QHBoxLayout()
		close_layout = QHBoxLayout()
		main_layout = QVBoxLayout()
		
		error_image = QLabel()
		error_image.setPixmap(QPixmap('resources/error.png'))
		error_image.setAlignment(Qt.AlignCenter)
		
		error_label = QLabel(error1_message,self)
		error_label.setAlignment(Qt.AlignCenter)
		error_label.setFont(QFont('Sans Serif',14))
		error_label.setStyleSheet('color: white;')
		
		close_button = QPushButton('Close')
		close_button.setFont(QFont('Sans Serif',12))
		close_button.setStyleSheet('color: white;')
		
		error1_layout.addWidget(error_image)
		error1_layout.addWidget(error_label)
		close_layout.addStretch()
		close_layout.addWidget(close_button)
		main_layout.addLayout(error1_layout)
		main_layout.addLayout(close_layout)
		
		# give priority
		self.setWindowFlags(Qt.WindowStaysOnTopHint)
		self.setWindowModality(Qt.ApplicationModal)
		
		self.setWindowIcon(QIcon('resources/icon.png'))
		self.setLayout(main_layout)
		self.setWindowTitle('Error 1')
		self.setStyleSheet('background-color: #373737;')

class EndlessModeInfo(QWidget):
	def __init__(self):
		super().__init__()
		self.EndlessGUI()
	def EndlessGUI(self):
		endless_layout = QHBoxLayout()
		close_layout = QHBoxLayout()
		main_layout = QVBoxLayout()
		
		endless_image = QLabel()
		endless_image.setPixmap(QPixmap('resources/endless.png'))
		endless_image.setAlignment(Qt.AlignCenter)
		
		endless_label = QLabel(endless_message,self)
		endless_label.setAlignment(Qt.AlignCenter)
		endless_label.setFont(QFont('Sans Serif',14))
		endless_label.setStyleSheet('color: white;')
		
		close_button = QPushButton('Close')
		close_button.setFont(QFont('Sans Serif',12))
		close_button.setStyleSheet('color: white;')
		
		endless_layout.addWidget(endless_image)
		endless_layout.addWidget(endless_label)
		close_layout.addStretch()
		close_layout.addWidget(close_button)
		main_layout.addLayout(endless_layout)
		main_layout.addLayout(close_layout)
		
		# give priority
		self.setWindowFlags(Qt.WindowStaysOnTopHint)
		self.setWindowModality(Qt.ApplicationModal)
		
		self.setWindowIcon(QIcon('resources/icon.png'))
		self.setLayout(main_layout)
		self.setWindowTitle('Endless Mode Info')
		self.setStyleSheet('background-color: #373737;')

class HunterModeInfo(QWidget):
	def __init__(self):
		super().__init__()
		self.HunterGUI()
	def HunterGUI(self):
		hunter_layout = QHBoxLayout()
		close_layout = QHBoxLayout()
		main_layout = QVBoxLayout()
		
		hunter_image = QLabel()
		hunter_image.setPixmap(QPixmap('resources/hunter.png'))
		hunter_image.setAlignment(Qt.AlignCenter)
		
		hunter_label = QLabel(hunter_message,self)
		hunter_label.setAlignment(Qt.AlignCenter)
		hunter_label.setFont(QFont('Sans Serif',14))
		hunter_label.setStyleSheet('color: white;')
		
		close_button = QPushButton('Close')
		close_button.setFont(QFont('Sans Serif',12))
		close_button.setStyleSheet('color: white;')
		
		hunter_layout.addWidget(hunter_image)
		hunter_layout.addWidget(hunter_label)
		close_layout.addStretch()
		close_layout.addWidget(close_button)
		main_layout.addLayout(hunter_layout)
		main_layout.addLayout(close_layout)
		
		# give priority
		self.setWindowFlags(Qt.WindowStaysOnTopHint)
		self.setWindowModality(Qt.ApplicationModal)
		
		self.setWindowIcon(QIcon('resources/icon.png'))
		self.setLayout(main_layout)
		self.setWindowTitle('Hunter Mode Info')
		self.setStyleSheet('background-color: #373737;')

def main():
	app = QApplication(sys.argv)
	window = MachineWindow()
	sys.exit(app.exec())
	
if __name__ == "__main__":
	main()