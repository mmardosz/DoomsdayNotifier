# Doomsday Notifier #
_A simple EAS-like notifier that goes off whenever POTUS tweets. Created for fun of course._

![Raspberry Pi in action](https://mardosz.com/git/DoomsdayNotifier/DN_01.jpg)

**Bottomline:**
* **Problem**: How to keep up with presidential tweets.
* **Solution**: Dust-off an old Raspberry Pi and write a simple Python script.
* **Action**: Python script that checks @realdonaldtrump for new tweets and uses Google Voice synthesis to read them out loud.

## Getting Started ##

### Prerequisites ### 

- Twitter API keys
- python-twitter
- gtts
- pygame
- Python 2.7

### Installing ### 

Clone project to local user directory (user pi):

```
git clone https://github.com/mmardosz/DoomsdayNotifier.git
```

Installing Python dependencies

```
sudo pip install -r requirements.txt
```

or alternatively

```
pip install pygame
pip install python-twitter
pip install gtts
```

If there is an issue with gtts, use pip workaround:
```
sudo pip install requests==2.6.0
```

## Running ##

### Updating Twitter API keys

Replace 'x' with keys in notifier.py:

```
CONSUMER_KEY = 'x'
CONSUMER_SECRET = 'x'
ACCESS_TOKEN = 'x'
ACCESS_TOKEN_SECRET = 'x'
```

### Changing audio output ### 

Change audio output to headphone jack. Go to ```sudo raspi-config``` and navigate to ```Advanced Options``` then ```Audio```.

### Increasing audio output volume ### 

Run following command:

```amixer set PCM -- 100%```

## Other ##

### Future improvements ### 

- Store in queue all recent tweets if tweet frequency is less than 15 seconds (API time limit)
- Remove Emojis from strings passed to gTTS.
- Add cron

### License ###
This project is licensed under the MIT License - see the LICENSE.md file for details




