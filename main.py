def main():
    numbers = []
    """
    ########################################
    Code Your Program here
    ########################################
    """
    input1 = int(input('Enter a number  '))
    numbers.append(input1)
    i = 0
    while True:
        input1 = int(input('Enter a number  '))
        if input1 < numbers[i]:
            numbers.append(input1)
        else:
            break
        i = i + 1

    ########################################
    # Do not delete the return statement
    ########################################
    print(*numbers)
    return numbers


if __name__ == '__main__':
    main()
