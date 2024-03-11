def main():
    print("Please enter the max number(list size): ")
    max_number = int(input())
    out_list = []
    for i in range(0, max_number):
        if i%2 != 0:
            out_list.append(i)
    print(f"the ouput list with all odd numbers is: {out_list}")

if __name__ == '__main__':
    main()