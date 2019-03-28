import requests
import json
web_hook_url = 'https://hooks.slack.com/services/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'
msg = {'text':'from python and slack'}

requests.post(web_hook_url,data=json.dumps(msg))