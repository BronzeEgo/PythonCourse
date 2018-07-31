print('How many Kilometers did you cycle today?')
kms = float(input())
miles = kms/1.6094
rounded_miles = round(miles, 2)
print(f'Your {kms}km ride was {rounded_miles} rounded miles.')

# round(miles, 2)
