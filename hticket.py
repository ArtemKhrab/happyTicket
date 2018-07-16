def hticketdetecrot(ar):
    ht = 0
    inct = 0
    uht = 0
    i = 0
    while not (i == len(ar)):
        arr = ar[i]
        i += 1
        if len(arr) == 6 and not arr[0] == '0':
            if int(arr[0])+int(arr[1])+int(arr[2]) == int(arr[3])+int(arr[4])+int(arr[5]):
                ht += 1
            else:
                uht += 1
        else:
            inct += 1
    print('hpt:', ht, " ", 'uhpt:', uht, " ", 'inct:', inct)
    return 0


if __name__ == "__main__":
    arr = ['123123', '100100', '012345', '2323']
    hticketdetecrot(arr)
