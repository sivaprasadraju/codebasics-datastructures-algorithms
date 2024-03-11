def main():
    with open("poem.txt", "r") as file:
        data = file.read()

    data_split = data.split()

    words_dict = {}
    for word in data_split:
        if word in words_dict:
            words_dict[word] += 1
        else:
            words_dict[word] = 1

    print(words_dict)

    x = 2

if __name__ == '__main__':
    main()