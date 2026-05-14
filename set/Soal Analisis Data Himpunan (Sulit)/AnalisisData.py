def solve():
    # Membaca jumlah input
    n_input = input().strip()
    n = int(n_input)
    hasil_set = set()
    status_valid = True

    for i in range(n):
        raw_input = input().strip()
        if len(raw_input) < 2 or raw_input[0] != '{' or raw_input[-1] != '}':
            status_valid = False
            break

        data_sekarang = eval(raw_input)
        
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