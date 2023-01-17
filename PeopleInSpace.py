import requests
response = requests.get("http://api.open-notify.org/astros.json")  #sends a GET request to URL and assigns it to the variable as a response
space_data = response.json()     #.json() returns a dictionary of the response and is assigned to the variable space_data
astronauts = space_data["people"] #creates a list of astronauts from the space_data dictionary
numberOfAstronauts = space_data["number"]  #takes the number value from the space_data dictionary
print("Number of people in space: "+ str(numberOfAstronauts) + "\n")   #prints the number of people in space
print ("People currently in space:\n"  "{:<20} {:<15}".format('Name','Craft'))  #uses .format to format the string Name takes up 20 characters and aligns it to the left
for astronaut in astronauts:    #for loop to go through each astronaut in the astronauts list
    print("{:<20} {:<15}".format(astronaut["name"],astronaut["craft"]))      #prints the name and craft for the astronaut and formats it to align with the printed Name Craft 'Columns'

