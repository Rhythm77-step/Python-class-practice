#Smart traffic light action using nested if-else
#Reading string inputs
"""
time_of_day=input("Enter time of day (Peak/Off-Peak):").strip()
traffic_density=input("Enter traffic density(High,Medium,Low):").strip()
emergency=input("Emergency vehicle detected?(Yes/No):").strip()
#Strictly nested decisiom logic
if emergency.lower()=="yes":
    action="Turn GREEN immediately"
else:
    if time_of_day.lower()=="peak":
        if traffic_density.lower()=="high":
            action="Extend GREEN light duration"
        elif traffic_density.lower()=="medium":
            action="Normal GREEN light duration"
        else:
            action="Reduce GREEEN light duration"
    else:
        #off peak hours behaviour
        action="Normal GREEN light duration"
print(f"Traffic light Action: {action}")

#Smart Airline system with capped discount
#Taking inputs 
age=int(input("Age:"))
travel_class=input("Travel Class:").strip().lower()
frequent_flyer=input("Frequent flyer:").strip().lower()
destination=input("Destination:").strip().lower()
base_price=float(input("Base price:"))
booking_charges=float(input("Booking Charges:"))
#Rule evaluation
if (age<12 and travel_class=="economy") or (frequent_flyer=="yes" and travel_class=="economy"):
    discount=1*booking_charges
elif age >=60 or (travel_class=="first" and destination !="delhi"):
    discount=0.60*base_price
elif travel_class=="business"  and destination=="mumbai":
    discount=(0.10*base_price)+(0.50*booking_charges)
elif frequent_flyer=="yes" and destination=="delhi":
    discount=0.80*booking_charges
else:
    discount=0.10*booking_charges
#Apply ceiling cap: Discount cannot exceed Base price
if discount> base_price:
    discount=base_price
final_ticket_price=base_price +booking_charges-discount
print(f"Discount Applied:{discount:.1f}")
print(f"Final ticket price:{final_ticket_price:.1f}")

#Taxi fare calculation
#take inputs
distance=float(input("Enter distance in km:"))
time_hour=int(input("Enter ride hour(0-23):"))
#Calculate fare based on distnace slabs
if distance<=5:
    fare=distance*20
elif distance <=15:
    fare=(5*20)+(distance-5)*15
     
#string operation using re module
import re
record="STU-66CSE, tripathirhythm247@gmail.com , +1-8305501296, score=90|Grade=A;status=pass"
#extract student code
student_code=re.findall(r"STU-\d{2}[A-Z]{3}",record)
#extract student email
emails=re.findall(r"[\w.-]+@[\w.-]+\.\w+",record)
#extract phone number
phones=re.findall(r"\+\d-\d{10}",record)
#printing the student details
print("Student Code:",student_code)
print("Email:",emails)
print("Phone:",phones)

#Student assignment and attendance score using nested lists

n=int(input("Enter no of students:"))
m=int(input("Enter no of courses:"))
Y=[]
for i in range(n):
    student=[]
    for j in range(m):
       a,b= map(int,input("Enter assignment and attendance:").split())
       student.append((a,b))

    Y.append(student)

for i in range(n):
    scores=[]
    grades=[]
    for j in range(m):
        a,b= Y[a][b]
        final_score=0.4*a+0.6*b
        scores.append(final_score)

        if final_score>=90:
            grade="A"
        elif final_score>=80:
            grade="B"
        elif final_score>=70:
            grade="C"
        elif final_score>=60:
            grade="D"
        else:
            grade="F"
        grades.append(grade)
print("Student:",i+1, "Final Score:",scores)
print("Student:",i+1, "Grades:",grades)
"""
#Matrix transformation using numpy
import numpy as np
#creating array





































