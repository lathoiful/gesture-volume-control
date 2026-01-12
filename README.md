# 🎚️ Gesture Volume Control (Python)

Project ini memungkinkan kamu **mengatur volume komputer menggunakan gerakan jari** melalui webcam.
Program memanfaatkan **MediaPipe Hand Tracking**, **OpenCV**, dan **PyCaw** (khusus Windows).

---

## ✨ Fitur

* Kontrol volume real-time menggunakan jarak jari
* Menggunakan webcam (tanpa hardware tambahan)
* Tracking 1 tangan (jempol & telunjuk)
* Tampilan visual bar volume

---

## 🧠 Cara Kerja Singkat

* Kamera mendeteksi tangan
* Sistem membaca posisi **jempol (id 4)** dan **telunjuk (id 8)**
* Jarak antar jari dikonversi menjadi persentase volume
* Volume sistem diubah secara langsung

---

## 🛠️ Requirements

* **Python 3.10.x (WAJIB)**
* **Windows OS** (karena PyCaw hanya support Windows)
* Webcam aktif

### Library yang digunakan:

* opencv-python
* mediapipe
* numpy
* pycaw
* comtypes
* absl-py

---

## 📦 Instalasi

Pastikan Python 3.10 sudah terinstall, lalu jalankan:

```bash
py -3.10 -m pip install -r requirements.txt
```

---

## ▶️ Menjalankan Program

Masuk ke folder project, lalu jalankan:

```bash
py -3.10 control_volume.py
```

Tekan **Q** untuk keluar dari program.

---

## ⚠️ Catatan Penting

* Program **tidak menggunakan virtual environment (venv)**
* Pastikan library terinstall di Python 3.10
* Jalankan di ruangan dengan pencahayaan cukup
* Jika webcam tidak terbuka, cek index kamera (`VideoCapture(0)`)

---

## 🧪 Troubleshooting

**MediaPipe error / AttributeError?**

* Pastikan versi mediapipe sesuai di `requirements.txt`

**Volume tidak berubah?**

* Pastikan OS Windows
* Jalankan terminal sebagai user biasa (bukan admin)

---

## 📸 Preview

*(Tambahkan screenshot / GIF demo di sini)*

---

## 📚 Teknologi

* Python 3.10
* OpenCV
* MediaPipe Hands
* PyCaw (Windows Audio API)

---

## 📜 Lisensi

Project ini dibuat untuk **belajar dan edukasi**.
Bebas digunakan dan dimodifikasi.

---

## 👤 Author

**Lathoiful Ikhsan**
SMK Student | Python & IoT Enthusiast

---

🔥 Cocok untuk tugas sekolah, portfolio GitHub, dan eksperimen Computer Vision.
