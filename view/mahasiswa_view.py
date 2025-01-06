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