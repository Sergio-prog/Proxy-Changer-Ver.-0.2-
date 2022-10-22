import logging
import datetime
import os


def get_name():
    time = datetime.datetime.now().time().strftime("%X").replace(":", "-")
    name_file = "log_{}".format(time) + ".txt"
    return name_file


logs = logging.getLogger("Log")
logs.setLevel(logging.DEBUG)

name_file = r"logs/{}".format(get_name())
if not os.path.exists("logs"):
    os.mkdir("logs")

formatter = logging.Formatter("""{%(asctime)s} [%(name)s:%(levelname)s] [%(filename)s <%(lineno)s>: %(message)s""")
handler = logging.FileHandler(name_file, "a+", 'utf-8')
handler.setFormatter(formatter)

logs.addHandler(handler)


def log(message, mode, *args):
    global logs
    if mode == 'info':
        logs.info(message, *args)
    elif mode == 'warn':
        logs.warning(message, *args)
    elif mode == 'error':
        logs.error(message, *args)
    elif mode == 'debug':
        logs.debug(message, *args)
    elif mode == 'critical':
        logs.critical(message, *args)
    elif mode == 'exception':
        logs.exception(message, *args)
