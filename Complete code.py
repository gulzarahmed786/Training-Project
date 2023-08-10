#!/usr/bin/env python
# coding: utf-8

# # IPL TEAM MANAGEMENT

# Hello Everyone I am Gulzar Ahmed As we knows that we got a project for player performance analysis and for selecting those player who got better performance from 2016 to 2022 and release their name for auction for 2024IPL according to their bit value as i assigned bit value for best batsman is 50000000 and for best bowler 750000000 and as i performed in this project statistical analysis of players and then select them in two way as of best batsman and best bowler i selected top 10 batsman and top 10 bowler

# Here are code for my analysis for data exploration,scrapping data and forming team ,handling with value redundancy and missling values i did everything according to my approach as i could approach

# as of my reference for my analysis , exploring data there is so many resources some of as kaggle and bcci for data  collection  and for my analytical skill 

# at first i gathered my data and then setting up my enviroment for coding and analytical skill and then first i imported my required library for data handling and loading i imported pandas for data handling and matplotlib for visualization

# # Library Importing

# In[16]:


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# # handling Missing Values

# after setting required library then i started my coding part as of i first created a list name as dfs which contains file paths of multiple csv files that are related to players score of batting and bowling this file are from different year 2016 to 2022 
# 
# in the next line defining a function named as check_missing_value to read a csv file or check for missing values and print it 
# 
# the function is started by reading the  csv file using pd.read_csv(file_path)
# 
# and then prints a message indicating which file is being processed: print(f"\nChecking missing values for file: {file_path}")
# 
# Next, it prints the column names that have missing values using the df.columns[df.isnull().any()] This will display only the columns that contain at least one missing value.
# 
#  then calculates and prints the total number of missing values in each column using "df.isnull()"".sum()". The "isnull()" function checks for missing (NaN) values, and sum() computes the number of missing values for each column.
# 
# Finally, it calculates and prints the total number of missing values in the entire DataFrame using df.isnull().sum().sum().
# 
# In the if __name__ == "__main__": block, the code iterates through each CSV file path in the dfs list and calls the check_missing_values
# 
# after running whole this section code for checking null value or missing value it output and code behind its as shown below.

# In[17]:


dfs = [r"C:\Users\ggulz\Downloads\archive\IPL Player Stats\Batting Stats\BATTING STATS - IPL_2016.csv",
r"C:\Users\ggulz\Downloads\archive\IPL Player Stats\Batting Stats\BATTING STATS - IPL_2017.csv",
r"C:\Users\ggulz\Downloads\archive\IPL Player Stats\Batting Stats\BATTING STATS - IPL_2018.csv",
r"C:\Users\ggulz\Downloads\archive\IPL Player Stats\Batting Stats\BATTING STATS - IPL_2019.csv",
r"C:\Users\ggulz\Downloads\archive\IPL Player Stats\Batting Stats\BATTING STATS - IPL_2020.csv",
r"C:\Users\ggulz\Downloads\archive\IPL Player Stats\Batting Stats\BATTING STATS - IPL_2021.csv",
r"C:\Users\ggulz\Downloads\archive\IPL Player Stats\Batting Stats\BATTING STATS - IPL_2022.csv",
r"C:\Users\ggulz\Downloads\archive\BOWLING STATS - IPL_2016.csv",
r"C:\Users\ggulz\Downloads\archive\BOWLING STATS - IPL_2017.csv",
r"C:\Users\ggulz\Downloads\archive\BOWLING STATS - IPL_2018.csv",
r"C:\Users\ggulz\Downloads\archive\BOWLING STATS - IPL_2019.csv",
r"C:\Users\ggulz\Downloads\archive\BOWLING STATS - IPL_2020.csv",
r"C:\Users\ggulz\Downloads\archive\BOWLING STATS - IPL_2021.csv",
r"C:\Users\ggulz\Downloads\archive\BOWLING STATS - IPL_2022.csv"]

def check_missing_values(file_path):
    df = pd.read_csv(file_path)
    print(f"\nChecking missing values for file: {file_path}")
    print("Columns with missing values:")
    print(df.columns[df.isnull().any()])
    print(f"Total missing values in each column:\n{df.isnull().sum()}")
    print(f"Total missing values in the entire dataframe: {df.isnull().sum().sum()}")

if __name__ == "__main__":
    for csv_file in dfs:
        check_missing_values(csv_file)


# # Finding Total Number Of column and rows

