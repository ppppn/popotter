import re
import os
from default_settings import DEFAULT_SETTINGS

SETTING_ITEMS = ('CONT_PRE', 'CONT_POST')
def LoadUsersData():
  path_to_userdata = os.environ.get('HOME') + '/.popotter.users'
  if os.path.isfile(path_to_userdata):
    raw_user_data = open(path_to_userdata)
    users_data = []
    for line in raw_user_data:
      line = line[:-1]
      users_data.append(line.split(','))
    return users_data
  return None

def LoadSettings():
  settings = DEFAULT_SETTINGS
  path_to_config = os.environ.get('HOME') + '/.popotter.config'
  if os.path.isfile(path_to_config):
    config_file = open(path_to_config)
    for line in config_file:
      line = line[:-1]
      itemname = line.split('=')[0]
      value = line.split('=')[1]
      settings[itemname] = value
  return settings

