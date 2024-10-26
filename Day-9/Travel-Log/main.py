travel_log = []


def add_new_country(country, visited_times, cities_visited):

    new_country = {"country": country, "visited": visited_times, "cities": cities_visited}
    travel_log.append(new_country)


country_name = input("Enter country name: ").title()

times = int(input("How many times do you visited the country: "))

cities_name = input("Enter cities visited: ").split()

add_new_country(country_name, times, cities_name)

print(travel_log)
