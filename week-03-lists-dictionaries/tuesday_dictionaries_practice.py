Student_Details = {
    "Name": "Clarance", 
    "Age": "28", 
    "Course": "MSIT", 
    "City": "Spain"
    }
print(Student_Details["Name"])
print(Student_Details["Age"])
print(Student_Details["Course"])
print(Student_Details["City"])
Student_Details["Certification"] = "PCEP"
print(Student_Details)

Student_Details.update({"Course": "PCAP Python"})
print(Student_Details)
Student_Details.pop("City")
print(Student_Details)

if "Age" in Student_Details:
    print("Age is available")
else:
    print("Age is not available") 

for i in Student_Details:
    print(i)