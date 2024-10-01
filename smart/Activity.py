import serial
import time
import pandas as pd


ser=serial.Serial('COM3',9600,timeout=0.5)
dataset=[]
count=0


while True:
    if ser.inWaiting() > 0:
        try:
            data = ser.readline().decode('utf-8')
            if(data.startswith("#")):
                a=data.split(',')
                dummy=[]
                dummy.append(a[1])
                dummy.append(a[2])
                dummy.append(a[3])
                dataset.append(dummy)
                count+=1
                if(count==50):
                    df=pd.DataFrame(dataset)
                    df.to_csv("gas.csv")
                    count=0
                print("Reading value ",count)
        except Exception as e:
            print(e)
            continue