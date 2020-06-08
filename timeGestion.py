#!/usr/bin/python3
# coding: utf-8
import time
import datetime

print("Hey ! Petite pause de 2 secondes...")
timeStamp1 = time.time()
time.sleep(2)
timeStamp2 = time.time()
print("...terminée ! On a véritablement attendu {} secondes.".format(timeStamp2-timeStamp1))

structTime = time.localtime(timeStamp1-3600)
timeStamp0 = time.mktime(structTime)
print("\nUne heure avant le lancement de ce programme nous étions le :\n"
    +"/".join([str(structTime.tm_mday),str(structTime.tm_mon),str(structTime.tm_year)])
    +", "
    +":".join([str(structTime.tm_hour),str(structTime.tm_min),str(structTime.tm_sec)])
    +" (GMT+{2}), soit le jour {0} de la semaine et le jour {1} de l'année".format(structTime.tm_wday+1,structTime.tm_yday,structTime.tm_isdst))
print("\nVoila le timestamp récupéré : {}".format(timeStamp0)
    +"\nEt la différence avec le timestamp au moment de l'éxecution : {}".format(timeStamp1-timeStamp0))

strTime = time.strftime("%d %B %Y, %H:%M:%S",structTime)
print("C'est plus simple en formatant : "+strTime)


