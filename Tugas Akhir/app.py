import json

# Fungsi untuk membaca data dari file JSON
def baca_data(nama_file):
    try:
        with open(nama_file, 'r') as file:
            data = json.load(file)
            return data
    except FileNotFoundError:
        print("File tidak ditemukan. Membuat file baru.")
        return []
    except json.JSONDecodeError:
        print("Kesalahan dalam membaca file JSON. Menggunakan data kosong.")
        return []

# Fungsi untuk menyimpan data ke file JSON
def simpan_data(nama_file, data):
    with open(nama_file, 'w') as file:
        json.dump(data, file, indent=4)

# Fungsi untuk menampilkan data dalam bentuk tabel yang rapi
def tampilkan_data(data):
    if not data:
        print("Tidak ada data untuk ditampilkan.")
        return

    # Tentukan lebar kolom
    nama_kolom = list(data[0].keys())
    lebar_kolom = {
        'nama': max(max(len(str(item['nama'])) for item in data), len('Nama')),
        'umur': max(max(len(str(item['umur'])) for item in data), len('Umur')),
        'kota': max(max(len(str(item['kota'])) for item in data), len('Kota')),
        'profesi': max(max(len(str(item['profesi'])) for item in data), len('profesi')),
    }

    # Cetak header
    header = f"| {'Nama':<{lebar_kolom['nama']}} | {'Umur':<{lebar_kolom['umur']}} | {'Kota':<{lebar_kolom['kota']}} |"
    garis_pemisah = "+" + "-" * (len(header) - 2) + "+"
    
    print(garis_pemisah)
    print(header)
    print(garis_pemisah)

    # Cetak data
    for item in data:
        baris = f"| {str(item['nama']):<{lebar_kolom['nama']}} | {str(item['umur']):<{lebar_kolom['umur']}} | {str(item['kota']):<{lebar_kolom['kota']}} |"
        print(baris)
    
    print(garis_pemisah)

# Fungsi untuk memfilter data berdasarkan kolom dan nilai tertentu
def saring_data(data, kolom, nilai):
    return [item for item in data if str(item.get(kolom)).lower() == str(nilai).lower()]

# Fungsi untuk mengurutkan data berdasarkan kolom tertentu
def urutkan_data(data, kolom, naik=True):
    return sorted(data, key=lambda x: x[kolom], reverse=not naik)

# Fungsi untuk menambahkan data baru
def tambah_data(data):
    nama = input("Masukkan nama: ")
    umur = int(input("Masukkan umur: "))
    kota = input("Masukkan kota: ")
    entri_baru = {"nama": nama, "umur": umur, "kota": kota}
    data.append(entri_baru)
    print("Data berhasil ditambahkan.")

# Fungsi untuk menghapus data berdasarkan nama
def hapus_data(data):
    nama = input("Masukkan nama yang ingin dihapus: ")
    panjang_awal = len(data)
    data[:] = [item for item in data if item.get("nama") != nama]
    if len(data) < panjang_awal:
        print("Data berhasil dihapus.")
    else:
        print("Data tidak ditemukan.")

# Fungsi untuk menampilkan menu
def tampilkan_menu():
    print("\nMenu:")
    print("1. Tampilkan Data")
    print("2. Tambah Data")
    print("3. Hapus Data")
    print("4. Saring Data")
    print("5. Urutkan Data")
    print("6. Simpan Data")
    print("7. Keluar")

# Fungsi utama
def main():
    nama_file = 'Tugas Akhir\data.json'
    data = baca_data(nama_file)

    while True:
        tampilkan_menu()
        pilihan = input("Pilih opsi (1-7): ")

        if pilihan == '1':
            tampilkan_data(data)
        elif pilihan == '2':
            tambah_data(data)
        elif pilihan == '3':
            hapus_data(data)
        elif pilihan == '4':
            kolom_saring = input("Masukkan kolom untuk disaring (nama/umur/kota): ")
            nilai_saring = input("Masukkan nilai untuk disaring: ")
            if kolom_saring == 'umur':
                nilai_saring = int(nilai_saring)
            data_tersaring = saring_data(data, kolom_saring, nilai_saring)
            print("\nData Setelah Disaring:")
            tampilkan_data(data_tersaring)
        elif pilihan == '5':
            kolom_urut = input("Masukkan kolom untuk diurutkan (nama/umur/kota): ")
            urutan = input("Urutkan naik (y/n)? ")
            naik = urutan.lower() == 'y'
            data_terurut = urutkan_data(data, kolom_urut, naik)
            print("\nData Setelah Diurutkan:")
            tampilkan_data(data_terurut)
        elif pilihan == '6':
            simpan_data(nama_file, data)
            print("Data berhasil disimpan.")
        elif pilihan == '7':
            simpan_data(nama_file, data)
            print("Keluar dari program.")
            break
        elif pilihan == '8':
            simpan_data(nama_file, data)
            print("Keluar dari program.")
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")

if __name__ == "__main__":
    main()