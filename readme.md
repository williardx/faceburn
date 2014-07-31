Faceburn
========

### Setup

Uses Python 2.7.

#### (Developer) Friendly Instructions

After cloning the repo, set up your virtual environment: `virtualenv venv`. Activate it with `source venv/bin/activate`. Make sure you have pip installed!

Run `setup.sh`, which installs required packages with pip, changes file permissions, and adds the working directory to your path.

Download Chromedriver (https://code.google.com/p/selenium/wiki/ChromeDriver) and save it to the Faceburn working directory.

Fill in your details in `config.py`.

Finally, test out the script by running it with the test flag: `./faceburn.py --test`. If the script is working correctly, it will open up a Chrome window, log into Facebook, navigate to your news feed, and then send you a text message whenever someone says the word "I" in a post. You should get a bunch of text messages!

Once you're satisfied it works, let the script run on autopilot: `./faceburn.py`. 

#### Friendlier Instructions

Instructions for non-developer users. This assumes you've never touched Python or the terminal and that you have a Mac. (Linux will be pretty much the same, but you probably know what you're doing if you have Linux.)

Open a terminal. (Search for "terminal" in Spotlight.) Download the zip archive of the repository, `faceburn-master.zip` and save it wherever you like. Assuming you downloaded it to `~/Downloads`, navigate to that directory with `cd ~/Downloads` and Unzip the archive using `unzip faceburn-master.zip`.

You should have Python installed by default on a Mac. Check the version with `python -V`. If it's not at least 2.7, download Python 2.7 (or above -- but not 3!)

Next we'll install pip, a Python package manager. You'll use it to get libraries that help Faceburn run. Run `sudo easy_install pip`. You'll likely need your password.

Once pip is installed, install virtualenv, a library that creates an isolated environment for you to run Faceburn. Run `sudo pip install virtualenv`. Once that's installed, go into the Faceburn directory (`cd faceburn-master`), create a new virtual environment with `virtualenv venv`. Run `source venv/bin/activate` to use the environment. If it's working, your terminal prompt should have `(venv)` in front of it.

Inside `faceburn-master`, run `chmod 744 setup.sh` and then `./setup.sh`. This will take care of some of the setup for you.

Download Chromedriver (https://code.google.com/p/selenium/wiki/ChromeDriver) and save it to the `faceburn-master` directory you created earlier. 

Next, add your information to `config.py` using nano, a lightweight text editor: run `nano config.py` and add your information in the object called `properties`. Add the information between the quotation marks for each property. It should look something like this in the end:

```
properties = {
	username: "foo@bar.com",
	password: "foofoofoo",
	...
}
```
Once you're done, exit it out of it with CTRL+X, hit y to save, and then hit enter.

At this point, everything should be ready to go. Run `./faceburn.py --test` to test the script. If it works, it will open up a Chrome window, log into Facebook, navigate to your news feed, and then send you a text message whenever someone says the word "I" in a post. You should get a bunch of text messages! Stop the script by pushing CTRL+C.

Once you know everything is working, run `./faceburn.py` and let the script run. Keep both the Chrome window and terminal window open, otherwise you will stop the script. Enjoy!

### Use Notes

Stop the script with CTRL+C. If you close the terminal and reopen it, you'll need to reenter the virtual environment to properly run the script: go into the `faceburn-master` working directory, run `source venv/bin/activate`, and then finally the script: `./faceburn.py`.