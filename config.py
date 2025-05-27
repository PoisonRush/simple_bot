import logging as logger

logger.basicConfig(
    level=logger.INFO,
    filename='errors.log',
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)