


def binary_search(itens, item):
    search_count = 0
    min = 0
    max = len(itens)

    while True:
        search_count += 1
        print('searching')

        mid = (min + max) // 2
        guess = itens[mid]
        print(f'min:{min} | max:{max} -> {guess}')
        from time import sleep; sleep(0.1)
        if guess == item:
            print(f'found in: {search_count}')
            return
        if item > guess:
            min = mid
            continue
        if item < guess:
            max = mid
            continue


binary_search([i for i in range(1,129*2)], 128*2)
