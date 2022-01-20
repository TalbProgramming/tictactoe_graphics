# client for TicTacToe game
from playGround import Ui_MainWindow
import socket
import sys

max_massage_length = 2000
server_ip = '127.0.0.1'
server_port = 5555

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # create tcp socket
client_socket.connect((server_ip, server_port))  # connect to main server


# clear screen and write to the client that its waiting for players

print("Waiting for another player...")
while True:
    data = client_socket.recv(max_massage_length).decode()

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
        # wait until the user chose a slot
        numberToSwitch = 0  # will equal to the slot chosen
        client_socket.send(numberToSwitch.encode())
        temp_board = client_socket.recv(max_massage_length).decode()


client_socket.close()


