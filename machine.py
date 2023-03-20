""" QUIZ MACHINE """

# created by cetin172004
# memorize foreign words easily

from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

from screeninfo import get_monitors
from PIL import Image

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
		if counter > 28 and counter < len(text) - 7:
			edited_score += character
			counter += 1
		else:
			counter += 1
	
	return edited_score

def deleteHuntedText(text):
	edited_hunted = ""
	counter = 0
	for character in text:
		if counter > 29 and counter < len(text) - 7:
			edited_hunted += character
			counter += 1
		else:
			counter += 1
	
	return edited_hunted

def Center(window):
	for monitor in get_monitors():
		screen_width = monitor.width
		screen_height = monitor.height

	window_x = (screen_width - window.width()) / 2
	window_y = (screen_height - window.height()) / 2
	
	window.move(int(window_x),int(window_y))

def HideWord(mode_controller,label):
	if mode_controller.text() == 'Mode: Hunter':
		words = os.listdir('words')
		words.remove('hunted')		
		word = random.choice(words)

		# if it's same with current word
		if deletePNG(word) == label.text():
			words.remove(word)
			word_alternative = random.choice(words)
			words.append(word)
			label.setText(deletePNG(word_alternative))
		
		# if it's not same with current word
		else:			
			label.setText(deletePNG(word))

""" BUTTON ACTIONS """

def TurnOff(window):
	if window.windowTitle() == 'Quiz Machine':
		
		hunted_words = os.listdir('words/hunted')
		for hunted_word in hunted_words:
			os.system('mv words/hunted/' + hunted_word + ' words/' + hunted_word)

		sys.exit()
	else:
		window.close()

def GetQuestion(mode_controller,label,score):
	# mode is endless
	if mode_controller.text() == 'Mode: Endless':
		words = os.listdir('words')
		words.remove('hunted')
		word = random.choice(words)
			
		# choose another one if they are same
		if label.text() == deletePNG(word):
			words.remove(word)
			alternative_word = random.choice(words)
			words.append(word)
			label.setText(deletePNG(alternative_word))	
		
			# refresh score
			old_score = deleteScoreText(score.text())
			new_score = int(old_score) + 1
			score.setText('Score:<font color="#ffd84d"> ' + str(new_score) + '</font>')
		
		else:
			
			label.setText(deletePNG(word))
			
			# refresh score
			old_score = deleteScoreText(score.text())
			new_score = int(old_score) + 1
			score.setText('Score:<font color="#ffd84d"> ' + str(new_score) + '</font>')

	# mode is hunter
	else:
		if label.text() == ' Press To Start Button ':
			words = os.listdir('words')
			words.remove('hunted')
			word = random.choice(words)			
		
			label.setText(deletePNG(word))

		else:
			file_name = label.text() + '.png'
			os.system('mv words/' + file_name + ' words/hunted/' + file_name)

			if len(os.listdir('words/')) == 1:
				print('tebrikler')
				
				hunted_words = os.listdir('words/hunted')
				for hunted_word in hunted_words:
					os.system('mv words/hunted/' + hunted_word + ' words/' + hunted_word)
				sys.exit()

			else:
				words = os.listdir('words')
				words.remove('hunted')
				word = random.choice(words)			
		
				# refresh hunted
				old_hunted = deleteHuntedText(score.text())
				new_hunted = int(old_hunted) + 1
				score.setText('Hunted:<font color="#ffd84d"> ' + str(new_hunted) + '</font>')
				
				label.setText(deletePNG(word))

def ShowAnswer(label,error_window,window,empty_label,layout):
	if label.text() == ' Press To Start Button ':
		error_window.show()
	else:
		file_name = label.text() + '.png'
		
		empty_label.setPixmap(QPixmap('words/' + file_name))
		layout.addWidget(empty_label)
		
		answer = Image.open('words/' + file_name)
		answer_width = answer.width
		answer_height = answer.height
		
		window.setWindowTitle('Answer of ' + deletePNG(file_name))
		window.setFixedSize(answer_width,answer_height)
		window.setLayout(layout)
		window.move(700,100)
		window.show()
		

def ChangeMode(button,mode1_window,mode2_window,score):
	if button.text() == 'Mode: Endless':
		button.setText('Mode: Hunter')
		score.setText('Hunted:<font color="#ffd84d"> ' + str(len(os.listdir('words/hunted'))) + '</font>')
		mode2_window.show()
	
	else:
		button.setText('Mode: Endless')
		score.setText('Score:<font color="#ffd84d"> 0</font>')
		mode1_window.show()

