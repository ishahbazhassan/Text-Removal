import cv2
import numpy as np
import easyocr
from PIL import Image
import requests
from io import BytesIO
import matplotlib.pyplot as plt

# Initialize EasyOCR reader
reader = easyocr.Reader(['ch_sim', 'en'], gpu=False)

# Download image from URL
def download_image(url):
    response = requests.get(url)
    image = Image.open(BytesIO(response.content)).convert("RGB")
    return cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)

# Create mask based on text bounding boxes
def create_text_mask(image):
    results = reader.readtext(image)
    mask = np.zeros(image.shape[:2], dtype=np.uint8)

    for (bbox, text, conf) in results:
        if conf > 0.3:  # Confidence threshold
            pts = np.array(bbox, dtype=np.int32)
            cv2.fillPoly(mask, [pts], 255)

    # Optional: dilate to expand the mask
    kernel = np.ones((5, 5), np.uint8)
    mask = cv2.dilate(mask, kernel, iterations=1)

    return mask

# Remove text using inpainting
def remove_text(image, mask):
    return cv2.inpaint(image, mask, 3, cv2.INPAINT_TELEA)

# Process and display
def process_and_show(url, idx):
    image = download_image(url)
    mask = create_text_mask(image)
    cleaned = remove_text(image, mask)

    # Save and display
    cv2.imwrite(f"cleaned_{idx}.png", cleaned)
    plt.figure(figsize=(12,6))
    plt.subplot(1,2,1)
    plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
    plt.title("Original")
    plt.axis('off')
    
    plt.subplot(1,2,2)
    plt.imshow(cv2.cvtColor(cleaned, cv2.COLOR_BGR2RGB))
    plt.title("Cleaned")
    plt.axis('off')
    plt.show()

# Image URLs
urls = [
    "https://img.alicdn.com/imgextra/i1/1712484042/O1CN01mLN6kk1fjHZODL77S_!!1712484042.jpg",
    "https://img.alicdn.com/imgextra/i3/1712484042/O1CN01btXCXm1fjHZYStUBU_!!1712484042.jpg"
]

for i, url in enumerate(urls, start=1):
    process_and_show(url, i)
