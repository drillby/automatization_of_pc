import configparser
from configparser import ConfigParser
from os import PathLike


def parse_cfg_file(path: PathLike) -> ConfigParser:
    """Returns object for parsing configuration file

    Args:
        path (PathLike): path to the configuration file

    Returns:
        ConfigParser: ConfigParser object for parsing configuration file
    """
    config_parser = configparser.ConfigParser()
    config_parser.read(path)
    return config_parser
