from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from screeninfo import get_monitors
import sys


def NewTab(window):
	window.show()

def Center(window):
	for monitor in get_monitors():
		screen_width = monitor.width
		screen_height = monitor.height

	window_x = (screen_width - window.width()) / 2
	window_y = (screen_height - window.height()) / 2
	
	window.move(int(window_x),int(window_y))

class MainWindow(QWidget):
	def __init__(self):
		super().__init__()
		self.MainWindowGUI()
	def MainWindowGUI(self):
		
		second_window = SecondWindow()
		
		button = QPushButton('Open New Tab',self)
		button.clicked.connect(lambda: NewTab(second_window))
		
		self.setGeometry(0,0,300,400)
		Center(self)
		self.setWindowTitle('main')
		self.show()

class SecondWindow(QWidget):
	def __init__(self):
		super().__init__()
		self.SecondWindowGUI()
	def SecondWindowGUI(self):
		self.setWindowTitle('second')
		Center(self)
def main():
	app = QApplication(sys.argv)
	window = MainWindow()
	sys.exit(app.exec())
	
if __name__ == "__main__":
	main()
