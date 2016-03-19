# coding:utf-8
import re, os
from glob import glob
from collections import OrderedDict
from configparser import ConfigParser, DuplicateOptionError, NoSectionError, NoOptionError


# Check config file and parse it
class ConfigLoader(ConfigParser):
    def __init__(self, config_path='config.ini'):
        super(ConfigLoader, self).__init__()
        self._load_config(config_path)

    # Rewrite optionxform from ConfigParser to make case sensitive
    def optionxform(self, optionstr):
        return optionstr

    def _load_config(self, config_path):
        if not os.path.exists(config_path):
            raise ConfigError(config_path + ' not exists!')
        try:
            self.read(config_path, encoding='utf-8')
        except DuplicateOptionError:
            raise ConfigError('Duplicate items exists in the config file!')

        self.config = OrderedDict()
        self._parse_button_config()

    def _parse_button_config(self):
        section = 'Button'
        if section not in self.sections():
            raise ConfigError('[Button] section not exists!')

        for option in self.options(section):
            raw_action = self.get(section, option).strip()
            action = None
            if raw_action.startswith('open'):
                temp = raw_action.split(maxsplit=2)
                action = temp if len(temp) == 2 else None
                action = self._check_path(action)

            elif raw_action.startswith('edit'):
                temp = re.search(r'(edit)\s+([\s\S]+)\s+from\s+([\s\S]+)\s+to\s+([\s\S]+)', raw_action)
                action = list(temp.groups()) if temp else None
                action = self._check_path(action)

            elif raw_action.startswith('cmd'):
                temp = re.search(r'(cmd)\s+([\s\S]+)', raw_action)
                action = list(temp.groups()) if temp else None

            if action:
                self.config[option] = action

    def _check_path(self, action):
        if not action:
            return None

        raw_path = action[1]
        path = self._parse_path(action[1])
        paths = glob(path)
        if paths:
            action[1] = paths[0]
            return action

        if raw_path == path:
            raise ConfigError('Path "{path}" not exists!'.format(path=path))
        else:
            raise ConfigError('Path "{raw_path}" -> "{path}" not exists!'.format(
                raw_path=action[1], path=path))

    def _parse_path(self, path):
        result = re.findall(r'(<(.+?)>)', path)
        if not result:
            return path

        for r in result:
            replaced = r[0]
            section, option = r[1].split(':', maxsplit=2)
            try:
                root = self.get(section, option)
                path = path.replace(replaced, root)
            except (NoSectionError, NoOptionError) as e:
                raise ConfigError('Config error in the config file! {}'.format(e))
        return path


# Config Exception
class ConfigError(Exception):
    def __init__(self, error):
        super(ConfigError, self).__init__(error)
        self.error = error

    def __str__(self):
        return self.error

    def __repr__(self):
        return repr(self.error)