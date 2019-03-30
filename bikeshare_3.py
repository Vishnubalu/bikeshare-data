import time
import pandas as pd
import numpy as np
import password


CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }
months = ['all','january', 'february', 'march', 'april', 'may', 'june']
cities = ['chicago','new york city','washington']
days = ['all','monday','tuesday','wednesday','thursday','friday','saturday','sunday']
def raw_data():
    city = input("select any city to see raw data :\n ").lower()
    while(city not in cities):
        city = input("There is no such city, please enter valid city name : ").lower()
    df = pd.read_csv(CITY_DATA[city])
    i = 1
    while(True):
        print(df.head(5*i))
        if(input("would you like to see more (enter yes or no): ").lower() != 'yes'):
            break
        else:
            i+=1
def get_filters():
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs

    city = input("Would you like to see specific data for Chicago,New york city, or Washington :\n ").lower()
    while(city not in cities):
        city = input("There is no such city, please enter valid city name : ").lower()
    # get user input for month (all, january, february, ... , june)
    month = input("month (all, january, february, ... , june)   :\n ").lower()
    while(month not in months):
        month = input("please enter a valid month name as shown above : ").lower()
    # get user input for day of week (all, monday, tuesday, ... sunday)
    
    day = input("day of week (all, monday, tuesday, ... sunday) :\n ").lower()
    while(day not in days):
        day = input("please enter valid day name as shown above : ").lower()

    print('-*-'*40)
    return city, month, day


def load_data(city, month, day):

    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name

    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]
    return df


def time_stats(df):
    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    months = ['january', 'february', 'march', 'april', 'may', 'june']
    # display the most common month
    df['month'] = df['Start Time'].dt.month
    popular_month = df['month'].mode()[0]
    print("Most Common Month : ", months[popular_month-1])
    # display the most common day of week
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    popular_weekday = df['day_of_week'].mode()[0]
    print("Most Common DAY   : ",popular_weekday)
    # display the most common start hour
    df['hour'] = df['Start Time'].dt.hour

    popular_hour = df['hour'].mode()[0]
    print("Most Common HOUR  : ",popular_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-*-'*40)


def station_stats(df):

    print('\n\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    popular_start = df['Start Station'].mode()[0]
    print("most commonly used start station:",popular_start)
    # display most commonly used end station
    popular_end = df['End Station'].mode()[0]
    print("most commonly used end station : ",popular_end)

    # display most frequent combination of start station and end station trip
    trip_series = df["Start Station"].astype(str) + " to " + df["End Station"].astype(str)
    print(" most frequent combination     : ",trip_series.describe()['top'])

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-*-'*40)


def trip_duration_stats(df):

    print('\n\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    print("Total No.of Trips     : ",df.describe()['Trip Duration']['count'])
    print("Total Trip Duration in seconds   : ",df['Trip Duration'].sum())
    # display mean travel time
    print("Average Trip Duration in seconds :",df.describe()['Trip Duration']['mean'])
    #print("Average Trip Duration : ",df['Trip Duration'].sum()/df.describe()['Trip Duration']['count'])
    print("\n\nThis took %s seconds." % (time.time() - start_time))
    print('-*-'*40)


def user_stats(df):
    
    print('\n\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types 
    print(df['User Type'].value_counts())

    # Display counts of genderS
    print("\n",df['Gender'].value_counts())

    # Display earliest, most recent, and most common year of birth
    print("\nMost Earliest year of birth  : ",df['Birth Year'].describe()['min'])
    print("Most Recent year of birth      : ",df['Birth Year'].describe()['max'])
    print("Most Common Year year of birth : ",df['Birth Year'].describe()['75%'])

    print("\n\nThis took %s seconds." % (time.time() - start_time))
    print('-*-'*40)


def main():
    print('\n\n\t\t***** Hello! Let\'s explore some US bikeshare data! *****\n\n')
    print("\n\n Cities :  ", cities) 
    while True:
        x = input("would you like to see raw data of any city (for raw data -yes, for specific data -no)  : ").lower()
        if(x == 'yes'):
            raw_data()
        else:
            city, month, day = get_filters()
            df = load_data(city, month, day)
            time_stats(df)
            station_stats(df)
            trip_duration_stats(df)
            user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            print("  ***HAVE A NICE DAY***  ")
            break

if __name__ == "__main__":
    main()
    
'''
if __name__ == "__main__":
    a = input("user name : ")
    b = input("password : ")
    response = password.Check(a,b)
    if (response.checkpass()):
        main()
    else:
        print("Permission Denied By VISHNU ")

'''
