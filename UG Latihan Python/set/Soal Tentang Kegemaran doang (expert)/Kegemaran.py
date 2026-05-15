def solve():
    n_str = input().strip()
    n = int(n_str)
    
    daftar_set = []
    semua_item_counts = {}
    is_valid = True

    for i in range(n):
        raw_input = input().strip()

        if len(raw_input) < 2 or raw_input[0] != '{' or raw_input[-1] != '}':
            is_valid = False
            break

        data_set = eval(raw_input)
        if type(data_set) != set:
            is_valid = False
            break
        
        daftar_set.append(data_set)
        
        for item in data_set:
            if item in semua_item_counts:
                semua_item_counts[item] += 1
            else:
                semua_item_counts[item] = 1

    if not is_valid:
        print("FORMAT SALAH")
        return

    hasil_akhir = []
    for item in semua_item_counts:
        count = semua_item_counts[item]
        if count > 1 and count < n:
            hasil_akhir.append(item)

    print(" ".join(sorted(hasil_akhir)))

if __name__ == "__main__":
    solve()