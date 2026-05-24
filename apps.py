import random
nama_game = "HaHaHa Game"

# Tuple untuk menyimpan elemen pemain (Karena elemen tidak berubah)
ELEMEN_PEMAIN = ("Air", "Daun", "Api", "Angin", "Serangga", "Batu", "Logam", "Listrik", "Es", "Racun", "Tanah")

# Aturan untuk menentukan kelemahan dan kekuatan elemen, menggunakan frozenset karena urutan tidak penting
KELEMAHAN_ELEMEN = {
    "Air": frozenset(["Api", "Batu", "Tanah"]),  # Air kuat dari Api, btu dan  tanah
    "Daun": frozenset(["Air", "Tanah", "Batu"]),
    "Api": frozenset(["Daun", "Serangga", "Logam", "Es"]),
    "Angin": frozenset(["Daun", "Serangga"]),
    "Serangga": frozenset(["Daun", "Tanah"]),
    "Batu": frozenset(["Api", "Serangga", "Angin", "Es"]),
    "Logam": frozenset(["Angin", "Batu", "Serangga", "Es"]),
    "Listrik": frozenset(["Air", "Angin"]),
    "Es": frozenset(["Air", "Daun", "Serangga", "Tanah"]),
    "Racun": frozenset(["Daun", "Serangga"]),
    "Tanah": frozenset(["Api", "Batu", "Logam", "Listrik", "Racun"])
}

# List untuk menyimpan daftar musuh yang akan dihadapi, berurutan dari yang paling mudah hingga yang paling sulit
daftar_musuh = [
    {"nama": "Ayam berkaki dua", "hp": 20, "serangan": 5},
    {"nama": "Orang", "hp": 50, "serangan": 10},
    {"nama": "Orang besar", "hp": 70, "serangan": 10}
]

PILIHAN_VALID = {str(i) for i in range(1, 12)} #set validasi input 

input_nama = input("Masukkan nama pemain: ")

# Dictionary untuk menyimpan statistik karakter pemain
pemain = {
    "nama": input_nama,
    "hp": 50,
    "serangan": 10,
}

print(f"Selamat datang di {nama_game}!")


# Hanya tiga Musuh

for ronde in range(0, 3):

    # Menampilkan Pilihan pemain
    j = 0
    for i in ELEMEN_PEMAIN:
        j += 1
        print(f"{j}. {i} ", end="")     # List pilihan pemain
    print("\n")

    hp_pemain = pemain["hp"]   # Mengambil Value hp dari dictionary
    hp_musuh = daftar_musuh[ronde]["hp"]
    print(f"Musuhmu sekarang: {daftar_musuh[ronde]['nama']} (HP: {daftar_musuh[ronde]['hp']}, Serangan: {daftar_musuh[ronde]['serangan']})")

    while True:

        pilihan_musuh = random.choice(ELEMEN_PEMAIN) # Pilihan musuh acak, dari tuple
     
        pilihan_pemain = input("Pilih elemen untuk menyerang (1-11): ")
        
        if pilihan_pemain in PILIHAN_VALID:
            elemen_pemain = ELEMEN_PEMAIN[int(pilihan_pemain) - 1] # karena dimulai dari 0
        else:
            print("Pilihan antara angka 1 sampai 11!")
            continue

        print(f"{pemain['nama']} memilih elemen: {elemen_pemain}")
        print(f"Musuh memilih elemen: {pilihan_musuh}")

        # apakah pilihan pemain ada di kelemahan musuh
        if elemen_pemain in KELEMAHAN_ELEMEN[pilihan_musuh]:
            print(f"{pilihan_musuh} lemah lawan {elemen_pemain}!")
            hp_pemain -= daftar_musuh[ronde]["serangan"]        # Jika ada hp pemain akan berkurang

        if pilihan_musuh in KELEMAHAN_ELEMEN[elemen_pemain]:
            print(f"{elemen_pemain} lemah lawan {pilihan_musuh}!")
            hp_musuh -= pemain["serangan"]

        if pilihan_musuh not in KELEMAHAN_ELEMEN[elemen_pemain] and elemen_pemain not in KELEMAHAN_ELEMEN[pilihan_musuh]:
            print("Seri!") # tidak ada kerusakan jka sama

        print(f"HP {pemain['nama']}: {hp_pemain}")
        print(f"HP {daftar_musuh[ronde]['nama']}: {hp_musuh}")

        if hp_pemain <= 0:
            print(f"{pemain['nama']} telah kalah! Game Over.")
            exit() # program selesai
        elif hp_musuh <= 0:
            print(f"{daftar_musuh[ronde]['nama']} telah dikalahkan! Lanjut ke ronde berikutnya.")
            break # lanjut ke loop berikutnya



    

