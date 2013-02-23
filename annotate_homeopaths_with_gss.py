from __future__ import print_function, division, absolute_import, unicode_literals

import json
import re
import requests
import urllib

def postcode_to_gss(postcode):
    if postcode is None: # Haxx
        return None

    url = "http://mapit.mysociety.org/postcode/%s" % urllib.quote(postcode, '')
    json_data = requests.get(url).json()
    if 'areas' not in json_data:
        return None

    for _, area in json_data['areas'].items():
        if area['type'] != "UTA": # Unitary Authority
            continue
        return area['codes']['gss']
    return None

def extract_homeopath_postcode(homeopath):
    address = homeopath.get('Address', "")
    for line in address.splitlines():
        line = line.strip()
        line = line.replace(',', '')
        if re.match(r'[A-Z]+\d+ \d+[A-Z]+', line):
            return line
    return None

def annotate_homeopaths_with_postcodes(homeopaths):
    for homeopath in homeopaths:
        try:
            postcode = extract_homeopath_postcode(homeopath)
            homeopath['gss'] = postcode_to_gss(postcode)
        except ValueError: #Sorry...
            pass
    return homeopaths

with open('homeopaths.json') as jf:
    homeopaths = json.loads(jf.read())
    print(json.dumps(annotate_homeopaths_with_postcodes(homeopaths)))
        

#print(autho
