# Naukri
naukri api - you can use to find jobs by various categories

## how to use
step 1

make sure you have requests library 
```note 
pip install requests
```

step 2
```text 
copy naukri.py file to your directory
```
```python 

from naukri import Naukri
api = Naukri()
data = api.search_by_keyword('aws')
print(data)
```
sample output json
```text
[
  {
    "title": "AWS BigData",
    "job created": "14 Days Ago",
    "location": "Chennai",
    "skills": "QuickSight,AWS Bigdata,EMR,Data Pipeline,Glue,DynamoDB,Redshift,AWS S3",
    "jobDescription": "Educational Qualification:  bachelor Must Have Skills :  AWS BigData Professional Attributes:  1 Good learning ability 2 Good Communication skills 3 Interpersonal skills 4 Good team player Work Experience :  4-6 years Good To Have Skills :  No Function Specialization",
    "companyname": "Accenture Solutions Pvt Ltd",
    "salary": "Not disclosed",
    "experience": "4-6 Yrs"
  }
]
```
