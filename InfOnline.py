import time
import vk_api
from threading import Thread
from config import TOKEN

# В файле config.py укажите токен авторизации страницы
def get_vk_session(acces_token, i):
    session = vk_api.VkApi(token=acces_token)
    vk_session = session.get_api()

    while True:
        try:
            print(f'Онлайн режим активирован для аккаунта: {i}')
            vk_session.account.setOnline() # 5 мин == 300 сек
            time.sleep(5)
        except Exception as e:
            print(f'Что-то пошло не так: {e}')
            time.sleep(30) # Пауза при ошибке

# Создаем и запускаем потоки для каждого токена
thread_1 = Thread(target=get_vk_session, args=(TOKEN, 1))
thread_1.start()

# Ожидаем завершения потоков (хотя они бесконечные)
thread_1.join()
