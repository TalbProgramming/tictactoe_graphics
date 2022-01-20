import sys

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QMainWindow
import socket
import sys
import time


class App(QWidget):
    def __init__(self):
        super().__init__()
        self.title = "Online Tic Tac Toe"
        self.button_list = []
        self.endgame_label = QLabel("", self)
        self.setup_ui()


    def setup_ui(self):
        self.setObjectName("App")
        self.resize(903, 699)
        self.setWindowTitle(self.title)
        b1 = QPushButton('1', self)
        b2 = QPushButton('2', self)
        b3 = QPushButton('3', self)
        b4 = QPushButton('4', self)
        b5 = QPushButton('5', self)
        b6 = QPushButton('6', self)
        b7 = QPushButton('7', self)
        b8 = QPushButton('8', self)
        b9 = QPushButton('9', self)

        # exit button
        self.exit_btn = QtWidgets.QPushButton(self, clicked=lambda: self.exit_app())
        self.exit_btn.setText("Exit :(")
        self.exit_btn.setGeometry(QtCore.QRect(230, 590, 75, 23))

        self.button_list = [b1, b2, b3, b4, b5, b6, b7, b8, b9]
        font = QtGui.QFont()
        font.setPointSize(70)

        for button in self.button_list:
            button.setFont(font)
            button.clicked.connect(lambda: self.on_click())

        b1.setGeometry(QtCore.QRect(300, 190, 101, 101))
        b4.setGeometry(QtCore.QRect(300, 300, 101, 101))
        b7.setGeometry(QtCore.QRect(300, 410, 101, 101))
        b2.setGeometry(QtCore.QRect(410, 190, 101, 101))
        b5.setGeometry(QtCore.QRect(410, 300, 101, 101))
        b8.setGeometry(QtCore.QRect(410, 410, 101, 101))
        b3.setGeometry(QtCore.QRect(520, 190, 101, 101))
        b6.setGeometry(QtCore.QRect(520, 300, 101, 101))
        b9.setGeometry(QtCore.QRect(520, 410, 101, 101))

        self.endgame_label = QLabel("", self)
        self.end_game_label_display("t")
        self.show()

    def on_click(self):
        print('PyQt5 button click - ' + self.sender().text())
        if can_change():
            self.sender().setText('X')  # player sign
            # disable all
            for btn in self.button_list:
                btn.setDisabled(True)

    def on_turn(self):
        for btn in self.button_list:
            btn.setDisabled(False)


    def exit_app(self):
        sys.exit()

    def end_game_label_display(self, which):
        font = QtGui.QFont()
        font.setPointSize(20)
        self.layout.addWidget(self.endgame_label)
        self.endgame_label.setFont(font)
        if which == "w":
            self.endgame_label.setText("You have won the game!")
        elif which == "l":
            self.endgame_label.setText("You have lost the game!")
        elif which == "t":
            self.endgame_label.setText("It's a tie!!!")

    def reset_window(self):
        self.hide()
        self.show()

def can_change():
    return True


if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window = App()
    main_window.setup_ui()
    main_window.end_game_label_display("w")
    sys.exit(app.exec_())
"""
    # set up server
    max_massage_length = 2000
    server_ip = '127.0.0.1'
    server_port = 5555

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # create tcp socket
    client_socket.connect((server_ip, server_port))  # connect to main server

    player_sign = client_socket.recv(max_massage_length).decode()
    # the first masssage from the server would be the player's sign

    while True:
        data = client_socket.recv(max_massage_length).decode()
        # data = the number the other guy chose the switch
        main_window.button_list[int(data)-1].setText(player_sign)

        if "won" in data or "lost" in data or "tie" in data:
            # print the won or lost massasge
            ###
            # play again part
            ###
            # if he pressed yes
            client_socket.close()  # close the socket
            client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # create tcp socket
            client_socket.connect((server_ip, server_port))  # rejoin to main server
            # if he pressed no
            sys.exit()  # close the window
        elif "disconnected" in data or data == "":
            # the other player disconnected scenario
            # loop until the user answers
            # play again part
            ###
            # if he pressed yes
            client_socket.close()  # close the socket
            client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # create tcp socket
            client_socket.connect((server_ip, server_port))  # rejoin to main server

            # if he pressed no
            sys.exit()  # close the window
        else:
            # let the player choose and then lock everything but the ones with x or o in them

            numberToSwitch = 0  # will equal to the slot chosen
            client_socket.send(numberToSwitch.encode())
"""

    #sys.exit(app.exec_())
