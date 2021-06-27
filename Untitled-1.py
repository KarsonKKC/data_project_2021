from numpy import NaN  # NaN means not a number
import pandas as pd

# %%
price_df = pd.read_excel(
    "price_history_checks_may2021.xlsx", parse_dates=["PriceUpdatedDate"]
)
price_df.head() #This step is importing the file and return the top 5 rows from the file.

# %%
fuel_codes = price_df.FuelCode.unique() #This line will return column FuelCode with the types of fuel and the type of the result
fuel_codes = [x for x in fuel_codes if type(x) is str] #This will find out if the value of the type is a string, testing it if it is an integer or a string
print(fuel_codes) #If it is a string, print the fuel codes.
# %%
new_column_names = (    
    [f"Price_{name}_UpdatedDate" for name in fuel_codes] #
    + [f"Price_{name}" for name in fuel_codes]
    + [
        name
        for name in price_df.columns
        if name not in ["FuelCode", "PriceUpdatedDate", "Price"]
    ]
)
new_column_names.sort() 
print(new_column_names) #This step is to make the data from FuelCode into a list and sort them together

# %%
# %%
new_rows = [] 
temp_row = pd.Series(index=new_column_names, dtype=object) 

for i, row in price_df.head().iterrows():
    fc = row.FuelCode
    if row.ServiceStationName is not NaN:
        new_rows.append(temp_row)
        temp_row = pd.Series(index=new_column_names, dtype=object)
        for key, element in row.iteritems():
            if key in temp_row.index:
                temp_row[key] = element
        temp_row[f"Price_{fc}_UpdatedDate"] = row.PriceUpdatedDate
        temp_row[f"Price_{fc}"] = row.Price
    elif row.ServiceStationName is NaN:
        temp_row[f"Price_{fc}_UpdatedDate"] = row.PriceUpdatedDate
        temp_row[f"Price_{fc}"] = row.Price

# %%
reshaped_df = pd.DataFrame(new_rows)
reshaped_df.drop([0], inplace=True)
reshaped_df.head()
