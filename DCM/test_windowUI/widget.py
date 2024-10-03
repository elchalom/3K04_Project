# This Python file uses the following encoding: utf-8
import sys

from PySide6.QtWidgets import QApplication, QWidget, QMessageBox

# Important:
# You need to run the following command to generate the ui_form.py file
#     pyside6-uic form.ui -o ui_form.py, or
#     pyside2-uic form.ui -o ui_form.py
from ui_form import Ui_Widget

class Widget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Widget()
        self.ui.setupUi(self)

        # Connect login button clicked signal to the login method
        self.ui.login_button.clicked.connect(self.handle_login)
        # self.ui.register_button.clicked.connect(self.handle_register)

    def handle_login(self):
        # Get the text from the username and password input fields
        username = self.ui.username_input.text()
        password = self.ui.password_input.text()

        # Save the username and password to a txt file
        with open('user_credentials.txt', 'a') as file:
            file.write(f"Username: {username}, Password: {password}\n")

        error_message = f"Welcome, {username}!"
        # Show a popup message box
        self.show_popup("Login Successful!", error_message)

    def show_popup(self, title, message):
        msg_box = QMessageBox()
        msg_box.setWindowTitle(title)
        msg_box.setText(message)
        msg_box.setIcon(QMessageBox.Warning)  # You can change the icon type (e.g., Warning, Critical, etc.)
        msg_box.exec()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = Widget()
    widget.show()
    sys.exit(app.exec())

