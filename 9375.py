import sys
for _ in range(int(sys.stdin.readline())):
    clothes_dict = {}
    for i in range(int(sys.stdin.readline())):
        clothes, category = sys.stdin.readline().split()
        if category in clothes_dict.keys():
            clothes_dict[category.rstrip()].append(clothes.rstrip())
        else:
            clothes_dict[category.rstrip()] = [clothes.rstrip()]
    print(clothes_dict)