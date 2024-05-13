import pickle
import socket
import time

import cv2
import numpy as np
from PyQt5.QtCore import QTimer
from PyQt5.QtGui import QImage, QPixmap
from PyQt5.QtWidgets import QMainWindow, QWidget
from ultralytics import YOLO

import utils
from pyui.viewScreen_python import Ui_ViewScreen


class ViewScrn(QWidget):

    def __init__(self, client_socket):
        super(ViewScrn, self).__init__()
        self.ui = Ui_ViewScreen()
        self.ui.setupUi(self)

        self.timer = QTimer(self)

        MESSAGE_PORT = 12345
        PC_IP = "0.0.0.0"
        print("Raspberry bağlantısı başarılı")

        # Soket oluştur
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_socket.bind((PC_IP, MESSAGE_PORT))
        server_socket.listen(5)

        print("Bağlantı bekleniyor")

        data_channel, address = server_socket.accept()

        print(address)

        print("Karşılıklı Bağlantı kuruldu.")

        # servo1 motorunun başlangıç değeri
        servo1_position = -38.5
        servo2_position = 0

        servo1_max_angle = 52.5
        servo2_max_angle = 90

        current_x_position = servo2_position
        current_y_position = servo1_position


        no_target = 0

        model = YOLO("best.pt")

        try:
            while True:
                # Kameradan görüntü al

                # Gelen veriyi al
                length = client_socket.recv(16)
                string_data = b''

                # Veriyi tampona al
                while len(string_data) < int(length):
                    string_data += client_socket.recv(int(length) - len(string_data))

                # Baytları görüntüye dönüştür
                data = np.frombuffer(string_data, dtype='uint8')

                # Görüntüyü yeniden şekillendir
                im = cv2.imdecode(data, cv2.COLOR_BGR2RGB)
                im = cv2.cvtColor(im, cv2.COLOR_BGR2RGB)

                height, width, sz = im.shape

                im, no_target, current_x_position, current_y_position, is_fire = utils.draw_squares_and_move_servos(model,
                                                                                                                 servo1_position,
                                                                                                                 servo2_position,
                                                                                                                 im,
                                                                                                                 no_target,
                                                                                                                 current_x_position,
                                                                                                                 current_y_position,
                                                                                                                 servo1_max_angle,
                                                                                                                 servo2_max_angle,
                                                                                                                 height,
                                                                                                                 width)

                fire = is_fire
                servo_angles = {"x_client": current_x_position, "y_client": current_y_position, "fire": fire}

                nesne_bytes = pickle.dumps(servo_angles)
                data_channel.send(nesne_bytes)
                # İşlenmiş görüntüyü göster

                h, w, ch = im.shape
                bytes_per_line = ch * w
                q_img = QImage(im.data, w, h, bytes_per_line, QImage.Format_RGB888)
                pixmap = QPixmap.fromImage(q_img)
                cv2.imshow("w", im)
                if cv2.waitKey(1) & 0xFF == ord('q'):
                    break

        except KeyboardInterrupt:
            # Ctrl+C'ye basıldığında programı kapat send servo defaul position
            # servo1.value = math.sin(math.radians(servo1_position))
            # servo2.value = math.sin(math.radians(servo2_position))

            pass
        finally:
            # Döngü kırıldığında kamerayı kapat
            cv2.destroyAllWindows()
            client_socket.close()
