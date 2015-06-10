TASK 1 

Due to the files being so large and my computer being an old model, I randomly sampled 1% of the original Data.  

python output:

length of Sampled searches is 204505
length of sampled booking is 99785


TASK 2

top ten arrivals airports in the world 2013
           pax
arr_port     
CDG       782
LAX       778
LHR       743
JFK       728
MCO       711
LAS       655
BKK       606
MIA       533
DXB       522
FCO       520



Task 3

For this task I used the groupby function by pandas on the destination and the month. The plot is found under monthlyNumberOfSearches.png name. 
The plot show that the most popular month to travel to barcelona, madrid and malaga is in the summer and destinations Barcelona and Madrid are much more popular that Malaga. However there might be some artifacts due to sampling.


Task 4:

for this task i made a new column called combi which will concat the origin:destination . Then pandas was used to
merge the two files with only the columns that were important.
at the first step only the searches were accepted that has the same origin:destination as the booking
for making this even more accurate I thought that the booking can only take place if the cre_date(creation date) is after the search date. 
The third condition was that the pax has to be greater than zero.Meaning the number of passengers did not cancel the booking.The result is written to a csv file. 


