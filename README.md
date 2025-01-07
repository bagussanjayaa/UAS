# UAS
Nama:  Bagus Sanjaya

NIM:  312410505

Kelas:  TI.24.A.5

## Penjelasan Program yang saya buat

1. File data/mahasiswa.py
File ini berisi definisi dari kelas Mahasiswa dan DataMahasiswa, serta fungsi hitung_nilai_akhir yang digunakan untuk menghitung nilai akhir mahasiswa.

a. Fungsi hitung_nilai_akhir:
```python
def hitung_nilai_akhir(tugas, uts, uas):
    return (tugas * 0.3) + (uts * 0.35) + (uas * 0.35)
```
Fungsi ini digunakan untuk menghitung nilai akhir dari seorang mahasiswa berdasarkan bobot nilai tugas (30%), UTS (35%), dan UAS (35%).

b. Kelas Mahasiswa:
```python
class Mahasiswa:
    def __init__(self, nim, nama, tugas, uts, uas):
        self.nim = nim
        self.nama = nama
        self.tugas = tugas
        self.uts = uts
        self.uas = uas
        self.nilai_akhir = hitung_nilai_akhir(tugas, uts, uas)
```
Kelas ini merepresentasikan seorang mahasiswa dengan atribut NIM, nama, nilai tugas, nilai UTS, nilai UAS, dan nilai akhir yang dihitung menggunakan fungsi hitung_nilai_akhir.

c. Kelas DataMahasiswa:
```python
class DataMahasiswa:
    def __init__(self):
        self.data_mahasiswa = {}

    def tambah(self, mahasiswa):
        self.data_mahasiswa[mahasiswa.nim] = mahasiswa
        print("Data berhasil ditambahkan!")

    def ubah(self, nim, nama, tugas, uts, uas):
        if nim in self.data_mahasiswa:
            mahasiswa = Mahasiswa(nim, nama, tugas, uts, uas)
            self.data_mahasiswa[nim] = mahasiswa
            print("Data berhasil diubah!")
        else:
            print("Data tidak ditemukan.")

    def hapus(self, nim):
        if nim in self.data_mahasiswa:
            del self.data_mahasiswa[nim]
            print("Data berhasil dihapus!")
        else:
            print("Data tidak ditemukan.")

    def lihat(self):
        return self.data_mahasiswa

    def cari(self, nim):
        return self.data_mahasiswa.get(nim, None)
```
Kelas ini digunakan untuk menyimpan, menambah, mengubah, menghapus, melihat, dan mencari data mahasiswa. Data mahasiswa disimpan dalam sebuah dictionary dengan NIM sebagai kunci.

2. File view/mahasiswa_view.py
File ini berisi definisi dari kelas View yang digunakan untuk menampilkan data mahasiswa dalam bentuk tabel.

a. Kelas View:
```python
class View:
    @staticmethod
    def display_data(data):
        if data:
            print("Daftar Nilai Mahasiswa")
            print("-----------------------------------------------------------------------------------------")
            print("| NO | NIM           | NAMA                 | TUGAS    | UTS      | UAS      | AKHIR    |")
            print("-----------------------------------------------------------------------------------------")
            for i, (nim, mhs) in enumerate(data.items(), start=1):
                print(f"| {i:<2} | {nim:<13} | {mhs.nama:<20} | {mhs.tugas:<8.2f} | {mhs.uts:<8.2f} | {mhs.uas:<8.2f} | {mhs.nilai_akhir:<8.2f} |")
                print("-----------------------------------------------------------------------------------------")
        else:
            print("Daftar Nilai Mahasiswa")
            print("-----------------------------------------------------------------------------------------")
            print("| NO | NIM           | NAMA                 | TUGAS    | UTS      | UAS      | AKHIR    |")
            print("-----------------------------------------------------------------------------------------")
            print("|                                    TIDAK ADA DATA                                     |")
            print("-----------------------------------------------------------------------------------------")
```
Kelas ini digunakan untuk menampilkan data mahasiswa dalam bentuk tabel. Jika tidak ada data, akan ditampilkan pesan "TIDAK ADA DATA".

3. File process/mahasiswa_process.py
File ini berisi definisi dari kelas Process yang digunakan untuk memvalidasi input nilai yang diberikan oleh pengguna.

