<h1 align="center">🌙🔐 Pixel Manipulation Image Encryption Tool (Dark Mode Edition)</h1>
<p align="center">
  <b>A Flask-based web app to encrypt and decrypt images using pixel manipulation and pixel swapping</b>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Mode-Dark%20%26%20Light-blueviolet">
  <img src="https://img.shields.io/badge/Language-Python-blue">
  <img src="https://img.shields.io/badge/Backend-Flask-orange">
  <img src="https://img.shields.io/badge/Encryption-Pixel--Level-purple">
  <img src="https://img.shields.io/badge/Status-Active-success">
</p>

---


## 📌 Overview  
The **Pixel Manipulation Image Encryption Tool** is a web-based application that allows users to **encrypt and decrypt images** using a numeric key.  
It modifies pixel values mathematically and swaps them for basic encryption demonstration.

✨ **Colorful and user-friendly interface**  
✨ **Preview processed images before downloading**  
✨ **Simple encryption and decryption steps for educational purposes**

---

## 🚀 Features  
- 🔒 Encrypt and decrypt images using a **numeric key**  
- 🎨 Pixel values are **modified mathematically** and **pixels are randomly shuffled**  
- 👁️ Preview the **processed image** in the browser  
- 💾 Download the **encrypted/decrypted image**  
- 🌈 Colorful and responsive **HTML/CSS interface**  
- ⚡ **Flask backend** handles processing  

---

## 🗂️ Project Structure
pixel_encryption_flask/
├── app.py # Flask backend
├── uploads/ # Temporary folder for uploaded images
├── static/ # Static files (CSS & processed images)
│ ├── style.css # Styling
│ └── processed_image.png # Generated encrypted/decrypted image
└── templates/ # HTML templates
├── index.html # Upload page
└── result.html # Processed image preview page



---

## ⚙️ Installation

### 1️⃣ Install Dependencies
```bash
pip install flask pillow
2️⃣ Run Backend

python app.py
3️⃣ Open Frontend

http://127.0.0.1:5000/
📡 How It Works
🔸 Encrypt
Add the numeric key to each pixel’s RGB values (mod 256)

Randomly swap pixels

Save result as processed_image.png

🔸 Decrypt
Subtract the numeric key from each pixel’s RGB values (mod 256)

Apply same pixel swaps

Restore original image

⭐ Future Improvements
Add Dark/Light Mode toggle

File upload encryption

Mobile-friendly interface

Online hosted version

🧑‍💻 Developer
Ramesh Kannan
Cybersecurity & Networking Enthusiast

GitHub Profile:
https://github.com/Rameshkannan9203

📜 License
For educational purposes & learning only
