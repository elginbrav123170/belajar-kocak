
line = input()

n = int(line)
koleksi_unik = set()
for _ in range(n):
    nama_kartu = input().strip()
    if nama_kartu:
        koleksi_unik.add(nama_kartu)
print(len(koleksi_unik))
