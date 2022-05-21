"""
This is a echo bot.
It echoes any incoming text messages.
"""

import logging
import wikipedia
from aiogram import Bot, Dispatcher, executor, types
wikipedia.set_lang('uz')
API_TOKEN = '5132802160:AAHdklTyqK-Tphz854cduhxnMhaNgLKnLMQ'

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

#handler - habarlar, buyruqlar bilan ishlovchi qism
@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    """
    This handler will be called when user sends `/start` or `/help` command
    """
    await message.reply("Assalomu alaykum, hush kelibsiz")


#echo - bu foydalanuvchini habarini o'ziga qaytarib yuboradigan
@dp.message_handler()
async def send(message: types.Message):
    #try - bu agar so'ralayotgan so'rov mavjud bo'lgan taqdirda
    try:
        surov = wikipedia.summary(message: types.Message)
        #await - foydalanuvchiga qaytaradigan buyruq
        await message.answer(surov)
        #except - bu o'sha buyruq mavjud bo'lmasa
    except:
        await message.answer("Ushbu mavzuga oid maqola topilmadi :(")

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)

#skip_updates - agar bot ishdan to'xtasa kelgan buyruqlarni bajarmaydi