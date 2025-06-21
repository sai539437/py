#calclaute people working days 
X=int(input("no.of work doneA:"))
Y=int(input("no of work doneB:"))
Z=int(input("no of work doneC:"))

T_no_work=(X*Y*Z)/((X*Y)*(Y*Z)*(Z*X)) # x*y

print('Number of work done by A, B, C : ',T_no_work)
