import requests

'''Numbers derived from eligibleSlotCategoryIds in JSON file'''
ppr_slots = {
    0: 'https://s3-us-west-1.amazonaws.com/fftiers/out/current/text_QB.txt',
    2: 'https://s3-us-west-1.amazonaws.com/fftiers/out/current/text_PPR-RB.txt',
    4: 'https://s3-us-west-1.amazonaws.com/fftiers/out/current/text_PPR-WR.txt',
    6: 'https://s3-us-west-1.amazonaws.com/fftiers/out/current/text_PPR-TE.txt',
    16: 'https://s3-us-west-1.amazonaws.com/fftiers/out/current/text_DST.txt',
    17: 'https://s3-us-west-1.amazonaws.com/fftiers/out/current/text_K.txt'
        }
positions = {
    'QB': 0,
    'RB': 2,
    'WR': 4,
    'TE': 6,
    'DST': 16,
    'K': 17
}
def get_tier(slot, name):
    r = requests.get(ppr_slots[slot])
    try:
        r.raise_for_status()
    except Exception as exc:
        print('There was a problem: %s' % (exc))
        
        
    tiers = r.text.splitlines()
    for i in range(len(tiers)):
        if name in tiers[i]:
            return i+1
    return 15

def get_slot(pos):
    return positions[pos]