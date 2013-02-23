from __future__ import print_function, division, absolute_import, unicode_literals

import csv
import json

def build_gss_homeopath_count_dict():
    gss_dict = {}
    with open('homeopaths_with_gss.json') as jf:
        homeopaths = json.loads(jf.read())
        for homeopath in homeopaths:
            gss = homeopath.get('gss')
            if gss is None:
                continue
            datum = gss_dict.get(gss, {})
            datum['homeopaths'] = datum.get('homeopaths', 0) + 1
            gss_dict[gss] = datum
    return gss_dict


def smoosh():
    gss = build_gss_homeopath_count_dict()
    data = []
    with open('gss_education.csv') as csv_file:
        reader = csv.reader(csv_file)
        _ = reader.next() # Skip header
        for row in reader:
            datum = {'gss': row[0]}
            homeopath_data = gss.get('gss')
            if homeopath_data:
                datum['homeopaths'] = gss.get('gss')['homeopaths']
            if row[1]:
                name = row[1]
            elif row[2]:
                name = row[2]
            elif row[3]:
                name = row[3]
            datum['name'] = name
            datum['population'] = row[4]
            datum['p_none'] = float(row[5])
            datum['p_l1'] = float(row[6])
            datum['p_l2'] = float(row[7])
            datum['p_app'] = float(row[8])
            datum['p_l3'] = float(row[9])
            datum['p_l4'] = float(row[10])
            datum['p_other'] = float(row[11])
            data.append(datum)
    return data

print(smoosh())
