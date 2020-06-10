#!/usr/bin/env python3
import argparse
import sys
import time

from chirpsdk import ChirpSDK, CallbackSet, CHIRP_SDK_STATE

print ("Starting up...\n")
time.sleep(0.5)
print ("There you go. \n\n")

class Callbacks(CallbackSet):

    def on_received(self, payload, channel):
        """
        Called when an entire chirp has been received.
        Note: A payload of None indicates a failed decode.
        """
        if payload is None:
            print('Decode failed!')
        else:
            print(payload.decode("utf-8"))
            with open("log.txt", 'a') as f:
                f.write(payload.decode("utf-8"))


def main():

    # Initialise Chirp SDK
    sdk = ChirpSDK()

    # Set callback functions
    sdk.set_callbacks(Callbacks())

    sdk.start()

    try:
        # Process audio streams
        while True:
            time.sleep(0.1)
    except KeyboardInterrupt:
        print('Exiting')

    sdk.stop()


if __name__ == '__main__':
    main()
