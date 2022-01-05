from datetime import datetime, timedelta
from clinic import app, db
from clinic.models import User, Detail, Patient, Medicine
from datetime import datetime, timedelta, date
import calendar
from sqlalchemy import extract  
import re

month = datetime.now().month
year = datetime.now().year

def getIncome(args):
    return int(re.search(r'\d+', str(args)).group())
for i in db.session.query(Detail.cost1).filter(extract('year', Detail.Date_of_diagnosis)==year).filter(extract('month', Detail.Date_of_diagnosis)==month).all():
    print(getIncome(i))