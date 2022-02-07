import json
from datetime import date
from datetime import datetime
import os


print("                                                                                     ")
print("____________________________VISITOR PARKING______________________________")
print("                                                                                     ")

motorcycle_spot=4
car_spot=3
bus_spot=3

bike_cost=100
car_cost=180
bus_cost=250

if os.path.exists('/home/dell31/Documents/ParkingLot/agent_details.json')==True:
    myfile=open("agent_details.json")
    opened_file=json.load(myfile)
    for i in opened_file['user_details']:
        c=0
        c1=0
        c2=0
        for j,k in i.items():
            if k=='bike':
                c+=1
                motorcycle_spot=motorcycle_spot-c
            elif k=='car':
                c1+=1
                car_spot=car_spot-c1
            elif k=='bus':
                c2+=1
                bus_spot=bus_spot-c2
else:          
    pass

d={}    
maindict={}

agent_name=input("enter your Name : ")
select_vehicle=input("select your vehicle type: \nplease ENTER bike, car OR bus : ")
vehicle_number=input("Enter your vehicle number :")
now = datetime.now()
time = now.strftime("%H:%M:%S")
today = date.today()
print("                                                                                     ")
print("hello", agent_name, " !!!!!! WELCOME TO AD SPACE :) ")


if select_vehicle=='bike':
    if motorcycle_spot>0:
        print("Your Parking token number is",motorcycle_spot)
        print(" Your Vehicle number is", vehicle_number)
        print("Entry Time ", time)
        print("Today's date:", today)
        d["token"]=motorcycle_spot       
        d["Cost"]=bike_cost
        print("please pay", bike_cost,"INR")
    else:
        print("WE ARE SORRY !!!!!!!!!!!!!!!!!!")

elif select_vehicle=='car':
    if car_spot>0: 
        print("Your Parking token number is",car_spot)
        print(" Your Vehicle number is", vehicle_number)
        print("Entry Time ", time)
        print("Today's date:", today)
        d["token"]=car_spot
        d["Cost"]=car_cost
        print("please pay", car_cost,"INR")
    else:
        print("WE ARE SORRY !!!!!!!!!!!!!!!!!!")

elif select_vehicle=='bus':
    if bus_spot>0:
        print("Your Parking token number is",bus_spot)
        print(" Your Vehicle number is", vehicle_number)
        print("Entry Time ", time)
        print("Today's date:", today)
        d["token"]=bus_spot
        d["Cost"]=bus_cost
        print("please pay", bus_cost,"INR")
    else:
        print("WE ARE SORRY !!!!!!!!!!!!!!!!!!")
else:
    print(" SORRY !! We could not find vehicle please enter correct vehicle Name")


def agent_slip(name, vehicle, v_number, in_time):
        l=[]    
        d["name"]=name
        d["vehicle_type"]=vehicle
        d["vehicle_number"]=v_number
        d["entry_time"]=in_time
        if os.path.exists('/home/dell31/Documents/ParkingLot/agent_details.json')== True:
            myfile=open("agent_details.json")
            opened_file=json.load(myfile)
            l=opened_file['user_details']
            l.append(d)
            maindict['user_details']=l
            if select_vehicle=='bike' and motorcycle_spot>0: 
                myfile=open("agent_details.json","w")
                json.dump(maindict,myfile,indent=4)
                myfile.close()            
            elif select_vehicle=='car' and car_spot>0: 
                myfile=open("agent_details.json","w")
                json.dump(maindict,myfile,indent=4)
                myfile.close()
            elif select_vehicle=='bus' and bus_spot>0: 
                myfile=open("agent_details.json","w")
                json.dump(maindict,myfile,indent=4)
                myfile.close()
            else:
                if select_vehicle=="car":
                    print("NO spots for are availabe car")
                elif select_vehicle=="bike":
                    print("NO spots are availabe for bike")
                elif select_vehicle=="bus":
                    print("NO spots are availabe for  buses") 
                
        else:
            if select_vehicle=='bike' or select_vehicle=='bus' or select_vehicle=='car':
                l.append(d)
                maindict['user_details']=l
                myfile=open("agent_details.json","a+")
                json.dump(maindict,myfile,indent=4)
                myfile.close()
            else:
                ("something went wrong")
        
agent_slip(agent_name, select_vehicle, vehicle_number,time)

