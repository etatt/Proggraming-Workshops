def main():
    numbers = [3, 1, 4, 1, 5, 9, 2]

    print(numbers[0])
    print(numbers[-1])
    print(numbers[3])
    print(numbers[:-1])
    print(numbers[3:4])
    print(5 in numbers)
    print(7 in numbers)
    print("3" in numbers)
    print(numbers + [6, 5, 3])
    print(numbers)

    numbers[0] = "ten"
    print(numbers)
    numbers[6] = 1
    print(numbers)
    print(numbers[2:7])
    if not 9 in numbers:
        print("False")
    else:
        print("True")

main()