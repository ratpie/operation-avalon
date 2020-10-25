import json
import subprocess
from os import path

mission_name = ''
mission_path = ''
build_options = None

with open(r'.\build.json') as settings_file:
    build_options = json.load(settings_file)

if build_options == None or len(build_options) == 0:
    print('You options file needs some work bud.')
    exit(1)

if build_options['mission-name'] == None:
    build_options['mission-name'] = ''

if build_options['mission-root'] == None:
    build_options['mission-root'] = ''

if build_options['mission-name'] == '':
    print('What is the name of your mission?')
    mission_name = input()
else:
    mission_name = build_options['mission-name']

if build_options['mission-root'] == '':
    print('What is the path where your missions are stored?')
    mission_root = input()
else:
    mission_root = build_options['mission-root']


mission_name = mission_name.replace('\\','')
if not mission_root.endswith('\\'):
    mission_root = mission_root + '\\'

full_path = path.join(mission_root,mission_name)

# Copy everything over except for stuff that we dont want
subprocess.call([r'xcopy','.\\',full_path,'/Y','/EXCLUDE:.buildignore'])

# Get the latest mission sqm
subprocess.call('xcopy',full_path + '.\\mission.sqm','.\\','/Y')



