from difflib import diff_bytes


if __name__ == '__main__':
    a = int(input())
    b = int(input())
    sum = a + b
    diff = a - b
    prod = a * b
    
    print(f"{sum}\n{diff}\n{prod}")