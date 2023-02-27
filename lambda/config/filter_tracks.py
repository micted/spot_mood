import pandas as pd
import boto3


def filtered_for_suggestion(url):

    # Read the CSV file
    # Read the CSV file
    df = pd.read_csv('recently_played.csv')

    # Group by Artist and Genre, and calculate the sum of the Count field
    df_grouped = df.groupby(['Artist', 'Genre']).sum().reset_index()

    # Find the common Artists by grouping on the Artist column and getting the count of rows for each Artist
    artist_count = df.groupby(['Artist']).count().sort_values(by=['Track Name'], ascending=False)

    # Get the top n common Artists based on the count of rows for each Artist
    n = 10
    top_n_artists = artist_count[:n].index.tolist()

    # Filter the dataframe to include only the rows with Artists in the top_n_artists list
    df_filtered = df_grouped[df_grouped['Artist'].isin(top_n_artists)]

    # Sort the filtered dataframe by Count and Genre
    df_sorted = df_filtered.sort_values(by=['Count', 'Genre'], ascending=[False, True])

    # Return the sorted dataframe

    
    #filtered_list = [track["Genre"],track["Mood"],track["Artist"]]
    
    return df_sorted


