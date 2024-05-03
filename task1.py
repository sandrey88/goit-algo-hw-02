from queue import Queue
import random
import time

# Створення черги заявок
queue = Queue()

# Структура заявки
class Request:
    def __init__(self, id, name, description, timestamp):
        self.id = id
        self.name = name
        self.description = description
        self.timestamp = timestamp

# Генератор заявок
def generate_request():
    id = 1
    while True:
        name = f"Клієнта {id}"
        description = random.choice(["Проблема з телефоном", "Проблема з ноутбуком", "Проблема з телевізором", "Проблема з побутовою технікою"])
        timestamp = time.time()
        new_request = Request(id, name, description, timestamp)
        print(f"Створено нову заявку №{new_request.id}")
        queue.put(new_request)
        yield new_request
        id += 1

# Функція обробки заявок
def process_request():
    if not queue.empty():
        request = queue.get()
        print(f"Обробка заявки №{request.id} від {request.name} ({request.description})")
        # Імітація обробки (затримка на 3 секунди)
        time.sleep(3)
        print(f"Заявка №{request.id} оброблена")
        print()
    else:
        print("Черга пуста")


# Головний цикл програми
# Програма буде виконуватися поки користувач не вийде з неї
request_generator = generate_request()
while True:
    new_request = next(request_generator)
    time.sleep(1)
    process_request()

    # Затримка перед наступною ітерацією
    time.sleep(2)
