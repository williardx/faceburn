#! ./venv/bin/python

import time
import config
import smtplib
import random
import string
from selenium import webdriver
from bs4 import BeautifulSoup

# setup
driver = webdriver.Chrome()
punctuation = set(string.punctuation)

def login_facebook():

    driver.get("http://www.facebook.com")

    form_email = driver.find_element_by_css_selector("#email")
    form_password = driver.find_element_by_css_selector("#pass")
    btn_login = driver.find_element_by_css_selector("#u_0_n")

    form_email.send_keys(config.facebook_email)
    form_password.send_keys(config.facebook_password)
    btn_login.click()

def simulate_activity():

    # pretend to scroll
    scroll_height = str(random.randint(100,1000))
    driver.execute_script("window.scrollTo(0, " + scroll_height + ");")
    time.sleep(3)
    driver.execute_script("window.scrollTo(0, 0);")

    # start a status update but then kill it
    textarea_status = driver.find_element_by_id("u_0_1o")
    message = "knock knock WHO'S THERE " * random.randint(1,5)
    textarea_status.send_keys(message)
    time.sleep(3)
    textarea_status.clear()

def is_ticket_mentioned(text):

    tickets = ["ticket", "tickets", "tix", "pass"]
    sell = ["sell", "selling", "give", "giving", "rid"]
    text = ''.join(ch for ch in text if ch not in punctuation)
    tokens = text.lower().split(" ")
    print tokens

    return "burning" in tokens \
           and "man" in tokens \
           and any(word in tokens for word in tickets) \
           and any(word in tokens for word in sell)

def test_mention(text):
    proc = ''.join(ch for ch in text if ch not in punctuation)
    print proc
    n = proc.lower().split(" ")
    return "i" in n

def notify(name):

    message = "%s might be talking about selling Burning Man tickets!" % name

    if config.carrier == "verizon":
        portal = "vtext.com"
    elif config.carrier == "att":
        portal = "txt.att.com"
    else:
        pass

    sms_email_address = config.phone_number + "@" + portal
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(config.gmail_email, config.gmail_password)
    server.sendmail(config.gmail_email, sms_email_address, message)

def parse_feed():
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(3)
    posts = driver.find_elements_by_css_selector(".userContentWrapper")
    for post in posts:
        soup = BeautifulSoup(post.get_attribute("innerHTML"))
        author_name = soup.select("span.fwb a")[0].getText()
        print author_name
        post_content = soup.select("div.userContent")[0]
        if post_content:
            post_text_nodes = post_content.select("p")
            post_text = [node.get_text() for node in post_text_nodes]
            if post_text:
                post_text_joined = " ".join(post_text)
                if is_ticket_mentioned(post_text_joined):
                    notify(author_name)


if __name__ == "__main__":

    login_facebook()
    time.sleep(10)

    while True:
        parse_feed()
        time.sleep(random.randint(10, 30))
        simulate_activity()
        time.sleep(random.randint(30, 60))
        driver.refresh()
        time.sleep(10) # wait for page to load