from whatsapp_chatbot_python import GreenAPIBot, Notification

bot = GreenAPIBot("1103153681", "31cc0e3fcf32454a8b64d489ba4b84c84ff45824bb9f4b2ba6", debug_mode=True,
                  bot_debug_mode=True)


@bot.router.message(
    text_message=['заселился', 'Заселился', 'мы заселились', 'Мы заселились', 'заселилась', 'я заселился',
                  'я заселилась', 'заехал', 'Я на месте', 'Мы на месте', 'мы на месте', 'я внутри', 'Я внутри',
                  'мы внутри', 'Мы внутри', 'я в квартире', 'Я в квартире', 'мы в квартире', 'Мы в квартире',
                  'я зашел в квартиру', 'Я зашел в квартиру', 'мы зашли в квартиру',
                  'заехала', 'заехали', 'Заехали', 'Заселились все ок',
                  'я зашла', 'Я зашла', 'я зашел', 'Я зашел', 'мы зашли', 'Мы зашли', 'я на месте', 'Заселились все ок',
                  'Заселился . Спасибо', 'Заселился. Спасибо', 'Заселились. Спасибо', 'Мы заселились. Спасибо.',
                  'Мы заселились , все хорошо', 'Засалилась', 'мы засалилась', 'Мы засалилась', 'Заселился. Спасибо',
                  'Заселился', 'мы заехали', 'Заселились, все ок', 'Заселились , все ок', 'я заехал', 'я заехала',
                  'Мы заселились', 'Заселился', 'Заселилась', 'Я заселился', 'зашли', 'Зашли', 'зашел', 'зашла',
                  'Зашел', 'Зашла', 'Я заселилась', 'Заехал', 'Заехала', 'Заехали', 'Мы зашли в квартиру',
                  'я зашла в квартиру', 'Я зашла в квартиру', 'мы заселились. Спасибо', 'Мы заселились. Спасибо',
                  'я заселился. Спасибо', 'я заселилась. Спасибо', 'я заселилась. спасибо',
                  'Мы заехали', 'Я заехал', 'Я заехала', 'заселился.',
                  'Заселился.', 'мы заселились.', 'Мы заселились.', 'заселилась.', 'я заселился', 'я заселилась.',
                  'заехал.', 'Я на месте.',
                  'Мы на месте.', 'мы на месте.', 'я внутри.', 'Я внутри.', 'мы внутри.', 'Мы внутри.', 'я в квартире.',
                  'Я в квартире.', 'мы в квартире.', 'Мы в квартире.', 'я зашел в квартиру.',
                  'Я зашел в квартиру.', 'мы зашли в квартиру.', 'заехала.', 'заехали.', 'Заехали.',
                  'Заселились все ок.', 'я зашла.', 'Я зашла.', 'я зашел.', 'Я зашел.', 'мы зашли.', 'Мы зашли.',
                  'я на  месте.', 'Заселились все ок.',
                  'Заселился. Спасибо.', 'Заселился. Спасибо.', 'Заселились. Спасибо.', 'Мы заселились. Спасибо.',
                  'Мы заселились , все хорошо.', 'Засалилась.', 'мы засалилась.', 'Мы засалилась.',
                  'Заселился. Спасибо.', 'Заселился.', 'мы заехали.',
                  'Заселились, все ок.', 'Заселились , все ок.', 'я заехал.', 'я заехала.', 'Мы заселились.',
                  'Заселился.', 'Заселилась.', 'Я заселился.', 'зашли.', 'Зашли.', 'зашел.',
                  'зашла.', 'Зашел.', 'Зашла.', 'Я заселилась.', 'Заехал.', 'Заехала.', 'Заехали.',
                  'Мы зашли в квартиру.', 'я зашла в квартиру.', 'Я заселился. Спасибо.', 'Заселился. Спасибо.',
                  'Я зашла в квартиру.', 'мы заселились. Спасибо.',
                  'Мы заселились. Спасибо.',
                  'я заселился. Спасибо.', 'я заселилась. Спасибо.', 'я заселилась. спасибо.', 'Мы заехали.',
                  'Я заехал.', 'Я заехала.', 'я внутри', 'Я внутри', 'Мы внутри', 'я внутри.', 'Я внутри.',
                  'Мы внутри.', 'Я заселился', 'Я заселился.', 'В квартиру заселился', 'Заселился', 'все я зашел',
                  'Все я зашел', 'все, я зашел', 'Все, я зашел', 'Открыл. Заселился.', 'Открыл. Заселился',
                  'Заселился. Все хорошо.', 'Заселился, все хорошо', 'Заселился. Все отлично',
                  'Заселился, все отлично', 'Все в порядке, заселился 🙂', 'Все я заселился', 'Все, я заселился',
                  'Все я заселилась', 'Все, я заселилась', 'Заселился. Спасибо!', 'Заселилась , все хорошо',
                  'Заселилась , все хорошо. Спасибо', 'Мы Заселились! Все хорошо!', 'Я заселилась! Все хорошо!',
                  'Я заселился! Все хорошо!', 'Все мы заселились', 'Все, мы заселились', 'Все я заселился',
                  'Все, я заселился', 'Все, я заселилась', 'Все, я заселилась', 'Я заселился. Спасибо', 'Мы заехали',
                  'Заехали, все ок!', 'Заселились', 'Заселился, всё хорошо 👍', 'Заселилась, спасибо',
                  'Зашли, все хорошо', 'зашли.', 'Заселись, все отлично', 'Заехал все хорошо 👌',
                  'Заселились, спасибо большое Вам',
                  'Все нормально, заселились', 'Все мы на месте', 'Спасибо, зашли.', 'Да заселились спасибо большое',
                  'Успешно', 'Только заселились', 'Мы заселились ,все хорошо', 'Я заселилась , спасибо',
                  'Я заселился, спасибо', 'Мы заселились , все ок', 'Я заселился, все ок',
                  'Заселились , все хорошо', 'Утро доброе я заселился все хорошо',
                  'Утро доброе я заселился, все хорошо',
                  'Заселился все отлично спасибо', 'Заселился, все отлично, спасибо',
                  'Заселилась, все отлично, спасибо',
                  'Заселились, все отлично, спасибо', 'Я зашёл спасибо', 'Я зашёл', 'Я зашла', 'Я зашла спасибо',
                  'мы заселились)', 'Мы заселились)', 'Мы зашли , все хорошо', 'Все хорошо , заселились',
                  'Мы на месте все хорошо', 'Заселились , все отлично 👍',
                  'Все заселился',
    'Все, заселился',
    'Все, заселилась',
    'Все заселилась',
    'Добрый вечер. Мы заселились',
    'Добрый день. Мы заселились',
    'Здравствуйте. Мы заселились',
    'Здравствуйте ещё раз. Мы заселились',
    'Доброе утро. Мы заселились',
    'Мы заселились, спасибо!',
    'Я заселился, спасибо!',
    'Я заселилась, спасибо!',
    'Заселились, спасибо!',
    'Заселилась, спасибо!',
    'Заселился, спасибо!'
                  ])
