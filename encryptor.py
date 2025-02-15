import cv2
import os

def encrypt_message(image_path, message, password):
    img = cv2.imread(image_path)
    d = {chr(i): i for i in range(256)}
    m, n, z = 0, 0, 0

    for i in range(len(message)):
        img[n, m, z] = d[message[i]]
        n += 1
        m += 1
        z = (z + 1) % 3

    output_path = os.path.join("output", "encryptedImage.png")
    os.makedirs("output", exist_ok=True)
    cv2.imwrite(output_path, img)
    return output_path

