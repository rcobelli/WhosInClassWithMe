import requests
import configparser
import json
import datetime

api_key = "2096~12345"

friends = [
    "Smith",
    "Barnes",
    "Doe"
]

# Query the API to get all of your classes
url = 'https://canvas.instructure.com:443/api/v1/courses?enrollment_type=student&enrollment_state=active&include[]=total_scores&state[]=available'

headers = {'Authorization': ('Bearer ' + api_key)}
r = requests.get(url, headers=headers)
data = json.loads(r.text)

# Loop through each course
for course in data:
    # Query the API to get a list of students in the course
    url = 'https://canvas.instructure.com:443/api/v1/courses/' + str(course['id']) + '/enrollments?type=StudentEnrollment&per_page=1000'
    r = requests.get(url, headers=headers)
    students = json.loads(r.text)

    # Loop through every student
    for student in students:
        # Extract their last name
        names = student["user"]["sortable_name"].split()
        name = names[0][:-1]

        # Check if their last name matches anybody in your list
        if (name in friends):
            print(course["name"] + ": " + student["user"]["sortable_name"])
