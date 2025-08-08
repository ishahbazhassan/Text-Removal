 🖼️ Text Removal from Images using Python, OpenCV & EasyOCR

This project removes printed text (**Chinese characters, English text, and numbers**) from images without damaging the background.  
It uses **EasyOCR** to detect text regions and **OpenCV inpainting** to seamlessly fill the removed areas.

---

🚀 Features
- Detects **Chinese (Simplified)** and **English** text from images.
- Automatically creates a mask over detected text regions.
- Uses **OpenCV's Telea inpainting** to fill removed areas with realistic background.
- Works with **online image URLs**.
- Adjustable confidence threshold for detection accuracy.
- Saves cleaned images for later use.

---

📦 Installation
```bash
pip install opencv-python easyocr pillow matplotlib requests numpy
 numbers) from images without damaging the background. It uses EasyOCR to detect text regions and OpenCV inpainting to seamlessly fill the removed areas.
