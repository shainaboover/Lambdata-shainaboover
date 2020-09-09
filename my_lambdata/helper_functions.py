
import pandas as pd 
from sklearn.model_selection import train_test_split

df = pd.read_csv('https://github.com/shainaboover/Loneliness/blob/master/datasets_117_1001_responses.csv')


# Train/validate/test split function for a dataframe

def split(df):
    """
    Takes a dataframe
    Performs a random train/validate/test split

    """

    train, test = train_test_split(df, train_size=.8, random_state=42)
    train, val = train_test_split(train, random_state=42)

    return train.shape, test.shape, val.shape

# Single function to take a list, turn it into a series 
# and add it to a dataframe as a new column





