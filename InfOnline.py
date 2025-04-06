import time
import vk_api
from config import TOKEN

# В файле config.py укажите токен авторизации страницы
session = vk_api.VkApi(token=TOKEN)
vk = session.get_api()

while True:
    try:
        print('Онлайн режим активирован')
        vk.account.setOnline()
# Каждые 5 минут (300) секунд будет активироваться метод setOnline
        time.sleep(300)
    except Exception as e:
        print(f'Что-то пошло не так: {e}')
# запустить командой InfOnline.py
