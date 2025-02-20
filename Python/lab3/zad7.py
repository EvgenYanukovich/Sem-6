def replace_p_with_asterisk(text):
    lower_text = text.lower()
    first_p_index = lower_text.find('п')
    
    if first_p_index == -1:
        return text
    
    result = text[:first_p_index + 1]
    remaining = text[first_p_index + 1:]
    result += remaining.replace('П', '*').replace('п', '*')
    
    return result
    
if __name__ == "__main__":
    test_text = input("Введите строку: ")
    result = replace_p_with_asterisk(test_text)
    print(f"Результат замены: {result}")