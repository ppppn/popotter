import re
import os
from default_settings import DEFAULT_SETTINGS

SETTING_ITEMS = ('CONT_PRE', 'CONT_POST')
def LoadUsersData():
  path_to_usersdata = os.environ.get('HOME') + '/.popotter.users'
  if os.path.isfile(path_to_usersdata):
    raw_users_data = open(path_to_usersdata)
    users_data = []
    for line in raw_users_data:
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
      line = re.sub('#.*', '', line)
      if re.search('=', line):
        itemname = line.split('=')[0]
        itemname = re.sub(' ', '', itemname)
        value = line.split('=')[1]
        value = re.sub('.*?"', '', value, count=1)
        value = re.sub('".*', '', value, count=1)
        settings[itemname] = value
  return settings

