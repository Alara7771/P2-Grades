

from grade_logic import *
from PyQt6.QtWidgets import QApplication

def main():
    application = QApplication([])
    window = Grades()
    window.show()
    application.exec()

if __name__ == "__main__":
    main()
