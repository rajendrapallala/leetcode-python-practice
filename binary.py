def binderived(i):
    b = []
    while i:
        q, rm = divmod(i, 2)
        b.append(rm)
        i = i >> 1
    print(b)
    return b[::-1] or [0]

if __name__ == "__main__":
    print(binderived(''))
