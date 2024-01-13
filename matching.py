import asyncio


class MatchingSystem:
    @staticmethod
    async def daily_match():
        while True:
            # Ожидание до 13:00 каждый день
            await asyncio.sleep(time_until_13_pm())

            # Получение анкет клиентов и нутрициологов
            client_profiles = get_client_profiles()
            nutritionist_profiles = get_nutritionist_profiles()

            # Рассылка анкет
            for client in client_profiles:
                await send_profiles(client, nutritionist_profiles, 'nutritionist')

            for nutritionist in nutritionist_profiles:
                await send_profiles(nutritionist, client_profiles, 'client')

            # Ожидание до следующего дня
            await asyncio.sleep(24 * 3600 - time_since_13_pm())


def time_until_13_pm():
    # Реализация функции, возвращающей время до 13:00
    pass


def time_since_13_pm():
    # Реализация функции, возвращающей время с 13:00
    pass


def get_client_profiles():
    # Получение профилей клиентов из базы данных
    pass


def get_nutritionist_profiles():
    # Получение профилей нутрициологов из базы данных
    pass


async def send_profiles(user, profiles, profile_type):
    # Рассылка анкет пользователям
    pass
