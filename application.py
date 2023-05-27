from aiogram import Bot, Dispatcher, executor
from aiogram.types import Message, KeyboardButton, ReplyKeyboardMarkup

from models.user import User
from models.event import Event
from exceptions.bot_exceptions import WrongMsgException

API_TOKEN = "<API_TOKEN>"

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

keyboard = ReplyKeyboardMarkup(resize_keyboard=True, keyboard=[
        [KeyboardButton(text='/start'), KeyboardButton(text='/help')]
    ])


@dp.message_handler(commands=['start', 'help'])  # 'help' move separate
async def welcome(msg: Message):
    user = User(msg.from_user.id)
    user.save_user()
    client = msg.from_user.full_name  # check, maybe save in User all info about
    await msg.reply(f"Hi {client}! My name is Lexa. If you often forget about various events, "
                    f"then I can help you remember them in time. Remind me of everything that matter.\n"
                    f"And please don't thank me!", reply_markup=keyboard)


@dp.message_handler(regexp='Добавить *')
async def save_event(msg: Message):
    """
        Add user event.
        example: "Добавить <название события> <дата[dd.mm.yyyy]> [повторять каждый [день, месяц, год]]"
    """
    event = Event(msg.from_user.id)
    event_details = event.add_event(msg.text)
    answer_msg = f"Добавлено событие '{event_details.event_name}' на {event_details.event_date}"
    await msg.answer(answer_msg)

    # try:
    #     evnt = event.add_event(msg)
    # except WrongMsgException as e:
    #     await msg.reply(str(e))
    # else:
    #     answer_msg = f"Добавлено событие {event.event_name} на {event.event_date}"
    #     await msg.answer(answer_msg)


# @dp.message_handler()
# async def echo(message: Message):
#     await message.reply(message.text)


if __name__ == '__main__':
    executor.start_polling(dp)
