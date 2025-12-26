import data_loader 
import cleaning 

print("START")
df = data_loader.load_covid_data()
print("LOADED")
# print(df.columns)

df = cleaning.clean_data(df)
# print(df.head())
df = cleaning.filter_countries(df)


print(df["location"].unique())
print(df.shape)