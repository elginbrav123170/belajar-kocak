def solve():
    n_input = input().strip()
    n = int(n_input)
    hasil_set = set()
    status_valid = True

    for i in range(n):
        koca = input().strip()
        if len(koca) < 2 or koca[0] != '{' or koca[-1] != '}':
            status_valid = False
            break

        data_sekarang = eval(koca)
        
        if type(data_sekarang) != set:
            status_valid = False
            break

        if i == 0:
            hasil_set = data_sekarang
        else:
            hasil_set = hasil_set ^ data_sekarang

    if status_valid:
        cetak_hasil = sorted(list(hasil_set))
        print(" ".join(cetak_hasil))
    else:
        print("FORMAT SALAH")

if __name__ == "__main__":
    solve()