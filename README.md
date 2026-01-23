# 🎚️ FingrVol — Gesture Volume Control (Python)

**FingrVol** memungkinkan kamu **mengatur volume komputer menggunakan gerakan jari** melalui webcam.  
Program ini memanfaatkan **MediaPipe Hand Tracking**, **OpenCV**, dan **PyCaw** (khusus Windows).

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
