from PyQt5.QtWidgets import QMainWindow
import socket

import utils
from pyui.connect_python import Ui_Dialog
from screens.view import ViewScrn


class ConnectUi(QMainWindow):

    def __init__(self):
        super(ConnectUi,self).__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.connect_button.clicked.connect(self.connect_button)

    def connect_button(self):
        try:
            self.ui.connect_button.setText("Connecting ...")
            ip = self.ui.ip_input.text()
            port = self.ui.port_input.text()

            print("IP", type(ip))
            print("CO", port)

            if ip == "" or port == "":
                raise utils.Error("Please enter port or ip address")

            # Raspberry Pi'nin IP adresi ve kullanacağınız port numarasını buraya yazın
            RPI_IP = ip  # Raspberry Pi'nin IP adresi

            # Kullanılacak port numarası
            PORT = int(port)

            # Soket oluştur
            try:
                client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                client_socket.connect((RPI_IP, PORT))
                # Open ViewScreem
                self.view_page = ViewScrn(client_socket)
                self.view_page.show()
                # Close connection screen

            except Exception as e:
                print(e)
                self.ui.connect_button.setText("Connection Failed")


        except Exception as e:
            print(e)