def message_handler(notification: Notification) -> None:
    notification.answer(
        "🙌 Четыре Сезона рада приветствовать Вас в нашей гостевой квартире.\n"
    "🛜 Пароль и Логин от Wi-Fi указан в правилах проживания в А4\n"
    "🛏️ Кровать застелена чистым постельным бельем\n"
    "‼️ Напоминаем про правила проживания: КУРЕНИЕ (в том числе и на балконе) и ШУМ запрещены\n"
    "🙏 Пожалуйста, относитесь бережно к имуществу в квартире\n"
    "☀️ Хорошего дня! Если что — мы на связи"
    )


@bot.router.message(text_message=['где пароль от вай фая', 'не могу найти пароль от вай фая', 'вай фай не работает',
                                  'не вижу пароль от вай фая', 'не вижу пароль от wifi', 'где у вас вай фай найти?',
                                  'Где пароль от вай фая', 'Не могу найти пароль от вай фая', 'вай фай не работает',
                                  'Не вижу пароль от вай фая', 'Не вижу пароль от wifi', 'Где у вас вай фай найти?',
                                  'где пароль от вай фая?', 'не могу найти пароль от вай фая', 'вай фай не работает?',
                                  'WiFi не работает',
                                  'не вижу пароль от вай фая', 'не вижу пароль от wifi', 'где у вас вай фай найти?',
                                  'Где пароль от вай фая?', 'Не могу найти пароль от вай фая',
                                  'Не вижу пароль от вай фая', 'Не вижу пароль от wifi', 'Где у вас вай фай найти?',
                                  'Подскажите где пароль от вай фая', 'Подскажите где пароль от вай фая ?',
                                  'Подскажите пожалуйста, где пароль от вай фая',
                                  'Не вижу какой пароль от wifi', 'Подскажите пожалуйста', 'где пароль от вай фая?'])
