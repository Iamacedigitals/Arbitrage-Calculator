from itertools import permutations, combinations
import numpy as np
import pandas as pd

currency_list = ["usd","ngn","eur","gbp","btc"]
groups = permutations(currency_list, 2)
r_list = []
e_list = []
for tp in groups:
    if f"{tp[1]+tp[0]}" not in r_list:
        r_list.append(f"{tp[0]+tp[1]}")
    e_list.append( f"{tp[0]+tp[1]}")

pair =  np.array(r_list)

site_data = pd.read_csv("Site Data/Custom_quotes2.csv")
df = pd.DataFrame(site_data, columns=["Quotes", "Price","Implied1", "Implied2", "Implied3", "XZ1", "XZ2", "XZ3", "XY1", "XY2", "XY3", "Is_aribitrage1", "Is_aribitrage2", "Is_aribitrage3",  "Profit"])
# Lets initiate the quotes
derived_quotes  = ["usdngn","eurngn","eurusd","gbpusd","gbpeur","gbpngn","btcusd","btcngn","btceur","btcgbp"]
# this is using of idiomatic expressions to give context to python code while improving its speed
pair_list =  { f"{i}":site_data["Price"].iloc[index] for i in pair for index, value in enumerate(site_data["Quotes"]) if i == value}
quoted_list = np.array([pair_list[i] for i in pair_list])

quote_z,quote_y,quote_x,quote_w,quote_v,quote_u,quote_t,quote_s,quote_r,quote_q = quoted_list

implied_list = np.array([
    np.array([((1/quote_v)/(1/quote_y)), ((1/quote_u)/(1/quote_x)), ((1/quote_t)/(1/quote_w))]), # Implied rates for quote_z
    np.array([(quote_v/(1/quote_z)), ((1/quote_s)/(1/quote_x)), ((1/quote_r)/(1/quote_w))]), # Implied rates for quotes_y
    np.array([(quote_u/(1/quote_z)), ((1/quote_q)/(1/quote_w)), (quote_s/(1/quote_y))]), # Implied rates for quotes_x
    np.array([(quote_t/(1/quote_z)), (quote_q/(1/quote_x)), ((quote_r)/(1/quote_y))]), # Implied rates for quotes_w
    np.array([((1/quote_r)/ (1/quote_t)), ((1/quote_s)/(1/quote_u)), (quote_y/(quote_z))]), # Implied rates for quotes_v
    np.array([((1/quote_q) /(1/quote_t)), (quote_s/(1/quote_v)), (quote_x/quote_z)]), # Implied rates for quotes_u
    np.array([(quote_q/ (1/quote_u)), (quote_r/(1/quote_v)), (quote_w/quote_z)]), # Implied rates for quotes_t
    np.array([((1/quote_q) /(1/quote_r)), (quote_u/(quote_v)), (quote_x/quote_y)]), # Implied rates for quotes_s
    np.array([((quote_q) /(1/quote_s)), (quote_t/(quote_v)), (quote_w/quote_y)]), # Implied rates for quotes_r
    np.array([((quote_r) /(quote_s)), (quote_t/(quote_u)), (quote_w/quote_x)]) # Implied rates for quotes_r
    
])
xz_list = np.array([
    np.array([1/quote_v,1/quote_u, 1/quote_t]), # z
    np.array([quote_v, 1/quote_s, 1/quote_r]), # y
    np.array([quote_u, 1/quote_q, quote_s]), # x
    np.array([quote_t, quote_q, (quote_r)]), # w
    np.array([1/quote_r, 1/quote_s, quote_y]), # v
    np.array([1/quote_q, quote_s, quote_x]), # u
    np.array([quote_q, quote_r, quote_w]), # t 
    np.array([1/quote_q, quote_u, quote_x]), # s
    np.array([quote_q, quote_t, quote_w]), # r
    np.array([quote_r, quote_t, quote_w]), # r
    ])
xy_list = np.array([xz_list/implied_list])
implied_df = pd.DataFrame(implied_list)

