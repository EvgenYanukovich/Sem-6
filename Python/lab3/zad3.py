def count_words_longer_than_five(text):
    words = text.split()
    count = 0
    
    for word in words:
        if len(word) > 5:
            count += 1
              
    return count

if __name__ == "__main__":
    test_text = input("Введите строку из русских слов: ")
    result = count_words_longer_than_five(test_text)
    print(f"Количество слов длиной больше 5 символов: {result}")