# again in this section of code i handling with finding the total number of columns and rows are present in this data set for this check i did this code whose explanation of code are
# 
# first again i define a function called get_rows_and_columns that takes a file_path as an argument This function is used to read a CSV file, determine whether it's a batting or bowling file, extract the year from the file name, and then print the file type, year, number of rows, and number of columns.
# 
# The function starts by reading the CSV file using pd.read_csv(file_path). As mentioned earlier
# 
# The function uses a conditional expression to determine the file type (Batting or Bowling) based on whether the string 'Batting' is present in the file_path. If 'Batting' is found, file_type is set to 'Batting'; otherwise, it is set to 'Bowling'.
# 
# The function extracts the year from the file_path using string manipulation. It first splits the file_path string by underscores ('_') and selects the last part of the resulting list using [-1]. Then, it further splits the selected part by periods ('.') and takes the first part of that split using [0]. This should extract the year from the file name. 
# 
# the function  then prints the file type and year using the extracted information: print(f"\nFile: {file_type} {year}")
# 
# Next, it prints the number of rows in the DataFrame using the shape[0]. The shape returns a tuple with the number of rows and columns, and shape[0] gives the number of rows
# 
# Similarly, it prints the number of columns in the DataFrame using the shape[1] attribute. shape[1] gives the number of columns.
# 
# In the if __name__ == "__main__": block, the code iterates through each CSV file path in the dfs list and calls the get_rows_and_columns function for each file
# This will print information about the file type (Batting or Bowling), the year, the number of rows, and the number of columns for each CSV file

# In[18]:


def get_rows_and_columns(file_path):
    df = pd.read_csv(file_path)
    file_type = 'Batting' if 'Batting' in file_path else 'Bowling'
    year = file_path.split('_')[-1].split('.')[0]
    print(f"\nFile: {file_type} {year}")
    print(f"Number of Rows: {df.shape[0]}")
    print(f"Number of Columns: {df.shape[1]}")

if __name__ == "__main__":
    for csv_file in dfs:
        get_rows_and_columns(csv_file)


# # To know All column Names 

# at next section of code of my project i started with again by defining function 
# a function called identify_columns that takes a file_path as an argument
# reading the CSV file using pd.read_csv(file_path). As mentioned earlier
# It prints a message indicating the file for which the columns are being identified: print(f"\nColumns in {file_path}:")
#     Next, it prints the column names present in the DataFrame using df.columns
#     if __name__ == "__main__": block, the code iterates through each CSV file path in the dfs list and calls the identify_columns function for each file.
#     

# In[19]:


def identify_columns(file_path):
    df = pd.read_csv(file_path)
    print(f"\nColumns in {file_path}:")
    print(df.columns)

if __name__ == "__main__":
    for csv_file in dfs:
        identify_columns(csv_file)


# # To gain Dataframe Information

# function that i define every it use to take argument and call for our use cases
#  DataFrame for which the information is being displayed: print(f"\nInformation about these DataFrame {file_path}:")
#  
#  necxt it prints the information about DataFrame using df.info() method of a dataframe gives a concise summary of the dataframe including the number of non-null value and data types of each column
#  

# In[20]:


def dataframe_information(file_path):
    df = pd.read_csv(file_path)
    print(f"\nInformation about these DataFrame {file_path}:")
    print(df.info())

if __name__ == "__main__":
    for csv_file in dfs:
        dataframe_information(csv_file)


# # Summary statics of numerical Columns

# in this section of code i try to prints the summary statistics for numerical columns in the DataFrame using df.describe(). The describe() method of a DataFrame provides various summary statistics, including count, mean, standard deviation, minimum, 25th percentile, median (50th percentile), 75th percentile, and maximum values for each numerical column

# In[21]:


def summary_statics(file_path):
    df = pd.read_csv(file_path)
    print(f"\nSummary statistics for numerical columns {file_path}:")
    print(df.describe())

if __name__ == "__main__":
    for csv_file in dfs:
        summary_statics(csv_file)


# # For Columns name is used for And their Alliases of short form for Bowlers

# a dictionary named column_aliases_of_Bowler,This dictionary contains column names found in a dataset of bowler statistics to their corresponding descriptive names (values).
# 
# for loop iterates through each key-value pair in the column_aliases_of_Bowler dictionary.
# 
#  it prints the key (column name) followed by a colon and then the value (alias/descriptive name) for that column.
#  
#  The loop also adds a comma (,) after each key-value pair, which means the output will have line breaks after each comma  creating a more readable and organized
#  The loop iterates over all the key-value pairs in the dictionary, and each pair is printed as a separate line.

# In[22]:


