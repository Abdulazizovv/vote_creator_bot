from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from bot.loader import dp
from bot.utils.db_api.db import get_or_create_user
from aiogram.dispatcher import FSMContext


@dp.message_handler(CommandStart(), state="*")
async def bot_start(message: types.Message, state: FSMContext):
    
    # disable all states
    await state.finish()

    user, created = await get_or_create_user(
        user_id=message.from_user.id,
        first_name=message.from_user.first_name,
        last_name=message.from_user.last_name,
        username=message.from_user.username
    )

    if created:
        await message.answer("Assalomu alaykum! Siz botimizga yangi keldingiz!")
    else:
        await message.answer("Assalomu alaykum! Siz botimizga qaytib keldingiz!")
        