N = int(input())

while N > 0:
    A, B = input().strip().split()
    if A.endswith(B):
        print("encaixa")

    else:
        print("nao encaixa")
    N -= 1