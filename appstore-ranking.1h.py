#!/usr/bin/env python
# -*- coding: utf-8 -*-
# <bitbar.title>AppStore Ranking</bitbar.title>
# <bitbar.version>v0.1</bitbar.version>
# <bitbar.author>more_more_for</bitbar.author>
# <bitbar.author.github>moremorefor</bitbar.author.github>
# <bitbar.desc>Shows your iOS app ranking.</bitbar.desc>
# <bitbar.dependencies>python</bitbar.dependencies>

import json
import urllib

# Reference: https://rss.itunes.apple.com/
RANKING_TYPE = {
    'Top Free Applications'         : {'label': 'Free',          'value': 'topfreeapplications'},
    'Top Free iPad Applications'    : {'label': 'Free iPad',     'value': 'topfreeipadapplications'},
    'Top Grossing Applications'     : {'label': 'Grossing',      'value': 'topgrossingapplications'},
    'Top Grossing iPad Applications': {'label': 'Grossing iPad', 'value': 'topgrossingipadapplications'},
    'Top Paid Applications'         : {'label': 'Paid',          'value': 'toppaidapplications'},
    'Top Paid iPad Applications'    : {'label': 'Paid iPad',     'value': 'toppaidipadapplications'}
}

# Reference: https://affiliate.itunes.apple.com/resources/documentation/genre-mapping/
GENRE = {
    'All'                           : {'label': 'All',            'value': 0},
    'Books'                         : {'label': 'Books',          'value': 6018},
    'Business'                      : {'label': 'Business',       'value': 6000},
    'Catalogs'                      : {'label': 'Catalogs',       'value': 6022},
    'Education'                     : {'label': 'Education',      'value': 6017},
    'Entertainment'                 : {'label': 'Entertainment',  'value': 6016},
    'Finance'                       : {'label': 'Finance',        'value': 6015},
    'Food & Drink'                  : {'label': 'Food',           'value': 6023},
    'Games'                         : {'label': 'Games',          'value': 6014},
    'Games - Action'                : {'label': 'Action',         'value': 7001},
    'Games - Adventure'             : {'label': 'Adventure',      'value': 7002},
    'Games - Arcade'                : {'label': 'Arcade',         'value': 7003},
    'Games - Board'                 : {'label': 'Board',          'value': 7004},
    'Games - Card'                  : {'label': 'Card',           'value': 7005},
    'Games - Casino'                : {'label': 'Casino',         'value': 7006},
    'Games - Dice'                  : {'label': 'Dice',           'value': 7007},
    'Games - Educational'           : {'label': 'Educational',    'value': 7008},
    'Games - Family'                : {'label': 'Family',         'value': 7009},
    'Games - Kids'                  : {'label': 'Kids',           'value': 7010},
    'Games - Music'                 : {'label': 'Music',          'value': 7011},
    'Games - Puzzle'                : {'label': 'Puzzle',         'value': 7012},
    'Games - Racing'                : {'label': 'Racing',         'value': 7013},
    'Games - Role Playing'          : {'label': 'RolePlaying',    'value': 7014},
    'Games - Simulation'            : {'label': 'Simulation',     'value': 7015},
    'Games - Sports'                : {'label': 'Sports',         'value': 7016},
    'Games - Strategy'              : {'label': 'Strategy',       'value': 7017},
    'Games - Trivia'                : {'label': 'Trivia',         'value': 7018},
    'Games - Word'                  : {'label': 'Word',           'value': 7019},
    'Health & Fitness'              : {'label': 'Health&Fitness', 'value': 6013},
    'Lifestyle'                     : {'label': 'Lifestyle',      'value': 6012},
    'Medical'                       : {'label': 'Medical',        'value': 6020},
    'Music'                         : {'label': 'Music',          'value': 6011},
    'Navigation'                    : {'label': 'Navigation',     'value': 6010},
    'News'                          : {'label': 'News',           'value': 6009},
    'Newsstand'                     : {'label': 'Newsstand',      'value': 6021},
    'Photo & Video'                 : {'label': 'Photo',          'value': 6008},
    'Productivity'                  : {'label': 'Productivity',   'value': 6007},
    'Reference'                     : {'label': 'Reference',      'value': 6006},
    'Social Networking'             : {'label': 'Social',         'value': 6005},
    'Sports'                        : {'label': 'Sports',         'value': 6004},
    'Travel'                        : {'label': 'Travel',         'value': 6003},
    'Utilities'                     : {'label': 'Utilities',      'value': 6002},
    'Weather'                       : {'label': 'Weather',        'value': 6001}
}


# Feed Setting ===============================================================
show_country = True

feed_settings = [
    {
        'RANKING_TYPE': RANKING_TYPE['Top Free Applications'], # See list above
        'GENRE'       : GENRE['Games'],                        # See list above
        'COUNTRY'     : 'jp',                                  # Country code (ISO 3166-1 alpha-2)
        'LIMIT'       : 200,                                   # 1~200
        'APP_ID'      : 0000000000                             # Your app id
    },
    {
        'RANKING_TYPE': RANKING_TYPE['Top Free Applications'],
        'GENRE'       : GENRE['Games - Simulation'],
        'COUNTRY'     : 'jp',
        'LIMIT'       : 200,
        'APP_ID'      : 0000000000
    },
    {
        'RANKING_TYPE': RANKING_TYPE['Top Grossing Applications'],
        'GENRE'       : GENRE['Games'],
        'COUNTRY'     : 'jp',
        'LIMIT'       : 200,
        'APP_ID'      : 0000000000
    }
]

# ============================================================================

for i in xrange(len(feed_settings)):
    if i == 1:
        print "---"
    feed = feed_settings[i]

    if feed['LIMIT'] > 200:
        print "param: LIMIT is invalid"
        break

    genre = "" if feed['GENRE']['label'] == 'All' else '/genre=' + str(feed['GENRE']['value'])
    if feed['GENRE']['label'] == 'All' and feed['LIMIT'] == 200:
        feed['LIMIT'] -= 1
    RSS_URL = "https://itunes.apple.com/" + feed['COUNTRY'] + "/rss/" + feed['RANKING_TYPE']['value'] + "/limit=" + str(feed['LIMIT']) + genre + "/json"

    r = urllib.urlopen(RSS_URL)
    data = json.loads(r.read())
    count = 0
    find_ranking = False
    for entry in data['feed']['entry']:
        count += 1
        if entry['id']['attributes']['im:id'] == str(feed['APP_ID']):
            country = feed['COUNTRY'].upper() + ":" if show_country else ""
            print "[" + country + "" + feed['RANKING_TYPE']['label'] + '] ' + feed['GENRE']['label'] + ": " + str(count)
            find_ranking = True
        elif count == feed['LIMIT'] and find_ranking == False:
            country = feed['COUNTRY'].upper() + ":" if show_country else ""
            print "[" + country + "" + feed['RANKING_TYPE']['label'] + '] ' + feed['GENRE']['label'] + ": ---"
