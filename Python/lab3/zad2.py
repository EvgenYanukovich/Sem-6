def count_words_with_letter_d(text):
    words = text.split()
    count = 0
    
    for word in words:
        if 'д' in word.lower():
            count += 1
                
    return count

if __name__ == "__main__":
    test_text = input("Введите строку из русских слов: ")
    result = count_words_with_letter_d(test_text)
    print(f"Количество слов, содержащих букву 'Д': {result}")