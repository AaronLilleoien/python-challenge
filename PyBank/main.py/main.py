#!/usr/bin/env python
# coding: utf-8

# In[1]:


import os
import csv

#open connection to csv 
file_to_load = os.path.join('.', 'Resources', 'budget_data.csv')

file_to_output = os.path.join(".","budget_analysis.txt")

total_months = 0
total_net = 0
net_change = 0 

net_change_list = []
month_of_changes = []

greatest = ["", 0]
least = ["", 999999999999999]




#Put csv in a list
with open(file_to_load) as financial_data:
    reader = csv.reader(financial_data)
    
    #remove header
    header= next(reader)
    
    first_row = next(reader)
    
   
    
    total_net += int(first_row[1])
    previous_net = int(first_row[1])
  
    total_months+= 1
    
    for row in reader:     
        total_months += 1
        total_net += int(row[1])
       
        
        #track net change
        net_change = int(row[1]) - previous_net
        previous_net = int(row[1])
        net_change_list.append(net_change)
        

        
        #calculate greatest increase
        if(net_change > greatest[1]):
            greatest[0] = row[0]
            greatest[1] = net_change
        
        
        #calculate greatest decrease
        if(net_change < least[1]):
            least[0] = row[0]
            least[1] = net_change
            
        
net_monthly_average = sum(net_change_list)/len(net_change_list)
 
with open(file_to_output, "w") as txt_file:
    
    output = (
            f"Financial Analysis\n"
            f"-------------------\n"
            f"Total months: {total_months}\n"
            f"Total: ${total_net}\n"
            f"Average Change ${net_monthly_average:.2f}\n"
            f"Greatest increase: {greatest[0]} (${greatest[1]})\n"
            f"Greatest decrease: {least[0]} (${least[1]})\n"
    )
    
    
    print(output)
    txt_file.write(output)
    
    
    
    
    
    
    
    
    
    
    
    
    #pl_array2 = []
    #pl_array2 = pl_array
    
    
    #total_pl_change =  (pl_array[0]) - pl_array[-1]
    #months_to_avg = num_months - 1
    #total_pl_change_avg = round(total_pl_change/months_to_avg,2)
    
    
    #print(f"Total: ${profit_loss}")
    #print(pl_array)
    #print(f"${total_pl_change_avg}")
    
    #print(pl_array2)
   
    #change_list = []
    #x = 0
    #for x in pl_array2:
        #last_num = pl_array.pop(-1)
        #new_last = pl_array[-1]
        #change = new_last - last_num
        #change_list.append(change)
    
    #print(change_list)
        
    
    
    


# In[ ]:


greatest_change = 0
   pl_array= [int(x) for x in pl_array]
   print(pl_array)
   #for x in pl_array:
    #   if pl_array[x] - pl_array[x+1] > greatest_change:
     #      print("higher")
      # else:
   result = 0
   highest = 0 
   print("")
   for x in range(len(pl_array)):
       last_row = x
   
   for x in range(len(pl_array)):
       if x = last_row:
           if pl_array[x] - pl_array[x+1] > greatest_change:
           print("higher")
           

