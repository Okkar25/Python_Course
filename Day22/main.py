def clean(input_str):

    # strip_str_index = []

    # for i in range(len(input_str)):
    #   # if input_str[i] != "\n" and input_str[i] != "\t" and input_str[i] != " ":
    #   if input_str[i] not in "\n\t ":
    #     strip_str_index.append(i)

    # strip_str = input_str[strip_str_index[0]: strip_str_index[-1] + 1]

    # return strip_str

    start = 0

    while input_str[start] in "\n\t ":
        start += 1

    end = len(input_str) - 1
    while input_str[end] in "\n\t ":

        end -= 1

    return input_str[start : end + 1]


# print( clean("\n\n\t what's up,\n\n doc? \n \t"))


def sequence(number):
    num_list = [number]

    # print(number)

    while number > 1:
        if number % 2 == 0:
            number = number // 2
            num_list.append(number)

        elif number % 2 != 0:
            number = number + 1
            num_list.append(number)

    for num in num_list:
        print(num)


# sequence(3)
# sequence(4)
# sequence(17)


if __name__ == "__main__":
    import doctest

    print(doctest.testfile("hw5TEST.py"))
