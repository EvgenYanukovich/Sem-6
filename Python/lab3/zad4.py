def encrypt_string(text):
    odd_chars = text[::2]
    even_chars = text[1::2][::-1]
    
    return odd_chars + even_chars

if __name__ == "__main__":
    test_text = input("Введите строку: ")
    result = encrypt_string(test_text)
    print(f"Зашифрованная строка: {result}")