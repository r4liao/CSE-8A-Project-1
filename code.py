import csv

# Functions that reads data (without header)
def load_data(filename):
    with open(filename, newline='') as csvfile:
        reader = csv.reader(csvfile)
        header = next(reader)
        return list(reader)

# Function that removes the $ from the price
def clean_price(price_str):
    return float(price_str.replace('$', '').replace(',', ''))

# Function that converts rating from string to integer
def clean_rating(rating_str):
    return float(rating_str)

# Function that removes mi. from the mileage
def clean_mileage(mileage_str):
    return int(mileage_str.replace(' mi.', '').replace(',', ''))

# Function that filters necessary variables
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

# Loads the data
mercedes = load_data("usa_mercedes_benz_prices.csv")

# Cleans the data
mercedes = clean_data(mercedes)

# Function that compares cars with high ratings and low Mileage with other cars
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

# Running the function
analysis(mercedes)
