class Pegawai:
    honor_per_jam = 30000 

    def __init__(self, nama, jam_kerja):
        self.nama = nama
        self.jam_kerja = jam_kerja

    def honor(self):
        return self.jam_kerja * Pegawai.honor_per_jam

pegawai1 = Pegawai("Andi", 40)
pegawai2 = Pegawai("Budi", 35)

print(f"Honor {pegawai1.nama}: Rp{pegawai1.honor():,}")
print(f"Honor {pegawai2.nama}: Rp{pegawai2.honor():,}")
