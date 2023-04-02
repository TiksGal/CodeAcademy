import logging, logging.config

# set up logging
logging.config.fileConfig("logging.conf")
logger = logging.getLogger("sLogger")

# log something
logger.debug("debug message")
logger.info("info message")
logger.warning("warn message")
logger.error("error message")
logger.critical("critical message")
