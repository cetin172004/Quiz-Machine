from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

import sys

def getme(label):
	print(label.text())

class MainWindow(QWidget):
	def __init__(self):
		super().__init__()
		self.MainWindowGUI()
	def MainWindowGUI(self):
		
		main_box = QVBoxLayout()
		
		
		
		button = QPushButton('Hello World',self)
		button.setStyleSheet('QPushButton {color: red;}')
		
		self.setLayout(main_box)
		self.setWindowTitle('test')
		self.show()
		
def main():
	app = QApplication(sys.argv)
	window = MainWindow()
	sys.exit(app.exec())
	
if __name__ == "__main__":
	main()



