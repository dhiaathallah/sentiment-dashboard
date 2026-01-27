# 📊 *Dashboard* Analisis Sentimen Ulasan Aplikasi BYOND by BSI
Dashboard ini merupakan aplikasi berbasis Streamlit yang digunakan untuk melakukan analisis sentimen ulasan pengguna aplikasi BYOND by BSI menggunakan pendekatan Natural Language Processing (NLP) dengan model IndoBERT. Aplikasi ini dirancang agar mudah digunakan oleh pengguna non-teknis sekalipun.

---

### ✨ Fitur Utama
- *Upload* data ulasan dalam format CSV atau Excel (.xlsx)
- Analisis sentimen otomatis menggunakan model IndoBERT
- Klasifikasi sentimen (Positif / Netral / Negatif)
- Visualisasi hasil analisis (grafik dan wordcloud)
- Tampilan *dashboard* interaktif

---

### 🧰 *Library* yang Digunakan
Berikut adalah *library* utama yang digunakan dalam pengembangan *dashboard* ini:
| *Library* | Fungsi |
|--------|--------|
| streamlit | Membuat *dashboard* web interaktif berbasis Python |
| torch | *Framework deep learning* untuk memuat dan menjalankan model (.pth) |
| transformers | *Library* NLP untuk model IndoBERT dan tokenizer |
| pandas | Pengolahan dan manipulasi data tabular |
| numpy | Operasi numerik dan *array* |
| matplotlib | Visualisasi grafik |
| wordcloud | Visualisasi kata dominan dari teks |
| openpyxl | Membaca *file* Excel (.xlsx) |

---
### 🌐 Panduan Penggunaan Dashboard
- Akses tautan berikut untuk membuka *dashboard*:
  [Dashboard Analisis Sentimen](https://sentiment-dashboard-byond.streamlit.app/)
- Pilih metode *input* data
- Jika memilih "Ketik manual", ketikkan ulasan yang ingin dilakukan analisis
- Jika memilih "*Upload file*", unggah data ulasan dalam bentuk `.csv` atau `.xlsx`. Lalu pilih kolom yang berisikan ulasan pada data
- Klik tombol "🔍 Analisis" untuk memproses
- Setelah proses selesai, *dashboard* akan menampilkan: tabel hasil klasifikasi, grafik distribusi, dan *wordcloud* dari kata yang sering muncul pada setiap kelas
---
### 📄 Penutup
*Dashboard* ini dikembangkan sebagai bagian dari tugas akhir/skripsi dengan tujuan mempermudah proses analisis sentimen ulasan pengguna aplikasi BYOND by BSI secara visual, interaktif, dan mudah digunakan.

📬 Jika terdapat pertanyaan atau kendala dalam penggunaan aplikasi, silakan hubungi pengembang pada kontak berikut ini:
- E-mail: dheaathallah@gmail.com
- WhatsApp: 081946853046
