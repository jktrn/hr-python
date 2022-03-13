if __name__ == '__main__':
    arr = []
    for _ in range(int(input())):
        temp = []
        name = input()
        score = float(input())
        arr = arr + [name, score]
        print(arr)
    sorted(arr, key=lambda x: x[1])
    print(arr)