from pycookiecheat import chrome_cookies 
from roster_driver import RosterDriver

#your URL here
url = 'http://games.espn.com/ffl/clubhouse?leagueId=1234567&teamId=10&seasonId=2016'
cookies = chrome_cookies(url)

d = RosterDriver(url, cookies)


for ros in d.roster:
    print(ros)
#d.tiered_update()
print()
w = d.fetch_waiver_targets()
for p in w:
    print(p)
d.quit_driver()