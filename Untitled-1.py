import matplotlib.pyplot as plt
import pandas as pd
import glob 

# create list of all the ManeuverBranch files
file_pattern = 'ManeuverBranchId*.csv'
files = glob.glob(file_pattern)

# create the demonsions of the graph (10 inches by 6 inches)
plt.figure(figsize=(10, 6))

for file in files:
    # read all the files cuz it is inside for loop
    df = pd.read_csv(file)
    # CHECK IF THIS IS RIGHT!!
    radial = df['positionDepRelToChiefLvlhX']
    crosstrack = df['positionDepRelToChiefLvlhY']

# Plot the maneuver plan
    plt.plot(crosstrack, radial, label='Maneuver Path', color='blue')
    plt.scatter(crosstrack.iloc[0], radial.iloc[0], color='green', label='Start Point')
    plt.scatter(crosstrack.iloc[-1], radial.iloc[-1], color='red', label='End Point')

    
plt.xlabel('Crosstrack')
plt.ylabel('Radial')
plt.title('Maneuver Plan of the Satellite')
plt.legend()
plt.grid(True)
plt.show()