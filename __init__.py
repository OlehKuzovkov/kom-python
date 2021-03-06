import os
import json

if os.environ.get("KOM_CONFIG_STRING"):
    env_file_content = json.loads(os.environ.get("KOM_CONFIG_STRING"))
else:
    config_file = 'kom_framework/src/resources/.kom.config.json'
    env_file_content = json.load(open(os.path.abspath(config_file)))

js_waiter_file = 'kom_framework/src/resources/.http.waiter.js'
