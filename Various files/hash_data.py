import hashlib
import pandas as pd

class Hash_DataFrame:

    def hash_Columns(dataframe, columns: list):

        # Checks if dataframe is a DataFrame Object.
        if not isinstance(dataframe, pd.DataFrame):
            
            # Parses a error message if dataframe is not a pd.DataFrame.
            raise TypeError(f"datafram need to be a DataFrame, not {type(dataframe).__name__}")
        
        else:

            # if is a dataFrame creates a new local dataFrame.
            df_data = dataframe

        # loops through list of columns. 
        for column in columns:

            # Checks if a column name is a string 
            if column not in df_data.columns:
                
                # Parses a error message if column is not a string.
                raise ValueError(f"Column do not exist: {column}")
            
            else:

                if df_data[column].dtype != object:

                    raise TypeError(f"Cant encrypt columns that are int or float")

                # encrypt the specific column with sha256
                df_data[column] = df_data[column].apply(lambda x: hashlib.sha256(x.encode()).hexdigest()) 

        # Returns the encrypted dataframe.
        return df_data



