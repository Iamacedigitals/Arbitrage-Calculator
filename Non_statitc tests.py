# say we have an  object like obj from pandas, and we have our own defined values here in our code i want to set the values of my code to be the values of the panda whatnot
import pandas as pd
from itertools import permutations, combinations 
import numpy as np
from Non_static_arbitage import implied_list
df =  pd.read_csv("Site Data/Custom_quotes2.csv", index_col="Quotes")

currency_list = ["usd","ngn","eur","gbp","btc"]
groups = permutations(currency_list, 2)

symbols = [i[0] + i[1] for i in groups]
pair_value = {i:df["Price"].loc[i] for i in symbols}

quoted_list = np.array([pair_value[i] for i in pair_value])

# quote_z,quote_y,quote_x,quote_w,quote_v,quote_u,quote_t,quote_s,quote_r,quote_q  = quoted_list

# implied_list = np.array([
#     np.array([((1/quote_v)/(1/quote_y)), ((1/quote_u)/(1/quote_x)), ((1/quote_t)/(1/quote_w))]), # Implied rates for quote_z
#     np.array([(quote_v/(1/quote_z)), ((1/quote_s)/(1/quote_x)), ((1/quote_r)/(1/quote_w))]), # Implied rates for quotes_y
#     np.array([(quote_u/(1/quote_z)), ((1/quote_q)/(1/quote_w)), (quote_s/(1/quote_y))]), # Implied rates for quotes_x
#     np.array([(quote_t/(1/quote_z)), (quote_q/(1/quote_x)), ((quote_r)/(1/quote_y))]), # Implied rates for quotes_w
#     np.array([((1/quote_r)/ (1/quote_t)), ((1/quote_s)/(1/quote_u)), (quote_y/(quote_z))]), # Implied rates for quotes_v
#     np.array([((1/quote_q) /(1/quote_t)), (quote_s/(1/quote_v)), (quote_x/quote_z)]), # Implied rates for quotes_u
#     np.array([(quote_q/ (1/quote_u)), (quote_r/(1/quote_v)), (quote_w/quote_z)]), # Implied rates for quotes_t
#     np.array([((1/quote_q) /(1/quote_r)), (quote_u/(quote_v)), (quote_x/quote_y)]), # Implied rates for quotes_s
#     np.array([((quote_q) /(1/quote_s)), (quote_t/(quote_v)), (quote_w/quote_y)]), # Implied rates for quotes_r
#     np.array([((quote_r) /(quote_s)), (quote_t/(quote_u)), (quote_w/quote_x)]) # Implied rates for quotes_r
    
# ])
# implied_df = pd.DataFrame(implied_list)
value_list = []
for price in pair_value:
    print(price)
    value_list.append(pair_value[price])
implied_df = pd.DataFrame(implied_list)
df2 = list(zip(pair_value, value_list, implied_list))
general_dataframe = pd.DataFrame(df2)
general_dataframe.columns = ["Quotes", "Price", "Implied1"]
print(general_dataframe)