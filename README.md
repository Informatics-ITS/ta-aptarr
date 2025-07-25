# 🏁 Tugas Akhir (TA) - Final Project

**Nama Mahasiswa**: Apta Rasendriya Wijaya  
**NRP**: 5025211139  
**Judul TA**: Pelatihan Kontinu Model Deteksi Intrusi Berbasis Jaringan Menggunakan Recurrent Neural Network (RNN)  
**Dosen Pembimbing**: Baskoro Adi Pratomo, S.Kom., M.Kom, PhD.   
**Dosen Ko-pembimbing**: Hudan Studiawan, S.Kom., M.Kom, PhD. 

---

## 📺 Demo Aplikasi  

<a href="https://youtu.be/_pCb_-ZeSdE">
  <img src="https://github.com/user-attachments/assets/af4a37d3-39c5-417b-80aa-849bfcedc266" alt="Demo Aplikasi" width="800" />
</a>

*Klik gambar di atas untuk menonton demo*


---

## 🛠 Panduan Instalasi & Menjalankan Software  

### Prasyarat  
- 🐍 Versi Python:  
  - Disarankan menggunakan **Python 3.9.x**  
    > ⚠️ Beberapa library mungkin tidak kompatibel dengan Python versi 3.10 ke atas.
- 📦 Library & Dependensi  
   Semua dependensi didefinisikan di file `requirements.txt`.

### Langkah-langkah  
1. **Clone Repository**  
   ```bash
   git clone https://github.com/Informatics-ITS/ta-aptarr.git
   ```

2. **Instalasi Dependensi**  
   Agar library Python yang ada di perangkat tidak tercampur dengan library aplikasi ini, disarankan menggunakan virtual environment (env).

   ```bash
   cd ta-aptarr
   python3 -m venv myenv
   ```

   Untuk mengaktifkan env:

   - **Linux/Mac:**

   ```bash
   source myenv/bin/activate
   ```

   - **Windows:**

   ```bash
   myenv\Scripts\activate
   ```

   Untuk menonaktifkan env, cukup jalankan:

   ```bash
   deactivate
   ```

   Setelah env aktif, instal semua dependensi dengan:

   ```bash
   pip install -r requirement.txt
   ```

   Atau Anda dapat menginstal library satu per satu saat menjalankan kode, jika muncul error terkait library yang belum ada.

   ## ⚠️ Saran:
   Jika Anda menggunakan **Windows**, disarankan **menonaktifkan sementara Windows Defender** saat proses instalasi library.  
   Beberapa library (terutama yang berbasis C atau mengakses sistem) terkadang **salah terdeteksi sebagai malware**, yang dapat menyebabkan instalasi gagal.

