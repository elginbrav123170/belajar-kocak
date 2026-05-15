def solve():
    p = int(input())
    
    bobot = {
        "Kill": 100,
        "Assist": 50,
        "Death": -25
    }
    
    skor_pemain = {}
    
    for _ in range(p):
        data = input().split()
        nama = data[0]
        aksi_list = data[1].split(",")
        
        total_poin = 0
        for aksi in aksi_list:
            if aksi in bobot:
                total_poin += bobot[aksi]
        
        skor_pemain[nama] = total_poin
    
    nama_urut = sorted(skor_pemain.keys())
    for nama in nama_urut:
        print(f"{nama}: {skor_pemain[nama]}")
    
    mvp = ""
    skor_tertinggi = -999999 
    
    for nama in nama_urut:
        if skor_pemain[nama] > skor_tertinggi:
            skor_tertinggi = skor_pemain[nama]
            mvp = nama
            
    print(f"MVP: {mvp}")

solve()