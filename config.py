import logging

logger = logging.basicConfig(
    level=logging.INFO,
    filename='errors.log',
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)