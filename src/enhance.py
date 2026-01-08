import cv2
import numpy as np
import os

input_path = "../input/sample.jpg"
output_path = "../output/enhanced.jpg"

img = cv2.imread(input_path)

alpha = 1.3  # 대비
beta = 20  # 밝기

enhanced = cv2.convertScaleAbs(img, alpha=alpha, beta=beta)
cv2.imwrite(output_path, enhanced)

print("Saved:", output_path)
