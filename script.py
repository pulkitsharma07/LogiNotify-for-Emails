from logipy import logi_led
from time import sleep
from feedparser import parse
import urllib2

def count_unread_msgs(user, passwd):
    auth_handler = urllib2.HTTPBasicAuthHandler()

    auth_handler.add_password(
    realm='mail.google.com',
    uri='https://mail.google.com',
    user='%s@gmail.com' % user,
    passwd= passwd
    )

    opener = urllib2.build_opener(auth_handler)
    urllib2.install_opener(opener)
    feed = urllib2.urlopen('https://mail.google.com/mail/feed/atom/%5Esmartlabel_personal')
    parsed = parse(feed.read())
    return parsed.feed.fullcount


logi_led.logi_led_init()
logi_led.logi_led_save_current_lighting()

while True:

    count = count_unread_msgs('username_account1','password_account1')   
    if int(count) > 0:
         logi_led.logi_led_flash_lighting(0,100,100,800*int(count),100)
         sleep(int(count))

    logi_led.logi_led_set_lighting(0,100,0)

    count = count_unread_msgs('username_account2','password_account2')
    if int(count) > 0:
        logi_led.logi_led_flash_lighting(100,100,0,800*int(count),100)
        sleep(int(count))

    logi_led.logi_led_set_lighting(0,100,0)
    sleep(5)
