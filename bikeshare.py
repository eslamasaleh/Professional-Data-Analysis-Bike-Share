import time
import pandas as pd
import numpy as np


CITY_DATA = { 'Chicago': 'chicago.csv',
              'New York City': 'new_york_city.csv',
              'Washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    cities=["Chicago","New York City","Washington"]
    Months=["January","February","March","April","May","June","All"]
    Days=["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday","All"]
    print('Hello! Let\'s explore some US bikeshare data!')
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city=str(input('What city (Chicago, New York City, Washington) you want to discover? '))
    city=city.title()
    #print(Tcity)
    if city not in cities:
        while True:
            print("Ohhh, Something is wrong. Please try again\n")
            cityx=str(input('Please Choose one of these Options (Chicago, New York City, Washington)\n'))
            Tcityx=cityx.title()
            #print(Tcityx)
            if Tcityx in cities:
                city=Tcityx
                break

    # get user input for month (all, january, february, ... , june)
    month=input('What month do you want to see?(All, January, February, March, April, May, June)\n ')
    month=month.title()
    if month not in Months:
        while True:
            print("Ohhh, Something is wrong. Please try again\n")
            Mx=str(input('Please Choose one of these Options (All, January, February, March, April, May, June)\n'))
            Mx=Mx.title()
            if Mx in Months:
                month=Mx
                break

    # get user input for day of week (all, monday, tuesday, ... sunday)
    day=input('What day do you want to see?(all,Sunday, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday)\n')
    day=day.title()
    if day not in Days:
        while True:
            print("Ohhh, Something is wrong. Please try again\n")
            Dx=str(input('Please Choose one of these Options (all,Sunday, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday)\n'))
            Dx=Dx.title()
            if Dx in Days:
                day=Dx
                break
    print('-'*60)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """

    df=pd.read_csv(CITY_DATA[city])


    df['Start Time']=pd.to_datetime(df['Start Time'])

    #Getting Month as Jan Feb Mar Apr May June(dt.strftime(%b))
    df['Month']=df['Start Time'].dt.strftime('%B')

    #Getting Name of days Friday saturday sunday monday tuesday wednesday thursday(dt.strftime(%A))
    df['Day']=df['Start Time'].dt.strftime('%A')

    if month != 'All':
        df =df[df['Month']==month.title()]


    if day !='All':
        df =df[df['Day']==day.title()]

    #print(df)

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    MNmost=df['Month'].mode()[0]
    MNcount=df['Month'].value_counts()[MNmost]
    print("The most common  Month: {}       Count: {}\n".format(MNmost,MNcount))
    # display the most common day of week
    Dmost=df['Day'].mode()[0]
    Dcount=df['Day'].value_counts()[Dmost]
    print("The most common  Day: {}          Count: {}\n".format(Dmost,Dcount))

    # display the most common start hour
    df['Hour']=df["Start Time"].dt.strftime("%H")
    Hr=df['Hour'].mode()[0]
    Hrc=df['Hour'].value_counts()[Hr]
    print("The most common Start Hour: {}         Count: {}\n".format(Hr,Hrc))
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*60)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    STmost=df['Start Station'].mode()[0]
    STcount=df['Start Station'].value_counts()[STmost]
    print("The most commonly used Start Station :{} count: {}\n".format(STmost,STcount))

    # display most commonly used end station
    ENDmost=df['End Station'].mode()[0]
    ENDcount=df['End Station'].value_counts()[ENDmost]
    print("The most commonly used End Station : {} count: {}\n".format(ENDmost,ENDcount))

    # display most frequent combination of start station and end station trip
    combin=df.groupby(['Start Station','End Station'])
    cntcomb=combin['Trip Duration'].count().idxmax()
    print("The most frequent combination of start station and end station trip:\n",cntcomb)
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*60)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    Tt=df['Trip Duration'].sum()


    # display mean travel time
    AverTt=df['Trip Duration'].mean()

    #print(Tt,AverTt)

    print("Total Travel Time: {}\n".format(Tt))
    print("Average Travel Time: {}\n ".format(AverTt))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*60)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    users=df['User Type'].value_counts()
    print('The Counts of User Types:-\n')
    print(pd.DataFrame(users))
    print('\n')
    # Display counts of gender
    try :
        gender=df['Gender'].value_counts()
        print('\n')
        print('The Counts of Gender:-\n')
        print(pd.DataFrame(gender))
        print('\n')
    except KeyError:
        print("Gender only avaiable in Chicago & New York City \n ")

    # Display earliest, most recent, and most common year of birth
    try:
        earl=df['Birth Year'].min()
        recent=df['Birth Year'].max()
        Mostcom=df['Birth Year'].mode()[0]
        print("The Earliest Year of Birth : {}\n".format(earl))
        print("The Most Recent Year of Birth : {}\n".format(recent))
        print("The Most Common Year of Birth : {}\n".format(Mostcom))
    except KeyError:
        print("Information of Year of Birth only avaiable in Chicago & New York City\n ")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*60)
def StatisticsDisplay(df):
    '''Function print 5 raw of data (Yes,No)
    '''
    usercheck=input("Do you want to display users statistics?(Yes,No) ")
    usercheck=usercheck.title()
    i=0
    while True:
        if usercheck=='Yes':
            print(df.iloc[i:i+5]) # Can print only user statistics print(df.iloc[i:i+5,6:9])
            usercheck=input("Do you want to display more users statistics?(Yes,No)")
            usercheck=usercheck.title()
            i+=5
        else:
            break
def main():
    count=0
    while count<5 :
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        StatisticsDisplay(df)
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        count+=1
        if count==4 and restart=='yes':
            print('Sorry,System will SHUT DOWN after using 5 Times')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