column_aliases_of_Bowler = {
    'POS': "Player's rank based on most wickets",
    'Player': "Player's name",
    'Mat': "Matches played",
    'Inns': "Innings Played",
    'Ov': "Overs",
    'Runs': "Total runs given by bowler",
    'Wkts': "Total Wickets taken",
    'BBI': "Best Bowling in Innings",
    'Avg': "Average",
    'Econ': "Economy",
    'SR': "Strike Rate",
    '4w': "4 wickets haul",
    '5w': "5 wickets haul"
}
print("Bowlers'column Name Aliases are :\n\n")
# Print the dictionary with line breaks after each comma
for key, value in column_aliases_of_Bowler.items():
    print(f"{key}: {value},")


# # Alliases and their uses in dataframe of Batsaman

# the use case line of code also same as bowler but the common aliases are difenrent in the batsman dataset so the aliases are diferently declared for it but writting of code is same

# In[23]:


column_aliases_of_batsman={
'POS': "Player's rank based on most runs",
'Player' : "Player's name",
'Mat' : "Matches played",
'Inns' : "Innings Played",
'NO' : "Number of Not Out in innings",
'Runs' : "Total Runs scored by a player",
'HS' : "Highest Score in innings [* -- Not Out in that Innings]",
'Avg' : "Average",
'BF' : "Bowls faced",
'SR' : "Strike Rate",
'100' : "No of times 100 scored",
'50' : "No of the times 50 scored",
'4s' : "Total Fours Scored",
'6s' : "Total Sixes Scored"
}

print("Batsman's column Name Aliases are :\n\n")
# Print the dictionary with line breaks after each comma
for key, value in column_aliases_of_batsman.items():
    print(f"{key}: {value},")


# # first 5 rows of data frame from batsman files

# inn this section of code i defined a function for batsman dataset and store or give all batsaman dataset path and seprated of all path giving( , )in the different paths btw
# and the creating a enpty dataframe for storing new data that extracted from dataset 
# 
#  then prints a message indicating the data for which IPL season is being displayed. It extracts the year from the file name using string manipulation (splitting the file name and selecting the last part )to display the ipl season.
#  
#  After that, it prints the first 5 rows of the DataFrame using df_season.head(5). This gives a preview of the data for the corresponding IPL season.
#  
#  After the loop completes, it concatenates all the DataFrames in the data_frames_Batsman list into a single DataFrame named combined_data. The pd.concat function is used to concatenate the DataFrames along the rows, effectively combining all the data into a single DataFrame.
#  
#  after the loop, the variable combined_data contains the combined data of all IPL seasons from 2016 to 2022 for batsman statistics.

# In[24]:


dfs_of_Batsman = [r"C:\Users\ggulz\Downloads\archive\IPL Player Stats\Batting Stats\BATTING STATS - IPL_2016.csv",
r"C:\Users\ggulz\Downloads\archive\IPL Player Stats\Batting Stats\BATTING STATS - IPL_2017.csv",
r"C:\Users\ggulz\Downloads\archive\IPL Player Stats\Batting Stats\BATTING STATS - IPL_2018.csv",
r"C:\Users\ggulz\Downloads\archive\IPL Player Stats\Batting Stats\BATTING STATS - IPL_2019.csv",
r"C:\Users\ggulz\Downloads\archive\IPL Player Stats\Batting Stats\BATTING STATS - IPL_2020.csv",
r"C:\Users\ggulz\Downloads\archive\IPL Player Stats\Batting Stats\BATTING STATS - IPL_2021.csv",
r"C:\Users\ggulz\Downloads\archive\IPL Player Stats\Batting Stats\BATTING STATS - IPL_2022.csv",]

data_frames_Batsman = []

for dfs_of_Batsman in dfs_of_Batsman:
    df_season = pd.read_csv(dfs_of_Batsman)
    print(f"\nData for {dfs_of_Batsman.split('_')[-1].split('.')[0]} IPL Season:")
    print(df_season.head(5)) 
    data_frames_Batsman.append(df_season)
    
combined_data = pd.concat(data_frames_Batsman)


# # first five rows of bowler from dataframe

# this section of coding is also same like above but the use case of this to print first five row of dataset from each datafile and the codding lline is also same like above because using to print first five row of data

# In[25]:


dfs_of_Bowler = [r"C:\Users\ggulz\Downloads\archive\BOWLING STATS - IPL_2016.csv",
r"C:\Users\ggulz\Downloads\archive\BOWLING STATS - IPL_2017.csv",
r"C:\Users\ggulz\Downloads\archive\BOWLING STATS - IPL_2018.csv",
r"C:\Users\ggulz\Downloads\archive\BOWLING STATS - IPL_2019.csv",
r"C:\Users\ggulz\Downloads\archive\BOWLING STATS - IPL_2020.csv",
r"C:\Users\ggulz\Downloads\archive\BOWLING STATS - IPL_2021.csv",
r"C:\Users\ggulz\Downloads\archive\BOWLING STATS - IPL_2022.csv"]
data_frames_Batsman = []

