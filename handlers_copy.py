from aiogram import F, Router, Bot
from aiogram.filters import CommandStart
from aiogram.types import Message, FSInputFile
import kbds_ex as kb 
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext
#import requests_ex as rq
import cv2, os
from config import TOKEN
#import aspose.barcode as barcode
from models import User
#from kbds import *
from kbds_copy import *
import requests_copy as rq_c
import nabroski as nb
import send_mail as sm
bot = Bot(TOKEN)
router = Router()

class Search(StatesGroup):
    reg_name = State()
    reg_region = State()
    reg_post = State()
    reg_town = State()
    reg_email = State()
    reg_loc = State()
    reg_confirm = State()
    reg_del_user = State()

class Reg_defect(StatesGroup):
    loc_defect = State()
    loc_defect_cell = State()
    DOC_number = State()
    ER_number = State()
    SSCC_number = State()
    NS_Code = State()
    Name_item = State()
    Serial_number = State()
    Sort_select = State()
    Cell_number = State()
    Comment = State()
    Doc_liter = State()
    confirm = State()
    Fin_confirm = State()

@router.message(CommandStart())
async def cmd_start(message: Message):
    #await rq.reg_user(message.from_user.id)
    await message.delete()
    await message.answer("Добро пожаловать!\nЧтобы корректно заполнить акт требуется регистрация пользователя.\nЕсли вы еще не зарегистрированы, пожалуйста, сделайте это прежде, чем начинать работу", reply_markup=main_kb)

@router.message(F.text == "ОТМЕНА")
async def cmd_cancel(message: Message, state: FSMContext):
    await state.clear()
    await message.answer("Действия отменены.", reply_markup=main_kb)

@router.message(F.text == "Удалить пользователя")
async def del_user(message:Message, state: FSMContext):
    await message.answer("Вы уверены, что хотите удалить свою запись из базы данных?", reply_markup=yes_no_kb)
    await state.set_state(Search.reg_del_user)

@router.message(F.text == "ДА", Search.reg_del_user)
async def del_user_2(message: Message, state: FSMContext):
    tg_id = message.from_user.id
    user_to_kill = await rq_c.kill_me_please(tg_id)
    if user_to_kill == None or user_to_kill == 0:
        await message.answer("Пользователь не найден", reply_markup=main_kb)
        await state.clear()
    else:
        await rq_c.target_to_kill(user_to_kill)
        await message.answer("Пользователь удален", reply_markup= main_kb)
        await state.clear()

@router.message(F.text == "НЕТ", Search.reg_del_user)
async def cancel_del_user(message: Message, state: FSMContext):
    await message.answer("Действие отменено", reply_markup= main_kb)
    await state.clear()

@router.message(F.text == "Регистрация")
async def register_new_user(message: Message, state: FSMContext):
    await state.set_state(Search.reg_name)
    await message.answer("Как тебя зовут? Представься в формате Фамилия И.О. (например, Иванов И.И.)",)

@router.message(Search.reg_name)
async def name(message: Message, state: FSMContext):
    await state.update_data(name = message.text)
    await state.set_state(Search.reg_region)
    await message.answer("Выбери регион в котором ты работаешь", reply_markup=city_kb)

@router.message(F.text == "Москва",Search.reg_region)
async def get_region(message: Message, state: FSMContext):
    await state.update_data(region = message.text)
    await state.set_state(Search.reg_town)
    await message.answer("Выбери город, в котором работаешь", reply_markup= town_kb_msk)

@router.message(F.text == "Самара",Search.reg_region)
async def get_region(message: Message, state: FSMContext):
    await state.update_data(region = message.text)
    await state.set_state(Search.reg_town)
    await message.answer("Выбери город, в котором работаешь", reply_markup= town_kb_sam)

@router.message(F.text == "Владивосток",Search.reg_region)
async def get_region(message: Message, state: FSMContext):
    await state.update_data(region = message.text)
    await state.set_state(Search.reg_town)
    await message.answer("Выбери город, в котором работаешь", reply_markup= town_kb_vld)

@router.message(F.text == "Екатеринбург",Search.reg_region)
async def get_region(message: Message, state: FSMContext):
    await state.update_data(region = message.text)
    await state.set_state(Search.reg_town)
    await message.answer("Выбери город, в котором работаешь", reply_markup= town_kb_ekb)

@router.message(F.text == "Новосибирск",Search.reg_region)
async def get_region(message: Message, state: FSMContext):
    await state.update_data(region = message.text)
    await state.set_state(Search.reg_town)
    await message.answer("Выбери город, в котором работаешь", reply_markup= town_kb_nsk)

