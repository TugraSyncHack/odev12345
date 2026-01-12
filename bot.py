#Bu kısım Handler // Bot.py tuğra tarafından logic.py yapay zekadan yardım alınmıştır
@bot.message_handler(commands=['my_score'])
def get_my_score(message):
    m = DatabaseManager(DATABASE)
    prizes = [x[0] for x in m.get_winners_img(message.from_user.id)]
    paths = [f'img/{x}' if x in prizes else f'hidden_img/{x}' for x in os.listdir('img')]
    res = create_collage(paths)
    if res is not None:
        cv2.imwrite("c.png", res)
        with open("c.png", "rb") as f: bot.send_photo(message.chat.id, f)
        os.remove("c.png")
    else:
        bot.reply_to(message, "Veri yok.")
