from __future__ import print_function, division, absolute_import, unicode_literals

from bs4 import BeautifulSoup


soup = BeautifulSoup(open('homeopaths.html'))


result_form = soup.find('form', attrs={'name':'frm_members'})
trs = result_form.find_all('tr')

homeopaths = []
homeopath = {}
for tr in trs:
    label_td = tr.find('td', class_='green')
    if not label_td:
        continue
    label = label_td.text.strip()
    content = tr.find('td', class_='silver').text.strip()
    if label == "Name":
        if homeopath:
            homeopaths.append(homeopath)
        homeopath = {}
    homeopath[label] = content

print(homeopaths[0])
