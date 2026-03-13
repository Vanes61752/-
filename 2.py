def decode_string(s):
    stack = []
    current_num = 0
    current_str = ''
    
    for char in s:
        if char.isdigit():
            current_num = current_num * 10 + int(char)
        elif char == '[':
            stack.append((current_str, current_num))
            current_str = ''
            current_num = 0
        elif char == ']':
            last_str, num = stack.pop()
            current_str = last_str + current_str * num
        else:
            current_str += char
    
    return current_str



while True:
    user_input = input("Введи строку для декодирования: ")
    
    try:
        result = decode_string(user_input)
        print(f"Результат: {result}\n")

    except Exception as e:
        print(f"Ошибка при декодировании: {e}. Проверь формат ввода.\n")

