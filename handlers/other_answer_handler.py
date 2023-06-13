from lexicon import lexicon_ru
from aiogram import Router
from aiogram.types import Message


router: Router = Router()


@router.message()
async def other_message_process(message: Message):
    try:
        await message.send_copy(chat_id=message.chat.id)
    except TypeError:
        await message.answer(lexicon_ru.LEXICON_RU['error'])
