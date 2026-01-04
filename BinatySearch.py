def binary_search(arr, x):
    low = 0
    high = len(arr) - 1
    mid = 0
    iterations = 0
    backup_res_index=-1
 
    while low <= high:
        iterations +=1
 
        mid = (high + low) // 2
 
        # якщо x більше за значення посередині списку, ігноруємо ліву половину
        if arr[mid] < x:
            low = mid + 1
            backup_res_index = mid+1
 
        # якщо x менше за значення посередині списку, ігноруємо праву половину
        elif arr[mid] > x:
            high = mid - 1
            backup_res_index = mid
 
        # інакше x присутній на позиції і повертаємо кількість ітерацій і його самого
        else:
            return (iterations, arr[mid])
 
    # якщо елемент не знайдений повертаємо кількість ітерацій та найменший елемент, який є більшим заданому значенню або None якщо такого немає
    try:
        backup_res = backup_res_index
    except IndexError:
        backup_res = None
    return (iterations, backup_res)

arr = [2, 3.5, 4, 10, 40]
x = 3.5
print(binary_search(arr, x))
