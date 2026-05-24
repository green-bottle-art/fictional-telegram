import random

nama_game = "Realm of code"

daftar_musuh = [
    {"id": 1, "nama": "Ayam Berkaki Dua", "hp": 10, "serangan": 5},
    {"id": 2, "nama": "Kucing Hitam Besar", "hp": 30, "serangan": 10},
    {"id": 3, "nama": "Kecebong Besar", "hp": 50, "serangan": 15},
    {"id": 4, "nama": "Naga Mini", "hp": 80, "serangan": 25}  
]

karakter_pemain = {
    "nama": "Arthas",
    "hp": 100,
    "serangan": 5,
    "defense": 0
}

print(f"Selamat datang di labirin {nama_game}!")

# Loop permainan utama
game_berjalan = True
lantai = 1

while game_berjalan:
    print(f"\n--- LANTAI {lantai} ---")
    print(f"Sekarang, kami di lantai {lantai} labirin. ada musuh yang harus dihadapi!")
    
    musuh_terpilih = random.choice(daftar_musuh)
    musuh_terpilih_copy = musuh_terpilih.copy()  # Buat salinan untuk setiap encounter
    
    print(f"Ada {musuh_terpilih_copy['nama']} musuh yang muncul! (Hp: {musuh_terpilih_copy['hp']}, Serangan: {musuh_terpilih_copy['serangan']})")
    
    # Loop pertarungan
    pertarungan_berlangsung = True
    while pertarungan_berlangsung:
        print(f"\nApa yang akan {karakter_pemain['nama']} lakukan?")
        aksi = input("1. Serang\n2. Lari\nPilih aksi (1/2): ")
        
        if aksi == "1":
            print(f"{karakter_pemain['nama']} menyerang {musuh_terpilih_copy['nama']}!")
            damage = karakter_pemain["serangan"]
            musuh_terpilih_copy["hp"] -= damage
            print(f"{musuh_terpilih_copy['nama']} menerima {damage} damage! (HP tersisa: {musuh_terpilih_copy['hp']})")
            
        elif aksi == "2":
            print(f"{karakter_pemain['nama']} mencoba untuk lari!")
            if random.random() < 0.5:
                print("Berhasil melarikan diri!")
                pertarungan_berlangsung = False
                continue
            else:
                print("Gagal melarikan diri! Musuh menyerang balik!")
                damage = musuh_terpilih_copy["serangan"] 
                karakter_pemain["hp"] -= damage
                print(f"{karakter_pemain['nama']} menerima {damage} damage! (HP tersisa: {karakter_pemain['hp']})")
        else:
            print(f"{karakter_pemain['nama']} bingung dan tidak melakukan apa-apa!")
        
        # Logika musuh menyerang balik jika masih hidup
        if musuh_terpilih_copy["hp"] > 0 and aksi == "1":
            print(f"\n{musuh_terpilih_copy['nama']} menyerang balik!")
            damage = musuh_terpilih_copy["serangan"] 
            karakter_pemain["hp"] -= damage
            print(f"{karakter_pemain['nama']} menerima {damage} damage! (HP tersisa: {karakter_pemain['hp']})")
        
        # Cek apakah musuh mati
        if musuh_terpilih_copy["hp"] <= 0:
            print(f"\n{musuh_terpilih_copy['nama']} telah dikalahkan!")
            pertarungan_berlangsung = False
            lantai += 1
        
        # Cek apakah pemain mati
        if karakter_pemain["hp"] <= 0:
            print(f"\n{karakter_pemain['nama']} telah mati! Game Over!")
            game_berjalan = False
            pertarungan_berlangsung = False

# Akhir permainan
print(f"\nTerima kasih telah bermain {nama_game}!")
print(f"Anda berhasil mencapai lantai {lantai}!")
