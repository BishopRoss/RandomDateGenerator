import random
from datetime import datetime, timedelta
variable = True 

def generate_random():
    rand = random.randint(1,20)
    return rand

def generate_random_date(start_date, end_date):
    timeBetween = end_date - start_date
    rand_num_days = random.randrange(timeBetween.total_seconds())
    rand_date = start_date + timedelta(seconds=rand_num_days)
    return rand_date

start_date = datetime(2023, 5, 16, 0, 0, 0)
end_date = datetime(2023, 5, 20, 23, 59, 59)



print("Welcome to the random number generator!\n")
while(variable == True):
    random_date = generate_random_date(start_date, end_date)
    print(random_date)
    print("Random Number: " + str(generate_random()))
    print("\n\nDo you want to go again?")
    choice = int(input( "One for yes, two for no: "))
    if choice == 1: 
        variable = True
    else:
        variable = False