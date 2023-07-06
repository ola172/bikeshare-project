import pandas as pd

CITY_DATA = { 'chicago': 'F:\\year3\\projects\\bikeshare\\chicago.csv',
              'new york city': 'F:\\year3\\projects\\bikeshare\\new_york_city.csv',
              'washington': 'F:\\year3\\projects\\bikeshare\\washington.csv' }
cities=['chicago','new york city','washington']
months=['january','february','march','april','may','june','all']
days=['saturday','sunday','monday','tuesday','wednesday','thursday','friday','all']


    
###functions used in the program
def GetData ():
    '''ask user to choose city ,month and day to analyze
       it returns:
           str(city):name of the city to analyze
           str(day):name of the day to filter the data(weekday)
           str(month):name of the month to filter the data(first 6 months of the year)'''
    #get city
    #choose data for filtering
    cityin=input("choose data for filtering (chicago - new york city - washington)? \n")
    cityin=cityin.lower()
    ##check if the input of city is correct
    if cityin in cities:
        city=cityin
    elif cityin not in cities:
        cityin=input("you input is invalid... you should choose one of these cities : (chicago - new york city- washington)\n choose city again \n" )
        cityin=cityin.lower()
    #----------------------------------------------------
    #get month and day
    ## (get day)
    ##check if the input of day is correct
    dayin=input("choose day.. \n (saturday, sunday, monday, tuesday, wednesday, thursday, friday, all) \n")
    dayin=dayin.lower()
    ##check if the input of day is correct
    if dayin in days:
        day=dayin  
    else:
        dayin=input("you input is invalid... you should enter correct format\n choose day again \n " )
        dayin=dayin.lower()   
     #-----------------------------------------------------   
    #(get month)
    monthin=input("choose one of the first 6 months.. \n 'january','february','march','april','may','june','all' \n")
    monthin=monthin.lower()
    ##check if the input of day is correct
    if monthin in months :
        month=monthin
    else:
        monthin=input("you input is invalid.. you should enter correct format  (from 1 to 12)\n choose month again  \n" )
        month=monthin.lower()   
  
    
    return city, day,month


def LoadData(city,month,day):
    '''take the output of GetData () (city, day,month) and load the data for chosen city ,
       it makes new columns in data for month, day_name and hour
       then it filters data by day and month chosen
       it returns:
           DataFrame(data):filteres data to analyze'''
       
    
    #load data and  convert the Start Time column to datetime
    data = pd.read_csv(CITY_DATA[city])
    data['Start Time'] = pd.to_datetime(data['Start Time'])
    
    # extract month , hour and weekday from Start Time to create new columns
    data['month'] = data['Start Time'].dt.month
    data['day_name'] = data['Start Time'].dt.weekday_name
    data['hour'] = data['Start Time'].dt.hour
    
    #filtering data
    if day != 'all':
        data = data[data['day_name']==day.title()]
    if month != 'all':
        month = (( months.index(month))+1)
        data=data[data['month']==month]  
    return data 


#function for most common time
def MostTime (data):
    '''this function analyze filtered data to answer some qusetions:
          1. the most common month in filtered data (first it converts str(month) to the corresponding integer)
          2.the most common day in filtered data
          3.the most common hour in filtered data'''
           
    #most common month
    print("most common month: ",data['month'].mode())
    #most common day
    print("most common day: ",data['day_name'].mode())
    #most common hour
    popular_hour = list(data['hour'])
    count={}
    for i in popular_hour:
        if i in count:
            count[i]+=1
        else:
            count[i]=1
    m=max(count.values())
    for i in count:
        if count[i]==m:
            print('most common hour of day:',i)

#function for most common station    
def MostStation (data):
    '''this function analyze filtered data to answer some qusetions:
          1. the most common start station in filtered data 
          2.the most common end station in filtered data
          3.the most frequent start and end station in filtered data'''
          
    #2 Popular stations and trip
    print("most common start station: ",data['Start Station'].mode())
    print("most common end station: ",data['End Station'].mode())
    group_start_and_end=data.groupby(['Start Station','End Station'])
    sorteddata=group_start_and_end.size().sort_values(ascending=False)
    print('Most frequent start and end station: ',sorteddata.head(1) )
    
#function for most common trip    
def MostTrip (data):
    '''this function analyze filtered data to answer some qusetions:
          1. thetotal travel time in filtered data 
          2.the average travel time in filtered data'''
          
    #total travel time
    print('total travel time: ',data['Trip Duration'].sum())
    #average travel time
    print('average travel time: ',data['Trip Duration'].mean())

#function for user info
def UserInfo (data):
    '''this function analyze filtered data to answer this qusetions:
           (the counts of each user type in filtered data)
         '''
    #counts of each user type
    print('counts of each user type: ', data['User Type'].value_counts())
def Userinfo(data):   
    '''this function is available for NYC and Chicago only (not available for washington)
    this function analyze filtered data to answer some qusetions:
          1. the counts of each gender in filtered data
          2.the cearliest year of birth in filtered data
          3.the most recent year of birth in filtered data
          4.the most common year of birth in filtered data
          '''
          
    #counts of each gender (only available for NYC and Chicago)  
    print('counts of each gender: ', data['Gender'].value_counts())
    #earliest, most recent, most common year of birth (only available for NYC and Chicago)    
    print('cearliest year of birth: ',  data['Birth Year'].min())
    print('most recent year of birth: ',  data['Birth Year'].max())
    print('most common year of birth : ',  data['Birth Year'].mode())
   
#function for showing data 
def ShowData (data):
    '''this function asks user if he/she would like to see a sample of data
       it continues asks him and shows data ehile the answer is "yes" 
       and it stops showing data if the answer is "no"'''
    m=data.shape[0]
    while (m>=5):
        Q=input("do you want do see another set of data?    (answers: yes or no) \n")
        if Q=='yes':
            print(data.head(5))
            data=data.iloc[5: , :]
        else:
            break
        
    
def Program ():
    while True:
        '''this function call the other functions to run the program and analyze the data'''
        city,day,month=GetData()
        data=LoadData(city,month,day)
        MostTime (data)
        MostStation (data)
        MostTrip (data)
        if city=='new york' or city=='chicago':
            UserInfo (data)
            Userinfo(data)
        else:
            UserInfo (data)
        ShowData (data)
       
# Start the program
print("                        welcome ^-^ ")
Program ()

    

       
    

        
    



