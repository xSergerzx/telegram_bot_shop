from aiogram import types, Dispatcher
from create_bot import dp, bot
from keyboards import kb_client
from aiogram.types import ReplyKeyboardRemove
from data_base import sqlite_db


# @dp.message_handler(commands=["start", 'help'])
async def command_start(message: types.Message):
    try:
        await bot.send_message(message.from_user.id, "Приятного аппетита", reply_markup=kb_client)
        await message.delete()
    except:
        await message.reply("Общение с ботом через ЛС,"
                            "напишите ему:\nhttps://t.me/Asdfdsdf_bot")


# @dp.message_handler(commands=["Режим_работы"])
async def shop_open_command(message: types.Message):
    try:
        await bot.send_message(message.from_user.id, "отсюда и до завтра")
        await message.delete()
    except:
        await message.reply("Общение с ботом через ЛС,"
                            "напишите ему:\nhttps://t.me/Asdfdsdf_bot")


# @dp.message_handler(commands=["Расположение"])
async def place_shop_command(message: types.Message):
    try:
        await bot.send_message(message.from_user.id, "где-то тут", reply_markup=ReplyKeyboardRemove())
        await message.delete()
    except:
        await message.reply("Общение с ботом через ЛС,"
                            "напишите ему:\nhttps://t.me/Asdfdsdf_bot")


async def shop_menu_command(message: types.Message):
    await sqlite_db.sql_read(message)


def register_handlers_client(dp: Dispatcher):
    dp.register_message_handler(command_start, commands=['start', 'help'])
    dp.register_message_handler(
        shop_open_command, commands=['Режим_работы'])
    dp.register_message_handler(
        place_shop_command, commands=['Расположение'])
    dp.register_message_handler(shop_menu_command, commands=['Меню'])
