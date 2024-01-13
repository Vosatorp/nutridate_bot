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
class Registration(StatesGroup):
    choosing_role = State()
    entering_details = State()

@dp.message_handler(commands=['start'], state="*")
async def welcome(message: types.Message, state: FSMContext):
    await Registration.choosing_role.set()
    await message.reply("Welcome! Are you a Client or a Nutritionist? Type /client or /nutritionist")

# Client Registration
@dp.message_handler(commands=['client'], state=Registration.choosing_role)
async def client_choice(message: types.Message, state: FSMContext):
    await state.update_data(role="client")
    await Registration.entering_details.set()
    await message.reply("You've chosen to register as a Client. Please enter your details in the format: Name, Age, Gender")

# Nutritionist Registration
@dp.message_handler(commands=['nutritionist'], state=Registration.choosing_role)
async def nutritionist_choice(message: types.Message, state: FSMContext):
    await state.update_data(role="nutritionist")
    await Registration.entering_details.set()
    await message.reply("You've chosen to register as a Nutritionist. Please enter your details in the format: Name, Qualification, Experience")

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
