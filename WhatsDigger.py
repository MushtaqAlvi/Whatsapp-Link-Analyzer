import requests
from bs4 import BeautifulSoup


# A method which gets all the group info and write them in storage

def save_url(url):
    GroupLink = url
    GroupIconLink = ""
    GroupName = ""
    print('\n     !--------------------!\n\nAnalyzing Group link : ')
    print(GroupLink)
    # requesting webpage for html content
    try:
        r = requests.get(GroupLink)
    except:
        print('\nInternet Connection Error!')

    # creating soup object for better vision and scrapping
    soup = BeautifulSoup(r.content, 'html.parser')

    # data scraping from html through all meta tags

    for meta in soup.find_all('meta'):
        # getting all links in content value of meta tags one by one
        IconLink = meta.get('content')
        if str(meta.get('property')) == str('og:title'):
            GroupName = str(meta.get('content'))

        if type(IconLink) == type('string'):

            if IconLink.find('pps.what') != -1:

                GroupIconLink = IconLink
                # GroupIconLink = IconLink
                try:
                    print('Trying to fetch Group Icon')
                    rr = requests.get(IconLink)
                    print('done...!')
                except:
                    print('     !--------------------!\nInter net Connection Error!\n')
                try:
                    print('Trying to save Group Details')
                    file_name = '' + GroupLink[26:] + ' - ' + GroupName + '.png'
                    file = open(str(file_name), 'wb')
                    file.write(rr.content)
                    file.close()
                    print('Group Icon Downloaded and Renamed with Group ID + Group Name')

                except:
                    print('\n!---Failed to Save Group Details---!\n')

    if str(GroupIconLink) != "":
        print('Group name is : ')
        print(GroupName)
        print('Group icon (DP) Image file link is:')
        print(GroupIconLink)
        print('\n     !--------------------!')
    else:
        print('Group not Found')
        print('\n     !--------------------!')

print('Please paste your Whatsapp Group Link:\n')
getlink = input()
save_url(getlink)
print('Developer: MushtaqAlvi')
print('https://github.com/MushtaqAlvi/WhatsDiger-v1.0')
# demo save_url('https://chat.whatsapp.com/DTjcs4UNvqfGnUcrbGBQwp')
