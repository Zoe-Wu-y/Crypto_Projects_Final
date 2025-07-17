import cv2
import numpy as np

def embed_watermark(image_path, watermark_text, output_path):
    img = cv2.imread(image_path)
    overlay = img.copy()
    cv2.putText(overlay, watermark_text, (30, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (255,255,255), 2)
    cv2.addWeighted(overlay, 0.3, img, 0.7, 0, img)
    cv2.imwrite(output_path, img)

if __name__ == "__main__":
    embed_watermark("samples/sample_image.jpg", "CONFIDENTIAL", "samples/output.jpg")
