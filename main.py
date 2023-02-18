import requests
import random
from pathlib import Path

print('Picking a country at random...')

# Read history file
history_file_path = Path.cwd() / 'history.txt'
if not history_file_path.exists():
    history_file_path.touch()

# List countries picked before
with open(history_file_path, 'r') as f:
    hit_countries = [country.strip() for country in f if country.strip()]
    print(f'Countries picked before: {hit_countries}')

# List countries not picked before
response = requests.get('https://restcountries.com/v3.1/all').json()
not_hit_countries = [entry['name']['common'] for entry in response if entry['name']['common'] not in hit_countries]
print(f'Countries not picked before: {not_hit_countries}')

# Select new random country
selected_country = not_hit_countries[random.randint(0, len(not_hit_countries))]
print(f'You\'ve landed in {selected_country}!')

# Write country to history file
with open(history_file_path, 'a') as file:
    file.write(f'\n{selected_country}')
    print(f'Wrote {selected_country} to history file')
