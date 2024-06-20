import sys, time
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont, QFontDatabase, QIcon, QKeySequence,
                           QLinearGradient, QPalette, QPainter, QPixmap, QRadialGradient)
from PySide2.QtWidgets import *
from PySide2.QtCore import *
import csv
import time
import pyttsx3
from main import *

import time
import logging
import time

import datetime


import json
from pickle import FALSE
from telnetlib import STATUS

import warnings
import pandas as pd
warnings.filterwarnings("ignore")
import datetime


import numpy as np

class MySignal(QObject):

    sig = Signal(str,str,str,str,str)
    sig1 = Signal(str,str,str)
    startpb = Signal()
    reset = Signal(str)
    plan_fa = Signal(str)
    plan_smt = Signal(str)
    retry = Signal(str)
    nginp = Signal(str,str)
    cttime = Signal(str)
    manin = Signal(str)

class Mylongthread(QThread):

    def __init__(self, parent=None):
        QThread.__init__(self, parent)

        self.signal = MySignal()
        self.capture= False
        self.mode = ""
        self.engine = pyttsx3.init() # object creationy

#""" RATE"""
        #rate = engine.getProperty('rate')   # getting details of current speaking rate
        #print (rate)                        #printing current voice rate
        self.engine.setProperty('rate', 150)     # setting up new voice rate


#"""VOLUME"""
        #volume = engine.getProperty('volume')   #getting to know current volume level (min=0 and max=1)
        #print (volume)                          #printing current volume level
        self.engine.setProperty('volume',1.0)    # setting up volume level  between 0 and 1

