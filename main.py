# -*- coding: utf-8 -*-
#!/usr/bin/env python
ID = "07F1B367"

import json
import time
from time import strftime

"""
from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.image import Image
from kivy.uix.label import Label
"""

data = json.loads(open('data.json').read())
print(data)

"""RFID = True
while RFID == True:
    try:
        #ser = serial.Serial(4,115200)

        #ID = ser.readline(8)

        #ser.close()

        gc = gspread.login('skelleftea.makerspace@gmail.com', 'lösenord')
    #wks1 = gc.open("Medlemsdatabas").sheet1
        wks1 = gc.open("Medlemsdatabas").sheet1

        localtime = strftime("%a, %d %b %Y %H:%M:%S") # År,Månad,Dag,Timmar,Minuter,Sekunder

        cell = wks1.find(ID)                         #hittar cellen med värdet ID
        namn = wks1.cell(cell.row, cell.col+2).value  #hämtar värdet av raden brevid ID

        cell = wks1.find(ID)
        val1 = wks1.cell(cell.row, cell.col+5).value
        val2 = wks1.cell(cell.row,cell.col-1).value
        a = val1
        b = val2
        c = "Betalat"
        d = "Ej betalat"
        if a >= b:
            wks = gc.open("test").sheet1

            tup1 = (localtime,ID,namn,c);
            wks.append_row(tup1[0:4])
        else:
            wks = gc.open("test").sheet1

            tup1 = (localtime,ID,namn,d);
            wks.append_row(tup1[0:4])

        class BudokanApp(App):

            def build(self):
                layout = FloatLayout(padding=0)
                wimg = Image(source='bg2.gif')
                label = Label(text='Välkommen\n%s'%namn)
                layout.add_widget(wimg)
                layout.add_widget(label)
                return layout


        if __name__ == '__main__':
            BudokanApp().run()


    except:
        print "Något blev fel meddela en tränare"
        time.sleep(10)
"""