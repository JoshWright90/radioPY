import subprocess
import csv
import time
import os

##Get URL of Station from CSV File/Choice
stations = []
with open('stations.csv') as csvDataFile:
    csvReader = csv.reader(csvDataFile)
    for row in csvReader:
        stations.append(row)

for station in stations:
    print(station[0],station[1])

chosen_station = input("Choose Station Index: ")

for station in stations:
    if chosen_station == station[0]:
        _url = station[2]

##Find location of VLC Program
for vlc_dir in ':\Program Files\VideoLAN\VLC\VLC.exe', ':\Program Files (x86)\VideoLAN\VLC\VLC.exe':
    for drive in 'a', 'b', 'c', 'd', 'e', 'f', 'g':
        found = os.path.isfile(drive + vlc_dir)
        if found is True:
            _vlc = drive + vlc_dir
            print("VLC Player found:", _vlc)
            break
if _vlc is None:
    print("VLC Player not found")
    input("Press enter to exit")
    exit()

##Launch VLC with Chosen Radio
try:
        subprocess.Popen(str(_vlc) + ' ' + str(_url))
        time.sleep(3)
except Exception as e:
        print(e)
        input("Press Enter to continue")

