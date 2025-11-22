# 🎨 Pixel Manipulation Image Encryption Tool

A **Flask-based web application** to **encrypt and decrypt images** using **pixel manipulation and pixel swapping**.  
This project demonstrates a simple image encryption method with a **colorful web interface**.  

---

## ✨ Features

- 🔒 Encrypt and decrypt images using a **numeric key**  
- 🎨 Pixel values are **modified mathematically** and pixels are **randomly shuffled**  
- 👁️ Preview the **processed image** on a web page  
- 💾 Download the encrypted or decrypted image  
- 🌈 Colorful, user-friendly interface using **HTML, CSS, and Flask**

---

## 📂 Folder Structure

pixel_encryption_flask/
│
├── app.py # Flask backend
├── uploads/ # Temporary folder for uploaded images
├── static/ # Static files like CSS and processed images
│ ├── style.css # CSS file for styling
│ └── processed_image.png # Generated encrypted/decrypted image
└── templates/ # HTML templates
├── index.html # Upload page
└── result.html # Processed image preview page

yaml
Copy code

---

## 🛠️ Requirements

- Python 3.x  
- Flask  
- Pillow (Python Imaging Library)

Install required packages:

```bash
pip install flask pillow
🚀 How to Run
Open terminal/command prompt in the project folder.

Run the Flask app:

bash
Copy code
python app.py
Open a web browser and go to:

cpp
Copy code
http://127.0.0.1:5000/
On the web page:

Upload an image (JPG, PNG, etc.)

Enter a numeric key 🔑

Click Encrypt or Decrypt

Preview the processed image

Click Download to save the image

🔑 How It Works
Encryption:

Adds the key to each pixel's RGB values (mod 256)

Randomly swaps some pixels

Saves the result as processed_image.png

Decryption:

Subtracts the key from each pixel's RGB values (mod 256)

Applies the same pixel swaps

Restores the original image

⚠️ Notes
Do NOT open index.html or result.html directly — always access via Flask URL: http://127.0.0.1:5000/

The encryption is basic and for educational purposes only.

👤 Author
Ramesh Kannan
Internship Project – Image Encryption Tool