def message_handler(notification: Notification) -> None:
    notification.answer("Пароль от WiFi указан в правилах проживания в квартире")


@bot.router.message(
    text_message=['Не работает Телевизор', 'Не работает телевизор', 'Не работает тв', 'Не работает ТВ',
                  'Не работает Тв',
                  'Телевизор не работает', ' Тв не работает', 'телевизор не работает', ' тв не работает',
                  'Проблема с теликом',
                  'Не включается телевизор', 'Не могу включить телевизор', 'не могу включить телевизор',
                  'не работает телевизор',
                  'тв глючит', 'TV', 'ТВ', 'тв', 'Тв', 'Не работает телевизор', 'подскажите как с телевизором',
                  'телевизор',
                  'не работает Телевизор', 'Подскажите как с телевизором', 'Телевизор', 'Не работает Телевизор.',
                  'Не работает телевизор.',
                  'Не работает тв.', 'Не работает ТВ.', 'Не работает Тв.', 'Телевизор не работает.', ' Тв не работает.',
                  'телевизор не работает.',
                  'тв не работает.', 'Проблема с теликом.', 'Не включается телевизор.', 'Не могу включить телевизор.',
                  'не могу включить телевизор.',
                  'не работает телевизор.', 'тв глючит.', 'TV.', 'ТВ.', 'тв.', 'Тв.', 'Не работает телевизор.',
                  'подскажите как с телевизором.',
                  'телевизор. ', 'не работает Телевизор.', 'Подскажите как с телевизором.', 'Телевизор.',
                  'Тут телевизор не показывает. Что делать?',
                  'Тут телевизор не показывает. Подскажите что делать?',
                  'Тут телевизор не показывает. Подскажите что сделать?', 'Телевизор не показывает. Что делать?',
                  'Телевизор не показывает. Подскажите что делать?',
                  'Телевизор не показывает. Подскажите что сделать?'])
def message_handler(notification: Notification) -> None:
    notification.answer(
        "Если не работает ТВ необходимо:\nперезагрузить его (вытащить из розетки, подождать 15 секунд и вставить обратно, подождать еще 15 секунд).\nНапишите пожалуйста, помогло ли?")


