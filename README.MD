# ESPN Fantasy Football Roster Driver

Roster Driver uses Selenium Webdriver to make changes to your ESPN fantasy football team. Using the requests library to gather data from borischen.co, your starting lineup can be set automatically with the best ranked players for each week. Waiver wire targets can also be identified by cross referencing the available free agents in your league with the tiers of players at borischen.co




## Usage

Each RosterDriver is tied to its own webdriver (using chrome driver). When you create an RosterDriver object, a list containing each player is created and filled from ESPN. Be sure to call quit_driver() when you are done using the RosterDriver object. 

The url variable should be set to the url that you reach when clicking My Team on your ESPN fantasy football page. If your league is public, leave the cookies list as is. Otherwise, fill the list with your cookies (which you can export from chrome). 

### Creating a RosterDriver object

```python3
>>> from roster_driver import RosterDriver
>>> url = 'http://games.espn.com/ffl/clubhouse?leagueId=1234567&teamId=10&seasonId=2016'
>>> cookies = []
>>> d = RosterDriver(url, cookies)
>>> d
Andrew Luck
Dion Lewis
Robert Kelley
Mike Evans
Alshon Jeffery
Jordan Reed
Tyrell Williams
Dolphins D
Dan Bailey
Jonathan Stewart
Theo Riddick
Antonio Brown
Spencer Ware
Marcus Mariota
Jeremy Hill
Bengals D
```

### Setting lineup automatically

```python3
>>> from roster_driver import RosterDriver
>>> url = 'http://games.espn.com/ffl/clubhouse?leagueId=1234567&teamId=10&seasonId=2016'
>>> cookies = []
>>> d = RosterDriver(url, cookies)
>>> d.tiered_update()
[{'slot_id': 'QB', 'tier': 2, 'name': 'Andrew Luck'}, {'slot_id': 'RB', 'tier': 5, 'name': 'Dion Lewis'}, {'slot_id': 'RB', 'tier': 2, 'name': 'Robert Kelley'}, {'slot_id': 'WR', 'tier': 1, 'name': 'Mike Evans'}, {'slot_id': 'WR', 'tier': 4, 'name': 'Alshon Jeffery'}, {'slot_id': 'TE', 'tier': 4, 'name': 'Jordan Reed'}, {'slot_id': 'WR', 'tier': 4, 'name': 'Tyrell Williams'}, {'slot_id': 'DST', 'tier': 15, 'name': 'Dolphins D'}, {'slot_id': 'K', 'tier': 4, 'name': 'Dan Bailey'}, {'slot_id': 'RB', 'tier': 7, 'name': 'Jonathan Stewart'}, {'slot_id': 'RB', 'tier': 15, 'name': 'Theo Riddick'}, {'slot_id': 'WR', 'tier': 15, 'name': 'Antonio Brown'}, {'slot_id': 'RB', 'tier': 15, 'name': 'Spencer Ware'}, {'slot_id': 'QB', 'tier': 15, 'name': 'Marcus Mariota'}, {'slot_id': 'RB', 'tier': 15, 'name': 'Jeremy Hill'}, {'slot_id': 'DST', 'tier': 15, 'name': 'Bengals D'}]
```

### Fetching waiver targets

```python3
>>> from roster_driver import RosterDriver
>>> url = 'http://games.espn.com/ffl/clubhouse?leagueId=1234567&teamId=10&seasonId=2016'
>>> cookies = []
>>> d = RosterDriver(url, cookies)
>>> d.fetch_waiver_targets()
[{'name': 'DeAngelo Williams', 'tier': 3, 'slot_id': 'RB'}, {'name': 'Adam Thielen', 'tier': 3, 'slot_id': 'WR'}, {'name': 'Rex Burkhead', 'tier': 3, 'slot_id': 'RB'}, {'name': 'Jacquizz Rodgers', 'tier': 3, 'slot_id': 'RB'}, {'name': 'Charles Clay', 'tier': 3, 'slot_id': 'TE'}, {'name': 'Cameron Meredith', 'tier': 2, 'slot_id': 'WR'}, {'name': 'Dustin Hopkins', 'tier': 2, 'slot_id': 'K'}, {'name': 'Eric Ebron', 'tier': 2, 'slot_id': 'TE'}, {'name': 'Alfred Blue', 'tier': 3, 'slot_id': 'RB'}, {'name': 'DeSean Jackson', 'tier': 3, 'slot_id': 'WR'}]
```

### Swapping starter and bench players

```python3
>>> from roster_driver import RosterDriver
>>> url = 'http://games.espn.com/ffl/clubhouse?leagueId=1234567&teamId=10&seasonId=2016'
>>> cookies = []
>>> d = RosterDriver(url, cookies)
>>> d.swap_players(0,13)
A. Luck to BE, M. Mariota to QB
```