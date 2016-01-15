# trans.rpy
# Сохраните файл под этим именем и положите в папку игры game
# Данный файл содержит список всех переведенных фраз "общего" режима Ren'Py.
init python:
 
    # Переводимые строки файла common/00developer.rpy
    config.translations[u"Developer Menu"] = u'Меню разработчика'
    config.translations[u"Return to the developer menu"] = u'Вернуться к меню разработчика'

    # Переводимые строки файла common/00library.rpy
    config.translations[u"Skip Mode"] = u'Режим Пропуска'
    config.translations[u"Fast Skip Mode"] = u'Быстрый Пропуск'
    config.translations[u"While Ren'Py games may be playable without the renpy module, some features may be disabled. For more information, read the module/README.txt file or go to http://www.bishoujo.us/renpy/."] = u"Игры Ren'Py могут запускаться и без модуля renpy, но некоторые функции возможно будут отключены. Более подробную информацию можно прочесть в файле module/README.txt или по адресу http://www.bishoujo.us/renpy/."
    config.translations[u"renpy module not found."] = u'не найден модуль renpy.'
    config.translations[u"The renpy module could not be loaded on your system."] = u'Не получается загрузить модуль renpy под вашей системой.'
    config.translations[u"Old renpy module found."] = u'Обнаружен устаревший модуль renpy.'
    config.translations[u"An old version (%d) of the Ren'Py module was found on your system, while this game requires version %d."] = u"Обнаружена устаревшая версия (%d) модуля Ren'Py. Игра требует версии старше %d."
    config.translations[u"Please click to continue."] = u'Для продолжения нажмите левую кнопку мыши.'

    # Переводимые строки файла common/00menus.rpy
    config.translations[u"Start Game"] = u'Новая игра'
    config.translations[u"Continue Game"] = u'Продолжить'
    config.translations[u"Preferences"] = u'Настройки'
    config.translations[u"Quit"] = u'Выйти'
    config.translations[u"Return"] = u'Вернуться'
    config.translations[u"Save Game"] = u'Сохранить'
    config.translations[u"Load Game"] = u'Загрузить'
    config.translations[u"Main Menu"] = u'Главное меню'
    config.translations[u"Are you sure you want to quit?"] = u'Вы уверены, что хотите выйти?'
    config.translations[u"Are you sure you want to return to the main menu?\nThis will lose unsaved progress."] = u'Вы уверены, что хотите перейти к главному меню?\nНе сохраненное прохождение будет утеряно.'

    # Переводимые строки файла common/_layout/one_column_preferences.rpym
    config.translations[u"Display"] = u'Режим экрана'
    config.translations[u"Transitions"] = u'Переходы'
    config.translations[u"Skip"] = u'Пропуск'
    config.translations[u"Begin Skipping"] = u'Начать пропуск...'
    config.translations[u"After Choices"] = u'После выбора'
    config.translations[u"Text Speed"] = u'Скорость текста'
    config.translations[u"Auto-Forward Time"] = u'Время автопрокрутки'
    config.translations[u"Music Volume"] = u'Громкость музыки'
    config.translations[u"Sound Volume"] = u'Громкость звуков'
    config.translations[u"Voice Volume"] = u'Громкость голоса'
    config.translations[u"Joystick..."] = u'Джойстик...'

    # Переводимые строки файла common/_layout/classic_yesno_prompt.rpym
    config.translations[u"Yes"] = u'Да'
    config.translations[u"No"] = u'Нет'

    # Переводимые строки файла common/_layout/scrolling_load_save.rpym
    config.translations[u"Empty Slot."] = u'Пустой слот.'
    config.translations[u"Are you sure you want to overwrite your save?"] = u'Вы уверены, что хотите перезаписать сохранение?'
    config.translations[u"Loading will lose unsaved progress.\nAre you sure you want to do this?"] = u'При загрузке несохраненное прохождение будет утеряно.\nТочно продолжить?'
    config.translations[u"q"] = u'в'
    config.translations[u"a"] = u'о'
    config.translations[u"Are you sure you want to delete this save?"] = u'Удалить это сохранение?'
    
    # Переводимые строки файла common/_layout/classic_joystick_preferences.rpym
    config.translations[u"Not Assigned"] = u'Не Незначено'
    config.translations[u"Joystick Mapping"] = u'Настройка Джойстика'
    config.translations[u"Left"] = u'Влево'
    config.translations[u"Right"] = u'Вправо'
    config.translations[u"Up"] = u'Вверх'
    config.translations[u"Down"] = u'Вниз'
    config.translations[u"Select/Dismiss"] = u'Выбрать/Отклонить'
    config.translations[u"Rollback"] = u'Вернуться'
    config.translations[u"Hold to Skip"] = u'Удерживать для пропуска'
    config.translations[u"Toggle Skip"] = u'Переключить пропуск'
    config.translations[u"Hide Text"] = u'Скрыть текст'
    config.translations[u"Menu"] = u'Меню'
    config.translations[u"Move the joystick or press a joystick button to create the mapping. Click the mouse to remove the mapping."] = u'Нажмите кнопку джойстика чтобы создать привязку к действию. Щелкните мышкой чтобы удалить привязку.'

    # Переводимые строки файла common/_layout/classic_preferences_common.rpym
    config.translations[u"Test"] = u'Тест'
    config.translations[u"Window"] = u'Окнонный'
    config.translations[u"Fullscreen"] = u'Полноэкранный'
    config.translations[u"All"] = u'Все'
    config.translations[u"Some"] = u'Некоторые'
    config.translations[u"None"] = u'Нет'
    config.translations[u"Seen Messages"] = u'Прочитанные'
    config.translations[u"All Messages"] = u'Все сообщения'
    config.translations[u"Stop Skipping"] = u'Прекратить пропуск'
    config.translations[u"Keep Skipping"] = u'Продолжить пропуск'

    # Переводимые строки файла common/_layout/classic_load_save.rpym
    config.translations[u"Auto"] = u'Автосейв'
    config.translations[u"Quick"] = u'Квиксейв'
    config.translations[u"Previous"] = u'<<'
    config.translations[u"Next"] = u'>>'

    #  Переводимые строки файла common/_compat/gamemenu.rpym
    config.translations[u"The error message was:"] = u'Сообщение об ошибке:'
    config.translations[u"You may want to try saving in a different slot, or playing for a while and trying again later."] = u'Попробуйте сохранить в другой слот или, немного поиграв, попробовать еще раз.'
    config.translations[u"Save Failed."] = u'Ошибка сохранения.'

    # Переводимые строки файла common/_compat/preferences.rpym
    config.translations[u"Joystick Configuration"] = u'Настройка джойстика'

    # Переводимые строки файла common/_compat/mainmenu.rpym
 
    config.translations[u"Continue Game"] = u'Продолжить игру'
