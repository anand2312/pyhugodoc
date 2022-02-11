import logging

from pyhugodoc import handler


log = logging.getLogger(__name__)


if __name__ == "__main__":
    log.info("Starting pyhugodoc")
    handler._transform_reference_files()
    log.info("Completed! 🚀")
