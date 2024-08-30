import logging

# Configuring logging
logging.basicConfig(
    filename="app1.log",
    filemode="w",
    level=logging.DEBUG,
    # format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    # datefmt="%Y-%m-%d %H:%M:%S"
)