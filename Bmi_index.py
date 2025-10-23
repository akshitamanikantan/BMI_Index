import csv
f=open("BMI_Ind.csv","w", newline="")
g=csv.writer(f)
l=["Weight","Height","BMI","Systolic pressure","Diastolic pressure","Heart rate"]
g.writerow(l)
f.close()
c=0
def disp():
    f=open("BMI_Ind.csv","r")
    h=csv.reader(f)
    next(h)
    for i in h:
        print()
        print()
        n=float(i[2])
        print("BMI: ",n)
        if n<18.5:
            print("Underweight")
        elif n>18.5 and n<24.9:
            print("Normal weight")
        elif n>24.9:
            print("Overweight")
        st=float(i[3])
        dt=float(i[4])
        print("Blood pressure:",st,"/",dt,"mmHg")
        if st<90 and dt<60:
            print("Low blood pressure")
        elif st>=90 and st<=120 and dt>=60 and dt<=80:
            print("Normal blood pressure")
        elif st>120 and dt>80:
            print("High blood pressure")
        hea=float(i[-1])
        print("Heart rate:",hea)
        if hea<60:
            print("Low heart rate")
        elif hea>=60 and hea<=100:
            print("Normal heart rate")
        else :
            print("High heart rate")
def inp():
    f=open("BMI_Ind.csv","a",newline="")
    g=csv.writer(f)
    w=float(input("Enter your weight: "))
    h=float(input("Enter your height in metres: "))
    b=w/h**2
    s=float(input("Enter your systolic pressure: "))
    d=float(input("Enter your diastolic pressure: "))
    r=float(input("Enter your heart rate: "))
    nl=[w,h,b,s,d,r]
    g.writerow(nl)
    f.close()
while c==0:
    x=int(input("Enter 1 to enter data, Enter 2 to view output, Enter 3 to exit:"))
    if x==1:
        z=int(input("Enter the number of records to be entered:"))
        for i in range(z):
            inp()
    elif x==2:
        disp()
    else:
        c=1
    

