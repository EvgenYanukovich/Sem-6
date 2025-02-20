def find_largest_common_prefix(str1, str2):
    min_len = min(len(str1), len(str2))
    
    prefix = ""
    for i in range(min_len):
        if str1[i] != str2[i]:
            break
        prefix += str1[i]
    
    return prefix if prefix else "Общий префикс не найден"

if __name__ == "__main__":
    str1 = input("Введите первую строку: ")
    str2 = input("Введите вторую строку: ")
    result = find_largest_common_prefix(str1, str2)
    print(f"Наибольший общий префикс: {result}")