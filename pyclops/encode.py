import hashlib
import pandas as pd


def hash_cat_cols(dataframe):
    for col in dataframe:
        # NEED TO COME UP WITH SOLUTION ON FINDING DATETIME VALUES
        # Any categorical column should be identified
        if dataframe[col].dtype == "object":
        	# Hash to handle sensitive data
            dataframe[col] = dataframe[col].apply(lambda x: hashlib.md5(x.encode('utf-8')).hexdigest())
            # One-hot encode & combine with original dataframe
            x = pd.get_dummies(dataframe[col], prefix=col)
            dataframe = pd.concat([dataframe, x], axis=1)
            # Remove old column
            del dataframe[col]
            
    return dataframe    