def ClosePopUp(window):
	window.close()

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
		answer_window = Answer()
		doc_window = Documentation()
		
		score_label = QLabel('Score:<font color="#ffd84d"> 0</font>')
		score_label.setFont(QFont('Sans Serif',16))
		score_label.setStyleSheet('color: white;')
		
		info_seperator = QLabel('  ')
		
		total_label = QLabel('Total: <font color="#ffd84d">' + str(len(os.listdir('words')) - 1) + '</font>')
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
		mode_button.setStyleSheet("QPushButton"
                             "{"
                             "color : white;"
                             "}"
                             "QPushButton::hover"
                             "{"
                             "background-color : #796719;"
                             "}"
                             )
		
		get_button = QPushButton('Get Question')
		get_button.setFont(QFont('Sans Serif',16))
		get_button.setStyleSheet("QPushButton"
                             "{"
                             "color : white;"
                             "}"
                             "QPushButton::hover"
                             "{"
                             "background-color : #796719;"
                             "}"
                             )
		
		show_button = QPushButton('Show Answer')
		show_button.setFont(QFont('Sans Serif',16))
		show_button.setStyleSheet("QPushButton"
                             "{"
                             "color : white;"
                             "}"
                             "QPushButton::hover"
                             "{"
                             "background-color : #796719;"
                             "}"
                             )
		
		documentation_button = QPushButton('Documentation')
		documentation_button.setFont(QFont('Sans Serif',16))
		documentation_button.setStyleSheet("QPushButton"
                             "{"
                             "color : white;"
                             "}"
                             "QPushButton::hover"
                             "{"
                             "background-color : #796719;"
                             "}"
                             )                      
		
		exit_button = QPushButton('Exit')
		exit_button.setFont(QFont('Sans Serif',16))
		exit_button.setStyleSheet("QPushButton"
                             "{"
                             "color : white;"
                             "}"
                             "QPushButton::hover"
                             "{"
                             "background-color : #796719;"
                             "}"
                             )
		
		# Actions
		exit_button.clicked.connect(lambda: TurnOff(self))
		get_button.clicked.connect(lambda: GetQuestion(mode_button,question_label,score_label))
		show_button.clicked.connect(lambda: ShowAnswer(question_label,error1_window,answer_window,answer_window.answer_image,answer_window.answer_layout))
		mode_button.clicked.connect(lambda: ChangeMode(mode_button,endless_window,hunter_window))
		documentation_button.clicked.connect(doc_window.show)

		# Shortcuts
		change_mod_sc = QShortcut(QKeySequence('Ctrl+m'),self)
		change_mod_sc.activated.connect(lambda: ChangeMode(mode_button,endless_window,hunter_window,score_label))
		
		turn_off_sc = QShortcut(QKeySequence('Ctrl+q'),self)
		turn_off_sc.activated.connect(lambda: TurnOff(self))

		get_question_sc = QShortcut(QKeySequence('Ctrl+g'),self)
		get_question_sc.activated.connect(lambda: GetQuestion(mode_button,question_label,score_label))

		show_answer_sc = QShortcut(QKeySequence('Ctrl+s'),self)
		show_answer_sc.activated.connect(lambda: ShowAnswer(question_label,error1_window,answer_window,answer_window.answer_image,answer_window.answer_layout))

		doc_sc = QShortcut(QKeySequence('Ctrl+d'),self)
		doc_sc.activated.connect(doc_window.show)		

		hide_sc = QShortcut(QKeySequence('Ctrl+h'),self)
		hide_sc.activated.connect(lambda: HideWord(mode_button,question_label))

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
		self.setFixedSize(450,550)
		Center(self)
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
		close_button.setStyleSheet("QPushButton"
                             "{"
                             "color : white;"
                             "}"
                             "QPushButton::hover"
                             "{"
                             "background-color : #796719;"
                             "}"
                             )
		
		close_button.clicked.connect(lambda: ClosePopUp(self))
		
		# shortcut
		close_popup_sc = QShortcut(QKeySequence('Ctrl+c'),self)
		close_popup_sc.activated.connect(lambda: ClosePopUp(self))		

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
		self.setFixedSize(420,120)
		self.move(700,500)
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
		close_button.setStyleSheet("QPushButton"
                             "{"
                             "color : white;"
                             "}"
                             "QPushButton::hover"
                             "{"
                             "background-color : #796719;"
                             "}"
                             )
		
		close_button.clicked.connect(lambda: ClosePopUp(self))
		
		# shortcut
		close_popup_sc = QShortcut(QKeySequence('Ctrl+c'),self)
		close_popup_sc.activated.connect(lambda: ClosePopUp(self))

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
		self.setFixedSize(390,120)
		self.move(700,500)
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
		close_button.setStyleSheet("QPushButton"
                             "{"
                             "color : white;"
                             "}"
                             "QPushButton::hover"
                             "{"
                             "background-color : #796719;"
                             "}"
                             )
		
		close_button.clicked.connect(lambda: ClosePopUp(self))
		
		# shortcut
		close_popup_sc = QShortcut(QKeySequence('Ctrl+c'),self)
		close_popup_sc.activated.connect(lambda: ClosePopUp(self))

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
		self.setFixedSize(390,120)
		self.move(700,500)
		self.setWindowTitle('Hunter Mode Info')
		self.setStyleSheet('background-color: #373737;')

class Answer(QWidget):
	def __init__(self):
		super().__init__()
		self.AnswerGUI()
	def AnswerGUI(self):
		self.answer_layout = QHBoxLayout()
		self.answer_image = QLabel()
		
		turn_off_answer_sc = QShortcut(QKeySequence('Ctrl+q'),self)
		turn_off_answer_sc.activated.connect(lambda: TurnOff(self))

		# give priority
		self.setWindowFlags(Qt.WindowStaysOnTopHint)
		self.setWindowModality(Qt.ApplicationModal)

		self.setStyleSheet('background-color: #373737;')

class Documentation(QWidget):
	def __init__(self):
		super().__init__()
		self.DocumentationGUI()
	def DocumentationGUI(self):

		turn_off_doc_sc = QShortcut(QKeySequence('Ctrl+q'),self)
		turn_off_doc_sc.activated.connect(lambda: TurnOff(self))

		# give priority
		self.setWindowFlags(Qt.WindowStaysOnTopHint)
		self.setWindowModality(Qt.ApplicationModal)
		
		self.setWindowTitle('Quiz Machine Documentation')
		self.setStyleSheet('background-color: #373737;')

def main():
	app = QApplication(sys.argv)
	window = MachineWindow()
	sys.exit(app.exec())
	
if __name__ == "__main__":
	main()