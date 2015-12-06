import re
import os

def LoadUserData():
	path_to_userdata = os.environ.get('HOME') + '/.popotter.user'
	if os.path.exists(path_to_userdata):
		userdata = open(path_to_userdata)

		user_data = []

		i = 0

		for line in user_data:
			rawdata = re.sub('\n', '', line)
			current_data = re.split(',',line)
			user_data.append(current_data)

		return user_data
	else:
		return False

def LoadSettings():
  path_to_config = os.environ.get('HOME') + '/.popotter.config'
  DEFAULT_SETTINGS = {'default-id': 0, 'time-diff': 9}
  settings = DEFAULT_SETTINGS
  if os.path.exists(path_to_config):
    config_file = open(path_to_config)
    for line in config_file:
      line = re.sub('\n', '', line)
      for current_item in DEFAULT_SETTINGS:
        if re.search(current_item + '=', line):
          settings[current_item] = re.sub(current_item + '=', '', line)
  return settings
