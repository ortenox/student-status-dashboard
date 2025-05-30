# Proyek Akhir: Menyelesaikan Permasalahan Perusahaan Edutech

## Business Understanding
Jaya Jaya Institut merupakan institusi pendidikan tinggi yang telah berdiri sejak tahun 2000. Meski dikenal sebagai salah satu perguruan terbaik dan telah mencetak banyak lulusan unggulan, Jaya Jaya Institut menghadapi tantangan serius: tingginya jumlah siswa yang tidak menyelesaikan pendidikannya alias dropout.

Fenomena ini berdampak besar bagi institusi:
- Menurunnya tingkat kelulusan yang dapat memengaruhi reputasi institusi.
- Berkurangnya pendapatan dari biaya pendidikan.
- Efektivitas program akademik yang berkurang karena ketidaktercapaian output siswa.

Sebagai upaya preventif, Jaya Jaya Institut ingin mendeteksi lebih awal siswa yang berpotensi dropout agar bisa diberikan bimbingan khusus. Mereka menyediakan dataset performa siswa dan meminta bantuan untuk membuat sistem prediksi serta dashboard monitoring berbasis data.

### Permasalahan Bisnis
Permasalahan utama yang ingin diselesaikan oleh institusi ini adalah:
- Mendeteksi siswa yang berpotensi dropout secara dini berdasarkan data historis.
- Memberikan visualisasi yang informatif untuk mendukung pengambilan keputusan.
- Meningkatkan efektivitas intervensi akademik dan bimbingan terhadap siswa berisiko tinggi.

### Cakupan Proyek
- Melakukan eksplorasi data performa siswa (EDA).
- Melakukan preprocessing dan encoding variabel.
- Membangun model klasifikasi untuk prediksi dropout menggunakan Random Forest.
- Mengevaluasi performa model menggunakan metrik akurasi, F1-score, dan confusion matrix.
- Menyediakan dashboard visualisasi interaktif berbasis Streamlit untuk memudahkan analisis data.

