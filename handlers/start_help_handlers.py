from lexicon import lexicon_ru
from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command, CommandStart


router: Router = Router()


@router.message(CommandStart())
async def start_command_process(message: Message):
    await message.answer(lexicon_ru.LEXICON_RU['start'])


@router.message(Command(commands=['help']))
async def help_command_process(message: Message):
    await message.answer(lexicon_ru.LEXICON_RU['help'])
