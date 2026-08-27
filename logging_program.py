import logging

logging.basicConfig(
    level = logging.INFO,
    format = "%(asctime)s %(levelname)s %(message)s"
)

def main():
    logging.info("Info message")
    logging.warning("Warning Message")
    logging.error("Error Message")  


if __name__ == "__main__":
    main()