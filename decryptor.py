import cv2

def decrypt_message(image_path, message_length):
    img = cv2.imread(image_path)
    c = {i: chr(i) for i in range(256)}
    n, m, z = 0, 0, 0
    message = ""

    for _ in range(message_length):
        message += c[img[n, m, z]]
        n += 1
        m += 1
        z = (z + 1) % 3

    return message

