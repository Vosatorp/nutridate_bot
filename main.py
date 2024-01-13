from aiogram import Bot, Dispatcher, executor, types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from config import API_TOKEN

bot = Bot(token=API_TOKEN)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)

# Define states for Nutritionist
class NutritionistRegistration(StatesGroup):
    name = State()
    experience = State()
    telegram_nick = State()
    # Add more states as needed

# Define states for User
class UserRegistration(StatesGroup):
    complaints = State()
    diet = State()
    analysis = State()
    # Add more states as needed

# Nutritionist registration handlers
@dp.message_handler(commands=['register_nutritionist'])
async def register_nutritionist(message: types.Message):
    await NutritionistRegistration.name.set()
    await message.reply("Введите ваше имя:")

# Add more handlers for each state in NutritionistRegistration

# User registration handlers
@dp.message_handler(commands=['register_user'])
async def register_user(message: types.Message):
    await UserRegistration.complaints.set()
    await message.reply("Опишите ваши жалобы:")

# Add more handlers for each state in UserRegistration

# Other bot handlers and functionality

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
