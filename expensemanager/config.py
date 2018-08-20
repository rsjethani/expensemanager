from pathlib import Path
import json

_DEFAULT_PROG_NAME = "expensemanager"

_DEFAULT_CONFIG_DIR = Path.home() / ("." + _DEFAULT_PROG_NAME)

_DEFAULT_CONFIG_FILE = _DEFAULT_CONFIG_DIR / "config.json"

_DEFAULT_DATA_DRIVER = "json"

_config = {
    "prog_name": _DEFAULT_PROG_NAME,
    "config_dir": _DEFAULT_CONFIG_DIR,
    "config_file": _DEFAULT_CONFIG_FILE,
    "data_driver": _DEFAULT_DATA_DRIVER,
    "json": {
        "version": "0.0.1",
        "indent": 2,
        "data_dir": _DEFAULT_CONFIG_DIR / "data" 
    }
}

try:
    with _config["config_file"].open() as f:
        props_from_file = json.load(f)
    _config.update(props_from_file)
except Exception as e:
    SystemExit("Error in reading config file({}): {}".format(str(_config["config_file"]), e))


Config = type("Config", (object,), _config)
