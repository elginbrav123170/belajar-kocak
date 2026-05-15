def get_network_broadcast(ip_tuple,subnet_tuple):
    network = []
    broadcast = []
    for kocak, kocap in zip(ip_tuple, subnet_tuple):
        kocay = kocak & kocap
        invert = 255 - kocap 
        kocal = kocay | invert
        network.append(kocay)
        broadcast.append(kocal)

    print("IP Address :",ip_tuple) 
    print("Subnet Mask :",subnet_tuple)
    print("Network Address :",tuple(network))
    print("Broadcast Address :",tuple(broadcast))

if __name__ == "__main__":
    ip_tuple = eval(input())
    subnet_tuple = eval(input())
    get_network_broadcast(ip_tuple,subnet_tuple)
