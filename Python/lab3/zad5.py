def replace_spaces_with_hash(text):
    return '#'.join(text.split())

if __name__ == "__main__":
    test_text = input("Введите строку из русских слов: ")
    result = replace_spaces_with_hash(test_text)
    print(f"Строка с разделителем '#': {result}")