
import urllib.request
import json
import time
import webbrowser
import winsound

#url_db = 'https://kn.mednet.de/api/express/covid/testreihen/all?praxis_id=10' #Testdaten
url_db = 'https://kn.mednet.de/api/express/covid/testreihen/all?praxis_id=17'
url_termin = 'https://kn.mednet.de/covid19/signup/?praxis=MVZ%20Birkenallee'

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

    places = find_values('slots_left', data)

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

def piep():
    frequency = 3700  # Set Frequency To 2500 Hertz
    duration = 1000  # Set Duration To 1000 ms == 1 second
    winsound.Beep(frequency, duration)



if __name__ == '__main__':
    main()

