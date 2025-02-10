from collecting_routine import *

if __name__ == "__main__":
    logging.basicConfig(level = logging.INFO, filename = ".\logs\logs.log", filemode = "w",
                        format = "%(asctime)s [%(levelname)s] %(message)s")
    logging.info("Launching the \"Collecting company ratings\" program.")
    
    collecting_routine()
    
    logging.info("Completion the \"Collecting company ratings\" program.")
