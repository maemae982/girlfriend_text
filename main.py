import time
import random
import schedule
import subprocess
import utils


def send_message():
    subprocess.call("osascript message.applescript '%s' '%s'" % (f'{6154187890}', f'{random.choice(cheese)}'), shell=True)


if __name__ == '__main__':
    schedule.every().day.at(2:00).do(send_message)

    while True:
        schedule.run_pending()
        time.sleep(1)
