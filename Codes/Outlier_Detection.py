import pandas as pd
import matplotlib.pyplot as plt

def detect_outlier( dataframe, column ):
    """
    Description :-
        detect_outlier() takes 2 arguments dataframe and column. Then find outlier on it if it's present
        
    Args :-
        datframe : It a DataFrame variable
        Column : It a Column name on which outlier has to detected

    Return :-
        return Dictionary in the following structure,
        If Outlier is present then,
        {
            'C1' : {
                lower_outlier : [ index1, index2, .. ]
                , upper_outlier : [ index1, index2, .. ]
                }
        }
        or
        {
            'C1' : {
                lower_outlier : [ index1, index2, .. ]
                }
        }
        or
        {
            'C1' : {
                upper_outlier : [ index1, index2, .. ]
                }
        }

        If Outlier is not present then,
        {
            'C1' : {}
        }
    """

    col_describe = dataframe[column].describe()
    iqr = 1.5 * ( col_describe['75%'] - col_describe['25%'] )
    lower_iqr = col_describe['25%'] - iqr
    upper_iqr = col_describe['75%'] + iqr
    
    # print( f"column = { column }, iqr = { iqr }, lower_iqr = { lower_iqr } and upper_iqr = { upper_iqr }" )
    lower_iqr_indexes = list( dataframe[ dataframe[column] < lower_iqr ].index )
    upper_iqr_indexes = list( dataframe[ dataframe[column] > upper_iqr ].index )

    outlier_index = {}
    if( len( lower_iqr_indexes ) > 0 ):
        outlier_index['lower_outlier'] = lower_iqr_indexes

    if( len( upper_iqr_indexes ) > 0 ):
        outlier_index['upper_outlier'] = upper_iqr_indexes
        
    return_dict = {
                    column : outlier_index
                 }
    
    return return_dict

def outlier_exectuor( data ):
    selected_columns = list( data.dtypes[ data.dtypes != 'object' ].index )

    outlier_columns = {}
    for col in selected_columns:
        op = detect_outlier( data, col )

        col_outlier_data = list( op.values() )[0]
        
        if( len( col_outlier_data ) > 0 ):
            outlier_columns[col] = col_outlier_data

    for col, col_outlier in outlier_columns.items():
        print( f"Col = {col}" )
        print( f"col_outlier = {col_outlier}" )
        print()
        print()
        data[col].plot( kind = 'box' )
        plt.title( f"{col} Column Outlier Graph" )
        plt.show()


# path = r"C:\Users\gauta\PycharmProjects\Statistics\Bunny_AI_Data.csv"
path = r"C:\Users\gauta\PycharmProjects\MachineLearning\Pre Processing\Topic 2 - Pandas\Excel Data\Country.csv"
data = pd.read_csv( path )
outlier_exectuor( data )
