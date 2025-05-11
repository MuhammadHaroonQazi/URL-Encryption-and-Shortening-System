# 🔐 URL Encryption and Shortening System

This project is a secure URL encryption and shortening system built with **Flask**. It allows users to encrypt URLs using various symmetric key algorithms, providing an additional layer of confidentiality before sharing sensitive links.

## 🧩 Features

- 🔑 Supports **AES**, **XOR**, **DES**, and **Blowfish** encryption
- 🧠 Dynamically shows key input based on selected algorithm
- ✅ Session-based logic (no database needed)
- ❌ Invalid key or mismatched algorithm shows friendly error
- 🌐 User-friendly web interface built with HTML & CSS

---

## 🚀 How It Works

1. User enters a long URL.
2. Selects an encryption algorithm from the dropdown.
3. Provides a secret key (required for selected algorithms).
4. System encrypts and shortens the URL.
5. Receiver can decrypt it by selecting the same algorithm and entering the correct key.

---


## 🛠️ Technology Stack

- **Python 3.13**
- **Flask**
- **Cryptography (Fernet)** – AES
- **PyCryptodome** – DES & Blowfish
- **HTML/CSS** for frontend

---

##  How to run it 
    -Create Virtual Environment
    -python -m venv venv
    -venv\Scripts\activate   # Windows
# OR
    -source venv/bin/activate  # macOS/Linux

    
  ## Install Requirements
  --- pip install -r requirements.txt


