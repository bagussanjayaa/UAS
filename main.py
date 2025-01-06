import time 
from data.mahasiswa import DataMahasiswa, Mahasiswa
from view.mahasiswa_view import View 
from process.mahasiswa_process import Process

def tambah_data(data_mahasiswa):
    nim = input("Masukan NIM: ")
    nama = input("Masukan Nama: ")

    while True:
        tugas = input("Masukan Nilai: ")
        tugas = Process.validate_nilai(tugas)
        if tugas is not None:
            break

    while True:
        uts = input("Masukan Nilai UTS: ")
        uts = Process.validate_nilai(uts)
        if uts is not None:
            break

    while True:
        uas = input("Masukan Nilai UAS: ")
        uas = Process.validate_nilai(uas)
        if uas is not None:
            break

    mahasiswa = Mahasiswa(nim, nama, tugas, uts, uas)
    data_mahasiswa.tambah(mahasiswa)
    time.sleep(1)

def ubah_data(data_mahasiswa):
    nim = input("MAsukan NIM mahasiswa yang akan diubah: ")
    if data_mahasiswa.cari(nim):
        nama = input("Masukan Nama baru: ")
        while True:
            tugas = input("Masukan Nilai Tugas baru: ")
            tugas = Process.validate_nilai(tugas)
            if tugas is not None:
                break

        while True:
            uts = input("Masukan Nilai UTS baru: ")
            uts = Process.validate_nilai(uts)
            if uts is not None:
                break

        while True:
            uas = input("Masukan Nilai UAS: ")
            uas = Process.validate_nilai(uas)
            if uas is not None:
                break

        data_mahasiswa.ubah(nim, nama, tugas, uts, uas)
    else:
        print("Data tidak ditemukan.")
    time.sleep(1)

def hapus_data(data_mahasiswa):
    nim = input("Masukan NIM Mahasiswa yang akan dihapus: ")
    data_mahasiswa.hapus(nim)
    time.sleep(1)

def cari_data(data_mahasiswa):
    nim = input("Masukan NIM Mahasiswa yang dicari: ")
    mahasiswa = data_mahasiswa.cari(nim)
    if mahasiswa:
        print("Data ditemukan:", mahasiswa)
    else:
        print("Data tidak ditemukan.")
    time.sleep(1)

def main():
    data_mahasiswa = DataMahasiswa()
    while True:
        pilihan = input("[ (T)ambah, (U)bah, (H)apus, (L)ihat, (C)ari, (K)eluar]: ").lower()
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
            print("Pilihan tidak valid, silahkan coba lagi.")
            time.sleep(1)

if __name__=="__main__":
    main()