a. Kelas Process:
```python
class Process:
    @staticmethod
    def validate_nilai(nilai):
        try:
            nilai = float(nilai)
            if nilai < 0 or nilai > 100:
                raise ValueError("Nilai harus antara 0 dan 100.")
            return nilai
        except ValueError as e:
            print(f"Input tidak valid: {e}")
            return None
```
Kelas ini digunakan untuk memvalidasi nilai yang dimasukkan oleh pengguna agar berada dalam rentang 0 hingga 100. Jika nilai tidak valid, akan mengembalikan None dan menampilkan pesan kesalahan.

4. File main.py
File ini berisi fungsi-fungsi utama yang digunakan untuk mengelola alur program, termasuk menambah, mengubah, menghapus, melihat, dan mencari data mahasiswa.

a. Fungsi tambah_data:
```python
import time
from data.mahasiswa import DataMahasiswa, Mahasiswa
from view.mahasiswa_view import View
from process.mahasiswa_process import Process

def tambah_data(data_mahasiswa):
    nim = input("Masukkan NIM: ")
    nama = input("Masukkan Nama: ")

    while True:
        tugas = input("Masukkan Nilai Tugas: ")
        tugas = Process.validate_nilai(tugas)
        if tugas is not None:
            break

    while True:
        uts = input("Masukkan Nilai UTS: ")
        uts = Process.validate_nilai(uts)
        if uts is not None:
            break

    while True:
        uas = input("Masukkan Nilai UAS: ")
        uas = Process.validate_nilai(uas)
        if uas is not None:
            break

    mahasiswa = Mahasiswa(nim, nama, tugas, uts, uas)
    data_mahasiswa.tambah(mahasiswa)
    time.sleep(1)
```
Fungsi ini digunakan untuk meminta input dari pengguna untuk menambah data mahasiswa, termasuk validasi nilai menggunakan kelas Process.

b. Fungsi ubah_data:
```python
def ubah_data(data_mahasiswa):
    nim = input("Masukkan NIM mahasiswa yang akan diubah: ")
    if data_mahasiswa.cari(nim):
        nama = input("Masukkan Nama baru: ")
        while True:
            tugas = input("Masukkan Nilai Tugas baru: ")
            tugas = Process.validate_nilai(tugas)
            if tugas is not None:
                break

        while True:
            uts = input("Masukkan Nilai UTS baru: ")
            uts = Process.validate_nilai(uts)
            if uts is not None:
                break

        while True:
            uas = input("Masukkan Nilai UAS baru: ")
            uas = Process.validate_nilai(uas)
            if uas is not None:
                break

        data_mahasiswa.ubah(nim, nama, tugas, uts, uas)
    else:
        print("Data tidak ditemukan.")
    time.sleep(1)
```
Fungsi ini digunakan untuk mengubah data mahasiswa yang sudah ada.

c. Fungsi hapus_data:
```python
def hapus_data(data_mahasiswa):
    nim = input("Masukkan NIM mahasiswa yang akan dihapus: ")
    data_mahasiswa.hapus(nim)
    time.sleep(1)
```
Fungsi ini digunakan untuk menghapus data mahasiswa berdasarkan NIM.

d. Fungsi cari_data:
```python
def cari_data(data_mahasiswa):
    nim = input("Masukkan NIM mahasiswa yang dicari: ")
    mahasiswa = data_mahasiswa.cari(nim)
    if mahasiswa:
        print("Data ditemukan:", mahasiswa)
    else:
        print("Data tidak ditemukan.")
    time.sleep(1)
```
Fungsi ini digunakan untuk mencari data mahasiswa berdasarkan NIM.

e. Fungsi main:
```python
def main():
    data_mahasiswa = DataMahasiswa()

    while True:
        pilihan = input("[ (T)ambah, (U)bah, (H)apus, (L)ihat, (C)ari, (K)eluar ]: ").lower()
        if pilihan == 't':
            tambah_data(data_mahasiswa)
        elif pilihan == 'u':
            ubah_data(data_mahasiswa)
        elif pilihan == 'h':
            hapus_data(data_mahasiswa)
        elif pilihan == 'l':
            View.display_data(data_mahasiswa.lihat())
        elif pilihan == 'c':
            cari_data(data_mahasiswa)
        elif pilihan == 'k':
            print("Terima kasih telah menggunakan program ini!")
            break
        else:
            print("Pilihan tidak valid, silakan coba lagi.")
        time.sleep(1)

if __name__ == "__main__":
    main()
```
Fungsi ini adalah fungsi utama yang mengatur alur program, meminta input dari pengguna untuk menambah, mengubah, menghapus, melihat, dan mencari data mahasiswa.

## Link YouTube Video Dokumentasi

[YouTube](https://youtu.be/qmEYDO0_DAc?si=8h1dh72b08pG8FfR)
