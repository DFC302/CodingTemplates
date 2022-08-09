#!/bin/usr/env python3

from discordwebhook import Discord
import argparse
import os
import sys

def sendNotification(message):
	webhook = options().web_hook
	discord = Discord(url=str(webhook))
	discord.post(content=message)

def options():
    parser = argparse.ArgumentParser()
    
    parser.add_argument(
      "--web-hook",
      help="Web hook to route proper notifications.",
      action="store"
    )

    if len(sys.argv[1:]) == 0:
    	print("Web hook is needed!")
    	parser.exit()

    args = parser.parse_args()
    return args

# 0 is file descriptor for input to program. 
# if 0 is not detected, then we know the input is not piped
if not os.isatty(0):
    for result in sys.stdin:
        result = result.strip("\n")

        sendNotification(result)
