# PA_klasifikasi_kanker_kulit_melanoma

## Deskripsi
Proyek ini adalah tentang klasifikasi kanker kulit melanoma menggunakan data citra kulit. Aplikasi ini gunakan untuk memprediksi apakah citra kulit mengindikasikan apakah termasuk kanker kulit benign atau malignant

## Dataset Yang Digunakan
Dataset yang digunakan dalam proyek ini adalah [Melanoma Skin Cancer Dataset](https://www.kaggle.com/datasets/hasnainjaved/melanoma-skin-cancer-dataset-of-10000-images). Dataset ini berisi 10.000 citra kulit dengan label benign dan malignant.

## Menggunakan Library:
- Flask
- Werkzeug
- pandas
- numpy
- matplotlib
- scikit-learn
- tensorflow:
- Pillow
- ssl

## Instalasi
1. Clone repositori ini:
   ```shell
   git clone https://github.com/safrizal21/PA_klasifikasi_kanker_kulit_melanoma.git
2. Masuk ke direktori proyek:
   ```shell
   cd PA_klasifikasi_kanker_kulit_melanoma/app
3. Buat Virtual Environment:
   ```shell
   conda create melanoma
4. Aktifkan Virtual Environtment:
   ```shell
   activate melanoma
5. Instal dependensi yang diperlukan menggunakan pip:
   ```shell
   pip install -r requirements.txt
4. Jalankan Aplikasi:
   ```shell
   python app.py
