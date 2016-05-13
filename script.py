from logipy import logi_led
from time import sleep
from feedparser import parse
import urllib2

class Blinker:
    
    def __init__(self,username,password,R,G,B):
        self.username = username
        self.password = password
        self.R = int(R > 0)*100
        self.G = int(G > 0)*100
        self.B = int(B > 0)*100


    def count_unread_msgs(self):
        auth_handler = urllib2.HTTPBasicAuthHandler()

        auth_handler.add_password(
        realm='mail.google.com',
        uri='https://mail.google.com',
        user='%s@gmail.com' % self.username,
        passwd= self.password
        )

        opener = urllib2.build_opener(auth_handler)
        urllib2.install_opener(opener)
        try:
            feed = urllib2.urlopen('https://mail.google.com/mail/feed/atom/important')
        except:
            print "Cannot connect to Atom feed"
            return 0
            
        parsed = parse(feed.read())
        return parsed.feed.fullcount


    def blink(self):
        count = self.count_unread_msgs()
        print count
        if int(count) > 0:
             logi_led.logi_led_flash_lighting(self.R,self.G,self.B,800*int(count),100)
             sleep(int(count))

        logi_led.logi_led_set_lighting(0,100,0)



logi_led.logi_led_init()
logi_led.logi_led_save_current_lighting()

Accounts = []

Accounts.append(Blinker('username_account1','password_account1',0,1,1))
Accounts.append(Blinker('username_account2','password_account2',1,1,0))

while True:
    for act in Accounts:
        act.blink()
    sleep(5)



