🌈🔐 Pixel Manipulation Image Encryption Tool (Flask Web App)  
A **Flask-based web application** to **encrypt and decrypt images** using **pixel manipulation and pixel swapping**.  

---

🌙 Dark/Light Mode Preview *(if added later)*  
![Preview Screenshot](https://your-screenshot-link-here)

📌 **Overview**  
This tool is a simple web-based application that allows users to encrypt and decrypt images using a **numeric key**, performing pixel-level modifications and swaps for educational purposes.  

---

🚀 **Features**

- 🔒 AES-like simple **pixel encryption/decryption** using a numeric key  
- 🎨 **Modify pixel values mathematically** and **randomly shuffle pixels**  
- 👁️ **Preview processed images** in browser  
- 💾 **Download encrypted/decrypted images**  
- 🌈 **Colorful, user-friendly interface** using HTML, CSS, and Flask  

---

📂 **Project Folder Structure**

pixel_encryption_flask/
├── app.py # Flask backend
├── uploads/ # Temporary folder for uploaded images
├── static/ # Static files like CSS and processed images
│ ├── style.css # CSS file for styling
│ └── processed_image.png # Generated encrypted/decrypted image
└── templates/ # HTML templates
├── index.html # Upload page
└── result.html # Processed image preview page





> ✅ Tip: `processed_image.png` is created automatically when encrypting/decrypting images.

---

⚙️ **Installation**

1️⃣ **Install dependencies**  

```bash
pip install flask pillow
2️⃣ Run the Flask app



python app.py
3️⃣ Open the web page


http://127.0.0.1:5000/
📡 How to Use

Upload the image (JPG, PNG, etc.)

Enter a numeric key 🔑

Click Encrypt or Decrypt

Preview the processed image

Click Download to save the image

🔑 How It Works

Encryption:

Adds the key to each pixel’s RGB values (mod 256)

Randomly swaps some pixels

Saves the result as processed_image.png

Decryption:

Subtracts the key from each pixel’s RGB values (mod 256)

Applies the same pixel swaps

Restores the original image

⭐ Future Improvements

Add Dark/Light mode toggle

Add file upload encryption

Make a mobile-friendly version

Host online (GitHub Pages / Cloud)

🧑‍💻 Developer

RameshKannan M
Cybersecurity & Networking Enthusiast

GitHub: https://github.com/Rameshkannan9203

📜 License

For educational purposes & learning only


