def is_vowel(char):
    return char.lower() in 'аеёиоуыэюя'

def count_words_with_different_ends_one_vowel(text):
    words = text.split()
    count = 0
    
    for word in words:
        if len(word) > 0:
            first = word[0]
            last = word[-1]
            
            if first != last and (is_vowel(first) or is_vowel(last)):
                count += 1
                
    return count

if __name__ == "__main__":
    test_text = input("Введите строку из русских слов: ")
    result = count_words_with_different_ends_one_vowel(test_text)
    print(f"Количество слов, где первая и последняя буква разные, но одна из них – гласная: {result}")