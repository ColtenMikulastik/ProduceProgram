# I'm ready to try this I think lmao
# The idea is to make a program based on the date,
# to give the produce that is available/good for that month
# according to the ProduceData.txt

# 10/24/2021: I created the '-' search, so yeah that's about as far as I got lmao
# 11/5-6/2021: created the month part, still bugs with the ; idk why python is so dead set on being a hoe lmao,
#   -I think I'm gonna use something like git to come back to it later lmao
# 11/14/2021: I finished, I could add a bash script to make it print the result on the "date" bash cmd
# but I have decided that I'm done with this program haha


print("Hello!")

data = open("Producedata.txt", 'r')


all_produce = data.readlines()
# here we are useing "readlines" mem func becasue it will read the input one line at a time :^)

# names of produce will be the keys and the months will be the values 
dic_of_all_produce = {}
names_of_all_produce = []
produce_months = []

# so I need to creat a list that has all the months so that I can then index through the list
# and find the actual months in between the two written months in the data
months_o_da_year = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December", 
"January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]

#First were gonna loop through the list of all the produce line by line
for produce in all_produce:
    list_produce = list(produce)
    list_produce.append(' ')
    
    #we will now look for the '-' character!
    check_char = ''
    iteration_counter = 0
    while check_char != '-':
        check_char = list_produce[iteration_counter]
        iteration_counter += 1
   
    # now we are going to keep tabs on wher the hyphon is
    hyphon_index = iteration_counter
    
    # once we have found the '-' char, we will now look for the preceding space char
    check_char = ''
    while check_char != ' ':
        check_char = list_produce[iteration_counter]
        iteration_counter -= 1
    iteration_counter += 2
    
    # so now we figure out how to do these months
    which_months = []
    fir_month = ''
    las_month = ''

    # find the first month
    fir_month = fir_month.join(list_produce[iteration_counter:hyphon_index - 1])
    
    # find the second month
    month_iterator = hyphon_index
    temp_char = ''
    while temp_char != ' ':
        temp_char = list_produce[month_iterator]
        month_iterator += 1
    las_month = las_month.join(list_produce[hyphon_index:month_iterator - 2])
    # make sure the the first word isn't "Year"

    if(fir_month == "Year"):
        for i in range(0,11):  # Make year-round all the months
            which_months.append(months_o_da_year[i])
    else:
        ind_of_fir_month = months_o_da_year.index(fir_month)
    
        # now start from the first month, and collect the months on the way to the last month
        sec_mon_found = False
        month_iterator = ind_of_fir_month
        while not(sec_mon_found):
            which_months.append(months_o_da_year[month_iterator])
            if(months_o_da_year[month_iterator] == las_month):
                sec_mon_found = True
            month_iterator += 1

    produce_months.append(list(which_months))
    
    # !right so here I kinda just gave up and did a thing that I didn't think would work, but it did... so that's pretty cool >:^D
    # so then we find the name of the produce, and the add it to the dictionary
    produce_name = ""
    produce_name = produce_name.join(list_produce[:iteration_counter - 1])
    names_of_all_produce.append(produce_name)

# we need to add these pairs to the original dictionary
for i in range(0, len(names_of_all_produce)):
    dic_of_all_produce[names_of_all_produce[i]] = produce_months[i]

data.close()

# print(dic_of_all_produce)

# this is an interesting loop, for the dictionary

for key, values in dic_of_all_produce.items():
    print(key, end=':')
    for value in values:
        print(value, end=' ')
    print()

# first im gonna get the month and prepare the list
input_month = input("What month is it now?: ")
produce_in_month =[]

# loop through the dic and see which produce has the ^ input month
for key, values in dic_of_all_produce.items():
    if input_month in values:
        produce_in_month.append(key)

# print that to the screen
print("Here is the produce in the month " + input_month + ":")
for produce in produce_in_month:
    print(produce)

print("Thank you for using my app")

# yeah boi we did it!

#loop through the names of the month

#I officially give up for right now lmao, I have some linux home work to do hahahahah
# I'm baaaaaack



