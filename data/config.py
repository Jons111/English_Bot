from environs import Env

# environs kutubxonasidan foydalanish
env = Env()
env.read_env()
adminlar='5081475715'
botlar = ['https://t.me/Ingliz_gramatika_bot']
# .env fayl ichidan quyidagilarni o'qiymiz
BOT_TOKEN = env.str("BOT_TOKEN")  # Bot toekn
ADMINS = env.list("ADMINS")  # adminlar ro'yxati
IP = env.str("ip")  # Xosting ip manzili
