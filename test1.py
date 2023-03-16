from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

import sys


def OpenWindow(window):
	window.show()

class MainWindow(QWidget):
	def __init__(self):
		super().__init__()
		self.MainWindowGUI()
	def MainWindowGUI(self):
		w = SecondWindow()
		box = QVBoxLayout()
		
		button = QPushButton('Open')
		button.clicked.connect(lambda: OpenWindow(w))
		
		box.addWidget(button)
		
		
		
		self.setLayout(box)
		self.setWindowTitle('main')
		self.show()
		
class SecondWindow(QWidget):
	def __init__(self):
		super().__init__()
		self.SecondWindowGUI()
	def SecondWindowGUI(self):
		self.setWindowTitle('second')
		
def main():
	app = QApplication(sys.argv)
	window = MainWindow()
	sys.exit(app.exec())
	
if __name__ == "__main__":
	main()
