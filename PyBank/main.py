import os
import csv

# Path to collect data from the Resources folder
budget_csv = os.path.join('Resources', 'budget_data.csv')

# Open the csv file in read mode
with open(budget_csv, 'r') as csvfile:

    # Split the data in file using commas
    csvreader = csv.reader(csvfile, delimiter=',')

    # Read the header row 
    header = next(csvreader)

    # Find the number of months in the data set
    months = 0
    total_pl = 0
    profitloss_change = []
    period = []
    change_counter = 0

    for row in csvreader:
        #Count the number of months
        months = months + 1

        # calculate total profit
        profit_loss = int(row[1])
        total_pl = total_pl + profit_loss 
        
        #calculate change in profit/loss and append to list pl_change
        if change_counter == 0:
            previous_pl = profit_loss
            change_counter += 1
        else:
            change_pl = profit_loss - previous_pl
            profitloss_change.append(change_pl)
            #Get the period and change in profit
            period.append(row[0])
            previous_pl = profit_loss
            change_counter += 1            

     #calculate average profit_loss change 
    average_change = round(sum(profitloss_change) / len(profitloss_change),2)

    #Find the greatest increase and greatest decrease in profit/loss
    max_change = max(profitloss_change)
    max_position = profitloss_change.index(max(profitloss_change))
    max_period = period[max_position]
    min_change = min(profitloss_change)
    min_position = profitloss_change.index(min(profitloss_change))
    min_period = period[min_position]
    
    #Print result to Terminal
    print(f"The total number of months is {str(months)}")
    print(f"The total profit/loss is {str(total_pl)}")
    print(f"The average change is ${str(average_change)}")
    print(f"The greatest increase in profit is {max_period}, $({max_change}) ")
    print(f"The greatest decrease in losses is {min_period}, $({min_change}) ")
    
    # Write result to output file
    # Specify the file and path
    output_path = os.path.join("Analysis", "Financial_Analysis.txt")

    # Open the file using "write" mode. Specify the variable to hold the contents
    with open(output_path, 'w') as txtfile:

    # Write the first row (column headers)
        txtfile.write("Financial Analysis\n")
        txtfile.write("------------------\n")
        txtfile.write("Total Months: %s\n" % (months))
        txtfile.write("Total: $%s\n" % (total_pl))
        txtfile.write("Average Change: $%s\n" % (average_change))
        txtfile.write("Greatest Increase in Profits: %s $(%s)\n" % (max_period,max_change))
        txtfile.write("Greatest descrease in Losses: %s $(%s)\n" % (min_period,min_change))   
      




        

    

