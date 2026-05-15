daftar_a = set(input().split()[1:])
daftar_b = set(input().split()[1:])
daftar_c = set(input().split()[1:])

ip_berbahaya = (daftar_a & daftar_b) - daftar_c

hasil_urut = sorted(list(ip_berbahaya))

print(" ".join(hasil_urut))