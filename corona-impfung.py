
import urllib.request
import json
import time
import webbrowser
import winsound

url_db = 'https://www.hausaerzte-rahden.de/wp-admin/admin-ajax.php?action=wpamelia_api&call=/events&dates[]=2021-05-01&dates[]=2021-07-31&page=0&tag=erstimpfung'
url_termin = 'https://www.hausaerzte-rahden.de/corona-erstimpfung/'

# Test Termine
#url_db = 'https://www.hausaerzte-rahden.de/wp-admin/admin-ajax.php?action=wpamelia_api&call=/events&dates[]=2021-05-01&dates[]=2021-07-31&page=0&tag=schnelltest'
#url_termin = 'https://www.hausaerzte-rahden.de/corona-erstimpfung/'

def main(): 

    piep()

    while 1:
        if (check_termin() == False):
            time.sleep(60 * 1)
        else:
            webbrowser.open(url_termin)
            while (check_termin() != False):
                piep()
                time.sleep(5)
                piep()
                time.sleep(5)
                piep()
                time.sleep(5)
                piep()
                time.sleep(5)
                piep()
                time.sleep(5)
                piep()
                time.sleep(5)
 

def check_termin():
    page = urllib.request.urlopen(url_db)
    data = page.read()
    impfstopf_typ = 'Impfstoff: '
    #ret = data.find('ASTRA ZENECA')

    if  b'ASTRA ZENECA' in data or \
        b'AstraZeneca ' in data:
        impfstopf_typ = impfstopf_typ + "ASTRA ZENECA, "

    if b'BIO' in data or\
       b'BioNTech' in data or\
       b'bio' in data or\
       b'Bio' in data:
        impfstopf_typ = impfstopf_typ +  "BioNTech, "

    places = find_values('places', data)

    print( time.strftime("%d.%m.%Y %H:%M:%S") , places, " " , impfstopf_typ)

    for index, item in enumerate(places):
        if item > 0:
            print ("Freie Termine:", item, "Termin Nr:", index," " , impfstopf_typ) 
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

def piep():
    frequency = 3700  # Set Frequency To 2500 Hertz
    duration = 1000  # Set Duration To 1000 ms == 1 second
    winsound.Beep(frequency, duration)



if __name__ == '__main__':
    main()

