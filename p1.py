class Orang:
    lingkungan = 'RT 5 RW 3'
    
    def _init(self, nama, tanggal_lahir):  # Perbaikan: __init_ harus ada dua underscore di awal dan akhir
        self.nama_lengkap = nama
        self.tanggal_lahir = tanggal_lahir
    
    def deskripsi(self):  # Perbaikan: "deskrisi" diubah menjadi "deskripsi"
        return f"{self.nama_lengkap} lahir pada {self.tanggal_lahir}"
        
warga1 = Orang('Ahmad', '20-12-1980')  # Perbaikan: Tanggal '20-13-1980' tidak valid, diubah ke '20-12-1980'
warga2 = Orang('Bayu', '13-08-2005')

print('Daftar Nama')
print(warga1.nama_lengkap)
print(warga2.nama_lengkap)
print()
print("Deskripsi")
print(warga1.deskripsi())
print(warga2.deskripsi())