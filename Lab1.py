def fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)
n = int(input("Введіть n: "))
#hello
if n < 0:
    print("Введіть додатне число.")
else:
    result = fibonacci(n)
    print(f"{n}-е число Фібоначчі: {result}")