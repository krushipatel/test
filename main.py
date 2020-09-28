import sys


from PyQt5.QtWidgets import QApplication
from view import GUI
# Client code
def main():
    """Main function."""
    # Create an instance of QApplication
    pycalc = QApplication(sys.argv)
    # Show the calculator's GUI
    view = GUI()
    view.show()
    sys.exit(pycalc.exec_())
    if _name_ == '_main_':
    main()