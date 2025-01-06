def hitung_nilai_akhir(tugas, uts, uas):
    return (tugas * 0.3) + (uts * 0.35) + (uas * 0.35)

class Mahasiswa:
    def __init__(self, nim, nama, tugas, uts, uas):
        self.nim = nim
        self.nama = nama
        self.tugas = tugas
        self.uts = uts
        self.uas = uas
        self.nilai_akhir = hitung_nilai_akhir(tugas, uts, uas)

class DataMahasiswa:
    def __init__(self):
        self.data_mahasiswa ={}
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
        return self.data_mahasiswa.get(nim,None)