for dfs_of_Bowler in dfs_of_Bowler:
    df_season_Bowling = pd.read_csv(dfs_of_Bowler)
    print(f"\nData for {dfs_of_Bowler.split('_')[-1].split('.')[0]} IPL Season:")
    print(df_season_Bowling.head(5)) 
    data_frames_Batsman.append(df_season_Bowling)
    
combined_data = pd.concat(data_frames_Batsman)


# # Top 10 performing player in each role batsman and as bowler

# in this section of code i print top perfroming players in a particular year
# 
# here i defines a function called load_csv that takes a file_path as an argument and tries to read the CSV file using pd.read_csv(file_path)
# 
# If the file is found, it returns the DataFrame read from the CSV. If the file is not found, it prints a message indicating that and returns None
# 
# and then defines a function called find_best_player that takes a DataFrame df, a metric (performance metric) to evaluate players, and an optional num_players argument (default value is 1) to specify the number of top players to be returned. The function sorts the DataFrame based on the specified metric in descending order and returns the top num_players players.
# 
#  defines the main function form_new_team, which takes the year, batting_file_path, and bowling_file_path as arguments 
#  it loads the batting and bowling CSV files using the load_csv function.
#  
#  It checks if either the batting or bowling DataFrame is None, which would indicate that there was an issue loading the CSV files, If so, the function returns without proceeding further
#  
#  The function then proceeds to find the best batsman and best bowler for the new team based on their batting and bowling averages using the find_best_player function.
#  
# After finding the best batsman and best bowler, it prints the results for the given year, including the best batsman's information and the best bowler's information.
# 
# In the if __name__ == "__main__": block, the code creates a list years_list containing the years from 2016 to 2022
# 
# It creates a dictionary file_paths_by_year, where each key represents a year, and the value is another dictionary containing the file paths for the corresponding batting and bowling CSV files.
# 
# The code then iterates through each year in years_list, gets the corresponding batting and bowling file paths from the file_paths_by_year dictionary, and calls the form_new_team function for each year, displaying the best batsman and best bowler for each IPL season.

# In[26]:


# Load CSV files
def load_csv(file_path):
    try:
        return pd.read_csv(file_path)
    except FileNotFoundError:
        print(f"File not found: {file_path}")
        return None

# Find the best player for each role based on performance metrics
def find_best_player(df, metric, num_players=1):
    sorted_df = df.sort_values(by=[metric], ascending=False)
    return sorted_df.head(num_players)

# Main function to form a new team
def form_new_team(year, batting_file_path, bowling_file_path):
    batting_df = load_csv(batting_file_path)
    bowling_df = load_csv(bowling_file_path)

    if batting_df is None or bowling_df is None:
        return

    # Finding the best batsman and best bowler for the new team
    best_batsman = find_best_player(batting_df, 'Avg', num_players=1)
    best_bowler = find_best_player(bowling_df, 'Avg', num_players=1)

    # Printing the results
    print(f"Year: {year}")
    print("Best Batsman:")
    print(best_batsman)
    print("Best Bowler:")
    print(best_bowler)

if __name__ == "__main__":
    years_list = [2016, 2017, 2018, 2019, 2020, 2021, 2022]
    file_paths_by_year = {
        2016: {
            'batting': r"C:\Users\ggulz\Downloads\archive\IPL Player Stats\Batting Stats\BATTING STATS - IPL_2016.csv",
            'bowling': r"C:\Users\ggulz\Downloads\archive\BOWLING STATS - IPL_2016.csv",
        },
        2017: {
            'batting': r"C:\Users\ggulz\Downloads\archive\IPL Player Stats\Batting Stats\BATTING STATS - IPL_2017.csv",
            'bowling': r"C:\Users\ggulz\Downloads\archive\BOWLING STATS - IPL_2017.csv",
        },
        2018: {
            'batting': r"C:\Users\ggulz\Downloads\archive\IPL Player Stats\Batting Stats\BATTING STATS - IPL_2018.csv",
            'bowling': r"C:\Users\ggulz\Downloads\archive\BOWLING STATS - IPL_2018.csv",
        },
        2019: {
            'batting': r"C:\Users\ggulz\Downloads\archive\IPL Player Stats\Batting Stats\BATTING STATS - IPL_2019.csv",
            'bowling': r"C:\Users\ggulz\Downloads\archive\BOWLING STATS - IPL_2019.csv",
        },
        2020: {
            'batting': r"C:\Users\ggulz\Downloads\archive\IPL Player Stats\Batting Stats\BATTING STATS - IPL_2020.csv",
            'bowling': r"C:\Users\ggulz\Downloads\archive\BOWLING STATS - IPL_2020.csv",
        },
        2021: {
            'batting': r"C:\Users\ggulz\Downloads\archive\IPL Player Stats\Batting Stats\BATTING STATS - IPL_2021.csv",
            'bowling': r"C:\Users\ggulz\Downloads\archive\BOWLING STATS - IPL_2021.csv",
        },
        2022: {
            'batting': r"C:\Users\ggulz\Downloads\archive\IPL Player Stats\Batting Stats\BATTING STATS - IPL_2022.csv",
            'bowling': r"C:\Users\ggulz\Downloads\archive\BOWLING STATS - IPL_2022.csv",
        },
        
    }

    for year in years_list:
        batting_file_path = file_paths_by_year[year]['batting']
        bowling_file_path = file_paths_by_year[year]['bowling']
        form_new_team(year, batting_file_path, bowling_file_path)


