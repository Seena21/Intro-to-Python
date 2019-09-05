# population

years_str = input("How many years: ")
years_int = int(years_str)
# Conversion of seconds in a years
year= 31536000

# define variables and do math
Birth = (4505142 * years_int)
Deaths = (2425846 * years_int)
Immigrants = (901028 * years_int)
current_pop_int = int(307357870)

# put all the values together and find estimated population
population = (current_pop_int + Birth + Immigrants - Deaths)

print("estimated population: ", population)
