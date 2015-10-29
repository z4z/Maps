change = {
	'Connecticut':	-0.19,
	'Massachusetts':	-0.12,
	'New Jersey':	-0.02,
	'District of Columbia':	-0.06,
	'Maryland':	-0.05,
	'New Hampshire':	-0.06,
	'Minnesota':	-0.03,
	'New York':	-0.15,
	'Colorado':	-0.05,
    'Hawaii':    -0.29,
	'Virginia':	-0.09,
	'California':	-0.22,
	'Washington':	-0.01,
	'Rhode Island':	-0.34,
	'Vermont':	-0.12,
	'Illinois':	-0.11,
	'Delaware': 0,
	'Wisconsin':	-0.04,
	'Nebraska':	0.11,
	'Pennsylvania':	0.03,
	'Alaska':	-0.29,
    'Iowa': 0,
	'Utah':	0.17,
	'Kansas':	0.03,
	'Maine':	0.09,
	'North Dakota': 0,
	'Arizona':	-0.01,
	'Oregon':	-0.04,
	'Wyoming':	0.30,
	'Florida':	-0.15,
	'South Dakota':	0.26,
	'Michigan':	-0.37,
	'Ohio':	-0.09,
	'Texas':	0.08,
	'Nevada':	0.09,
	'Georgia':	-0.10,
	'Missouri':	0.06,
	'North Carolina':	-0.04,
	'Indiana':	-0.08,
	'Montana':	0.20,
	'New Mexico':	0.03,
	'Idaho':	0.13,
	'South Carolina':	0.08,
	'Tennessee':	0.11,
	'Oklahoma':	0.13,
	'Louisiana':	0.27,
	'Alabama':	0.07,
	'Kentucky':	-0.10,
	'West Virginia':	0.11,
	'Arkansas':	0.06,
	'Mississippi': 0.23
}

states = {
    'DC': 'District of Columbia',
    'AK': 'Alaska',
    'AL': 'Alabama',
    'AR': 'Arkansas',
    'AZ': 'Arizona',
    'CA': 'California',
    'CO': 'Colorado',
    'CT': 'Connecticut',
    'DE': 'Delaware',
    'FL': 'Florida',
    'GA': 'Georgia',
    'HI': 'Hawaii',
    'IA': 'Iowa',
    'ID': 'Idaho',
    'IL': 'Illinois',
    'IN': 'Indiana',
    'KS': 'Kansas',
    'KY': 'Kentucky',
    'LA': 'Louisiana',
    'MA': 'Massachusetts',
    'DC': 'Maryland',
    'MD': 'Maryland',
    'ME': 'Maine',
    'SP-': 'Michigan',
    'MI-': 'Michigan',
    'MN': 'Minnesota',
    'MO': 'Missouri',
    'MS': 'Mississippi',
    'MT': 'Montana',
    'NC': 'North Carolina',
    'ND': 'North Dakota',
    'NE': 'Nebraska',
    'NH': 'New Hampshire',
    'NJ': 'New Jersey',
    'NM': 'New Mexico',
    'NV': 'Nevada',
    'NY': 'New York',
    'OH': 'Ohio',
    'OK': 'Oklahoma',
    'OR': 'Oregon',
    'PA': 'Pennsylvania',
    'PR': 'Puerto Rico',
    'RI': 'Rhode Island',
    'SC': 'South Carolina',
    'SD': 'South Dakota',
    'TN': 'Tennessee',
    'TX': 'Texas',
    'UT': 'Utah',
    'VA': 'Virginia',
    'VT': 'Vermont',
    'WA': 'Washington',
    'WI': 'Wisconsin',
    'WV': 'West Virginia',
    'WY': 'Wyoming'
}

from BeautifulSoup import BeautifulSoup
import os, sys

svg = open('blank-us-map.svg', 'r').read()
soup = BeautifulSoup(svg, selfClosingTags=['defs'])
paths = soup.findAll('path')

path_style = 'stroke:#000000;stroke-opacity:1;stroke-width:0.75;stroke-miterlimit:4;stroke-dasharray:none;fill:'

for path in paths: 
    if path['id'] in ['State_Lines', 'separator']:
        continue
    if path['id'] not in states: 
        continue
    
    state = states[path['id']]
    hdi = change[state]
    print(state + ': ' + str(hdi))

    if hdi > 0:
        red = 255 - hdi * 600
        green = 255
    elif hdi <= 0:
        red = 255
        green = 255 + hdi * 600

    rgb = (red, green, 0)
    color = '#%02x%02x%02x' % rgb
    
    path['style'] = path_style + color
    

blank = open('blank-us-map.svg','r')
header = blank.readlines()[0:43]
blank.close()

new = open('new.svg', 'w')
new.write(soup.prettify())
new.close
new = open('new.svg','r')
body = new.readlines()[16:-1]
new.close
os.remove('new.svg')

os.remove('hdi.svg')
f = open('hdi.svg','w+')
f.writelines(header)
f.writelines(body)
f.close();