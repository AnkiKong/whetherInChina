
def ip2int(ip:str):
    ip = ip.split(".")
    return int(ip[0])<<24 | int(ip[1])<<16 | int(ip[2]) << 8 | int(ip[3])

f = open("ip2.txt").read().split("\n")
data = []
for i in f:
    i = i.split(" ")
    data.append((ip2int(i[0]), 0))
    data.append((ip2int(i[1]), 1))
data = sorted(data, key=lambda x: x[0])

for i in range(len(data)-1):
    if data[i][1] == data[i+1][1]:
        print("Find")

def check(ip):
    value = ip2int(ip)
    l, r = 0, len(data) - 1
    while r - l > 0:
        mid = (l + r) >> 1
        if data[mid][0] > value:
            r = mid
        else:
            l = mid + 1
    return r > 0 and data[r-1][0] <= value and data[r][0] >= value and data[r-1][1] == 0 and data[r][1] == 1


for i in ["114.114.114.114", "119.29.29.29", "1.0.0.1", "8.8.8.8", "93.46.8.90", "59.36.119.55", "61.151.180.158"]:
    print(check(i), i)
