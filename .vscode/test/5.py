#hotel managment syestme
hotel="welcome to taj hotel managment system"
hotel1="enjoy the stay of luxury and comfort"
print(hotel)
print(hotel1)
stay=int(input("enter the number of days you want to stay:"))
room_type=int(input("enter the type of room you want to stay 1.delux 2.super delux 3.suite 4.regular room:"))
if room_type==1:
    cost_per_day=5000
    print("you have selected delux room")
    print("you will enjoy private pool ,free breakfast and free wifi")
elif room_type==2:
    cost_per_day=6500
    print("you have selected our super delux room")
    print("you will enjoy private pool,free breakfast,jungle safari and free wifi")
elif room_type==3:
    cost_per_day=8000
    print("you have slected our suite room")
    print('you will enjoy private pool,free breakfast,jungle safari,spa and free wifi')
elif room_type==4:
    cost_per_day=1000
    print("you have selected regular room")
    print("you will enjoy hot shower , free breakfast and free wifi")
else:
    print("room type is invalid")
    total_cost=cost_per_day*stay
    print("the total cost of your stayu is:",total_cost)
    print("thank you staying at hotel taj have a great day ahead")
taj_food=input("welcome to taj hotel food court do you wish to order food yes/no")
if taj_food=="yes":
    table=int(input("enter the number of people and table sitting you want:"))
    food_menu=("1.north indian","2.south indian","3.chinese food",)
if taj_food==1:
    print("you will be served with amazing north indian food ")
    print("north indian menu consits of , butter chicken , naan , panner , roti , rice , north indian thali")
elif taj_food==2:
    print("you will be served with south indian food")
    
