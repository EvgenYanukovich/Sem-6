def extract_folder_names(path):
    parts = [part for part in path.replace('\\', '/').split('/') if part]
    
    folder_vars = {}
    for i, folder in enumerate(parts[:-1], 1):
        folder_vars[f'folder_{i}'] = folder
    
    return folder_vars

if __name__ == "__main__":
    test_path = input("Введите полный путь к файлу: ")
    result = extract_folder_names(test_path)
    
    print("Имена папок в пути:")
    for var_name, folder_name in result.items():
        print(f"{var_name} = '{folder_name}'")