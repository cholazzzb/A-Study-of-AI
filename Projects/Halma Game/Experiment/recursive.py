def recursive(number):
    print(number)
    if number > 0:
        recursive(number-1)
    print("haha")
    return 10

print(recursive(3))