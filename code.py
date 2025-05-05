import csv

# Function 1: Reads Data (Without Header)
def load_data(filename):
    with open(filename, newline='') as csvfile:
        reader = csv.reader(csvfile)
        header = next(reader)
        return list(reader)

# Functions 2: Data Clean-Up + Filtering Variables
def clean_price(price_str):
    return float(price_str.replace('$', '').replace(',', ''))

def clean_rating(rating_str):
    return float(rating_str)

def clean_mileage(mileage_str):
    return int(mileage_str.replace(' mi.', '').replace(',', ''))

def clean_data(rows):
    cleaned = []
    for row in rows:
        try:
            rating = clean_rating(row[2])
            mileage = clean_mileage(row[1])
            price = clean_price(row[4])
            cleaned.append((rating, mileage, price))
        except:
            continue
    return cleaned

# Function 3: Loading + Cleaning Data
mercedes = load_data("usa_mercedes_benz_prices.csv")
mercedes = clean_data(mercedes)
