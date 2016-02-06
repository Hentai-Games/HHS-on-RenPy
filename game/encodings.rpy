init -50 python:
    import sys
    import codecs
    def setup_console(sys_enc="utf-8"):
        reload(sys)
        try:
            # для win32 вызываем системную библиотечную функцию
            if sys.platform.startswith("win"):
                    import ctypes
                    enc = "cp%d" % ctypes.windll.kernel32.GetOEMCP() #TODO: проверить на win64/python64
            else:
                    # для Linux всё, кажется, есть и так
                    enc = (sys.stdout.encoding if sys.stdout.isatty() else
                                    sys.stderr.encoding if sys.stderr.isatty() else
                                        sys.getfilesystemencoding() or sys_enc)
            # кодировка для sys
            sys.setdefaultencoding(sys_enc)
            # переопределяем стандартные потоки вывода, если они не перенаправлены
            if sys.stdout.isatty() and sys.stdout.encoding != enc:
                    sys.stdout = codecs.getwriter(enc)(sys.stdout, 'replace')
            if sys.stderr.isatty() and sys.stderr.encoding != enc:
                    sys.stderr = codecs.getwriter(enc)(sys.stderr, 'replace')
        except:
            pass # Ошибка? Всё равно какая - работаем по-старому...
    setup_console()