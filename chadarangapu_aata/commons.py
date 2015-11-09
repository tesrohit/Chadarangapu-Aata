'''
This script should contain generic functions generally not related to game logic
All modules can use this scipt for performing such ommons tasks
'''
import os
import logging

_logger = logging.getLogger(__name__)

def configure_logging(curr_logger):
    '''
    This method configures logging for the root logger.
    Can be used for debugging
    :param curr_logger:
    :return:
    '''
    levels ={
        "ERROR":    logging.ERROR,
        "WARNING":  logging.WARNING,
        "WARN":     logging.WARNING,
        "INFO":     logging.INFO,
        "DEBUG":    logging.DEBUG
    }
    # Set the environment variable AATA_LOG_LEVEL to DEBUG to get debug logs
    log_level = levels.get(os.environ.get("AATA_LOG_LEVEL"), logging.INFO)

    curr_logger.setLevel(log_level)

    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.DEBUG)
    formatter = logging.Formatter('%(name)s - %(levelname)s - %(message)s')
    console_handler.setFormatter(formatter)

    curr_logger.addHandler(console_handler)

    _logger.debug("Logger started")