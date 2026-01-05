import timeit
import requests

LINK = "https://drive.google.com/uc?export=view&id="
ID1 = "18_R5vEQ3eDuy2VdV3K5Lu-R-B-adxXZh"
ID2 = "18BfXyQcmuinEI_8KDSnQm4bLx6yIFS_w"

#Алгоритм Кнута-Морріса-Пратта
def compute_lps(pattern):
    lps = [0] * len(pattern)
    length = 0
    i = 1

    while i < len(pattern):
        if pattern[i] == pattern[length]:
            length += 1
            lps[i] = length
            i += 1
        else:
            if length != 0:
                length = lps[length - 1]
            else:
                lps[i] = 0
                i += 1

    return lps

def kmp_search(main_string, pattern):
    M = len(pattern)
    N = len(main_string)

    lps = compute_lps(pattern)

    i = j = 0

    while i < N:
        if pattern[j] == main_string[i]:
            i += 1
            j += 1
        elif j != 0:
            j = lps[j - 1]
        else:
            i += 1

        if j == M:
            return i - j

    return -1  # якщо підрядок не знайдено

#Алгоритм Боєра-Мура
def build_shift_table(pattern):
  table = {}
  length = len(pattern)
  # Для кожного символу в підрядку встановлюємо зсув рівний довжині підрядка
  for index, char in enumerate(pattern[:-1]):
    table[char] = length - index - 1
  # Якщо символу немає в таблиці, зсув буде дорівнювати довжині підрядка
  table.setdefault(pattern[-1], length)
  return table

def boyer_moore_search(text, pattern):
  # Створюємо таблицю зсувів для патерну (підрядка)
  shift_table = build_shift_table(pattern)
  i = 0  # Ініціалізуємо початковий індекс для основного тексту

  # Проходимо по основному тексту, порівнюючи з підрядком
  while i <= len(text) - len(pattern):
    j = len(pattern) - 1  # Починаємо з кінця підрядка

    # Порівнюємо символи від кінця підрядка до його початку
    while j >= 0 and text[i + j] == pattern[j]:
      j -= 1  # Зсуваємось до початку підрядка

    # Якщо весь підрядок збігається, повертаємо його позицію в тексті
    if j < 0:
      return i  # Підрядок знайдено

    # Зсуваємо індекс i на основі таблиці зсувів
    # Це дозволяє "перестрибувати" над неспівпадаючими частинами тексту
    i += shift_table.get(text[i + len(pattern) - 1], len(pattern))

  # Якщо підрядок не знайдено, повертаємо -1
  return -1

#Алгоритм Рабіна-Карпа
def polynomial_hash(s, base=256, modulus=101):
    """
    Повертає поліноміальний хеш рядка s.
    """
    n = len(s)
    hash_value = 0
    for i, char in enumerate(s):
        power_of_base = pow(base, n - i - 1) % modulus
        hash_value = (hash_value + ord(char) * power_of_base) % modulus
    return hash_value

def rabin_karp_search(main_string, substring):
    # Довжини основного рядка та підрядка пошуку
    substring_length = len(substring)
    main_string_length = len(main_string)
    
    # Базове число для хешування та модуль
    base = 256 
    modulus = 101  
    
    # Хеш-значення для підрядка пошуку та поточного відрізка в основному рядку
    substring_hash = polynomial_hash(substring, base, modulus)
    current_slice_hash = polynomial_hash(main_string[:substring_length], base, modulus)
    
    # Попереднє значення для перерахунку хешу
    h_multiplier = pow(base, substring_length - 1) % modulus
    
    # Проходимо крізь основний рядок
    for i in range(main_string_length - substring_length + 1):
        if substring_hash == current_slice_hash:
            if main_string[i:i+substring_length] == substring:
                return i

        if i < main_string_length - substring_length:
            current_slice_hash = (current_slice_hash - ord(main_string[i]) * h_multiplier) % modulus
            current_slice_hash = (current_slice_hash * base + ord(main_string[i + substring_length])) % modulus
            if current_slice_hash < 0:
                current_slice_hash += modulus

    return -1

def text_from_link(link):
    try:
        response = requests.get(link)
        response.raise_for_status()
        return response.text
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
        return None


if __name__ == "__main__":
    print("dowloading texts")
    text1 = text_from_link(LINK+ID1)
    text2 = text_from_link(LINK+ID2)
    pattern1 = "Arrays.binarySearch"
    pattern2 = "AMD Ryzen 5 3600"
    pattern_fake = "EzXGgr4kD76HnFwyTE"
    print("download complete")

    print(f"Алгоритм Боєра-Мура, стаття1, рядок дійсний:     {timeit.timeit('boyer_moore_search(text1, pattern1)', number=10000, globals=globals())}")
    print(f"Алгоритм Боєра-Мура, стаття2, рядок дійсний:     {timeit.timeit('boyer_moore_search(text2, pattern2)', number=10000, globals=globals())}")
    print(f"Алгоритм Боєра-Мура, стаття1, рядок НЕдійсний:   {timeit.timeit('boyer_moore_search(text1, pattern_fake)', number=10000, globals=globals())}")
    print(f"Алгоритм Боєра-Мура, стаття2, рядок НЕдійсний:   {timeit.timeit('boyer_moore_search(text2, pattern_fake)', number=10000, globals=globals())}")

    print(f"Алгоритм КМП, стаття1, рядок дійсний:            {timeit.timeit('kmp_search(text1, pattern1)', number=10000, globals=globals())}")
    print(f"Алгоритм КМП, стаття2, рядок дійсний:            {timeit.timeit('kmp_search(text2, pattern2)', number=10000, globals=globals())}")
    print(f"Алгоритм КМП, стаття1, рядок НЕдійсний:          {timeit.timeit('kmp_search(text1, pattern_fake)', number=10000, globals=globals())}")
    print(f"Алгоритм КМП, стаття2, рядок НЕдійсний:          {timeit.timeit('kmp_search(text2, pattern_fake)', number=10000, globals=globals())}")

    print(f"Алгоритм Рабіна-Карпа, стаття1, рядок дійсний:   {timeit.timeit('rabin_karp_search(text1, pattern1)', number=10000, globals=globals())}")
    print(f"Алгоритм Рабіна-Карпа, стаття2, рядок дійсний:   {timeit.timeit('rabin_karp_search(text2, pattern2)', number=10000, globals=globals())}")
    print(f"Алгоритм Рабіна-Карпа, стаття1, рядок НЕдійсний: {timeit.timeit('rabin_karp_search(text1, pattern_fake)', number=10000, globals=globals())}")
    print(f"Алгоритм Рабіна-Карпа, стаття2, рядок НЕдійсний: {timeit.timeit('rabin_karp_search(text2, pattern_fake)', number=10000, globals=globals())}")