@bot.router.message(
    text_message = [
    'Не работает вай фай', 'Где пароль от вай Фая', 'Где пароль от вай Фая?', 'Где пароль от вай фая',
    'Где пароль от вай фая?', 'Доброе утро. WiFi не работает. Что делать?',
    'Доброе день. WiFi не работает. Что делать?',
    'Доброе вечер. WiFi не работает. Что делать?', 'Здравствуйте. WiFi не работает. Что делать?',
    'Доброе утро. Вай фай не работает. Что делать?', 'Доброе день. Вай фай не работает. Что делать?',
    'Доброе вечер. Вай фай не работает. Что делать?', 'Где найти пароль от вай фая',
    'Где найти пароль от вай фая?',
    'Не работает WiFi', 'Не работает wifi', 'не могу подключиться к вай фаю',
    'не могу подключиться к wifi', 'не могу подключиться к WiFi',
    'не работает вай фай', 'не работает WiFi', 'не работает wifi', 'WiFi не работает. Что делать?',
    'Вай Фай не работает. Что делать?', 'Вай фай не работает. Что делать?',
    'Не могу подключиться к вай фаю', 'Не могу подключиться к wifi', 'Сети нет', 'сети нет', 'Вай Фай',
    'Вай фай', 'вай фай', 'Интернет', 'WiFi', 'wifi', 'Wi-Fi', 'Мне нужен вай Фай', 'мне нужен вай фай',
    'мне нужен WiFi', 'Мне нужен WiFi', 'Не могу подключиться к WiFi', 'В квартире не работает интернет',
    'в квартире не работает интернет',
    'Не работает интернет',
    'не работает интернет',
    'Добрый вечер, у нас пропал интернет',
    'Добрый день, у нас пропал интернет',
    'Доброе утро, у нас пропал интернет'
])
def message_handler(notification: Notification) -> None:
    notification.answer(
        "Если не работает WiFi необходимо:\nперезагрузить роутер (вытащить из розетки, подождать 15 секунд и вставить обратно, подождать еще 15 секунд).\nНапишите пожалуйста, помогло ли?")


@bot.router.message(
    text_message=[
        'Где найти инструкцию', 'Где посмотреть инструкцию', 'Где найти инструкцию?', 'Где посмотреть инструкцию?',
        'Какой адрес?', 'Какой адрескакой адрес?', 'какой адрес',
        'Где найти эту инструкцию', 'Где посмотреть эту инструкцию', 'Где найти этуинструкцию?',
        'Где посмотреть эту инструкцию?', 'Где найти инструкцию по заезду',
        'Где посмотреть инструкцию по заезду', 'Где найти инструкцию заезду?', 'Где посмотреть инструкцию заезду?',
        'Где найти инструкцию по заселению',
        'Где посмотреть инструкцию по заселению', 'Где найти инструкцию по заселению?',
        'Где посмотреть инструкцию заселению?',
        'Адрес, этаж, квартира?', 'Адрес, этаж, квартира?', 'Адрес, этаж, квартира', 'Адрес, этаж, квартира',
        'Я оплатил, что дельше', 'я оплатил, что дельше?',
        'я оплатил, что дельше', 'я оплатил, что дельше?', 'чеr прикрепил, что дальше?', 'Чек прикрепил, что дальше?',
        'чек прикрепил, что дальше', 'Чек прикрепил, что дальше'])
def message_handler(notification: Notification) -> None:
    notification.answer(
        "По той же ссылке, по которой вы проходили процедуру заселения, Вам направлена инструкция по заселению в файле\n«НЕОБХОДИМО ПОСМОТРЕТЬ ИНСТРУКЦИЮ»\nОзнакомьтесь пожалуйста 🙏\nКак заселитесь, напишите нам, пожалуйста")


@bot.router.message(
    text_message=[
        'Когда вернёте залог?', 'когда вернёте залог?', 'Когда вернётся залог?', 'когда вернётся залог?',
        'Когда вернут залог?', 'когда вернут залог?', 'Когда вернёте залог ?', 'когда вернёте залог ?',
        'Когда вернётся залог ?', 'когда вернётся залог ?', 'Когда вернут залог ?', 'когда вернут залог ?',
        'Когда вернете залог?', 'когда вернете залог?', 'Когда вернется залог?', 'когда вернется залог?',
        'Приняли квартиру?', 'Когда вернете залог ?', 'когда вернете залог ?', 'Когда вернется залог ?',
        'когда вернется залог ?', 'Что с залогом?', 'что с залогом?', 'Как с залогом?', 'как с залогом?',
        'Что там с залогом?', 'как по залогу?', 'Как по залогу?'
    ]
)
def deposit_query_handler(notification: Notification) -> None:
    notification.answer(
        "Залог вернём сегодня, в течение дня, после проверки квартиры. Пожалуйста, ожидайте)"
    )


bot.run_forever()
