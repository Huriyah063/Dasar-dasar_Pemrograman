import requests

class DataObject:
    """
    Representasi dari satu entitas data dari API.
    """
    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)

    def __repr__(self):
        return str(self.__dict__)

class APIClient:
    """Klien untuk mengakses API dan mengelola data"""

    def __init__(self, base_url):
        self.base_url = base_url
        self.data = []
        self.page = 0
        self.page_size = 10
        self.ascending = True

    def fetch_data(self):
        """Mengakses API dan mengambil data"""
        print("Mengambil data dari API...")
        response = requests.get(self.base_url)
        if response.status_code == 200:
            raw_data = response.json()
            self.data = [DataObject(**item) for item in raw_data]
            self.sort_data()
        else:
            print(f"Gagal mengakses API. Status code: {response.status_code}")
            self.data = []

    def sort_data(self):
        """Mengurutkan data berdasarkan atribut tertentu"""
        self.data.sort(
            key=lambda x: getattr(x, 'id', 0),
            reverse=not self.ascending
        )

    def display_page(self):
        """Menampilkan halaman saat ini"""
        start = self.page * self.page_size
        end = start + self.page_size
        print(f"\nHalaman {self.page + 1}:")
        for item in self.data[start:end]:
            print(item)
        if not self.data[start:end]:
            print("Tidak ada data untuk ditampilkan.")

    def next_page(self):
        """Pindah ke halaman berikutnya"""
        if (self.page + 1) * self.page_size < len(self.data):
            self.page += 1
        else:
            print("Ini adalah halaman terakhir.")
        self.display_page()

    def previous_page(self):
        """Pindah ke halaman sebelumnya"""
        if self.page > 0:
            self.page -= 1
        else:
            print("Ini adalah halaman pertama.")
        self.display_page()

    def toggle_sort_order(self):
        """Membalikkan urutan pengurutan"""
        self.ascending = not self.ascending
        self.sort_data()
        self.page = 0
        self.display_page()

if __name__ == "__main__":
    # Menggunakan API JSONPlaceholder untuk mendapatkan daftar postingan
    base_url = 'https://jsonplaceholder.typicode.com/posts'
    client = APIClient(base_url)

    # Mengambil data dari API
    client.fetch_data()

    # Menampilkan halaman pertama
    client.display_page()

    while True:
        print("\nPilihan:")
        print("1. Halaman berikutnya")
        print("2. Halaman sebelumnya")
        print("3. Balikkan urutan pengurutan")
        print("4. Keluar")

        choice = input("Pilih tindakan (1-4): ")
        if choice == '1':
            client.next_page()
        elif choice == '2':
            client.previous_page()
        elif choice == '3':
            client.toggle_sort_order()
        elif choice == '4':
            print("Keluar dari program.")
            break
        else:
            print("Pilihan tidak valid, silakan coba lagi.")