@router.message(F.text == "Краснодар",Search.reg_region)
async def get_region(message: Message, state: FSMContext):
    await state.update_data(region = message.text)
    await state.set_state(Search.reg_town)
    await message.answer("Выбери город, в котором работаешь", reply_markup= town_kb_krd)

@router.message(F.text == "Москва",Search.reg_town)
async def get_town(message: Message, state: FSMContext):
    await state.update_data(town = message.text)    
    await state.set_state(Search.reg_loc)
    await message.answer("Укажи место работы", reply_markup=reg_loc_kb_msk)

@router.message(F.text == "Санкт-Петербург",Search.reg_town)
async def get_town(message: Message, state: FSMContext):
    await state.update_data(town = message.text)    
    await state.set_state(Search.reg_loc)
    await message.answer("Укажи место работы", reply_markup=reg_loc_kb_dc)

@router.message(F.text == "Нижний Новгород",Search.reg_town)
async def get_town(message: Message, state: FSMContext):
    await state.update_data(town = message.text)    
    await state.set_state(Search.reg_loc)
    await message.answer("Укажи место работы", reply_markup=reg_loc_kb_dc)

@router.message(F.text == "Воронеж",Search.reg_town)
async def get_town(message: Message, state: FSMContext):
    await state.update_data(town = message.text)    
    await state.set_state(Search.reg_loc)
    await message.answer("Укажи место работы", reply_markup=reg_loc_kb_dc)

@router.message(F.text == "Калининград",Search.reg_town)
async def get_town(message: Message, state: FSMContext):
    await state.update_data(town = message.text)    
    await state.set_state(Search.reg_loc)
    await message.answer("Укажи место работы", reply_markup=reg_loc_kb_dc)

@router.message(F.text == "Ярославль",Search.reg_town)
async def get_town(message: Message, state: FSMContext):
    await state.update_data(town = message.text)    
    await state.set_state(Search.reg_loc)
    await message.answer("Укажи место работы", reply_markup=reg_loc_kb_dc)

@router.message(F.text == "Рязань",Search.reg_town)
async def get_town(message: Message, state: FSMContext):
    await state.update_data(town = message.text)    
    await state.set_state(Search.reg_loc)
    await message.answer("Укажи место работы", reply_markup=reg_loc_kb_dc)

@router.message(F.text == "Владивосток",Search.reg_town)
async def get_town(message: Message, state: FSMContext):
    await state.update_data(town = message.text)    
    await state.set_state(Search.reg_loc)
    await message.answer("Укажи место работы", reply_markup=reg_loc_kb_dc_rc)

@router.message(F.text == "Хабаровск",Search.reg_town)
async def get_town(message: Message, state: FSMContext):
    await state.update_data(town = message.text)    
    await state.set_state(Search.reg_loc)
    await message.answer("Укажи место работы", reply_markup=reg_loc_kb_dc)

@router.message(F.text == "Новосибирск",Search.reg_town)
async def get_town(message: Message, state: FSMContext):
    await state.update_data(town = message.text)    
    await state.set_state(Search.reg_loc)
    await message.answer("Укажи место работы", reply_markup=reg_loc_kb_dc_rc)

@router.message(F.text == "Красноярск",Search.reg_town)
async def get_town(message: Message, state: FSMContext):
    await state.update_data(town = message.text)    
    await state.set_state(Search.reg_loc)
    await message.answer("Укажи место работы", reply_markup=reg_loc_kb_dc)

@router.message(F.text == "Кемерово",Search.reg_town)
async def get_town(message: Message, state: FSMContext):
    await state.update_data(town = message.text)    
    await state.set_state(Search.reg_loc)
    await message.answer("Укажи место работы", reply_markup=reg_loc_kb_dc)

@router.message(F.text == "Иркутск",Search.reg_town)
async def get_town(message: Message, state: FSMContext):
    await state.update_data(town = message.text)    
    await state.set_state(Search.reg_loc)
    await message.answer("Укажи место работы", reply_markup=reg_loc_kb_dc)

@router.message(F.text == "Барнаул",Search.reg_town)
async def get_town(message: Message, state: FSMContext):
    await state.update_data(town = message.text)    
    await state.set_state(Search.reg_loc)
    await message.answer("Укажи место работы", reply_markup=reg_loc_kb_dc)

@router.message(F.text == "Челябинск",Search.reg_town)
async def get_town(message: Message, state: FSMContext):
    await state.update_data(town = message.text)    
    await state.set_state(Search.reg_loc)
    await message.answer("Укажи место работы", reply_markup=reg_loc_kb_dc)

