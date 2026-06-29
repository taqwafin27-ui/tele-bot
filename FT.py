import os
import telebot
from telebot import types

TOKEN = "8830976188:AAE5m2f40_cxGyJwHmilMvffnJyXO4nXNlk"

bot = telebot.TeleBot(TOKEN)
links = {
    "التمويل الإسلامي": "رابط_هنا",
    "إدارة المحافظ": "رابط_هنا",
    "داتا بيز": "رابط_هنا",
    "بايثون": "https://drive.google.com/drive/folders/1gipoicti-BvN_1VTiF4ywfbY2PAsxifi  ",
    "سايبر": "https://drive.google.com/drive/mobile/folders/1EdS_gbdcgIdSayRfTL_78f5D5G5z1N9d?fbclid=IwY2xjawLLk9RleHRuA2FlbQIxMQABHlJ2v7jpgh0b6VEr7jLu7fV2XOaHkw2Sa1pXlCS1hPA1EVKz2U7G2bYFQfpe_aem_Ifed2EqnCaZEFsA9V5Y1gg&sfnsn=wa",
    "علم البيانات": " https://drive.google.com/drive/folders/1h1-DrQOZffAFGUN5hN9VmuTHPRvVqoBm?usp=drive_link ",
    "الذكاء الاصطناعي": "https://drive.google.com/drive/folders/1y-7mt41MXOFnus3xgCfmJIobSs4Fsquf",
    "التكنولوجيا المالية": " https://drive.google.com/drive/folders/1VX8YHaYOB0dRMJxjmv--IX_pdsU0aQdW?usp=drive_link ",
    "مالية الشركات": " https://drive.google.com/drive/folders/1OJUitWdXcSrv28nIPDKByfJPKO7HCbgZ?usp=drive_link ",
    "خدمات إلكترونية": " https://drive.google.com/drive/folders/1M4qE0ALcqBIXkLjOztxIu4K4lsS2pgkK?usp=drive_link ",
    "نماذج الأعمال": "https://drive.google.com/drive/folders/12OSSs2I9Jq4hWSBZfWF_YKM-1jVk89pN  ",
    "التشريعات التقنية": "https://drive.google.com/drive/folders/1ZoTWOVAIFEsTVGul0jkbpvL6gSTjigiN  ",
    "إدارة البنوك": " https://drive.google.com/drive/folders/1pDg72uD19upfhrd2PAByTsB7NCbqzDMo?usp=drive_link ",
    "أسواق": "  https://drive.google.com/drive/folders/1h0boRE5GCPnE3ulhXWjXUj2bD2GT2OAe?usp=drive_link ",
    "إدارة مالية": "رابط_هنا",
    "تمثيل مرئي": "رابط_هنا",
    "إدارة التحول التقني": "رابط_هنا",
    "نظم المعلومات المالية": "رابط_هنا",
    "التحليل المالي": "رابط_هنا",
    "البلوكشين": "رابط_هنا",
    "إدارة المخاطر": "رابط_هنا",
    "النمذجة المالية": "رابط_هنا",
    "محاسبة (1)": "  https://drive.google.com/drive/folders/1mly1ZljDmyyKTaF292xH1syhw9jEV730 ",
    "إدارة (1)": " https://drive.google.com/drive/folders/1hr6AvokLq0x6xVDQZ2qpiWqp3WDlsfFx  ",
    "مالية (1)": " https://drive.google.com/drive/folders/1qhr-j69bVVycTETxzWNbS4LWAXO4LEW5?usp=drive_link ",
    "رياضي": "https://drive.google.com/drive/folders/1GDbnT9ivUHybamQDB_WUSn9MtuD0vVTi?usp=drive_link  ",
    "الإدارة العامة": "رابط_هنا",
    "جزئي": "https://drive.google.com/drive/folders/15f2DKSK70etQASlF4hkngYQ5BV3DFmiN ",
    "التسويق (1)": "رابط_هنا",
    "إحصاء": "رابط_هنا"
}

subjects = list(links.keys())

@bot.message_handler(commands=["start"])
def start(message):
    keyboard = types.InlineKeyboardMarkup()

    for i, subject in enumerate(subjects):
        keyboard.add(
            types.InlineKeyboardButton(
                text=subject,
                callback_data=str(i)
            )
        )

    bot.send_message(
        message.chat.id,
        "📚 أهلاً بك في بوت المواد.\n\nاختر المادة:",
        reply_markup=keyboard
    )


@bot.callback_query_handler(func=lambda call: True)
def callback(call):
    subject = subjects[int(call.data)]
    link = links[subject]

    bot.answer_callback_query(call.id)

    bot.send_message(
        call.message.chat.id,
        f"📖 {subject}\n\n🔗 {link}"
    )

 
print("Bot is running...")

bot.infinity_polling(skip_pending=True)
