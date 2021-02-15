import requests as re
import os
import uuid
import json
from dotenv import load_dotenv
load_dotenv()

#https://sheets.googleapis.com/v4/spreadsheets/1tj6eQlVLFgmskoXouVt87POxYVwR1yWT2vOSQEPyDtg/values/%27Responses%27!A2:O?key=
WINS_API_KEY = os.getenv('WINS_API_KEY')
SPREAD_SHEET_ID = '1tj6eQlVLFgmskoXouVt87POxYVwR1yWT2vOSQEPyDtg'
BASE_API_URL = 'https://sheets.googleapis.com/v4/spreadsheets'


request_url = f"{BASE_API_URL}/{SPREAD_SHEET_ID}/values/\'Responses\'!A2:O?key={WINS_API_KEY}"

request_data = re.get(request_url).json()['values']

container = [{f'key_{index}':value for (index,value) in enumerate(person) } for person in request_data]

with open('wins-data.json','w+') as f: json.dump(container,f)














# class Wins():

#     def __init__(self,time,email,name,linkedin_url,linkedin_permission,github_url,githhub_permission,team,role,specific_role,join_date,win,overview,crap,display):
#         self.userdata = {'id':uuid.uuid4().hex,
#                          'time':time,
#                          'email':email,
#                          'name':name,
#                          'linkedin_url':linkedin_url,
#                          'linkedin_permission':linkedin_permission,
#                          'github_url':githhub_permission,
#                          'team':team,
#                          'role':role,
#                          'specific_role':specific_role,
#                          'join_date':join_date,
#                          'win':win,
#                          'overview':overview,
#                          'display':display
#                          }
    
# # windata = Wins(*request_data[1])
# # print(windata.userdata)

# write_ready_object = [ Wins(*item).userdata for item in request_data ]
# print(write_ready_object)