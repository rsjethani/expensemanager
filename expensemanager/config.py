
from pathlib import Path
import json

_PROG_NAME = "expensemanager"

_CONFIG_DIR = Path.home() / ("." + _PROG_NAME)

_CONFIG_FILE = _CONFIG_DIR / "config.json"

_STORAGE_LOCATION = "file_system"

_STORAGE_TYPE = "json"

_DATA_LOCATION = _CONFIG_DIR / "data"

_config = {
    "prog_name": _PROG_NAME,
    "config_dir": _CONFIG_DIR,
    "config_file": _CONFIG_FILE,
    "storage_location": _STORAGE_LOCATION,
    "storage_type": _STORAGE_TYPE,
    "data_location": _DATA_LOCATION
}



try:
    with _config["config_file"].open() as f:
        props_from_file = json.load(f)
    _config.update(props_from_file)
except Exception as e:
    SystemExit("Error reading from config file({}): {}".format(str(_config["config_file"]), e))


Config = type("Config", (object,), _config)
