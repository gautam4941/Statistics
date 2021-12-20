import pandas as pd
pd.set_option('display.max_columns', None)

data = pd.read_csv( r"House_price_data.csv" )
print( f"data :- \n{ data }\n" )

import random
temp = list( data['price'] )

sample_price = []
for i in range( 1, 51 ):
    sample_price.append( random.choices( temp ) )

import numpy as np
print( f"Population Mean = { np.mean( data['price'] ) }" )
print( f"Sample Mean = { np.mean( sample_price ) }\n" )

#Now we can see that Population Mean and Sample mean both are different

#H0 -> There is no difference in Population Mean and Sample mean
#H1 -> There is difference in Population Mean and Sample mean

from scipy.stats import ttest_1samp
ttest, p_value = ttest_1samp( sample_price, np.mean( temp ) )

print( f"p_value = { p_value } and p_value[0] = { p_value[0] }" )
p_value = p_value[0]

if( p_value < 0.05 ):
    print( "Type 1 Error -> Null Hyposthesis got rejected" )
else:
    print("We are Accepting Null Hyposthesis")