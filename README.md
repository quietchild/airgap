# Airgap keylogger

A simple keylogger that can bridge an airgapped-system over near-ultrasonic frequencies.

It uses the audio channel to transmit data over inaudible soundwaves, hence the target machine only require to have a speaker.  

This project was only made for educational purpose and to show a demonstration of how an airgap attack works on an acoustic channel. 

## Setup

Install dependencies on both computers.

```
pip3 install chirpsdk pynput 
apt install python3-dev python3-setuptools portaudio19-dev libffi-dev libsndfile1
```

Create ~/.chirprc file with your app key, secret and config on both computers.
You can get these from [developers.chirp.io](http://developers.chirp.io)

```
# ~/.chirprc
app_key = xXxXXxxxXXXxxXXXxXxXXxXxx
app_secret = xxXxXXXxXxxXXXxXXXXxXxXxxxXxxxXXxXxXxxxXXxXxXXxXxX
app_config = XxXXXXxXxXxxxXxxxXXxXxXxxxXXxXxXXxXxXxxXxXXxxxXXXxxXxx
```

## Usage

* Place the keylog.py in the Victim machine and run it. 
* Start the listner on the Attacker machine and enjoy.
