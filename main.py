import csv
import math
import os

os.system("clear")

with open ("source.csv","r+") as file_r:
  with open ("result.csv","w+") as file_w:
    f=csv.reader(file_r,delimiter=";")
    f_w=csv.writer(file_w,delimiter=";")
    f_w.writerow(["Дата",
     "Tн.в. - температура наружного воздуха, гр.С (ГМЦ)",
     "Тв.р. - температура воздуха внутри помещения расчетная, гр.С","Тп.р. - температура подающего трубопровода расчетная, гр.С",
     "То.р. - температура обратного трубопровода расчетная, гр.С",
     "Tн.р. - расчетная температура наружного воздуха, гр.С",
     "q - относительная тепловая мощность системы отопления",
     "n - показатель степени",
     "q - относительная тепловая мощность системы отопления в степени = 0,8",
     "Т3 - расчетная температура темлоносителя в подающем трубопроводе после смесительного устройства, гр. С",
     "Фактическая температура теплоносителя (согласно показаний ОДПУ)",
     "Tн.в. - температура наружного воздуха, гр.С (расчетная)"])
    for row in f:
      data=row[0]
      Tnv=float(row[1].replace(",", "."))
      Tvr=float(row[2].replace(",", "."))
      Tpr=float(row[3].replace(",", "."))
      Tor=float(row[4].replace(",", "."))
      Tnr=float(row[5].replace(",", "."))
      q=float(row[6].replace(",", "."))
      n=float(row[7].replace(",", "."))
      q_st=float(row[8].replace(",", "."))
      T3=float(row[9].replace(",", "."))
      T3fact=float(row[10].replace(",", "."))
      Tnv_podbor=-70.00
      T3_cycle=0.00
      while(T3_cycle!=T3fact and Tnv_podbor<=20.00):
        Tnv_podbor=round(Tnv_podbor,2)
        Tnv_podbor+=0.01
        if(Tvr-Tnv_podbor <=0):
          break
        q_cycle=(Tvr-Tnv_podbor)/(Tvr-Tnr)  
        T3_cycle=Tvr+0.5*(Tpr-Tor)* q_cycle + 0.5*(Tpr+Tor - 2*Tvr)* math.pow(q_cycle,0.8)
        T3_cycle=round(T3_cycle,2)
      f_w.writerow([data,
      str(Tnv).replace(".", ","),
      int(Tvr),
      int(Tpr),
      int(Tor),
      int(Tnr),
      str(q).replace(".", ","),
      str(n).replace(".", ","),
      str(q_st).replace(".", ","),
      str(T3).replace(".", ","),
      str(T3fact).replace(".", ","),
      str(round(Tnv_podbor,4)).replace(".", ",")])
  
