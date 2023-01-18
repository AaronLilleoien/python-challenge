#!/usr/bin/env python
# coding: utf-8

# In[8]:


import os
import csv

#open connection to csv 
file_to_load = os.path.join('.', 'Resources', 'election_data.csv')

file_to_output = os.path.join(".","election_analysis.txt")

num_votes = 0
charles_votes = 0
diana_votes = 0
raymon_votes = 0 
charles_pct = 0
diana_pct = 0
raymon_pct = 0

#Put csv in a list
with open(file_to_load) as election_data:
    reader = csv.reader(election_data)
    
#remove header
    header= next(reader)
    
    

    for row in reader:
        #total number of rows gives number of votes
        num_votes += 1
        #count votes for each person
        if row[2] == "Charles Casper Stockham":
            charles_votes += 1
        elif row[2] == "Diana DeGette":
            diana_votes += 1
        elif row[2] == "Raymon Anthony Doane":
            raymon_votes += 1
        
        
        
        #calculate percent of votes for each person
    charles_pct = round(charles_votes / num_votes *100,3)
    diana_pct = round(diana_votes / num_votes *100,3)
    raymon_pct = round(raymon_votes / num_votes *100,3)
    
    #who is the winner - find most votes and who they belong to
var = {charles_votes:"Charles Casper Stockham",diana_votes:"Diana DeGette",raymon_votes:"Raymon Anthony Doane"}

with open(file_to_output, "w") as txt_file:
    
    output = (
        f"Election Results\n"
        f"------------------------\n"
        f"Total Votes: {num_votes}\n"
        f"------------------------\n"
        f"Charles Casper Stockham: {charles_pct}% ({charles_votes}) \n"
        f"Diana DeGette: {diana_pct}% ({diana_votes})\n"
        f"Raymon Anthony Doane: {raymon_pct}% ({raymon_votes})\n"
        f"------------------------\n"
        f"Winner: {var.get(max(var))}\n"
        f"------------------------\n"
    )

    print(output)
    txt_file.write(output)


# In[ ]:




