REGION = {'Chico': 0.5, 'Groucho':0.7, 'Harpo':0.5, 'Zeppo':0.4}

def calculate_tax(price, region, hour):
    return price+price*REGION[region]*(hour/24)