import time
import datetime
import os   
while(True):
    CurrentTime = datetime.datetime.now()
    with open(r"/sys/class/thermal/thermal_zone0/temp") as File:
        CurrentTemp = File.readline()
        calculated = float(CurrentTemp) / 1000

    print(str(CurrentTime) + " - " + str(calculated))

    if calculated > 40 and calculated < 55:
        print("normal temp - 1.5GHz")
        os.system('sudo cpufreq-set -r -u 1.5GHz')

    elif calculated > 55 and calculated < 65:
        print("high temp - 1.0GHz")
        os.system('sudo cpufreq-set -r -u 1.0GHz')

    elif calculated > 65 and calculated < 75:
        print("very high temp - 1.0GHz")
        os.system('sudo cpufreq-set -r -u 600MHz')

    

    time.sleep(3)
    os.system("clear")
