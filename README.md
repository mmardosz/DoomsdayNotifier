# Doomsday Notifier #
_A simple EAS-like notifier that raises alarm whenever the President tweets. Created for fun of course._

Since Sean Spicer [announced](http://www.newsweek.com/trump-tweets-spicer-official-statements-621919) that presidential tweets should be treated as official White House announcements, it sounds like a great idea to to reuse an old Raspberry Pi collecting dust in a drawer. Because, nobody knows which tweet can spark a new chain of unexpected events, having an alert system similar to Emergency Announcement System (EAS) sound great.

![Raspberry Pi in action](https://mardosz.com/git/DoomsdayNotifier/DN_01.jpg)

**Bottomline:**
* **Problem**: How to keep up with presidential tweets at any time.
* **Solution**: Dust-off an old Raspberry Pi and write a simple Python script.
* **Action**: Python script that checks @readdonaldtrump for new tweets and uses Google Voice synthesis to read them out loud.

## Getting Started ##

### Prerequisites ### 

- Twitter API keys
- python-twitter
- gtts
- pygame
- Python 2.7

### Installing ### 

Installing Python dependencies

```
pip install -r requirements.txt
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

Clone project to local user directory (user pi):

```
git clone https://github.com/mmardosz/DoomsdayNotifier.git
```


## Running ##

### Changing audio output ### 

Change audio output to headphone jack. Go to ```sudo raspi-config``` and navigate to ```Advanced Options``` then ```Audio```.

### Increasing audio output volume ### 

Run following command:

```amixer set PCM -- 100%```

### Starting with each boot ### 

Make ```launcher.sh``` executable:

```
chmod 755 launcher.sh
```

Create logs directory for cron

```cd``` and then ```mkdir logs```

Add a crontab by ```sudo crontab -e``` and add following line:

```
@reboot sh /home/pi/DoomsdayNotifier/launcher.sh >/home/pi/logs/cronlog 2>&1
```

## Other ##

### Future improvements ### 

- Store in queue all recent tweets if tweet frequency is less than 15 seconds (API time limit)
- Remove Emojis from strings passed to gTTS.
- Replace EAS noise with Donald Trump's classic sound bites such as "Tremendous" or "China!" picked at random.

### License ###
This project is licensed under the MIT License - see the LICENSE.md file for details



