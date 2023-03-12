import pandas as pd
import sys

def load_data(profile_filepath, transcript_filepath):
    '''
    PURPOSE: 
    The purpose of the function is to load in the datasets and merge
    them into one dataframe.
    
    INPUT:
    profile_filepath - text string with the filepath for the profile.json file
    transcript_filpath - text string with the filepath for the transcript.json file
    
    OUTPUT:
    df - dataframe containing the columns from the categories and messages csv files
    '''
    # read in the json files
    profile = pd.read_json(profile_filepath, orient='records', lines=True)
    transcript = pd.read_json(transcript_filepath, orient='records', lines=True)

    # change the column name of person to id
    transcript.rename(columns={'person':'id'}, inplace=True)

    # merge the two dataframes on id
    df = pd.merge(transcript, profile, on="id")

    return df

def main():
    if len(sys.argv) == 3:

        profile_filepath, transcript_filepath, database_filepath = sys.argv[1:]

        print('Loading data...\n    MESSAGES: {}\n    CATEGORIES: {}'
              .format(profile_filepath, transcript_filepath))
        df = load_data(profile_filepath, transcript_filepath)

        print('Cleaning data...')
        df = clean_data(df)
        
        print('Saving data...\n    DATABASE: {}'.format(database_filepath))
        save_data(df, database_filepath)
        
        print('Cleaned data saved to database!')
    
    else:
        print('Please provide the filepaths of the messages and categories '\
              'datasets as the first and second argument respectively, as '\
              'well as the filepath of the database to save the cleaned data '\
              'to as the third argument. \n\nExample: python process_data.py '\
              'disaster_messages.csv disaster_categories.csv '\
              'DisasterResponse.db')


if __name__ == '__main__':
    main()