# # uses of useful columns instead of droping or deleteing columns

# in this section i use usefull columns and ignore those columns that aren't neccessary and print after sorting the players according to performance .
# 
# in this code defines a function called find_best_player that takes a DataFrame df, a metric (performance metric) to evaluate players, an optional num_players argument (default value is 1) to specify the number of top players to be returned, and a batting argument (default value is True) to indicate whether to find the best batsman or bowler. Depending on the value of the batting argument, it selects different columns as required (either batting columns or bowling columns).
# 
# Inside the find_best_player function, it sorts the DataFrame based on the specified metric in descending order using df.sort_values(by=[metric], ascending=False)
# 
# then checks whether batting is True. If True, it selects the required columns for the best batsman and stores them in the required_columns list. Otherwise, it selects the required columns for the best bowler and stores them in the required_columns list
# 
# The function returns the top num_players players along with the selected required columns using sorted_df.head(num_players)[required_columns].
# 
#  defines the main function form_new_team, which takes the year, batting_file_path, and bowling_file_path as arguments. Inside the function, it loads the batting and bowling CSV files using the load_csv function

# In[27]:


def load_csv(file_path):
    try:
        return pd.read_csv(file_path)
    except FileNotFoundError:
        print(f"File not found: {file_path}")
        return None

# Find the best player for each role based on performance metrics
def find_best_player(df, metric, num_players=1, batting=True):
    sorted_df = df.sort_values(by=[metric], ascending=False)
    if batting:
        required_columns = ['Player', 'HS', 'Avg', 'SR', 'Runs']
    else:
        required_columns = ['Player', 'BBI', 'Avg', 'Econ', 'SR', 'Wkts']
    return sorted_df.head(num_players)[required_columns]

# Main function to form a new team
def form_new_team(year, batting_file_path, bowling_file_path):
    batting_df = load_csv(batting_file_path)
    bowling_df = load_csv(bowling_file_path)

    if batting_df is None or bowling_df is None:
        return

    # Finding the best batsman and best bowler for the new team
    best_batsman = find_best_player(batting_df, 'Avg', num_players=1, batting=True)
    best_bowler = find_best_player(bowling_df, 'Avg', num_players=1, batting=False)

    # Printing the results
    print(f"Year: {year}")
    print("Best Batsman:")
    print(best_batsman)
    print("\nBest Bowler:")
    print(best_bowler)

if __name__ == "__main__":
    years_list = [2016, 2017, 2018, 2019, 2020, 2021, 2022]
    file_paths_by_year = {
        2016: {
            'batting': r"C:\Users\ggulz\Downloads\archive\IPL Player Stats\Batting Stats\BATTING STATS - IPL_2016.csv",
            'bowling': r"C:\Users\ggulz\Downloads\archive\BOWLING STATS - IPL_2016.csv",
        },
        2017: {
            'batting': r"C:\Users\ggulz\Downloads\archive\IPL Player Stats\Batting Stats\BATTING STATS - IPL_2017.csv",
            'bowling': r"C:\Users\ggulz\Downloads\archive\BOWLING STATS - IPL_2017.csv",
        },
        2018: {
            'batting': r"C:\Users\ggulz\Downloads\archive\IPL Player Stats\Batting Stats\BATTING STATS - IPL_2018.csv",
            'bowling': r"C:\Users\ggulz\Downloads\archive\BOWLING STATS - IPL_2018.csv",
        },
        2019: {
            'batting': r"C:\Users\ggulz\Downloads\archive\IPL Player Stats\Batting Stats\BATTING STATS - IPL_2019.csv",
            'bowling': r"C:\Users\ggulz\Downloads\archive\BOWLING STATS - IPL_2019.csv",
        },
        2020: {
            'batting': r"C:\Users\ggulz\Downloads\archive\IPL Player Stats\Batting Stats\BATTING STATS - IPL_2020.csv",
            'bowling': r"C:\Users\ggulz\Downloads\archive\BOWLING STATS - IPL_2020.csv",
        },
        2021: {
            'batting': r"C:\Users\ggulz\Downloads\archive\IPL Player Stats\Batting Stats\BATTING STATS - IPL_2021.csv",
            'bowling': r"C:\Users\ggulz\Downloads\archive\BOWLING STATS - IPL_2021.csv",
        },
        2022: {
            'batting': r"C:\Users\ggulz\Downloads\archive\IPL Player Stats\Batting Stats\BATTING STATS - IPL_2022.csv",
            'bowling': r"C:\Users\ggulz\Downloads\archive\BOWLING STATS - IPL_2022.csv",
        },
        
    }

    for year in years_list:
        batting_file_path = file_paths_by_year[year]['batting']
        bowling_file_path = file_paths_by_year[year]['bowling']
        form_new_team(year, batting_file_path, bowling_file_path)


