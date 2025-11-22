🌙🔐 Pixel Manipulation Image Encryption Tool (Dark Mode Edition)  
A **Flask-based web application** to **encrypt and decrypt images** using **pixel manipulation and pixel swapping**.  

---

🌌 **Dark Mode Preview** *(add screenshot if available)*  
![Dark Mode Screenshot](https://your-darkmode-image-link-here)

🌞 **Light Mode Preview** *(optional)*  
![Light Mode Screenshot](https://your-lightmode-image-link-here)

📌 **Overview**  
This tool is a **secure educational app** that allows users to encrypt and decrypt images using a numeric key.  
It modifies pixels mathematically and swaps them for basic encryption demonstration.  

---

🚀 **Features**

- 🔒 **Pixel-level encryption/decryption** using a numeric key  
- 🎨 **Mathematically modify pixel values** and **randomly shuffle pixels**  
- 👁️ **Preview encrypted/decrypted images** in browser  
- 💾 **Download processed images**  
- 🌈 **User-friendly, colorful interface** using **HTML, CSS, Flask**  
- 🌙 Optional **Dark Mode** theme (can be added to CSS later)  

---

📂 **Project Folder Structure**

pixel_encryption_flask/
├── app.py # Flask backend
├── uploads/ # Temporary folder for uploaded images
├── static/ # Static files like CSS and processed images
│ ├── style.css # CSS file for styling (can include dark mode)
│ └── processed_image.png # Generated encrypted/decrypted image
└── templates/ # HTML templates
├── index.html # Upload page
└── result.html # Processed image preview page


> ✅ Tip: `processed_image.png` is automatically generated when encrypting/decrypting images.

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

Add Dark/Light Mode toggle in CSS

Add file upload encryption

Make a mobile-friendly version

Host online (GitHub Pages / Cloud)

🧑‍💻 Developer

RameshKannan
Cybersecurity & Networking Enthusiast

GitHub: https://github.com/Rameshkannan9203

📜 License

For educational purposes & learning only
