from datetime import date, timedelta

start_100days = date(2017, 3, 30)
pybites_founded = date(2016, 12, 19)
pycon_date = date(2018, 5, 8)


def get_hundred_days_end_date():
    """Return a string of yyyy-mm-dd"""
    #pass
    return str(start_100days + timedelta(days=100))


def get_days_between_pb_start_first_joint_pycon():
    """Return the int number of days"""
    #pass
    date_diff = pycon_date - pybites_founded
    #print(type(date_diff))
    return date_diff.days

x = get_hundred_days_end_date()
print(x)

y = get_days_between_pb_start_first_joint_pycon()
print(y)