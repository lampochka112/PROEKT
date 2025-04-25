from loguru import logger

logger.add("debug.log", rotation="10 MB", level="DEBUG")