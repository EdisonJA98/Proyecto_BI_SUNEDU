import logging

def get_logger(name):
    """
    Retorna un logger configurado con formato estándar.
    """
    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)

    # Si ya tiene handlers, no los duplicamos
    if not logger.handlers:
        ch = logging.StreamHandler()
        ch.setLevel(logging.INFO)
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        ch.setFormatter(formatter)
        logger.addHandler(ch)

    return logger