#"""VOICE"""
        voices = self.engine.getProperty('voices')       #getting details of current voice
        #engine.setProperty('voice', voices[0].id)  #changing index, changes voices. o for male
        self.engine.setProperty('voice', voices[0].id)

    def run(self):

        

        try:

           
            #lines = ['SMT-L02','SMT-L03','SMT-L04','SMT-L05','SMT-L06']
            lines = ['SMT-L02','SMT-L03','SMT-L04','SMT-L05','SMT-L06','W105ASSY','RBCASSY','Q5CLUASSY','AI3ASSY','FA-L15 BI3','FA-L14 RE','FA-L19 QY','FA-L20 VW','FA-L16 JDCLU','Q5SILVERBOX','FA-L23 W601 DIS','FA-L37 Z101MIDDISP']
            #cluster = ['W105ASSY','RBCASSY','Q5CLUASSY','AI3ASSY','FA-L15 BI3','FA-L14 RE','FA-L19 QY','FA-L20 VW','FA-L16 JDCLU','Q5SILVERBOX','FA-L23 W601 DIS','FA-L37 Z101MIDDISP']
            user = "API_ANDON_ANDONPLANT"
            password = "4nd0n.P@ssw0rd"
            #cluster = ['FA-L23 W601 DIS','FA-L37 Z101MIDDISP']
            i=1
            j=1
            jay = False
            

            while True:
            #while jay == True:

                current_time = datetime.datetime.now().time()      

                print(self.mode)
                

                if current_time >= datetime.time(0,15,0) and current_time <= datetime.time(7,15,0):
                    shift = "1"
                    
                elif current_time >= datetime.time(7,16,0) and current_time <= datetime.time(15,45,0):
                    shift = "2"
                    
                else:
                    shift = "3"

                old_time = datetime.datetime.now()
                new_time = old_time - datetime.timedelta(hours=0, minutes=20)
                date = str(new_time.date())
                print(shift)



                if current_time >= datetime.time(0,20,0) and current_time <= datetime.time(0,40,0):
                    self.signal.reset.emit("")
                    self.signal.plan_fa.emit("")
                    self.signal.plan_smt.emit("")

                if (shift == "2" or shift=="3") and i == 1:

                    shift = "1"
                    i = 0


                elif shift == "3" and j == 1:


                    shift = '2'
                    j = 0

                                
                for line in lines:

                    URL = 'https://veicim011.vistcorp.ad.visteon.com/andon/api/AndonStatus/'+line
                    model = 'http://10.218.199.159/termite/service.svc/LnOverview/'+line+'/'+'SNG'
                    URL2 = 'https://veicim011.vistcorp.ad.visteon.com/andon/api/HrXHr/getHrXHr/'+line+'/'+date+'/'+shift
                    print(URL2)

                ######################## andon status ##################
                    try:
                        response = requests.get(
                                        URL ,
                                        auth=(user,password),verify=False)

                        data = response.json()
                        status = str(data[0]['status'])
                        reason = str(data[0]['comments'])
                        stop_time =(data[0]['initial'])

                    ######### model #########################
                        response1 = requests.get(model)
                        x  = response1.text

                        res = x.split(",")[2]
                        print(res)
                        model = res[16:]
                        product = str(model)
                        eff = ""
                        down = ""

                 ##########  Running  ###############

                        if status != "Running" :

                            date_time_str = stop_time.replace("T", " ")
                            print(stop_time)
                            date_time_obj = datetime.datetime.strptime(date_time_str, '%Y-%m-%d %H:%M:%S.%f')
                            now = datetime.datetime.now()
                            delta = now - date_time_obj
                            sec = delta.total_seconds()
                            down = str(round((sec / 60)))
                            if status == "No Plan" or status == "CLRI" or status == "Changeover":
                                pass

                            elif self.mode == "Shopfloor":
                                print("audio on")
                                winsound.Beep(440, 3000)
                                self.engine.say(line+ "stopped for past   , "+ down+ " minutes!! for " + status +"    "+ reason )
                                self.engine.runAndWait()
                                self.engine.stop()

                            elif self.mode == "Supervisor" and int(down) >= 15:
                                print("15 alert")
                                winsound.Beep(440, 3000)
                                self.engine.say(line+ "stopped for past   , "+ down+ " minutes!! for " + status +"    "+ reason )
                                self.engine.runAndWait()
                                self.engine.stop()

                            elif self.mode == "Maintenance" and status == "Maintenance":

                                winsound.Beep(440, 3000)
                                self.engine.say(line + "stopped for past   , " + down + " minutes!! for " + status + "    " + reason)

                                self.engine.runAndWait()
                                self.engine.stop()


                            elif self.mode == "Manager" and int(down) >= 30:
                                print("30 alert")
                                winsound.Beep(440, 3000)
                                self.engine.say(line+ "stopped for past   , "+ down+ " minutes!! for " + status +"    "+ reason )
                                self.engine.runAndWait()
                                self.engine.stop()




                    except Exception as e:
                        print("error in andon get for "+ line)
                        print(e)
                        status = "error"

                 ############ Production count ###############

                    try:

                        response2 = requests.get(URL2,auth=(user,password),verify=False)
                        data = response2.json()
                   # print(data)
                        if len(data) != 0:
                            x = pd.DataFrame(data)
                            prod = (x['hourProduction'].sum())
                            eff= prod

                        else:
                            eff = 0
                            print("No prouction data for "+ line)

                    except Exception as e:
                        print(e)
                        print("production data get error"+line+ "shift:"+shift)
                        eff= "err"

                    self.signal.sig.emit(status,reason,line,down,product)
                    self.signal.sig1.emit(str(line),str(shift),str(eff))
                    time.sleep(5)

                time.sleep(60)

        # Exception error for the 
        except Exception as e:
                print(e)
                print("error main loop"+line+date+shift)
                self.signal.retry.emit("retry")
            


#class Mythread(QThread):

#    def __init__(self, parent=None):
#        QThread.__init__(self, parent)

#        self.signal1 = MySignal()
#        sig = Signal1(str,str)

#    def run(self):

      
            
            
            






       

       

            
            


        



                


        








           










