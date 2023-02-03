from aiogram.types import ReplyKeyboardMarkup, KeyboardButton  # , ReplyKeyboardRemove

b1 = KeyboardButton("/Режим_работы")
b2 = KeyboardButton("/Расположение")
b3 = KeyboardButton("/Меню")
b4 = KeyboardButton("Поделиться контактом", request_contact=True)
b5 = KeyboardButton("Поделиться местоположением", request_location=True)
kb_client = ReplyKeyboardMarkup(
    resize_keyboard=True, one_time_keyboard=True, row_width=2).add(b3).add(b1, b2)  # после б2 скобку убрать, b4, b5)
