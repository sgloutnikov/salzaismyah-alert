import smtplib
from email.mime.text import MIMEText
from bs4 import BeautifulSoup
import urllib.request
import unicodedata


# Watch For List
watchlist = []

# Month Url (
monthurl = "http://www.salzaismyah.bg/bg/playbill-calendar/2016-07"

# SMTP
toaddress = ['@gmail.com']
smtpserver = 'smtp.gmail.com:587'
user = '@gmail.com'
passwd = ''


def processpage():
    if len(watchlist) == 0:
        print("Define watchlist above, and re-run.")
        return
    count = 0
    html = urllib.request.urlopen(monthurl).read()
    soup = BeautifulSoup(html, "html.parser")

    links = soup.find_all('a', href=True)

    for link in links:
        for play in watchlist:
            if caseless_equal(str(link.text).strip(), play):
                # Found on page, send email
                print("Found: " + play)
                count += 1
                sendemail(play)
    return count


def sendemail(playname):
    # Construct message
    msg = MIMEText("A play you are watching for is now available. \n"
                   "Tickets/Info: " + monthurl)
    msg['Subject'] = "Available: " + playname
    msg['From'] = "Salza i Smyah Alert"

    # Send the mail
    server = smtplib.SMTP(smtpserver)
    server.starttls()
    server.login(user, passwd)
    server.sendmail('alert@salzaismyah.bg', toaddress, msg.as_string())
    server.quit()


# Safe way to compare unicode strings from: http://stackoverflow.com/a/29247821
def normalize_caseless(text):
    return unicodedata.normalize("NFKD", text.casefold())


def caseless_equal(left, right):
    return normalize_caseless(left) == normalize_caseless(right)


# Start me up...
c = processpage()
print("Finished. Found: " + str(c))
