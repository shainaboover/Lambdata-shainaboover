
import pandas as pd 
from sklearn.model_selection import train_test_split


# State abbreviation -> Full Name and visa versa. 
# FL -> Florida, etc. (Handle Washington DC and territories like Puerto Rico etc.)

def add_state_name_col(df):
    """
    Add a column of corresponding state names to a dataframe
    Params (df) a DataFrame with a column called 'abbrev' that has state abbreviations
    Return a copy of original DataFrame with extra column
    """
    new_df = df.copy()

    names_map = {'CA': 'California',
                 'CO': 'Colorado',
                 'CT': 'Connecticut',
                 'DC': 'Dist of Colombia',
                 'TX': 'Texas'}

    new_df['name'] = new_df['abbrev'].map(names_map)


    return new_df

if __name__ == '__main__':
    df = pd.DataFrame({'abbrev': ['CA', 'CO', 'CT', 'DC', 'TX']})
    print(df.head)

    add_state_name_col(df)
    print(df.head)

    mapped_df = add_state_name_col(df)
    print(mapped_df.head())

# Train/validate/test split function for a dataframe

#def split(df):
 #   """
 #   Takes a dataframe
 #   Performs a random train/validate/test split

 #   """

  #  train, test = train_test_split(df, train_size=.8, random_state=42)
  #  train, val = train_test_split(train, random_state=42)

   # return train.shape

#if __name__ == '__main__':

    #df = pd.read_csv('https://github.com/shainaboover/Loneliness/blob/master/datasets_117_1001_responses.csv')
#    df = pd.DataFrame({'test': [0, 1, 2, 3, 4]})
 #   print(df.head(2))