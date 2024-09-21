# Write code below 💖

height = int(input("Enter your height in cm: "))
credits = int(input("Enter the number of credits you have: "))

height_required = 137
credits_required = 10

if height >= height_required and credits >= credits_required:
    print("Enjoy the ride!")
elif height < height_required and credits >= credits_required:
    print("You are not tall enough to ride.")
elif height >= height_required and credits < credits_required:
    print("You don't have enough credits.")
else:
    print("You have not met either requirement.")