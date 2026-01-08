import cv2
import numpy as np
import os

input_path = "../input/sample.jpg"
output_dir = "../output"
os.makedirs(output_dir, exist_ok=True)

alpha = 1.5   # 대비
beta = 30     # 밝기

img = cv2.imread(input_path)
enhanced = cv2.convertScaleAbs(img, alpha=alpha, beta=beta)

save_path = os.path.join(output_dir, "enhanced.jpg")
cv2.imwrite(save_path, enhanced)

print("Saved:", save_path)
