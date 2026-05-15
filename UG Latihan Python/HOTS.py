def main():
    # Input 1: Dictionary Stok Awal
    stok = eval(input())
    # Input 2: List Permintaan
    permintaan = eval(input())
    
    # Dictionary untuk mencatat transaksi yang gagal
    gagal = {}
    
    for barang in permintaan:
        # Cek apakah barang ada di stok dan jumlahnya lebih dari 0
        if barang in stok and stok[barang] > 0:
            stok[barang] -= 1
        else:
            # Jika gagal, catat frekuensi gagalnya di dictionary 'gagal'
            gagal[barang] = gagal.get(barang, 0) + 1
            
    print("--- Laporan Gudang ---")
    
    # Menampilkan stok yang masih tersisa saja
    print("Stok Sisa:")
    for b in stok:
        if stok[b] > 0:
            print(f"{b}: {stok[b]}")
            
    # Menampilkan barang yang gagal diambil
    print("\nTransaksi Gagal (Stok Habis/Tidak Ada):")
    for b in gagal:
        print(f"{b}: {gagal[b]} kali")

main()