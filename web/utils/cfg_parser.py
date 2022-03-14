import configparser
from os import PathLike


def return_cfg_file(path: PathLike):
    config_parser = configparser.ConfigParser()
    return config_parser.read(path)