@router.message(F.text == "Екатеринбург",Search.reg_town)
async def get_town(message: Message, state: FSMContext):
    await state.update_data(town = message.text)    
    await state.set_state(Search.reg_loc)
    await message.answer("Укажи место работы", reply_markup=reg_loc_kb_dc_rc)

@router.message(F.text == "Пермь",Search.reg_town)
async def get_town(message: Message, state: FSMContext):
    await state.update_data(town = message.text)    
    await state.set_state(Search.reg_loc)
    await message.answer("Укажи место работы", reply_markup=reg_loc_kb_dc)

@router.message(F.text == "Тюмень",Search.reg_town)
async def get_town(message: Message, state: FSMContext):
    await state.update_data(town = message.text)    
    await state.set_state(Search.reg_loc)
    await message.answer("Укажи место работы", reply_markup=reg_loc_kb_dc)

@router.message(F.text == "Самара",Search.reg_town)
async def get_town(message: Message, state: FSMContext):
    await state.update_data(town = message.text)    
    await state.set_state(Search.reg_loc)
    await message.answer("Укажи место работы", reply_markup=reg_loc_kb_dc_rc)

@router.message(F.text == "Казань",Search.reg_town)
async def get_town(message: Message, state: FSMContext):
    await state.update_data(town = message.text)    
    await state.set_state(Search.reg_loc)
    await message.answer("Укажи место работы", reply_markup=reg_loc_kb_dc)

@router.message(F.text == "Саратов",Search.reg_town)
async def get_town(message: Message, state: FSMContext):
    await state.update_data(town = message.text)    
    await state.set_state(Search.reg_loc)
    await message.answer("Укажи место работы", reply_markup=reg_loc_kb_dc)

@router.message(F.text == "Уфа",Search.reg_town)
async def get_town(message: Message, state: FSMContext):
    await state.update_data(town = message.text)    
    await state.set_state(Search.reg_loc)
    await message.answer("Укажи место работы", reply_markup=reg_loc_kb_dc)

@router.message(F.text == "Оренбург",Search.reg_town)
async def get_town(message: Message, state: FSMContext):
    await state.update_data(town = message.text)    
    await state.set_state(Search.reg_loc)
    await message.answer("Укажи место работы", reply_markup=reg_loc_kb_dc)

@router.message(F.text == "Краснодар",Search.reg_town)
async def get_town(message: Message, state: FSMContext):
    await state.update_data(town = message.text)    
    await state.set_state(Search.reg_loc)
    await message.answer("Укажи место работы", reply_markup=reg_loc_kb_dc_rc)

@router.message(F.text == "Ростов-на-Дону",Search.reg_town)
async def get_town(message: Message, state: FSMContext):
    await state.update_data(town = message.text)    
    await state.set_state(Search.reg_loc)
    await message.answer("Укажи место работы", reply_markup=reg_loc_kb_dc)

@router.message(F.text == "Волгоград",Search.reg_town)
async def get_town(message: Message, state: FSMContext):
    await state.update_data(town = message.text)    
    await state.set_state(Search.reg_loc)
    await message.answer("Укажи место работы", reply_markup=reg_loc_kb_dc)

@router.message(F.text == "Пятигорск",Search.reg_town)
async def get_town(message: Message, state: FSMContext):
    await state.update_data(town = message.text)    
    await state.set_state(Search.reg_loc)
    await message.answer("Укажи место работы", reply_markup=reg_loc_kb_dc)

@router.message(F.text == "Симферополь",Search.reg_town)
async def get_town(message: Message, state: FSMContext):
    await state.update_data(town = message.text)    
    await state.set_state(Search.reg_loc)
    await message.answer("Укажи место работы", reply_markup=reg_loc_kb_dc)

@router.message(F.text == "Сочи",Search.reg_town)
async def get_town(message: Message, state: FSMContext):
    await state.update_data(town = message.text)    
    await state.set_state(Search.reg_loc)
    await message.answer("Укажи место работы", reply_markup=reg_loc_kb_dc)

@router.message(Search.reg_loc)
async def get_loc(message: Message, state: FSMContext):
    await state.update_data(loc = message.text)
    await state.set_state(Search.reg_post)
    await message.answer("Укажи свою должность", reply_markup=post_kb)

@router.message(Search.reg_post)
async def get_post(message: Message, state: FSMContext):
    await state.update_data(post = message.text)
    await state.set_state(Search.reg_email)
    await message.answer("Укажи email на который будем отправлять документ")