# # Visualizing player top 10 batsman and bowlers Performance 

# in this section of code i visualize the players performance using bar graph it will show year wise player batsman and bowlers bar in a single graph and so on for all players

# In[28]:


def load_csv(file_path):
    try:
        return pd.read_csv(file_path)
    except FileNotFoundError:
        print(f"File not found: {file_path}")
        return None

def find_best_player(df, metric, num_players=1):
    return df.sort_values(by=[metric], ascending=False).head(num_players)

def form_new_team(year, batting_file_path, bowling_file_path):
    batting_df = load_csv(batting_file_path)
    bowling_df = load_csv(bowling_file_path)

    if batting_df is None or bowling_df is None:
        return

    best_batsman = find_best_player(batting_df, 'Avg', num_players=1)
    best_bowler = find_best_player(bowling_df, 'Avg', num_players=1)

    best_batsman['Avg'] = pd.to_numeric(best_batsman['Avg'])
    best_bowler['Avg'] = pd.to_numeric(best_bowler['Avg'])

    # Concatenate the DataFrames
    best_players = pd.concat([best_batsman, best_bowler])

    plt.figure(figsize=(10, 6))
    sns.barplot(data=best_players, x='Player', y='Avg', hue='POS', palette='pastel')
    plt.title(f"Best Batsman and Bowler - {year}")
    plt.xticks(rotation=45)
    plt.legend(title='Category', loc='upper left', labels=["Best Batsman", "Best Bowler"])

    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    years_list = [2016, 2017, 2018, 2019, 2020, 2021, 2022]
    file_paths_by_year = {
        2016: {
            'batting': r"C:\Users\ggulz\Downloads\archive\IPL Player Stats\Batting Stats\BATTING STATS - IPL_2016.csv",
            'bowling': r"C:\Users\ggulz\Downloads\archive\BOWLING STATS - IPL_2016.csv",
        },
        2017: {
            'batting': r"C:\Users\ggulz\Downloads\archive\IPL Player Stats\Batting Stats\BATTING STATS - IPL_2017.csv",
            'bowling': r"C:\Users\ggulz\Downloads\archive\BOWLING STATS - IPL_2017.csv",
        },
        2018: {
            'batting': r"C:\Users\ggulz\Downloads\archive\IPL Player Stats\Batting Stats\BATTING STATS - IPL_2018.csv",
            'bowling': r"C:\Users\ggulz\Downloads\archive\BOWLING STATS - IPL_2018.csv",
        },
        2019: {
            'batting': r"C:\Users\ggulz\Downloads\archive\IPL Player Stats\Batting Stats\BATTING STATS - IPL_2019.csv",
            'bowling': r"C:\Users\ggulz\Downloads\archive\BOWLING STATS - IPL_2019.csv",
        },
        2020: {
            'batting': r"C:\Users\ggulz\Downloads\archive\IPL Player Stats\Batting Stats\BATTING STATS - IPL_2020.csv",
            'bowling': r"C:\Users\ggulz\Downloads\archive\BOWLING STATS - IPL_2020.csv",
        },
        2021: {
            'batting': r"C:\Users\ggulz\Downloads\archive\IPL Player Stats\Batting Stats\BATTING STATS - IPL_2021.csv",
            'bowling': r"C:\Users\ggulz\Downloads\archive\BOWLING STATS - IPL_2021.csv",
        },
        2022: {
            'batting': r"C:\Users\ggulz\Downloads\archive\IPL Player Stats\Batting Stats\BATTING STATS - IPL_2022.csv",
            'bowling': r"C:\Users\ggulz\Downloads\archive\BOWLING STATS - IPL_2022.csv",
        },
       
    }


    for year in years_list:
        form_new_team(year, file_paths_by_year[year]['batting'], file_paths_by_year[year]['bowling'])


