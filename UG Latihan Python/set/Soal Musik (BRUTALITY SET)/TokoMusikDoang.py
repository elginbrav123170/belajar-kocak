def solve():
    baris_awal = input().strip()
    n = int(baris_awal)
    
    is_valid = True
    daftar_gudang = []

    def cek_format(teks):
        if len(teks) < 2 or teks[0] != '{' or teks[-1] != '}':
            return False
        return True

    for _ in range(n):
        raw_set = input().strip()
        if not cek_format(raw_set):
            is_valid = False
            break
        
        data_set = eval(raw_set)    
        if type(data_set) != set:
            is_valid = False
            break
            
        daftar_gudang.append(data_set)

    if is_valid:
        raw_discontinue = input().strip()
        if not cek_format(raw_discontinue):
            is_valid = False
        else:
            set_discontinue = eval(raw_discontinue)
            if type(set_discontinue) != set:
                is_valid = False

    if not is_valid:
        print("FORMAT SALAH")
        return

    muncul_sekali = set()
    muncul_berkali_kali = set()

    for gudang in daftar_gudang:
        duplikat_baru = muncul_sekali & gudang
        muncul_berkali_kali = muncul_berkali_kali | duplikat_baru
        muncul_sekali = (muncul_sekali | gudang) - muncul_berkali_kali
    hasil_akhir = muncul_sekali - set_discontinue

    print(" ".join(sorted(list(hasil_akhir))))


if __name__ == "__main__":
    solve()