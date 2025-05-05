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

# Function 4: Compares Cars with High Ratings and Low Mileage with Normal Cars
def analysis(data):
    high_rating_low_mileage = []
    other_cars = []

    for rating, mileage, price in data:
        if rating >= 4.5 and mileage < 25000:
            high_rating_low_mileage.append(price)
        else:
            other_cars.append(price)

    avg_high_rating_low_mileage = sum(high_rating_low_mileage) / len(high_rating_low_mileage)
    avg_other = sum(other_cars) / len(other_cars)

    print("Do cars with higher ratings and lower mileage tend to have a higher price?\n")
    print(f"Average Price of High-Rated, Low-Mileage Cars: ${round(avg_high_rating_low_mileage, 2)}")
    print(f"Average Price of Other Cars: ${round(avg_other, 2)}\n")
    print(f"High-Rated, Low-Mileage Cars are on average ${round(avg_high_rating_low_mileage, 2) - round(avg_other, 2)} more expensive than other cars")

# Function 5: Running Function 4
analysis(mercedes)