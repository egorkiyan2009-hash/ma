import telebot
from telebot import types

bot = telebot.TeleBot("8275571837:AAEmr01_HXHhRIQHQLxjwCqmQfgHkPlsAIk")  # Замени на свой токен

# Задания по темам
tasks = {
    "ОГЭ": {
        "Арифметика и алгебраические выражения": [
            {"question": "Вычисли: (8 + 2) × 3", "answer": "30", "solution": "(8 + 2) = 10, 10 × 3 = 30"},
            {"question": "Найди значение: 2² + 3²", "answer": "13", "solution": "2² = 4, 3² = 9, 4 + 9 = 13"},
        ],
        "Уравнения и неравенства": [
            {"question": "Реши уравнение: 3x - 6 = 9", "answer": "5", "solution": "3x = 15 → x = 5"},
            {"question": "Реши неравенство: x + 2 < 7", "answer": "x < 5", "solution": "x < 5"},
        ],
        "Текстовые задачи": [
            {"question": "Скорость 60 км/ч. Сколько времени на 180 км?", "answer": "3", "solution": "180 / 60 = 3"},
            {"question": "Цена тетради — 25 руб. Сколько стоят 4?", "answer": "100", "solution": "25 × 4 = 100"},
        ],
        "Последовательности": [
            {"question": "Найди 5-й член: 2, 4, 6, 8...", "answer": "10", "solution": "Арифм. прогрессия с d=2 → 2+4×2 = 10"},
            {"question": "Найди сумму первых 3 членов: 1, 2, 3...", "answer": "6", "solution": "1 + 2 + 3 = 6"},
        ],
        "Функции и графики": [
            {"question": "y = 2x. Чему равен y при x = 3?", "answer": "6", "solution": "2 × 3 = 6"},
            {"question": "y = x². Найди y при x = -2", "answer": "4", "solution": "(-2)² = 4"},
        ],
        "Геометрия (треугольники, многоугольники, окружность)": [
            {"question": "Сколько градусов в треугольнике?", "answer": "180", "solution": "Сумма углов треугольника — 180°"},
            {"question": "Сколько сторон у шестиугольника?", "answer": "6", "solution": "Шестиугольник — 6 сторон"},
        ],
        "Площадь, объём, преобразования": [
            {"question": "Площадь квадрата со стороной 4", "answer": "16", "solution": "S = a² = 4² = 16"},
            {"question": "Объем куба со стороной 3", "answer": "27", "solution": "V = a³ = 3³ = 27"},
        ],
        "Координатная плоскость": [
            {"question": "Координаты точки A(3, 4). Какое это направление?", "answer": "I четверть", "solution": "Обе координаты положительные → I четверть"},
        ],
        "Статистика и вероятность": [
            {"question": "Среднее арифметическое 4, 6, 10", "answer": "6.67", "solution": "(4 + 6 + 10)/3 = 20/3 ≈ 6.67"},
            {"question": "Какова вероятность выпадения чётного числа на кубике?", "answer": "1/2", "solution": "Чётные: 2, 4, 6 → 3 из 6 → 1/2"},
        ]
    },
    "ЕГЭ": {
        "Числа и их свойства": [
            {"question": "НОД(24, 36)?", "answer": "12", "solution": "НОД = 2×2×3 = 12"},
            {"question": "Чётное ли число 45?", "answer": "нет", "solution": "45 — нечётное"},
        ],
        "Алгебраические выражения": [
            {"question": "(a² - b²)/(a - b)", "answer": "a + b", "solution": "Разложение: (a - b)(a + b) / (a - b) = a + b"},
        ],
        "Уравнения и неравенства": [
            {"question": "Реши: x² - 9 = 0", "answer": "3 или -3", "solution": "x² = 9 → x = ±3"},
        ],
        "Текстовые задачи": [
            {"question": "Из пункта А в Б выехали... (смесь, работа, движение)", "answer": "решение зависит", "solution": "Пример задачи"},
        ],
        "Функции и графики": [
            {"question": "y = log₂(x), x = 8. Найди y", "answer": "3", "solution": "log₂(8) = 3"},
        ],
        "Производная и исследование функции": [
            {"question": "Производная x²?", "answer": "2x", "solution": "(x²)' = 2x"},
        ],
        "Начала анализа": [
            {"question": "Найди предел lim x→0 x²", "answer": "0", "solution": "x² → 0"},
        ],
        "Геометрия": [
            {"question": "Объём шара радиуса 3", "answer": "113.1", "solution": "V = 4/3πr³ = ~113.1"},
        ],
        "Тригонометрия": [
            {"question": "cos(0)", "answer": "1", "solution": "cos(0) = 1"},
        ],
        "Комбинаторика и вероятность": [{"question": "Сколькими способами выбрать 2 из 4?", "answer": "6", "solution": "C(4,2) = 6"},
        ],
        "Параметры": [
            {"question": "Реши: x² - 2x + a = 0 имеет 1 корень. a = ?", "answer": "1", "solution": "D = 0 → 4 - 4a = 0 → a = 1"},
        ]
    }
}

# Состояние пользователя
user_state = {}

# Старт
@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add("ОГЭ", "ЕГЭ")
    bot.send_message(message.chat.id, "Привет! Выбери экзамен:", reply_markup=markup)

# Выбор экзамена
@bot.message_handler(func=lambda msg: msg.text in tasks)
def exam_handler(message):
    exam = message.text
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    for topic in tasks[exam]:
        markup.add(topic)
    user_state[message.chat.id] = {"exam": exam}
    bot.send_message(message.chat.id, f"Выбери тему {exam}:", reply_markup=markup)

# Выбор темы
@bot.message_handler(func=lambda msg: user_state.get(msg.chat.id, {}).get("exam") and msg.text in tasks[user_state[msg.chat.id]["exam"]])
def topic_handler(message):
    exam = user_state[message.chat.id]["exam"]
    topic = message.text
    user_state[message.chat.id]["topic"] = topic
    user_state[message.chat.id]["task_index"] = 0
    send_task(message.chat.id)

# Отправка задания
def send_task(chat_id):
    state = user_state[chat_id]
    exam = state["exam"]
    topic = state["topic"]
    index = state["task_index"]
    task_list = tasks[exam][topic]

    if index < len(task_list):
        bot.send_message(chat_id, f"Задание {index + 1}:\n{task_list[index]['question']}")
    else:
        bot.send_message(chat_id, "✅ Все задания по этой теме выполнены!")
        user_state[chat_id]["topic"] = None

# Проверка ответа
@bot.message_handler(func=lambda msg: user_state.get(msg.chat.id, {}).get("topic") is not None)
def check_answer(message):
    state = user_state[message.chat.id]
    exam = state["exam"]
    topic = state["topic"]
    index = state["task_index"]
    task = tasks[exam][topic][index]

    if message.text.strip().lower() == task["answer"].strip().lower():
        bot.send_message(message.chat.id, "✅ Правильно!")
    else:
        bot.send_message(message.chat.id, f"❌ Неправильно.\nПравильный ответ: {task['answer']}\nРешение: {task['solution']}")

    state["task_index"] += 1
    send_task(message.chat.id)

bot.polling()