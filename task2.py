from collections import deque

def is_palindrome(text):
    # Нечутливість до регістру та пробілів
    normalized_text = text.lower().replace(" ", "")

    # Двостороння черга
    deque_obj = deque(normalized_text)

    # Перевірка рядку на паліндромність
    while len(deque_obj) > 1:
        first_char = deque_obj.popleft()
        last_char = deque_obj.pop()
        if first_char != last_char:
            return False

    return True


# Приклади

print()
print("Приклади перевірки тексту на паліндромність:")
print()

examples_list = ["Анна", "rats live on no evil star", "example 123", "Madam, I'm Adam."]

for i in examples_list:
    if is_palindrome(i):
        print(f"{i} - це паліндром!")
        print()
    else:
        print(f"{i} - це не паліндром.")
        print()


# Інтерактив

print()
print("Спробуйте самостійно перевірити будь-який текст на паліндромність.")
print()

while True:
    # Введення тексту з командного рядка
    user_text = input("Введіть текст: ")

    # Перевірка на паліндромність
    if is_palindrome(user_text):
        print(f"{user_text} - це паліндром!")
        print()
    else:
        print(f"{user_text} - це не паліндром.")
        print()

# Для виходу з програми її необхідно закрити