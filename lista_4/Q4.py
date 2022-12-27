for i in range(0, 13):
    number = int(input())
    if number % 15 == 0:
        print(f'{number} é múltiplo de três e cinco')
    elif number % 5 == 0:
        print(f'{number} é múltiplo de cinco')
    elif number % 3 == 0:
        print(f'{number} é múltiplo de três')
    else:
        print(f'{number}')