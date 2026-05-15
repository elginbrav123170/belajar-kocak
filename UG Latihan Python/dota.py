def solve():
    n_str = input()
    if not n_str:
        return
    n = int(n_str)

    item_shop = {}
    for _ in range(n):
        data = input().split()
        nama_item = data[0]
        harga = int(data[1])
        item_shop[nama_item] = harga

    m_str = input()
    if not m_str:
        return
    m = int(m_str)

    items_bought = input().split()

    player_inventory = {}
    net_worth = 0

    for item in items_bought:
        if item in item_shop:
            net_worth += item_shop[item]
            player_inventory[item] = player_inventory.get(item, 0) + 1

    print(f"Total Net Worth: {net_worth}")
    
    daftar_item_urut = sorted(player_inventory.keys())
    for item in daftar_item_urut:
        print(f"{item}: {player_inventory[item]}")

solve()