### Persiapan
**Sumber Data:**(https://github.com/dicodingacademy/dicoding_dataset/blob/main/students_performance/data.csv)

Setup environment:
```
- Setup Environment - Shell/Terminal
pip install pipenv
pipenv install
pipenv shell
pip install -r requirement.txt
```
**Run File**
- Jalankan file dengan perintah :
    python notebook.py

## Business Dashboard
**Business Dashboard:**[Business Dashboard](https://public.tableau.com/views/GemaEkaPutraPrameswara-StudentStatusDashboard/Dashboard1?:language=en-US&:sid=&:redirect=auth&:display_count=n&:origin=viz_share_link)

Dashboard ini bertujuan untuk mengidentifikasi pola dan faktor yang mempengaruhi status akademik mahasiswa (Dropout, Enrolled, Graduate) untuk membantu institusi dalam:
- Meningkatkan tingkat kelulusan
- Menurunkan angka dropout
- Merancang intervensi strategis berbasis data

1. Grafik: Jumlah Mahasiswa Berdasarkan Status
Insight:

- Graduate: 2.209 mahasiswa (~48%)
- Dropout: 1.421 mahasiswa (~31%)
- Enrolled (Aktif): 794 mahasiswa (~17%)

Interpretasi:

Mayoritas mahasiswa berhasil lulus, namun tingkat dropout masih tergolong tinggi dan perlu perhatian lebih lanjut.

2. Grafik: Status Mahasiswa berdasarkan Umur Saat Masuk (Age at Enrollment)
Insight:

- Mahasiswa yang lulus memiliki jumlah umur akumulatif tertinggi (48.120)
- Disusul oleh dropout (37.044), dan enrolled (17.761)

Interpretasi:

- Mahasiswa yang dropout tampaknya juga memiliki umur yang cukup tinggi saat masuk, yang bisa jadi berdampak pada risiko tidak menyelesaikan kuliah.
- Umur masuk kuliah bisa menjadi indikator risiko dropout, terutama jika dikombinasikan dengan faktor lain seperti pekerjaan atau tanggungan keluarga.

3. Grafik: Status Mahasiswa Berdasarkan Kepemilikan Beasiswa (Scholarship Holder)
Insight:

- Penerima beasiswa paling banyak berhasil lulus (835 orang)
- Dropout dan enrolled di kalangan penerima beasiswa relatif rendah (134 dan 130)

Interpretasi:

- Beasiswa terbukti memiliki pengaruh positif terhadap keberhasilan studi mahasiswa.
- Penerima beasiswa memiliki kemungkinan lebih besar untuk menyelesaikan studinya.

## Menjalankan Sistem Machine Learning
Setup environment:
```
- Setup Environment - Shell/Terminal
pip install pipenv
pipenv install
pipenv shell
pip install -r requirement.txt
```
**Run File**
- Jalankan file dengan perintah :
    python app.py

- Dashboard streamlit cloud bisa diakses di
**Streamlit Cloud:**(https://eaezfyj4bhtpmxhxmwhx3b.streamlit.app/)

## Conclusion
Berdasarkan dashboard yang telah dibuat: 
1. Beasiswa adalah Investasi Strategis:

- Perluasan program beasiswa sangat disarankan untuk meningkatkan angka kelulusan.

- Lakukan pemetaan demografi penerima beasiswa agar lebih tepat sasaran.

2. Faktor Umur Penting Diperhatikan:

- Mahasiswa yang lebih tua saat masuk kuliah berisiko lebih tinggi dropout.

- Buat program pendampingan atau fleksibilitas akademik bagi mahasiswa non-tradisional (dewasa).

3. Analitik Prediktif Bisa Diimplementasikan:

- Gunakan data ini untuk membangun sistem early warning mahasiswa yang berisiko dropout.

- Kombinasikan data umur, beasiswa, gender, nilai akademik, dll.

4. Penguatan Monitoring Mahasiswa Aktif:

- Mahasiswa berstatus “Enrolled” bisa diarahkan secara aktif untuk menyelesaikan studi.

- Gunakan intervensi akademik seperti tutoring, konseling, atau pendampingan karir.

Model klasifikasi berhasil mengidentifikasi siswa yang berpotensi dropout dengan akurasi yang cukup tinggi. Temuan penting dari proyek ini adalah:

- Siswa yang dropout cenderung memiliki pola nilai akademik atau latar belakang tertentu.

- Siswa yang "enrolled" sulit diprediksi karena posisinya yang berada di tengah-tengah (belum dropout, belum lulus).

- Model Random Forest memberikan hasil terbaik dalam klasifikasi tiga kelas target.

Dengan adanya sistem prediksi ini, Jaya Jaya Institut dapat:

- Mengidentifikasi siswa berisiko tinggi dan melakukan intervensi sejak dini.

- Meningkatkan tingkat kelulusan dan efisiensi program pendidikan.

- Menyediakan pendekatan berbasis data untuk kebijakan akademik dan layanan konseling.

### Rekomendasi Action Items
# Action Items untuk Menurunkan Angka Dropout di Jaya Jaya Institut

Berdasarkan hasil analisis dan model prediksi dropout yang dibangun, berikut adalah sejumlah rekomendasi berbasis data yang dapat dilakukan oleh Jaya Jaya Institut untuk mengurangi angka siswa yang tidak menyelesaikan pendidikan:

## 1. Identifikasi dan Intervensi Dini terhadap Siswa Berisiko Tinggi

**Deskripsi:**  
Gunakan model prediksi yang telah dikembangkan untuk secara rutin mengevaluasi seluruh siswa aktif dan mengidentifikasi mereka yang termasuk kategori “Dropout” atau “Enrolled” dengan probabilitas tinggi.

**Tindakan:**
- Integrasikan model ke dalam sistem informasi akademik.
- Buat notifikasi otomatis untuk tim bimbingan akademik saat siswa dengan risiko tinggi terdeteksi.
- Sediakan program mentoring khusus bagi siswa ini.

## 2. Analisis dan Tindak Lanjut terhadap Pola Nilai Akademik

**Deskripsi:**  
Beberapa fitur nilai mata pelajaran seperti Math, Reading, dan Writing memiliki kontribusi signifikan dalam memprediksi kemungkinan dropout.

**Tindakan:**
- Lakukan monitoring berkala terhadap nilai siswa di mata pelajaran utama.
- Identifikasi siswa dengan tren penurunan nilai signifikan.
- Tawarkan kelas remedial atau program pendampingan akademik.

## 3. Pendekatan Psikologis dan Sosial

**Deskripsi:**  
Siswa dengan latar belakang tertentu cenderung memiliki risiko lebih tinggi untuk dropout.

**Tindakan:**
- Lakukan assessment psikologis rutin, terutama untuk siswa baru dan yang berisiko tinggi.
- Perkuat peran konselor sekolah untuk membantu siswa mengelola stres dan motivasi belajar.
- Libatkan orang tua dalam proses pendampingan siswa, terutama dari kelompok rentan.

## 4. Dashboard Monitoring Berkala

**Deskripsi:**  
Dashboard berbasis Streamlit yang telah dibuat dapat digunakan oleh tim manajemen untuk monitoring performa siswa secara real-time.

**Tindakan:**
- Tampilkan metrik dropout mingguan/bulanan pada dashboard manajemen.
- Gunakan dashboard untuk mengevaluasi efektivitas program intervensi yang berjalan.
- Lakukan update model secara berkala agar prediksi tetap akurat.

## 5. Evaluasi dan Perbaikan Model Secara Berkala

**Deskripsi:**  
Model prediksi perlu divalidasi ulang secara rutin agar tetap relevan dengan data terbaru.

**Tindakan:**
- Lakukan retraining model setiap semester dengan data terbaru.
- Tambahkan fitur tambahan jika tersedia (misalnya kehadiran, catatan pelanggaran).
- Bandingkan performa model secara berkala (misalnya Random Forest vs XGBoost).
