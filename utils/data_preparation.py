# Utility functions. No tests yet

def split_time_based(df, split_col, test_size):
    quantile = 1. - test_size
    
    split_point = df[split_col].quantile(quantile)
    df_train = df[df[split_col] <= split_point]
    df_test = df[df[split_col] > split_point]
    
    return df_train, df_test