import threading
import socket
import cv2
import numpy as np
from time import time
from ultralytics import YOLO

# Raspberry Pi'nin IP adresi ve kullanacağınız port numarasını buraya yazın
RPI_IP = '192.168.1.112'  # Raspberry Pi'nin IP adresi
PORT = 12347  # Kullanılacak port numarası

# Soket oluştur
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((RPI_IP, PORT))

print("Bağlantı kuruldu.")

# servo1 motorunun başlangıç değeri
servo1_position = -38.5
servo2_position = 0

servo1_max_angle = 52.5
servo2_max_angle = 90

areas = ["positive", "negative"]

current_x_position = servo2_position
current_y_position = servo1_position

threshold = 0.6
frame_count = 0
no_target = 0

model = YOLO("yolov8n.pt")

# Son işlem zamanı
last_operation_time = time()


def decide_X_area(max_width, x_pixel):
    center_pixel = max_width / 2
    if (x_pixel < center_pixel):
        return "positive"
    else:
        return "negative"


def decide_Y_area(max_height, y_pixel):
    center_pixel = max_height / 2
    if (y_pixel > center_pixel):
        return "positive"
    else:
        return "negative"


def pixel_to_angle_X(max_width, maximum_servo_angle, center_x):
    max_servo = maximum_servo_angle
    area = decide_X_area(max_width, center_x)
    print(area)

    if (area == "negative"):
        max_servo = -max_servo
    one_pixel_required_angle = max_servo / (max_width / 2)
    print("one_pixel_required_angle", one_pixel_required_angle)
    angle = abs((max_width / 2) - center_x) * one_pixel_required_angle

    return angle


def pixel_to_angle_Y(max_height, maximum_servo_angle, center_y):
    max_servo = maximum_servo_angle
    area = decide_Y_area(max_height, center_y)
    print(area)
    if (area == "negative"):
        max_servo = -max_servo
    one_pixel_required_angle = max_servo / (max_height / 2)
    angle = abs((max_height / 2) - center_y) * one_pixel_required_angle
    return angle


# Karelerin çizilmesi ve servo hareketlerinin kontrol fonksiyonu
def draw_squares_and_move_servos(im, camera_height, camera_width):
    global servo1_position
    global servo2_position
    global last_operation_time
    global no_target
    global current_x_position
    global current_y_position

    # Nesne tespiti
    print("No target", no_target)
    if no_target == 5:
        current_x_position = servo2_position
        current_y_position = servo1_position

        # send servo default position
        # servo1.value = math.sin(math.radians(servo1_position))
        # servo2.value = math.sin(math.radians(servo2_position))
        no_target = 0

    results = model.predict(im)[0]

    if results.boxes:
        # Tespit edilen nesneleri çerçeve üzerine çiz
        for result in results[0].boxes.data.tolist():
            x1, y1, x2, y2, score, class_id = result

            no_target = 0

            # Karenin merkezini hesapla
            center_x = (x1 + x2) / 2
            center_y = (y1 + y2) / 2

            # Kare merkezine göre servo açılarını hesapla
            target_angle_x = pixel_to_angle_X(camera_width, 20, center_x)
            target_angle_y = pixel_to_angle_Y(camera_height, 12, center_y)

            current_x_position = current_x_position + target_angle_x

            current_y_position = current_y_position + target_angle_y

            cv2.circle(im, (int(center_x), int(center_y)), radius=5, color=(0, 0, 255), thickness=-1)

            if (
                    current_x_position >= servo2_max_angle or current_x_position <= -servo2_max_angle or current_y_position >= servo1_max_angle or current_y_position <= -servo1_max_angle):
                current_x_position = servo2_position
                current_y_position = servo1_position

                # Kameranın ortasına artı işareti çiz

            # send servo position
            # servo1.value = math.sin(math.radians(current_y_position))
            # servo2.value = math.sin(math.radians(current_x_position))
            print(current_x_position)
            print(current_y_position)

    else:
        no_target += 1

    # Son işlem zamanını güncelle
    last_operation_time = time()


# Görüntü alma ve işleme işlemi
def receive_and_process_image():
    while True:
        # Gelen veriyi al
        length = client_socket.recv(16)
        string_data = b''

        # Veriyi tampona al
        while len(string_data) < int(length):
            string_data += client_socket.recv(int(length) - len(string_data))

        # Baytları görüntüye dönüştür
        data = np.frombuffer(string_data, dtype='uint8')

        # Görüntüyü yeniden şekillendir
        im = cv2.imdecode(data, cv2.COLOR_RGBA2RGB)
        print("image",im)
        height, width, _ = im.shape

        # Karelerin çizilmesi ve servo hareketlerinin kontrol edilmesi
        draw_squares_and_move_servos(im, height, width)
        print("im", im)

        # İşlenmiş görüntüyü göster
        cv2.imshow("Processed Image", im)
        # Son işlem zamanını güncelle
        last_operation_time = time()

        # Klavye olaylarını dinleme
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break


# Başlangıçta işlem döngüsünü başlat
process_thread = threading.Thread(target=receive_and_process_image)
process_thread.start()