@router.message(Search.reg_email)
async def get_email(message: Message, state: FSMContext):
    await state.update_data(email = message.text)
    data = await state.get_data()
    await message.answer(f'Будет зарегистрирован пользователь,\n{data["name"]}, {data["post"]},\nиз города {data["town"]}, РЦ {data["region"]}.\nCозданные документы будем отправлять на \n{data["email"]}\n\nЗавершить регистрацию?', reply_markup=fin_reg_kb)
    await state.set_state(Search.reg_confirm)

@router.message(F.text == "Ошибка, еще раз",Search.reg_confirm)
async def confirm(message: Message, state: FSMContext):
    data = await state.get_data()
    await message.answer(f'Регистрация пользователя {data["name"]} отменена. \nНачните регистрацию с начала')
    await message.answer("Как тебя зовут? Представься в формате Фамилия И.О. (например, Иванов И.И.)",)
    await state.set_state(Search.reg_name)

@router.message(F.text == "Всё верно",Search.reg_confirm)
async def confirm(message: Message, state: FSMContext):
    data = await state.get_data()
    await message.answer(f'Регистрация пользователя {data["name"]} завершена', reply_markup=main_kb)
    tg_id = message.from_user.id
    name = data["name"]
    region = data["region"]
    town = data['town']
    email = data['email']
    loc = data["loc"]
    post = data["post"]
    await rq_c.reg_user(tg_id, name, region, town, loc, email, post)
    await state.clear()

@router.message(F.text == "Проверить регистрацию")
async def who_am_i(message: Message):
    result = await rq_c.find_me(message.from_user.id)
    if result == None or result == 0:
        await message.answer("Пользователь в системе не найден")
    else:
        await message.answer(f"Пользователь {result} зарегистрирован в системе.")

@router.message(F.text == "Оформить акт")
async def loc_defect(message:Message, state: FSMContext):
    await message.answer("Укажи место обнаружения дефекта", reply_markup=reg_loc_defect_kb)

    await state.set_state(Reg_defect.loc_defect)

@router.message(F.text == "Разгрузка", Reg_defect.loc_defect)
async def loc_cell(message: Message, state: FSMContext):
    await state.update_data(loc_defect = "&KARANTIN")
    await state.update_data(Doc_liter = "Н-ПР-")
    await message.answer("Введи номер паллета SSCC")
    await state.set_state(Reg_defect.SSCC_number)

@router.message(F.text == "Ячейка склада", Reg_defect.loc_defect)
async def set_cell_warehouse(message: Message, state: FSMContext):
    await message.answer("Укажи ячейку отбора")
    await state.update_data(Doc_liter = "Н-СК-")
    await state.set_state(Reg_defect.loc_defect_cell)

@router.message(Reg_defect.loc_defect_cell)
async def loc_cell_warehouse(message: Message, state: FSMContext):
    await state.update_data(loc_defect = str.upper(message.text))
    await message.answer("Введи номер паллета SSCC")
    await state.set_state(Reg_defect.SSCC_number)

@router.message(Reg_defect.SSCC_number)
async def set_sscc_number(message: Message, state: FSMContext):
    await state.update_data(SSCC_number = message.text)
    await message.answer("Укажи номер документа прихода")
    await state.set_state(Reg_defect.ER_number)

@router.message(Reg_defect.ER_number)
async def set_er_num(message: Message, state: FSMContext):
    await state.update_data(ER_number = str.upper(message.text))
    await message.answer("Введи NS код товара. ТОЛЬКО ЦИФРЫ!")
    await state.set_state(Reg_defect.NS_Code)

@router.message(Reg_defect.NS_Code)
async def result(message: Message, state: FSMContext):
    if  len(message.text) != 7:
        await message.answer("Некорректный NS код. Попробуй ещё раз")
        await state.set_state(Reg_defect.NS_Code)
    else:
        await state.update_data(NS_Code = ("NS-")+(message.text))
        data = await state.get_data()
        #await message.answer(f"Ищем товар {data['NS_code']}")
        name = await rq_c.get_name(data['NS_Code'])
        if name == None or name == 0:
            await message.answer("Я ничего не нашёл. Проверь NS. Попробуй ещё раз")
            await state.set_state(Reg_defect.NS_Code)
        else:
            await message.answer(f"{name[0]}")
            await state.update_data(Name_item = name)
            await state.set_state(Reg_defect.Serial_number)
            await message.answer("Введи серийный номер товара")

@router.message(Reg_defect.Serial_number)
async def get_serial(message: Message, state: FSMContext):
    await state.update_data(Serial_number = message.text)
    await message.answer("Укажи сорт дефекта", reply_markup=sort_kb)
    await state.set_state(Reg_defect.Sort_select)