3. **Jalankan Aplikasi**  
   **a. Converting Data**
   ```python
   python3 converting.py [mode] [protokol] [port] [panjang-n-gram] [file-pcap]
   ```
   Penjelasan Argumen:

   - **[mode]:** Tentukan apakah data yang akan dikonversi untuk training atau testing. Pilih training untuk data pelatihan dan testing untuk data pengujian.

   - **[protokol]:** Jenis protokol jaringan yang digunakan, seperti tcp, udp, dll.

   - **[port]:** Port yang digunakan, misalnya 21 untuk FTP, 80 untuk HTTP dan lain-lain.

   - **[panjang-n-gram]:** Panjang n-gram kata yang digunakan dalam analisis. Contoh: 5 untuk n-gram berukuran 5.

   - **[file-pcap]:** Lokasi file pcap yang akan dikonversi. 

   Contoh:
   ```python
   python3 converting.py training tcp 80 5 "CIC-IDS-2017_Dataset/Tuesday-WorkingHours.pcap"
   ```
   **b. Training Model** 
   ```python
   python3 rnnids-vectorizer.py training [model] [protokol] [port] [hidden-layer] [panjang-n-gram] [dropout] [jumlah-kamus] [file-traning] [batch-size]
   ```
   Penjelasan Argumen:

   - **[model]:** Jenis model yang digunakan untuk training, seperti lstm, gru, dll.

   - **[protokol]:** Jenis protokol yang digunakan, misalnya tcp.

   - **[port]:** Port yang digunakan, seperti 21 untuk FTP, 80 untuk HTTP dan lain-lain.
     
   - **[hidden-layer]:** Jumlah unit atau lapisan tersembunyi (hidden layers) dalam model. Contoh: 2.

   - **[panjang-n-gram]:** Panjang n-gram untuk fitur yang digunakan dalam model.

   - **[dropout]:** Tingkat dropout untuk regularisasi, misalnya 0.2.

   - **[jumlah-kamus]:** Ukuran kamus yang digunakan dalam model.

   - **[file-traning]:** File dataset (dalam format .txt) yang digunakan untuk pelatihan.

   - **[batch-size]:** Jumlah data yang diproses dalam setiap iterasi (epoch), misalnya 128.

   Contoh:
   ```python
   python3 rnnids-vectorizer.py training lstm tcp 80 2 5 0.2 1500 Tuesday-WorkingHours_training_80 128
   ```
   **c. Testing Model**
   ```python
   python3 rnnids-vectorizer.py testing [model] [protokol] [port] [hidden-layer] [panjang-n-gram] [dropout] [jumlah-kamus] [nama-model] [file-testing]
   ```
   Penjelasan Argumen:

   - **[model]:** Jenis model yang digunakan untuk pengujian, seperti lstm.

   - **[protokol]:** Jenis protokol yang digunakan, misalnya tcp.

   - **[port]:** Port yang digunakan, seperti 21 untuk FTP, 80 untuk HTTP dan lain-lain.
     
   - **[hidden-layer]:** Jumlah unit atau lapisan tersembunyi (hidden layers) dalam model. Contoh: 2.

   - **[panjang-n-gram]:** Panjang n-gram untuk fitur yang digunakan dalam model.

   - **[dropout]:** Tingkat dropout yang digunakan untuk pengujian model.

   - **[jumlah-kamus]:** Jumlah kamus yang digunakan dalam model.

   - **[nama-model]:** Nama model yang akan diuji.

   - **[file-testing]:** File dataset (dalam format .txt) yang digunakan untuk pengujian.

   Contoh:
   ```python
   python3 rnnids-vectorizer.py testing lstm tcp 80 2 5 0.2 1500 Tuesday-WorkingHours_training_80 Monday-WorkingHours_testing_80
   ```
   **d. Retraining Model**
   ```python
   python3 rnnids-retraining.py retraining [model] [protokol] [port] [hidden-layer] [panjang-n-gram] [dropout] [jumlah-kamus] [nama-model] [file-testing]
   ```
   Penjelasan Argumen:

   - **[model]:** Jenis model yang digunakan untuk retraining, misalnya lstm.

   - **[protokol]:** Jenis protokol yang digunakan, seperti tcp.

   - **[port]:** Port yang digunakan, seperti 21 untuk FTP, 80 untuk HTTP dan lain-lain.
     
   - **[hidden-layer]:** Jumlah unit atau lapisan tersembunyi (hidden layers) dalam model. Contoh: 2.

   - **[panjang-n-gram]:** Panjang n-gram untuk fitur yang digunakan dalam model.

   - **[dropout]:** Tingkat dropout yang digunakan dalam retraining.

   - **[jumlah-kamus]:** Jumlah kamus yang digunakan untuk retraining.

   - **[nama-model]:** Nama model yang akan diretrain.

   - **[file-testing]:** File dataset testing (dalam format .txt) yang digunakan untuk retraining.

   Keterangan:  

   Perintah retraining hampir sama dengan testing, namun berbeda pada argumen pertama yang menggunakan retraining. Setelah proses training dan testing selesai, program akan menghitung pergeseran data anomaly antara training dan testing untuk memperbarui model.  


   Contoh:
   ```python
   python3 rnnids-retraining.py retraining lstm tcp 21 2 2 0.2 3500 part_1_Treatment_training_21 part_2_Treatment_testing_21
   ```
---

## ➕ Tambahan

### 📊 Dataset yang Digunakan  
Dataset yang digunakan dalam tugas akhir ini adalah:  
- [Download Dataset](https://itsacid-my.sharepoint.com/:u:/g/personal/baskoro_its_ac_id/EVAOAuxs67JGkf0y6lRD2bIB4_kVB1dPjoDFJM2QtT66cA?e=Ec7HWj)

### 🤖 Model yang Digunakan  
Model machine learning export yang digunakan:  
- [Download Model](https://itsacid-my.sharepoint.com/:u:/g/personal/baskoro_its_ac_id/Ed8kj9bit5hBvxTDU3YtAMgBERYmEI9JiNZxWRyKGOc8hg?e=grjbmz)

---

## ⁉️ Pertanyaan?

Hubungi:
- Penulis: apta.rasendriya@gmail.com
- Pembimbing Utama: baskoro@if.its.ac.id
