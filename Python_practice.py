'''
print("Hello World")
counties = ["Arapahoe","Denver","Jefferson"]
if counties[1] == 'Denver':
    print(counties[1])

if "El Paso" in counties:
    print("El Paso is in the list of counties.")
else:
    print("El Paso is not the list of counties.")

if "Arapahoe" in counties and "El Paso" in counties:
    print("Arapahoe and El Paso are in the list of counties.")
else:
    print("Arapahoe or El Paso is not in the list of counties.")

'''

counties_dict = {"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438}

for county, voters in counties_dict.items():
    
    print(county , voters)

    #print (county  +" county has " + str(voters) +" registered voters")

    
    print(format(f"{county:,} county has {voters:,} registered voters"))

'''
candidate_votes = int(input("How many votes did the candidate get in the election? "))
total_votes = int(input("What is the total number of votes in the election? "))
message_to_candidate = (
    f"You received {candidate_votes:,} number of votes. "
    f"The total number of votes in the election was {total_votes:,}. "
    f"You received {candidate_votes / total_votes * 100: .2f}% of the total votes.")

print(message_to_candidate)
'''