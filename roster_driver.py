from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from tiers import get_tier, get_slot

class RosterDriver(object):
    '''Creates a webdriver speficially for ESPN fantasy'''
    def __init__(self, url, cookies):
        self.url = url
        self.cookies = cookies
        self.driver = webdriver.Chrome()
        self.driver.get(url)
        for cookie in cookies:
            n = cookie
            c = {'name': n, 'value': cookies[n]}
            self.driver.add_cookie(c)
        self.driver.get(url)
        assert "Log In" not in self.driver.title
        self.roster = []
        self.fetch_roster()

    def __repr__(self):
        r = ''
        for p in self.roster:
            r += p['name'] + '\n'
        return r
        #return 'RosterDriver(%s)' % (self.url, )
        
    def fetch_roster(self):
        self.roster = self.fetch_players()
        
    def quit_driver(self):
        self.driver.quit()
    
    def fetch_players(self):
        players = []
        elements = self.driver.find_elements_by_class_name('playertablePlayerName')
        for player in elements:
            p = player.text.replace('ST D/', 'ST D')
            p = p.replace('/', ', ')
            name, info = p.split(',')
            slot = info.split(' ')
            tier = get_tier(get_slot(slot[2]), name)
            players.append({'name' : name, 'tier' : tier, 'slot_id': slot[2]})
        return players
            
    def fetch_waiver_wire(self):
        self.driver.find_element_by_xpath('//*[@id="games-tabs"]/li[3]/a').click()
        self.driver.find_element_by_xpath('//*[@id="playertable_0"]/tbody/tr[2]/td[15]/a').click()
        waivers = self.fetch_players()
        return waivers
        
    def fetch_waiver_targets(self):
        #tier of worst player at each slot (for RB WR and TE this is the flex)
        ros_tiers = {
            'QB': self.roster[0]['tier'],
            'RB': self.roster[5]['tier'],
            'WR': self.roster[5]['tier'],
            'TE': self.roster[5]['tier'],
            'DST': self.roster[7]['tier'],
            'K': self.roster[8]['tier']
        }
        targets = []
        waivers = self.fetch_waiver_wire()
        for p in waivers:
            if p['tier'] < ros_tiers[p['slot_id']]:
                targets.append(p)
        return targets
        
    def swap_players(self, s_slot, b_slot):
        '''swaps player in starting lineup with one on bench'''
        #build id attributes for move buttons
        id = 'pncEditSlot_'
        #flex ID is actually slot 15, which shifts the rest minus 1 
        if s_slot > 6: s_slot -=  1
        elif s_slot == 6: s_slot = 15
        s = id + str(s_slot)
        b = id + str(b_slot-1)
        self.driver.find_element_by_id(s).click()
        self.driver.find_element_by_id(b).click()
        
        
        try:
            print(self.driver.find_element_by_class_name('undoStackMove').text)
        except NoSuchElementException:
            print('no such element')
            self.driver.find_element_by_tag_name('body').send_keys(Keys.COMMAND + 'r')
            #self.driver.get(self.driver.getCurrentUrl())
            self.swap_players(s_slot, b_slot)
            
        #prints pending move, then submits it
        self.driver.find_element_by_id("pncSaveRoster0").click()
      
    def tiered_update(self):
        n = 9 #number of starters, used to split roster into starters and bench
        ros = self.roster
        starters = ros[:n]
        bench = ros[n:]
        for i, s in enumerate(starters):
            r = -1 #index of replacement player to be swapped into starting lineup
            t = s['tier'] #lowest tier for slot
            if s['tier'] > 1:
                for j, b in enumerate(bench):
                    if b['slot_id'] == s['slot_id'] and b['tier'] < t:
                        r = j
                        t = b['tier']
                if r > -1:
                    print(s, i, r+n)
                    self.swap_players(i, r+n)
                    starters[i], bench[r] = bench[r], starters[i]            
        return starters + bench    
