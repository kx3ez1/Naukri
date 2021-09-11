import re
import requests as r

root = 'https://www.naukri.com/jobapi/v3/search'
search_by_keyword = lambda \
        keyword: root + f'?noOfResults=20&urlType=search_by_keyword&searchType=adv&keyword={keyword}&src=jobsearchDesk&latLong='
search_by_location = lambda \
        location: root + f'?noOfResults=10&location={location}&urlType=search_by_key_loc&searchType=adv&keyword=latest&src=jobsearchDesk&latLong='
search_by_salary = lambda \
        salary: root + f'?noOfResults=20&urlType=search_by_keyword&searchType=adv&keyword=cyber%20security&sort=p&ctcFilter=0to3&ctcFilter=3to6&ctcFilter={salary}&seoKey=cyber-security-jobs&src=jobsearchDesk&latLong='
search_by_experiance = lambda \
        experiance: root + f'?noOfResults=20&urlType=search_by_keyword&searchType=adv&keyword=cyber%20security&sort=p&experience={experiance}&seoKey=cyber-security-jobs&src=jobsearchDesk&latLong=&sid=16312691456641973_6'
search_by_graduation = lambda \
        graduation: root + f'?noOfResults=20&urlType=search_by_keyword&searchType=adv&keyword=cyber%20security&sort=p&ugTypeGid={graduation}&seoKey=cyber-security-jobs&src=jobsearchDesk&latLong=&sid=16312691456641973_7'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.3',
    'Referer': 'https://www.naukri.com/latest-jobs',
    'gid': 'LOCATION,INDUSTRY,EDUCATION',
    'systemid': '109',
    'clientid': 'd3skt0p',
    'appid': '108'
}


class Naukri:
    def common_function(self, url):
        data = r.get(url, headers=headers)
        print(f'status code is -- {data.status_code}')
        data = data.json()
        jobs = data['jobDetails']
        print('TOtal Results Found', len(jobs), '\n')
        list_of_jobs = []
        for j in range(len(jobs)):
            title = jobs[j]['title']
            companyname = jobs[j]['companyName']
            skills = jobs[j]['tagsAndSkills']
            jobDescription = jobs[j]['jobDescription']
            jobDescription = re.sub('<[^<]+?>', '', jobDescription)
            job_created = jobs[j]['footerPlaceholderLabel']
            experience = ''
            salary = ''
            location = ''
            for i in jobs[j]['placeholders']:
                if i['type'] == 'experience':
                    experience = i['label']
                elif i['type'] == 'salary':
                    salary = i['label']
                elif i['type'] == 'location':
                    location = i['label']
            job = {'title': title, 'job created':job_created,'location': location, 'skills': skills,'jobDescription':jobDescription,'companyname': companyname, 'salary': salary, 'experience': experience }
            list_of_jobs.append(job)
        return list_of_jobs


    def search_by_keyword(self, keyword='python'):
        return self.common_function(search_by_keyword(keyword))

    def search_by_location(self, location='hyderabad'):
        return self.common_function(search_by_location(location))

    def search_by_salary(self, salary='1to3'):
        return self.common_function(search_by_salary(salary))

    def search_by_experiance(self, experiance='1to3'):
        return self.common_function(search_by_experiance(experiance))

    def search_by_graduation(self, graduation):
        return self.common_function(search_by_graduation(graduation))
