import random
import datetime


def generate_with_random_time(from_hours, to_hours):
    d = datetime.datetime.today()
    h_delta = random.randint(from_hours, to_hours)
    m_delta = random.randint(0, 60)
    d=d.replace(hour=0, minute=0)
    d = d + datetime.timedelta(hours=h_delta)
    time_vaccine = d + datetime.timedelta(minutes=m_delta)

    return time_vaccine
    