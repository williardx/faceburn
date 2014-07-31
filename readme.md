Faceburn
========

### Setup

Uses Python 2.7.

#### Developer-friendly Instructions

After cloning the repo, set up your virtual environment: `virtualenv venv`. Activate it with `source venv/bin/activate`.

Install the package requirements: `pip install -r requirements.txt`.

Download Chromedriver (https://code.google.com/p/selenium/wiki/ChromeDriver) and save it to the Faceburn working directory. Add the Faceburn working directory to your path.

Change the permissions on `faceburn.py` so that you can run it: `chmod u+x faceburn.py`

Fill in your details in `config.py`.

Finally, test out the script by running it with the test flag: `./faceburn.py --test`. If the script is working correctly, it will open up a Chrome window, log into Facebook, navigate to your news feed, and then send you a text message whenever someone says the word "I" in a post. You should get a bunch of text messages!

Once you're satisfied it works, let the script run on autopilot: `./faceburn.py`. 