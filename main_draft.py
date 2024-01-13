from aiogram import Bot, Dispatcher, executor, types
# from aiogram.utils import executor
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from config import API_TOKEN

bot = Bot(token=API_TOKEN)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)


# Define states
class NutritionistRegistration(StatesGroup):
    name = State()
    experience = State()
    telegram_nick = State()


@dp.message_handler(commands=['register_nutritionist'])
async def register_nutritionist(message: types.Message):
    await NutritionistRegistration.name.set()
    await message.reply("Введите ваше имя:")


@dp.message_handler(state=NutritionistRegistration.name)
async def process_name(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['name'] = message.text
    await NutritionistRegistration.next()
    await message.reply("Опишите ваш опыт и услуги:")


@dp.message_handler(state=NutritionistRegistration.experience)
async def process_experience(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['experience'] = message.text
    await NutritionistRegistration.next()
    await message.reply("Введите ваш телеграмм-ник:")


@dp.message_handler(state=NutritionistRegistration.telegram_nick)
async def process_telegram_nick(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['telegram_nick'] = message.text
        # Здесь можно добавить код для сохранения данных в базе данных
    await state.finish()
    await message.reply("Регистрация нутрициолога завершена!")


class ClientRegistration(StatesGroup):
    name = State()
    complaints = State()
    diet = State()
    # Для упрощения, предположим, что анализы и симптомы не требуются в этом примере


@dp.message_handler(commands=['register_client'])
async def register_client(message: types.Message):
    await ClientRegistration.name.set()
    await message.reply("Введите ваше имя:")


# Аналогичные обработчики для состояний клиентской регистрации


@dp.message_handler(commands=['start'], state="*")
async def welcome(message: types.Message, state: FSMContext):
    await Registration.choosing_role.set()
    await message.reply("Welcome! Are you a Client or a Nutritionist? Type /client or /nutritionist")


# Client Registration
@dp.message_handler(commands=['client'], state=ClientRegistration.choosing_role)
async def client_choice(message: types.Message, state: FSMContext):
    await state.update_data(role="client")
    await ClientRegistration.entering_details.set()
    await message.reply("You've chosen to register as a Client. Please enter your details in the format: Name, Age, "
                        "Gender")


# Nutritionist Registration
@dp.message_handler(commands=['nutritionist'], state=NutritionistRegistration.choosing_role)
async def nutritionist_choice(message: types.Message, state: FSMContext):
    await state.update_data(role="nutritionist")
    await NutritionistRegistration.entering_details.set()
    await message.reply("You've chosen to register as a Nutritionist. Please enter your details in the format: Name, "
                        "Qualification, Experience")


# Handling Details Input
@dp.message_handler(state=Registration.entering_details)
async def process_details(message: types.Message, state: FSMContext):
    user_data = await state.get_data()
    role = user_data.get("role")

    # Here, you'd normally save the details to your database.
    # For this example, we're just echoing back the details.
    if role == "client":
        # Extract and process client details
        # For now, just echo back
        await message.reply(f"Received your details as a Client: {message.text}")
    elif role == "nutritionist":
        # Extract and process nutritionist details
        # For now, just echo back
        await message.reply(f"Received your details as a Nutritionist: {message.text}")

    await state.finish()


# Execute the bot
if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)