# # Visualizing player performance according to perfromance stats

# in this section of code i visualize all players statics by their performance matrices it helps to compare to those players that played before visualization are of yearwise and the stats of bowler and batsman are seprated

# In[29]:


# Load CSV files
def load_csv(file_path):
    try:
        return pd.read_csv(file_path)
    except FileNotFoundError:
        print(f"File not found: {file_path}")
        return None

# Find the best player for each role based on performance metrics
def find_best_player(df, metric):
    best_player = df[df[metric] == df[metric].max()]
    return best_player

# Main function to form a new team
def form_new_team(year, batting_file_path, bowling_file_path):
    batting_df = load_csv(batting_file_path)
    bowling_df = load_csv(bowling_file_path)

    if batting_df is None or bowling_df is None:
        return

    # Finding the best batsman and best bowler for the new team
    best_batsman = find_best_player(batting_df, 'Avg')
    best_bowler = find_best_player(bowling_df, 'Avg')

    return best_batsman, best_bowler

if __name__ == "__main__":
    years_list = [2016, 2017, 2018, 2019, 2020, 2021, 2022]
    file_paths_by_year = {
        2016: {
            'batting': r"C:\Users\ggulz\Downloads\archive\IPL Player Stats\Batting Stats\BATTING STATS - IPL_2016.csv",
            'bowling': r"C:\Users\ggulz\Downloads\archive\BOWLING STATS - IPL_2016.csv",
        },
        2017: {
            'batting': r"C:\Users\ggulz\Downloads\archive\IPL Player Stats\Batting Stats\BATTING STATS - IPL_2017.csv",
            'bowling': r"C:\Users\ggulz\Downloads\archive\BOWLING STATS - IPL_2017.csv",
        },
        2018: {
            'batting': r"C:\Users\ggulz\Downloads\archive\IPL Player Stats\Batting Stats\BATTING STATS - IPL_2018.csv",
            'bowling': r"C:\Users\ggulz\Downloads\archive\BOWLING STATS - IPL_2018.csv",
        },
        2019: {
            'batting': r"C:\Users\ggulz\Downloads\archive\IPL Player Stats\Batting Stats\BATTING STATS - IPL_2019.csv",
            'bowling': r"C:\Users\ggulz\Downloads\archive\BOWLING STATS - IPL_2019.csv",
        },
        2020: {
            'batting': r"C:\Users\ggulz\Downloads\archive\IPL Player Stats\Batting Stats\BATTING STATS - IPL_2020.csv",
            'bowling': r"C:\Users\ggulz\Downloads\archive\BOWLING STATS - IPL_2020.csv",
        },
        2021: {
            'batting': r"C:\Users\ggulz\Downloads\archive\IPL Player Stats\Batting Stats\BATTING STATS - IPL_2021.csv",
            'bowling': r"C:\Users\ggulz\Downloads\archive\BOWLING STATS - IPL_2021.csv",
        },
        2022: {
            'batting': r"C:\Users\ggulz\Downloads\archive\IPL Player Stats\Batting Stats\BATTING STATS - IPL_2022.csv",
            'bowling': r"C:\Users\ggulz\Downloads\archive\BOWLING STATS - IPL_2022.csv",
        },
    }

    # Store the best batsmen and bowlers along with their performance stats
    best_batsmen_stats = []
    best_bowlers_stats = []
    for year in years_list:
        batting_file_path = file_paths_by_year[year]['batting']
        bowling_file_path = file_paths_by_year[year]['bowling']
        best_batsman, best_bowler = form_new_team(year, batting_file_path, bowling_file_path)
        best_batsmen_stats.append(best_batsman)
        best_bowlers_stats.append(best_bowler)

    # Visualization
    plt.figure(figsize=(16, 6))

    # Best Batsmen Performance
    plt.subplot(1, 2, 1)
    for i, year in enumerate(years_list):
        plt.bar(str(year), best_batsmen_stats[i]['Avg'], label=str(year))
    plt.xlabel('Year')
    plt.ylabel('Average')
    plt.title('Best Batsman Performance from 2016 to 2022')
    plt.legend()

    # Best Bowlers Performance
    plt.subplot(1, 2, 2)
    for i, year in enumerate(years_list):
        plt.bar(str(year), best_bowlers_stats[i]['Avg'], label=str(year))
    plt.xlabel('Year')
    plt.ylabel('Average')
    plt.title('Best Bowler Performance from 2016 to 2022')
    plt.legend()

    plt.tight_layout()
    plt.show()


