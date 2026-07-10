import cv2
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[1]
IMAGE_PATH = PROJECT_ROOT / "assets" / "test.jpg"
OUTPUT_PATH = PROJECT_ROOT / "results" / "gray_test.jpg"

image = cv2.imread(str(IMAGE_PATH))

if image is None:
    raise FileNotFoundError(f"Could not read image: {IMAGE_PATH}")

gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

cv2.imwrite(str(OUTPUT_PATH), gray_image)

cv2.imshow("Original Image", image)
cv2.imshow("Grayscale Image", gray_image)

print(f"Original image shape: {image.shape}")
print(f"Grayscale image saved to: {OUTPUT_PATH}")

cv2.waitKey(0)
cv2.destroyAllWindows()
