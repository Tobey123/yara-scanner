__author__ = "Moath Maharmeh"
__license__ = "GNU General Public License v2.0"
__version__ = "1.0"
__email__ = "moath@vegalayer.com"
__created__ = "4/Apr/2019"
__modified__ = "30/Mar/2020"
__status__ = "Production"
__project_page__ = "https://github.com/iomoath/yara-scanner"

import logging
from settings import debug_log_file_path
from settings import debug_log_enabled
from settings import log_file_path
from settings import date_time_format
import common_functions

logging.basicConfig(filename=debug_log_file_path,
                    level=logging.INFO,
                    format="%(asctime)s  %(levelname)-8s %(message)s",
                    datefmt=date_time_format)


def log_error(message, module_name):
    if not debug_log_enabled:
        return
    logging.error("({}): {}".format(module_name, message))


def log_debug(message, module_name):
    if not debug_log_enabled:
        return
    logging.debug("({}): {}".format(module_name, message))


def log_critical(message, module_name):
    if not debug_log_enabled:
        return
    logging.critical("({}): {}".format(module_name, message))


def log_warning(message, module_name):
    if not debug_log_enabled:
        return
    logging.warning("({}): {}".format(module_name, message))


def log_info(message, module_name):
    if not debug_log_enabled:
        return
    logging.info("({}): {}".format(module_name, message))


def log_incident(file_path, rules_matched, yara_rules_file_name):
    try:
        # Log format: [%time%] "%file_path%" "%rules_matched%" "yara_rules_file_name"
        log_row = "[{}] \"{}\" \"{}\" \"{}\"".format(common_functions.get_datetime(), file_path, rules_matched, yara_rules_file_name)

        with open(log_file_path, 'a+') as f:
            f.write(log_row)
            f.write("\n")
    except Exception as e:
        log_critical(e, "logger.py")