# # Assigning Player Price for Auction Every best Batsman And Best Bowler Price starts for bitting from  50000000 to 75000000 and their bar visualization

# in this section i assign value price of players for the starts for everyone ,that is 5000000 for best batsman and 75000000 for best bowler also i visualize their price and name for whom

# In[30]:


import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load CSV files
def load_csv(file_path):
    try:
        return pd.read_csv(file_path)
    except FileNotFoundError:
        print(f"File not found: {file_path}")
        return None

# Find the best player for each role based on performance metrics
def find_best_player(df, metric, num_players=1):
    sorted_df = df.sort_values(by=[metric], ascending=False)
    return sorted_df.head(num_players)

# Main function to form a new team
def form_new_team(year, batting_file_path, bowling_file_path):
    batting_df = load_csv(batting_file_path)
    bowling_df = load_csv(bowling_file_path)

    if batting_df is None or bowling_df is None:
        return

    # Finding the best batsman and best bowler for the new team
    best_batsman = find_best_player(batting_df, 'Avg', num_players=1)
    best_bowler = find_best_player(bowling_df, 'Avg', num_players=1)

    # Printing the results
    print(f"Year: {year}")
    print("Best Batsman:")
    print(best_batsman)
    print("Best Bowler:")
    print(best_bowler)

    # Player prices (replace with actual prices)
    player_prices = {
        best_batsman.iloc[0]['Player']: 50000000,
        best_bowler.iloc[0]['Player']: 75000000,
    }

    # Adding player prices to the DataFrames
    best_batsman['Price'] = best_batsman['Player'].map(player_prices)
    best_bowler['Price'] = best_bowler['Player'].map(player_prices)

    # Concatenate the DataFrames
    best_players = pd.concat([best_batsman, best_bowler])

    # Plotting the prices of the best players
    plt.figure(figsize=(10, 6))
    sns.barplot(data=best_players, x='Player', y='Price', hue='POS', palette='pastel')
    plt.title(f"Best Batsman and Bowler Prices - {year}")
    plt.xticks(rotation=45)
    plt.legend(title='Category', loc='upper left', labels=["Best Batsman", "Best Bowler"])

    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    years_list = [2016, 2017, 2018, 2019, 2020, 2021, 2022]
    file_paths_by_year = {
        2016: {
            'batting': r"C:\Users\ggulz\Downloads\archive\IPL Player Stats\Batting Stats\BATTING STATS - IPL_2016.csv",
            'bowling': r"C:\Users\ggulz\Downloads\archive\BOWLING STATS - IPL_2016.csv",
        },
        2017: {
            'batting': r"C:\Users\ggulz\Downloads\archive\IPL Player Stats\Batting Stats\BATTING STATS - IPL_2017.csv",
            'bowling': r"C:\Users\ggulz\Downloads\archive\BOWLING STATS - IPL_2017.csv",
        },
        2018: {
            'batting': r"C:\Users\ggulz\Downloads\archive\IPL Player Stats\Batting Stats\BATTING STATS - IPL_2018.csv",
            'bowling': r"C:\Users\ggulz\Downloads\archive\BOWLING STATS - IPL_2018.csv",
        },
        2019: {
            'batting': r"C:\Users\ggulz\Downloads\archive\IPL Player Stats\Batting Stats\BATTING STATS - IPL_2019.csv",
            'bowling': r"C:\Users\ggulz\Downloads\archive\BOWLING STATS - IPL_2019.csv",
        },
        2020: {
            'batting': r"C:\Users\ggulz\Downloads\archive\IPL Player Stats\Batting Stats\BATTING STATS - IPL_2020.csv",
            'bowling': r"C:\Users\ggulz\Downloads\archive\BOWLING STATS - IPL_2020.csv",
        },
        2021: {
            'batting': r"C:\Users\ggulz\Downloads\archive\IPL Player Stats\Batting Stats\BATTING STATS - IPL_2021.csv",
            'bowling': r"C:\Users\ggulz\Downloads\archive\BOWLING STATS - IPL_2021.csv",
        },
        2022: {
            'batting': r"C:\Users\ggulz\Downloads\archive\IPL Player Stats\Batting Stats\BATTING STATS - IPL_2022.csv",
            'bowling': r"C:\Users\ggulz\Downloads\archive\BOWLING STATS - IPL_2022.csv",
        },
        
    }

    for year in years_list:
        batting_file_path = file_paths_by_year[year]['batting']
        bowling_file_path = file_paths_by_year[year]['bowling']
        form_new_team(year, batting_file_path, bowling_file_path)


# In[ ]:




