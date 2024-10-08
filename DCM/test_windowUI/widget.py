# This Python file uses the following encoding: utf-8
import sys
import pandas as pd
import os

from PySide6.QtWidgets import QApplication, QWidget, QMessageBox, QGraphicsDropShadowEffect
from PySide6.QtGui import QColor

from ui_form import Ui_LoginScreen
from ui_home import Ui_HomeScreen

# Get the path to the folder where the executable is running
if getattr(sys, 'frozen', False):  # Check if it's running as an executable
    base_path = sys._MEIPASS  # Temporary folder created by PyInstaller
else:
    base_path = os.path.abspath(".")

# Construct the path to credentials.txt
file = os.path.join(base_path, "credentials.txt")

# file = os.path.join("credentials.txt")

class LoginScreen(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_LoginScreen()
        self.ui.setupUi(self)

        # Store the new screen instance as an attribute
        self.new_screen = None

        # Hide the register screen by default
        self.ui.register_screen.hide()

        # Connect the register buttons to the function that shows the register screen
        self.ui.register_screen_button.clicked.connect(self.show_register_screen)
        self.ui.register_screen_button_2.clicked.connect(self.show_register_screen)

        # Connect the login buttons to the function that shows the login screen
        self.ui.login_screen_button.clicked.connect(self.show_login_screen)
        self.ui.login_screen_button_2.clicked.connect(self.show_login_screen)

        # Handle the Login button
        self.ui.login_button.clicked.connect(self.handle_login)

        # Handle the Register button
        self.ui.register_button.clicked.connect(self.handle_register)

    # Function to show the register screen and hide the login screen
    def show_register_screen(self):
        self.ui.login_screen.hide()     # Hide login screen
        self.ui.register_screen.show()  # Show register screen

    # Function to show the login screen and hide the register screen
    def show_login_screen(self):
        self.ui.register_screen.hide()  # Hide register screen
        self.ui.login_screen.show()     # Show login screen

    def handle_login(self):
        # Get the text from the username and password input fields
        username = self.ui.username_input.text()
        password = self.ui.password_input.text()

        # Simulate successful login by showing a new screen
        if username and password:  # Simple check for demonstration
            if (' ' in username or ',' in username):
                self.show_popup_warning("Login Failed", "Username contains invalid characters (',' or ' '). Try again.")
            elif (' ' in password or ',' in password):
                self.show_popup_warning("Login Failed", "Username contains invalid characters (',' or ' '). Try again.")
            else:
                credentials = pd.read_csv(file)
                size = credentials['Username'].size
                for i in range(size):
                    if username == str(credentials['Username'][i]):
                        if (password == str(credentials['Password'][i])):
                            self.show_new_screen(username)
                            return True
                        else:
                            self.show_popup_warning("Login Failed", "Username or password is invalid.")
                            return False
                self.show_popup_warning("Login Failed", "Username or password is invalid.")
                return False
        else:
            self.show_popup_warning("Login Failed", "Please enter both username and password.")

    def handle_register(self):
        # Get the text from the username and password input fields
        username = self.ui.reg_username_input.text()
        password1 = self.ui.reg_password_input_1.text()
        password2 = self.ui.reg_password_input_2.text()

        # If registration is successful
        # If there is content in all the input boxes
        if username and password1 and password2:  # Simple check for demonstration
            if (password1 != password2):
                self.show_popup_warning("Registration Failed", "Passwords do not match. Try again.")
                self.ui.reg_password_input_2.clear()
            else:
                if (' ' in username or ',' in username):
                    self.show_popup_warning("Registration Failed", "Username contains invalid characters (',' or ' '). Try again.")
                elif (' ' in password1 or ',' in password1):
                    self.show_popup_warning("Registration Failed", "Password contains invalid characters (',' or ' '). Try again.")
                elif (len(password1) < 6):
                    self.show_popup_warning("Registration Failed", "Password too short (minimum 6 character). Try again.")
                else:
                    credentials = pd.read_csv(file, dtype=str)
                    size = credentials['Username'].size
                    if (size >= 10):
                        self.show_popup_warning("Registration Failed", "Maximum number of profiles reached")
                    else:
                        for i in range(size):
                            if username == credentials['Username'][i]:
                            # Checks if credentials already exis
                                self.show_popup_warning("Registration Failed", "Username taken. Try again.")
                                return(False)
                        credentials.loc[size+1,'Username'] = str(username)
                        credentials.loc[size+1,'Password'] = str(password1)

                        credentials.to_csv(file, index = False)
                        self.show_popup_info("Registration Successful", "Please login using new credentials.")
                        self.show_login_screen()
        else:
            self.show_popup_warning("Registration Failed", "Please fill out all boxes.")

    def show_popup_info(self, title, message):
        msg_box = QMessageBox()
        msg_box.setWindowTitle(title)
        msg_box.setText(message)
        msg_box.setIcon(QMessageBox.Information)
        msg_box.exec()

    def show_popup_warning(self, title, message):
        msg_box = QMessageBox()
        msg_box.setWindowTitle(title)
        msg_box.setText(message)
        msg_box.setIcon(QMessageBox.Warning)
        msg_box.exec()

    def show_new_screen(self, username):
        # Create a new window/screen and keep a reference to it
        self.new_screen = HomeScreen(username)
        self.new_screen.show()
        self.close()  # Close the current login window

class HomeScreen(QWidget):
    def __init__(self, username, parent=None):
        super().__init__(parent)
        self.ui = Ui_HomeScreen()  # Create an instance of the new screen UI class
        self.ui.setupUi(self)  # Set up the UI

        # Display Username
        self.ui.username.setText(username)

        # Logout Functionality
        self.ui.signout.clicked.connect(self.show_login_screen)

        # Add shadow to the connection_box and user_box
        self.add_shadow_to_widget(self.ui.connection_box)
        self.add_shadow_to_widget(self.ui.user_box)

        # Add glow to the connect button and the AOO mode by default
        self.add_greenglow_to_widget(self.ui.connect_button)
        self.AOO_on()

        # Initialize the connection state
        self.connected = False
        self.ui.connect_button.clicked.connect(self.toggle_connection)
        self.ui.disconnect_button.clicked.connect(self.toggle_connection)

        # Update the UI based on the connection state
        self.update_connection_status()

        # Logic for Mode states
        self.ui.AOO_mode.clicked.connect(self.AOO_on)
        self.ui.AAI_mode.clicked.connect(self.AAI_on)
        self.ui.VOO_mode.clicked.connect(self.VOO_on)
        self.ui.VVI_mode.clicked.connect(self.VVI_on)

    def AOO_on(self):
        # show the corresponding parts for AOO mode
        self.add_greenglow_to_widget(self.ui.AOO_mode) # add glow
        self.ui.AOO_mode.setStyleSheet("border-top-right-radius: 30px;border-bottom-right-radius: 30px;color: #ffffff;background-color: #00b075;") # change background colour
        self.ui.AOO_screen.show()  # Show the AOO screen

        # remove all other modes
        self.remove_greenglow_from_widget(self.ui.AAI_mode) # remove glow
        self.remove_greenglow_from_widget(self.ui.VOO_mode) # remove glow
        self.remove_greenglow_from_widget(self.ui.VVI_mode) # remove glow
        self.ui.AAI_mode.setStyleSheet("border-top-right-radius: 30px;border-bottom-right-radius: 30px;color: #ffffff;background-color: #393939;") # change background colour
        self.ui.VOO_mode.setStyleSheet("border-top-right-radius: 30px;border-bottom-right-radius: 30px;color: #ffffff;background-color: #393939;") # change background colour
        self.ui.VVI_mode.setStyleSheet("border-top-right-radius: 30px;border-bottom-right-radius: 30px;color: #ffffff;background-color: #393939;") # change background colour
        self.ui.AAI_screen.hide()  # Show the AOO screen
        self.ui.VOO_screen.hide()  # Show the AOO screen
        self.ui.VVI_screen.hide()  # Show the AOO screen

    def AAI_on(self):
        # Show the corresponding parts for AAI mode
        self.add_greenglow_to_widget(self.ui.AAI_mode)  # Add glow
        self.ui.AAI_mode.setStyleSheet("border-top-right-radius: 30px;border-bottom-right-radius: 30px;color: #ffffff;background-color: #00b075;")  # Change background color
        self.ui.AAI_screen.show()  # Show the AAI screen

        # Remove all other modes
        self.remove_greenglow_from_widget(self.ui.AOO_mode)  # Remove glow
        self.remove_greenglow_from_widget(self.ui.VOO_mode)  # Remove glow
        self.remove_greenglow_from_widget(self.ui.VVI_mode)  # Remove glow
        self.ui.AOO_mode.setStyleSheet("border-top-right-radius: 30px;border-bottom-right-radius: 30px;color: #ffffff;background-color: #393939;")  # Change background color
        self.ui.VOO_mode.setStyleSheet("border-top-right-radius: 30px;border-bottom-right-radius: 30px;color: #ffffff;background-color: #393939;")  # Change background color
        self.ui.VVI_mode.setStyleSheet("border-top-right-radius: 30px;border-bottom-right-radius: 30px;color: #ffffff;background-color: #393939;")  # Change background color
        self.ui.AOO_screen.hide()  # Hide the AOO screen
        self.ui.VOO_screen.hide()  # Hide the VOO screen
        self.ui.VVI_screen.hide()  # Hide the VVI screen

    def VOO_on(self):
        # Show the corresponding parts for VOO mode
        self.add_greenglow_to_widget(self.ui.VOO_mode)  # Add glow
        self.ui.VOO_mode.setStyleSheet(self.ui.VOO_mode.styleSheet() + "background-color: #00b075;")  # Change background color
        self.ui.VOO_screen.show()  # Show the VOO screen

        # Remove all other modes
        self.remove_greenglow_from_widget(self.ui.AOO_mode)  # Remove glow
        self.remove_greenglow_from_widget(self.ui.AAI_mode)  # Remove glow
        self.remove_greenglow_from_widget(self.ui.VVI_mode)  # Remove glow
        self.ui.AOO_mode.setStyleSheet("border-top-right-radius: 30px;border-bottom-right-radius: 30px;color: #ffffff;background-color: #393939;")  # Change background color
        self.ui.AAI_mode.setStyleSheet("border-top-right-radius: 30px;border-bottom-right-radius: 30px;color: #ffffff;background-color: #393939;")  # Change background color
        self.ui.VVI_mode.setStyleSheet("border-top-right-radius: 30px;border-bottom-right-radius: 30px;color: #ffffff;background-color: #393939;")  # Change background color
        self.ui.AOO_screen.hide()  # Hide the AOO screen
        self.ui.AAI_screen.hide()  # Hide the AAI screen
        self.ui.VVI_screen.hide()  # Hide the VVI screen

    def VVI_on(self):
        # Show the corresponding parts for VVI mode
        self.add_greenglow_to_widget(self.ui.VVI_mode)  # Add glow
        self.ui.VVI_mode.setStyleSheet("border-top-right-radius: 30px;border-bottom-right-radius: 30px;color: #ffffff;background-color: #00b075;")  # Change background color
        self.ui.VVI_screen.show()  # Show the VVI screen

        # Remove all other modes
        self.remove_greenglow_from_widget(self.ui.AOO_mode)  # Remove glow
        self.remove_greenglow_from_widget(self.ui.AAI_mode)  # Remove glow
        self.remove_greenglow_from_widget(self.ui.VOO_mode)  # Remove glow
        self.ui.AOO_mode.setStyleSheet("border-top-right-radius: 30px;border-bottom-right-radius: 30px;color: #ffffff;background-color: #393939;")  # Change background color
        self.ui.AAI_mode.setStyleSheet("border-top-right-radius: 30px;border-bottom-right-radius: 30px;color: #ffffff;background-color: #393939;")  # Change background color
        self.ui.VOO_mode.setStyleSheet("border-top-right-radius: 30px;border-bottom-right-radius: 30px;color: #ffffff;background-color: #393939;")  # Change background color
        self.ui.AOO_screen.hide()  # Hide the AOO screen
        self.ui.AAI_screen.hide()  # Hide the AAI screen
        self.ui.VOO_screen.hide()  # Hide the VOO screen

    def update_connection_status(self):
        """Update the UI based on whether the device is connected."""
        if self.connected:
            self.ui.connect_label.setText("Device Connected")  # Show the connect label when connected
            self.ui.disconnect_button.hide()  # Hide the disconnect button when connected
            self.ui.connect_button.show()  # Show the connect button when connected
        else:
            self.ui.connect_label.setText("Device Disconnected")  # Hide the connect label when connected
            self.ui.connect_button.hide()  # Hide the connect button when connected
            self.ui.disconnect_button.show()  # Show the disconnect button when connected

    def toggle_connection(self):
        """This is an example function to toggle connection state."""
        # Change the connection status
        self.connected = not self.connected
        self.update_connection_status()  # Update the UI based on new state

    def add_shadow_to_widget(self, widget):
    # Create the shadow effect
        shadow = QGraphicsDropShadowEffect(self)
        shadow.setBlurRadius(50)  # Adjust for a stronger blur
        shadow.setXOffset(5)      # Shadow offset horizontally
        shadow.setYOffset(5)      # Shadow offset vertically
        shadow.setColor(QColor(0, 0, 0, 150))  # Set shadow color (RGBA, A = transparency)

        # Apply the shadow effect to the widget
        widget.setGraphicsEffect(shadow)

    def add_greenglow_to_widget(self, widget):
        # Create the shadow effect
        shadow = QGraphicsDropShadowEffect(self)
        shadow.setBlurRadius(50)  # Adjust for a stronger blur
        shadow.setXOffset(5)      # Shadow offset horizontally
        shadow.setYOffset(5)      # Shadow offset vertically
        shadow.setColor(QColor(0, 176, 117, 150))  # Set shadow color (RGBA, A = transparency)

        # Apply the shadow effect to the widget
        widget.setGraphicsEffect(shadow)

    def remove_greenglow_from_widget(self, widget):
        # Remove the shadow effect from the widget
        widget.setGraphicsEffect(None)

    def show_login_screen(self):
        # Create a new window/screen and keep a reference to it
        self.new_screen = LoginScreen()
        self.new_screen.show()
        self.close()  # Close the current login window

if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = LoginScreen()
    widget.show()
    sys.exit(app.exec())
