from urllib.request import Request, urlopen
import urllib.request
import json
import time
import webbrowser

url_db = 'https://smcb.no-q.info/api/v1/gyms/685/checkins/public-slots/at/1192/date/2021/05/19?task_token='
url_dbstart = 'https://smcb.no-q.info/api/v1/gyms/685/checkins/public-slots/at/1192/date/'
url_dbend = '?task_token='

url_termin = 'https://app.no-q.info/neue-apotheke-bruchmuehlen/checkins#/1192/2021-05-19'

def main(): 

    while 1:
        if (check_termin() == False):
            time.sleep(60 * 5)
        else:
            webbrowser.open(url_termin)
            time.sleep(60 * 5)
            return 0  

def check_termin():
    req = Request(url_dbstart + time.strftime("%Y/%m/%d") + url_dbend , headers={'User-Agent': 'Mozilla/5.0'})
    #print (url_dbstart + time.strftime("%Y/%m/%d") + url_dbend)
    page = urllib.request.urlopen(req)
    data = page.read()

    places = find_values('free_spots', data)

    print( time.strftime("%d.%m.%Y %H:%M:%S") , places)

    for index, item in enumerate(places):
        if item > 0:
            print ("Freie Termine:", item, "Termin Nr:", index) 
            return index, item

    return False

def find_values(id, json_repr):
    results = []

    def _decode_dict(a_dict):
        try:
            results.append(a_dict[id])
        except KeyError:
            pass
        return a_dict

    json.loads(json_repr, object_hook=_decode_dict) # Return value ignored.
    return results

if __name__ == '__main__':
    main()

