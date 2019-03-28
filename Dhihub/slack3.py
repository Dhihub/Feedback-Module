import sys
from slacker import Slacker
slack = Slacker('xoxb-575060474148-585358061488-sKHNxUnHSwFO2qehLyEgWIZj')
message = "Hello Everyone"
slack.chat.post_message('#general',message)