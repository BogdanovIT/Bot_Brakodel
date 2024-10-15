from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

main_kb = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='Оформить акт')],    
    [KeyboardButton(text='Регистрация')],    
    [KeyboardButton(text='Проверить регистрацию')],
    [KeyboardButton(text='Удалить пользователя')],    
    ], resize_keyboard=True, one_time_keyboard=True)

city_kb = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text="Москва"), KeyboardButton(text="Самара")],
    [KeyboardButton(text="Владивосток"), KeyboardButton(text="Екатеринбург")],
    [KeyboardButton(text="Новосибирск"), KeyboardButton(text="Краснодар")],
    [KeyboardButton(text='ОТМЕНА')],
], resize_keyboard=True, one_time_keyboard=True)

town_kb_msk = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text="Москва"), KeyboardButton(text="Санкт-Петербург")],
    [KeyboardButton(text="Нижний Новгород"), KeyboardButton(text="Воронеж ")],
    [KeyboardButton(text="Калининград"), KeyboardButton(text="Ярославль")],
    [KeyboardButton(text="Рязань")],
    [KeyboardButton(text='ОТМЕНА')],
], resize_keyboard=True, one_time_keyboard=True)
    
town_kb_sam = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text="Самара"), KeyboardButton(text="Казань")],
    [KeyboardButton(text="Саратов"), KeyboardButton(text="Оренбург")],
    [KeyboardButton(text="Уфа")],
    [KeyboardButton(text='ОТМЕНА')],
], resize_keyboard=True, one_time_keyboard=True)

town_kb_vld = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text="Владивосток")], [KeyboardButton(text="Хабаровск")],
    [KeyboardButton(text='ОТМЕНА')],
], resize_keyboard=True, one_time_keyboard=True)

town_kb_nsk = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text="Новосибирск"), KeyboardButton(text="Красноярск")],
    [KeyboardButton(text="Кемерово"), KeyboardButton(text="Иркутск")],
    [KeyboardButton(text="Барнаул")],
    [KeyboardButton(text='ОТМЕНА')],
], resize_keyboard=True, one_time_keyboard=True)

town_kb_ekb = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text="Екатеринбург"), KeyboardButton(text="Челябинск")],
    [KeyboardButton(text="Пермь"), KeyboardButton(text="Тюмень")],
    [KeyboardButton(text='ОТМЕНА')],
], resize_keyboard=True, one_time_keyboard=True)

town_kb_krd = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text="Краснодар"), KeyboardButton(text="Ростов-на-Дону")],
    [KeyboardButton(text="Волгоград"), KeyboardButton(text="Пятигорск")],
    [KeyboardButton(text="Симферополь"), KeyboardButton(text="Сочи")],
    [KeyboardButton(text='ОТМЕНА')],
], resize_keyboard=True, one_time_keyboard=True)

post_kb = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text="Управляющий"), KeyboardButton(text="Заместитель управляющего")],
    [KeyboardButton(text="Старший кладовщик"), KeyboardButton(text="Кладовщик")],
    [KeyboardButton(text='ОТМЕНА')],
], resize_keyboard=True, one_time_keyboard=True)

fin_reg_kb = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text="Всё верно"), KeyboardButton(text="Ошибка, еще раз")],
], resize_keyboard=True, one_time_keyboard=True)

sort_kb = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text="СОРТ 1"), KeyboardButton(text="СОРТ 2")],
    [KeyboardButton(text="СОРТ 3"), KeyboardButton(text="СОРТ 4")],
    [KeyboardButton(text="СОРТ 5"), KeyboardButton(text="НА ЭКСПЕРТИЗУ")],
    [KeyboardButton(text="Подсказка по сортам брака")],
    [KeyboardButton(text='ОТМЕНА')],
], resize_keyboard=True, one_time_keyboard=True)

reg_loc_kb_msk = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text="Центральный офис"), KeyboardButton(text="ФРЦ БРИЗ Шереметьево")],
    [KeyboardButton(text="МОС БРИЗ Медведково"), KeyboardButton(text="МОС БРИЗ Саларьево")],
    [KeyboardButton(text="МОС БРИЗ Рязанское"), KeyboardButton(text="ДРЦ БРИЗ Быково")],
    [KeyboardButton(text='ОТМЕНА')],
], resize_keyboard=True, one_time_keyboard=True)

reg_loc_kb_dc = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text="Дистрибьюторский центр")],
    [KeyboardButton(text='ОТМЕНА')],
], resize_keyboard=True, one_time_keyboard=True)

reg_loc_kb_dc_rc = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text="Дистрибьюторский центр")],
    [KeyboardButton(text="РРЦ")],
    [KeyboardButton(text='ОТМЕНА')],
], resize_keyboard=True, one_time_keyboard=True)

reg_loc_defect_kb = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text="Разгрузка")],
    [KeyboardButton(text="Ячейка склада")],
    [KeyboardButton(text='ОТМЕНА')],
], resize_keyboard=True, one_time_keyboard=True)

ok_kb = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text="OK")],
    [KeyboardButton(text='ОТМЕНА')],
], resize_keyboard=True)

yes_no_kb = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text="ДА")], [KeyboardButton(text='НЕТ')],
], resize_keyboard=True, one_time_keyboard=True)