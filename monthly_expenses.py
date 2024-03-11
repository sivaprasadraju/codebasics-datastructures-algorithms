def main():
    monthly_expenses = [2200, 2350, 2600, 2130, 2190]

    print(f"In Feb I spent {monthly_expenses[1]} dollars")
    print(f"Total expense of first qurater is {monthly_expenses[0]+monthly_expenses[1]+monthly_expenses[2]}")
    if 2000 in monthly_expenses:
        print(monthly_expenses.index(2000))
    else:
        print(f"There is no excatly 2000 spent in any month")

    monthly_expenses.append(1980)
    monthly_expenses[3] = monthly_expenses[3] - 200
    print(monthly_expenses)


if __name__ == '__main__':
    main()