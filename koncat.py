def main():
    # Input berupa list of dicts: [{"pekerjaan": "X", "umur": Y}, ...]
    data_warga = eval(input())
    
    # Dictionary untuk menampung total umur
    total_umur = {}
    # Dictionary untuk menampung jumlah orang per pekerjaan
    jumlah_orang = {}
    
    for warga in data_warga:
        profesi = warga["pekerjaan"]
        usia = warga["umur"]
        
        # Akumulasi total umur dan jumlah orang (Logika Dasar Dictionary)
        total_umur[profesi] = total_umur.get(profesi, 0) + usia
        jumlah_orang[profesi] = jumlah_orang.get(profesi, 0) + 1
    
    # Ambil kunci (pekerjaan) dan urutkan sesuai abjad
    pekerjaan_urut = sorted(total_umur.keys())
    
    for p in pekerjaan_urut:
        rata_rata = total_umur[p] / jumlah_orang[p]
        # Menampilkan hasil rata-rata
        print(f"{p}: {rata_rata}")

main()