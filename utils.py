import cv2


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
def draw_squares_and_move_servos(model, servo1_position, servo2_position, im, no_target, current_x_position,
                                 current_y_position, servo1_max_angle, servo2_max_angle, camera_height, camera_width):
    # Nesne tespiti
    fire = 0
    centerX = camera_width/2
    centerY = camera_height/2
    if no_target == 48:
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
            print("CLASS",class_id)
            if class_id == 0 and score >= 0.5:
                no_target = 0

                # Kameranın ortasına artı işareti çiz
                cv2.rectangle(im, (int(x1), int(y1)), (int(x2), int(y2)), (255, 0, 0), 2)
                # Kameranın ortasına artı işareti çiz
                cv2.line(im, (int(camera_width / 2) - 10, int(camera_height / 2)),
                         (int(camera_width / 2) + 10, int(camera_height / 2)), (0, 255, 0), 2)
                cv2.line(im, (int(camera_width / 2), int(camera_height / 2) - 10),
                         (int(camera_width / 2), int(camera_height / 2) + 10), (0, 255, 0), 2)

                # Karenin merkezini hesapla
                center_x = (x1 + x2) / 2
                center_y = (y1 + y2) / 2

                # Kare merkezine göre servo açılarını hesapla
                target_angle_x = pixel_to_angle_X(camera_width, 15, center_x)
                target_angle_y = pixel_to_angle_Y(camera_height, 10, center_y)

                current_x_position = current_x_position + target_angle_x

                current_y_position = current_y_position + target_angle_y

                cv2.circle(im, (int(center_x), int(center_y)), radius=5, color=(0, 0, 255), thickness=-1)

                if (
                        current_x_position >= servo2_max_angle or current_x_position <= -servo2_max_angle or current_y_position >= servo1_max_angle or current_y_position <= -servo1_max_angle):
                    current_x_position = servo2_position
                    current_y_position = servo1_position
                if x1 <= centerX <=x2  and y1 <= centerY <= y2:

                    fire = 1
                # send servo position
                # servo1.value = math.sin(math.radians(current_y_position))
                # servo2.value = math.sin(math.radians(current_x_position))



    else:
        no_target += 1
    print("FİREEEEEE",fire)
    return im, no_target, current_x_position, current_y_position,fire


class Error(Exception):
    pass