@router.message(F.text == "Подсказка по сортам брака", Reg_defect.Sort_select)
async def show_help(message:  Message, state: FSMContext):
    await message.answer(f"Сорт 1   Ветхая, поврежденная упаковка, которая не подлежит восстановлению, товар надлежащего качества с подтвержденной работоспособностью.\n"
                         f"Сорт 2   Повреждения упаковки – от 10 до 15 см» - товар надлежащего качества с подтвержденной работоспособностью.\n"
                         f"Сорт 3   Повреждения упаковки – значительные повреждения от 15 до 30 см» - товар надлежащего качества с подтвержденной работоспособностью\n"
                         f"Сорт 4   Повреждения упаковки – значительные повреждения более 30 см и / или ветхие коробки - товар надлежащего качества с подтвержденной работоспособностью\n"
                         f"Сорт 5   Товар, имеющий повреждения внешнего вида, не влияющие на работоспособность и функциональность (царапина, потертости и т.п)\n"
                         f"На экспертизу   Товар, имеющий повреждения внешнего вида, которые вызывают сомнения в работоспособности и функциональности (замятие, вмятина, бой и т.п.)", reply_markup=sort_kb)

@router.message(Reg_defect.Sort_select)
async def set_sort(message: Message, state: FSMContext):
    await state.update_data(Sort_select = message.text)
    await message.answer("Добавь комментарий")
    await state.set_state(Reg_defect.Comment)

@router.message(Reg_defect.Comment)
async def get_comment(message: Message, state: FSMContext):
    await state.update_data(Comment = message.text)
    await message.answer("Не забудь сделать фотографии", reply_markup=ok_kb)
    await state.set_state(Reg_defect.confirm)
    
@router.message(F.text == "OK", Reg_defect.confirm)    
async def confirm_data(message: Message, state: FSMContext):
    data = await state.get_data()
    Doc_data = await rq_c.date_doc_f()
    doc_liter = data["Doc_liter"]
    Doc_number = await rq_c.num_doc_f(doc_liter)
    ER_number = data["ER_number"]
    SSCC_number = data["SSCC_number"]
    NS_Code = data["NS_Code"]
    Name_item = data["Name_item"][0]
    Serial_number = data["Serial_number"]
    Sort_select = data["Sort_select"]
    Cell_number = data["loc_defect"]
    Comment = data["Comment"]
    await message.answer(f"Давай проверим, что у нас получилось.\n"
                         f"Сегодня: {Doc_data}\n"
                         f"Мы отправляем в брак: {Name_item}\n"
                         f"Серийный номер товара: {Serial_number}\n"
                         f"из {Cell_number}\n"
                         f"Поступивший по документу: {ER_number}\n"
                         f"С комментарием: {Comment}\n"
                         f"Присваиваем товару {Sort_select} и номер {SSCC_number}.\n"
                         f"Всё верно?", reply_markup=fin_reg_kb)
    await state.set_state(Reg_defect.Fin_confirm)

@router.message(F.text == "Всё верно", Reg_defect.Fin_confirm)
async def fin_confirm(message: Message, state: FSMContext):
    await message.answer("Созданный документ отправлен на почту указанную при регистрации", reply_markup=main_kb)
    tg_id = message.from_user.id
    data = await state.get_data()
    Doc_data = await rq_c.date_doc_f()
    doc_liter = data["Doc_liter"]
    Doc_number = await rq_c.num_doc_f(doc_liter)
    ER_number = data["ER_number"]
    SSCC_number = data["SSCC_number"]
    NS_Code = data["NS_Code"]
    Name_item = data["Name_item"][0]
    Serial_number = data["Serial_number"]
    Sort_select = data["Sort_select"]
    Cell_number = data["loc_defect"]
    Comment = data["Comment"]
    recipient_email = await rq_c.find_email(tg_id)
    await rq_c.save_data(Doc_data=Doc_data, Doc_liter = doc_liter, Doc_number = Doc_number, ER_number = ER_number,
                         SSCC_number = SSCC_number, NS_Code = NS_Code, Name_item = Name_item, Serial_number = Serial_number,
                           Sort_select = Sort_select, Cell_number = Cell_number, Comment = Comment)
    await nb.zapolni_akt(SSCC_number, tg_id)
    await sm.send_email(recipient_email[0])
    await state.clear()

@router.message(F.text == "Ошибка, еще раз", Reg_defect.Fin_confirm)
async def fin_confirm(message: Message, state: FSMContext):
    await message.answer("Собранная информация удалена, начните процедуру с начала", reply_markup=main_kb)
    await state.clear()

    
