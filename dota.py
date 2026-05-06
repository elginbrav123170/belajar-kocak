import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    ptr = 0
    
    N = int(input_data[ptr])
    ptr += 1
    
    item_shop = {}
    for _ in range(N):
        name = input_data[ptr]
        price = int(input_data[ptr + 1])
        item_shop[name] = price
        ptr += 2
    
    M = int(input_data[ptr])
    ptr += 1
    
    items_bought = input_data[ptr : ptr + M]
    
    player_inventory = {}
    net_worth = 0

    for item in items_bought:
        if item in item_shop:
            net_worth += item_shop[item]
            player_inventory[item] = player_inventory.get(item, 0) + 1

    print(f"Total Net Worth: {net_worth}")
    for item in sorted(player_inventory.keys()):
        print(f"{item}: {player_inventory[item]}")

if __name__ == "__main__":
    solve()