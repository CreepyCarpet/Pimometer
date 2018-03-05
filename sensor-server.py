import os
import glob
import time
import datetime
import json
from bottle import route, run, static_file

#Sensor program, use read_temp to get temperature value
os.system('modprobe w1-gpio')
os.system('modprobe w1-therm')

#base_dir = '/sys/bus/w1/devices/'
#device_folder = glob.glob(base_dir + '28*')[0]
#device_file = device_folder + '/w1_slave'

def read_temp_raw():
    f = open(device_file, 'r')
    lines = f.readlines()
    f.close()
    return lines

#Returns temperature value in degrees celcius
def read_temp():
    lines = read_temp_raw()
    while lines[0].strip()[-3:] != 'YES':
        time.sleep(0.2)
        lines = read_temp_raw()
    equals_pos = lines[1].find('t=')
    if equals_pos != -1:
        temp_string = lines[1][equals_pos+2:]
        temp_c = float(temp_string) / 1000.0
        return temp_c

@route('/<filename>')
def serve_page(filename):
    return static_file(filename, root=r"C:\Users\Staal\Pimometer")

run(host='localhost', port=8181, debug=True)
