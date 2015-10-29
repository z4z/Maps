co2 = {
    'Texas':	656,
    'California':	364,
    'Pennsylvania':	245,	
    'Ohio':	233,
    'Florida':	227,
    'Illinois':	225,
    'Louisiana':	223,
    'Indiana':	207,
    'New York':	158,
    'Michigan':	157,
    'Georgia':	154,
    'Kentucky':	148,
    'Missouri':	133,
    'Alabama':	129,
    'North Carolina':	123,
    'New Jersey':	110,
    'Oklahoma':	107,
    'Tennessee':	103,
    'Virginia':	97,
    'Wisconsin':	96,
    'West Virginia':	96,
    'Arizona':	92,
    'Minnesota':	91,
    'Colorado':	91,
    'Iowa':	84,
    'South Carolina':	78,
    'Kansas':	73,
    'Washington':	69,
    'Arkansas':	67,
    'Massachusetts':	66,
    'Maryland':	64,
    'Utah':	64,
    'Wyoming':	64,
    'Mississippi':	60,
    'New Mexico':	    57,
    'North Dakota':	54,
    'Nebraska':	52,
    'Alaska':	38,
    'Oregon':	36,
    'Connecticut':	33,
    'Nevada':	33,
    'Montana':	32,
    'Hawaii':	19,
    'Maine':	18,
    'New Hampshire':	16,
    'Idaho':	16,
    'South Dakota':	14,
    'Delaware':	12,
    'Rhode Island':	11,		
    'Vermont':	            6,
    'District of Columbia':	3
}

gdp = {
    'California': 2287021,
    'Texas':	1602584,
    'New York':	1350286,
    'Florida':	833511,
    'Illinois':	742407,
    'Pennsylvania':	664872,
    'Ohio':	584696,
    'New Jersey':	560667,
    'North Carolina':	491572,
    'Georgia':	472423,
    'Virginia':	464606,
    'Massachusetts':		462748,
    'Michigan':		449218,
    'Washington':		425017,
    'Maryland':		351234,
    'Indiana':	328212,
    'Minnesota':		326125,
    'Colorado':		309721,
    'Tennessee':		296602,
    'Wisconsin':	293126,
    'Arizona':	288924,
    'Missouri':		285135,
    'Connecticut':	258996,
    'Louisiana':		257008,
    'Oregon':	229241,
    'Alabama':		199727,
    'Oklahoma':	192176,
    'South Carolina':	190176,
    'Kentucky':	189667,
    'Iowa':	174512,
    'Kansas':	149153,
    'Utah':	148017,
    'Nevada':	136903,
    'Arkansas':	129745,
    'Nebraska':	115250,
    'Mississippi':	109179,
    'District of Columbia':	105465,
    'New Mexico':	95310,
    'Hawaii':	78110,
    'West Virginia':	78050,
    'New Hampshire': 70118,
    'Idaho':	66548,
    'Delaware':		65029,
    'North Dakota':		62772,
    'Alaska':	60542,
    'Maine':	56163,
    'South Dakota': 49142,
    'Wyoming':	48538,
    'Rhode Island':	45962,
    'Montana':	45846,
    'Vermont':	30723
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
    if path['id'] not in ["State_Lines", "separator"]:
        if path['id'] in states: 
            state = states[path['id']]
        else:  
            continue
    
        rate = co2[state] / float(gdp[state]) * 200000
        print(state + ': ' + str(rate))
        
        if rate > 70:    
            rgb = (255, 255+50 - rate*1.05, 0)
        else:
            rgb = (rate*5-100, 255, 0) 
            
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

f = open('co2.svg','w+')
f.writelines(header)
f.writelines(body)
f.close();