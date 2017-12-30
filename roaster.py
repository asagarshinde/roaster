import calendar
from datetime import datetime
import numpy as np
"""
SHIFT_CODE
M : morning
G : general
A : afternoon
N : night
H : holiday
W : Week off
C : compoff
X : default
L : leave
"""

SHIFT_CODE = ['M','G','A','N','H','W','C','X','L']
USER = {1:'ram',2:'shyam',3:'sagar',4:'mayur',5:'rani'}
month = datetime.today().month
year = datetime.today().year
days_of_month = calendar.monthrange(year , month)[1]
 
class User:
    def __init__(self,username,userid):
        self.username = username
        self.userid = userid
        self.no_of_days_per_user = 5
        self.week_off = 2

for id in USER.keys():
    employee = (id,USER[id])
    print (id ,":" ,USER[id])

users = [USER[id] for id in USER.keys() ]
roastar = np.chararray([len(users),days_of_month])

for user in range(roastar.shape[0]):
    for day in range(roastar.shape[1]):
                
        if (day)%7 == 6:
            roastar[user,day]='L'
        else:
            roastar[user,day]='G'

## test
counter = 1
for i in roastar[0]:
    print (counter, ":" , i)
    counter = counter + 1
