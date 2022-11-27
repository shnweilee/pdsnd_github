import time
import pandas as pd
import numpy as np


CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }


def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    
    # To get user input for city (chicago, new york city, washington).
    while True:
        city =  input('Would you like to see data for Chicago, New York City, or Washington?').lower()
        
        if city in CITY_DATA.keys():
            break
        else:
            print('\nInvalid input, please try again.\n')
    
    # To get user input for month (all, january, february, ... , june)
    month = input('Which month? January, February, March, April, May, June. Otherwise enter ALL').lower()
    
    # To get user input for day of week (all, monday, tuesday, ... sunday)
    day = input('Which day? Monday, Tuesday, Wednesday...Sunday. Otherwise enter ALL').lower()

    print('-'*40)
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
    
    #load data to dataframe
    df = pd.read_csv(CITY_DATA[city])
    
    #convert Start Time to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    
    #extract month, day of week and hour from Start Time column
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    df['hour'] = df['Start Time'].dt.hour
    
    #filter by month
    if month != 'all':
        #use index of months list to get int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
            
        #filter by month to create new df
        df = df[df['month'] == month]
    
    #filter by day of week
    if day != 'all':
        #filter by day if week to create new df
        df = df[df['day_of_week'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    most_common_month = df['month'].mode()[0]        
    print('Most Common Month: ', most_common_month)

    # TO DO: display the most common day of week
    most_common_day = df['day_of_week'].mode()[0]
    print("Most Common Day of the Week: ", most_common_day)

    # TO DO: display the most common start hour
    most_common_hour = df['hour'].mode()[0]
    print("Most Common Start Hour: ", most_common_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

    
def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    most_common_start_station = df['Start Station'].mode()[0]
    print('Most Common Start Station: ', most_common_start_station)

    # TO DO: display most commonly used end station
    most_common_end_station = df['End Station'].mode()[0]
    print('Most Common End Station: ', most_common_end_station)

    # TO DO: display most frequent combination of start station and end station trip
    combination_group = df.groupby(['Start Station', 'End Station'])
    most_frequent_combination = combination_group.size().sort_values(ascending=False).head(1)
    print('Most Frequent Combination of Start Station and End Station Trip: ', most_frequent_combination)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

    
def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time = df['Trip Duration'].sum()
    print('Total Travel Time: ', total_travel_time)

    # TO DO: display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    print('Mean Travel Time: ', mean_travel_time)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

    
def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    print('Counts of User Types: ', df['User Type'].value_counts())

    # NOTE: Washington data does not have Gender and Birth Year
    # TO DO: Display counts of gender
    try:
        print('Counts of Gender: ', df['Gender'].value_counts())
    except:
        print('Gender is unavailable in this data.')
                                     
    # TO DO: Display earliest, most recent, and most common year of birth
    try:
        earliest_year = df['Birth Year'].min()
        print('Earliest Year of Birth: ', earliest_year)

        most_recent_year = df['Birth Year'].max()
        print('Most Recent Year of Birth: ', most_recent_year)

        most_common_year = df['Birth Year'].mode()[0]
        print('Most Common Year of Birth: ', most_common_year)

    except:
        print('Birth Year is unavaiable in this data.')
        
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

    
# Option for user to view raw data
def show_raw_data(df):
    row = 0
    while True:
        view_raw_data = input('Would you like to see the raw data? Enter YES or NO').lower()
        
        if view_raw_data == 'yes':
            print(df.iloc[row:row + 5])
            row += 5
        elif view_raw_data == 'no':
            break
        else: 
            print('You have entered the wrong input. Please try again.')

    
def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        show_raw_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
