import logging

# logging.basicConfig(level=logging.DEBUG)
# logging.debug("debug")
# logging.info("info")
# logging.warning("warning")
# logging.error("error")
# logging.critical("critical")
#
# logging.basicConfig(level=logging.DEBUG)
# logging.debug("debug1")
# logging.info("info1")

logging.basicConfig(level=logging.DEBUG,
                    filename="logs.log",
                    filemode="w",
                    format="My log message: %(asctime)s - %(name)s - %(levelname)s - %(message)s")
# logging.debug("debug")
# logging.info("info")
try:
    print(5/0)
except ZeroDivisionError:
    logging.exception("ZeroDivisionError")
