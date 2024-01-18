'''if message.text.lower() == 'Текст'
бот читает любой шрифт сообщения
bot.reply_to(message, {})
ответ на сообщение
@bot.message_handler(content_types = ['photo'])
бот будет реагировать на фото
bot.send_message(message.chat.id, 'Ожидаем ответа оператора', parse_mode = 'html')
3й параметр позволяет воспользоваться (в данном случае) html, форматировать текст
<b>  </b>
жирный текст
<em>  </em>
курсив
<u>  </u>
подчеркнуть'''
