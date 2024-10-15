from models import async_session
from models import User, Brak, Catalog
from sqlalchemy import distinct, not_, select, func
from sqlalchemy.orm import selectinload, subqueryload
from sqlalchemy.sql.functions import count
from aiogram.fsm.state import State
from aiogram.types import Message, FSInputFile
from aiogram.fsm.context import FSMContext
#from kbds_ex import *
import datetime
from kbds_copy import *

async def reg_user(tg_id, name, region, town, loc, email, post):
    async with async_session() as session:
            session.add(User(tg_id = tg_id, name = name, region = region, town = town, location = loc, email = email, post = post))
            await session.commit()

async def find_me(tg_id):
    async with async_session() as session:
        return await session.scalar(select(User.name).where(User.tg_id == tg_id))
    
async def get_name(clear_data):
    async with async_session() as session:
        name = await session.execute(select(Catalog.product).where(Catalog.primary_code == clear_data))
        result = name.fetchone()
        return result

async def kill_me_please(tg_id):
    async with async_session() as session:
        user_to_delete = await session.get(User, tg_id)
        return user_to_delete
    
async def target_to_kill(user_to_delete):
    async with async_session() as session:
        await session.delete(user_to_delete)
        await session.commit()

async def num_doc_f(doc_liter):
    current_datetime = datetime.datetime.now()
    formatted_datetime = current_datetime.strftime("%d%m%Y%H%M")
    number_doc = str(doc_liter + formatted_datetime)
    return  number_doc

async def date_doc_f():
    current_datetime = datetime.datetime.now()
    month_num = current_datetime.strftime("%m")
    day = current_datetime.strftime("%d")
    year = current_datetime.strftime("%Y")
    def month_name(month_num):
        month_num = int(month_num)
        month = ['Января', 'Февраля', 'Марта', 'Апреля', 'Мая', 'Июня', 'Июля', 'Августа', 'Сентября', 'Октября', 'Ноября', 'Декабря']
        return month[month_num-1]
    month = month_name(month_num)
    date_doc = str(day + " " + month + " " + year)   
    return date_doc

async def save_data(Doc_data, Doc_liter, Doc_number, ER_number, SSCC_number, NS_Code, Name_item, Serial_number, Sort_select, Cell_number, Comment):
    async with async_session() as session:
        session.add(Brak(Doc_data=Doc_data, Doc_liter = Doc_liter, Doc_number = Doc_number, ER_number = ER_number,
                         SSCC_number = SSCC_number, NS_Code = NS_Code, Name_item = Name_item, Serial_number = Serial_number,
                           Sort_select = Sort_select, Cell_number = Cell_number, Comment = Comment))
        await session.commit()

async def find_email(tg_id):
    async with async_session() as session:
        result = await session.execute(select(User.email).where(User.tg_id == tg_id))
        recipient_mail = result.fetchone()
        return recipient_mail