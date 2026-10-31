temperature = int(input("Enter today's temperature in Celsius: "))

if temperature < 20:

    outfit = "jacket"

    print("It is cold today.")

    print("Wear a", outfit)

else:

    outfit = "t-shirt"

    print("It is warm today.")

    print("Wear a", outfit)

    is_raining = input("Is it raining today? (yes/no): ")

if is_raining == "yes":

    print("Bring an umbrella!")

    wind_speed = int(input("Enter the wind speed in km/h: "))

# PART 6: Decide whether a windbreaker is needed

if wind_speed > 30:

    needs_windbreaker = "yes"

    print("It is windy today.")

    print("Wear a windbreaker over your", outfit)

else:

    needs_windbreaker = "no"

    print("It is calm today.")

    print("No windbreaker needed over your", outfit)

# PART 7: Ask whether there are puddles on the ground
has_puddles = input("Are there puddles on the ground? (yes/no): ")

# PART 8: Decide between boots and sneakers

if has_puddles == "yes":

    shoes = "boots"

    print("The ground is wet.")

    print("Wear", shoes)

else:

    shoes = "sneakers"

    print("The ground is dry.")

    print("Wear", shoes)

    print("")

    print("Weather check complete!")

    print("===== WEATHER OUTFIT PICKER =====")

    print("Temperature:", temperature)

    print("Outfit Chosen:", outfit)

    print("Raining:", is_raining)

    print("Windbreaker Needed:", needs_windbreaker)

    print("Shoes Chosen:", shoes)

    print("===================================")

