#!/usr/bin/env python3
import os
import datetime
import reports
import json
directory=os.getcwd()+'/supplier-data/descriptions/'
string='<br/><br/>'
for file in os.listdir(directory):
        with open(directory+file) as data:
                string=string+'name: '+data.readline()
                string=string+'<br/>'+'weight: '+data.readline()+'<br/><br/>'
        data.close()
now=datetime.datetime.now()
reports.generate_report('/tmp/processed.pdf', 'Processed Update on '+now.strftime('%b %d, %Y'), string)
