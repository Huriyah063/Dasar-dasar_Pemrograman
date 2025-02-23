print("Mulai")

class Orang:
    lingkungan = "RT 2/30 Kelurahan Majujaya"

    def _init_(self, nama, tgl_lahir):
        self.nama_lengkap = nama
        self.tgl_lahir = tgl_lahir

    def deskripsi(self):
        return f"{self.nama_lengkap} lahir pada {self.tgl_lahir}"


warga1 = Orang("Ahmad", "20-03-1987")
warga2 = Orang("Bayu", "12-05-1988")

daftar_warga = [warga1, warga2]  
for o in daftar_warga:
    print(o.deskripsi())