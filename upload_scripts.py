import requests
import os
url=r'http://localhost/upload/'
for file in os.listdir(os.getcwd()+r'/supplier-data/images'):
        if file.endswith('.jpeg'):
                with open(os.getcwd()+r'/supplier-data/images/'+file, 'rb') as opened:
                        r=requests.post(url,files={'file':opened})
                opened.close()