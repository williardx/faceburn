Faceburn
========

### Setup

Uses Python 2.7.

#### Friendly Instructions

After cloning the repo, set up your virtual environment: `virtualenv venv`. Activate it with `source venv/bin/activate`.

Install the package requirements: `pip install -r requirements.txt`.

Download Chromedriver (https://code.google.com/p/selenium/wiki/ChromeDriver) and save it to the Faceburn working directory. Add the Faceburn working directory to your path.

Change the permissions on `faceburn.py` so that you can run it: `chmod u+x faceburn.py`

Fill in your details in `config.py`.

Finally, test out the script by running it with the test flag: `./faceburn.py --test`. If the script is working correctly, it will open up a Chrome window, log into Facebook, navigate to your news feed, and then send you a text message whenever someone says the word "I" in a post. You should get a bunch of text messages!

Once you're satisfied it works, let the script run on autopilot: `./faceburn.py`. 

#### Friendlier Instructions

Instructions for non-developer users. This assumes you've never touched Python and that you have a Mac. (Linux will do fine, but you probably know what you're doing in that case.)

Open a terminal. (Search for "terminal" in Spotlight.) Download the zip archive of the repository, `faceburn-master.zip` and save it wherever you like. Assuming you downloaded it to `~/Downloads`, navigate to that directory with `cd ~/Downloads` and Unzip the archive using `unzip faceburn-master.zip`.

You should have Python installed by default on a Mac. Check the version with `python -V`. If it's not at least 2.7, download Python 2.7 (or above -- but not 3!)

Install pip, a Python package manager. You'll use it to get libraries that help Faceburn run. Run `sudo easy_install pip`. You'll likely need your password.

Once pip is installed, install virtualenv, a library that creates an isolated environment for you to run Faceburn. `sudo pip install virtualenv`. Once that's installed go into the Faceburn directory (`cd faceburn-master`), create a new virtual environment with `virtualenv venv`. Run `source venv/bin/activate` to use the environment.

Now, install all the packages we need: `pip install -r requirements.txt`.

Download Chromedriver (https://code.google.com/p/selenium/wiki/ChromeDriver) and save it to the `faceburn-master` directory you created earlier. Next, we'll add faceburn-master to your system's path so that it can find it: first, from inside of `faceburn-master` run `pwd` to get the full path of where you are. (The right path will end in `faceburn-master`.) Copy the output of that command and run this command: `echo "export PATH=YOUR_PATH_HERE:$PATH" >> ~/.bash_profile`. If you get an error about the file not existing, run `touch ~/.bash_profile` and then try again. Verify that `faceburn-master` is in your path by running `echo $PATH` -- you should see it in there. If successful, run `source ~/.bash_profile`.

The main script is called `faceburn.py`. Change the permissions on `faceburn.py` so that you can run it: `chmod u+x faceburn.py`. Next, add your information to `config.py`: run `nano config.py` and add your information in the object called `properties`. Nano is a lightweight text editor that works mostly as it looks. Add the information between the quotation marks for each property. It should look something like this in the end:

```
properties = {
	username: "foo@bar.com",
	password: "foofoofoo",
	...
}
```
Once you're done, exit it out of it with CTRL+X, hit `y` to save, and then hit enter.

At this point, everything should be ready to go. Run `./faceburn.py --test` to test the script. If it works, it will open up a Chrome window, log into Facebook, navigate to your news feed, and then send you a text message whenever someone says the word "I" in a post. You should get a bunch of text messages! Stop the script by pushing CTRL+C.

Once you know everything is working, run `./faceburn.py` and let the script run. Keep both the Chrome window and terminal window open, otherwise you will stop the script. Enjoy!