# import the random module
import random

# create the class Fortune_Teller
class Fortune_Teller:
    # create the constructor (__init__) method
    # it takes as input: 
    #   a list of possible fortunes and 
    # it sets this object's fortune_list (instance variable) to the passed list 
    # it sets this object's history_list to the empty list (instance variable)

    # create the tell method
    # it randomly picks an index from 0 to the number of items in the 
    #       fortune_list minus one
    # it adds that index to the end of the history_list 
    # it returns the fortune at that index in this object's fortune_list

    # create the __str__ method
    # if the length of history_list is 0 it returns "Last fortune: not given yet"
    # else it returns the fortune at the last index in the history_list as 
    # "Last fortune: fortune"
    
    # create the print_history method
    # prints "[index] fortune" for each of the indicies in the history_list 
    # from the first to the last with each on a single line

    # create the print_count_for_num method
    # it prints how many times the passed index is found in the history_list  
    
    # EXTRA POINTS
    # create the five_hundred method
    # it tells a fortune 500 times, prints the counts for each index, and 
    # prints the most frequently occurring index

# main funtion for testing
def main():
    # you can change these possible fortunes
    fortune_list = ["Win the lottery", \
                    "Slip and fall", \
                    "Snow day on Wednesday",  \
                    "Frostbite on Wednesday",  \
                    "Snow day on Thursday", \
                    "Get an A in SI 206"]    
    
    #Create a fortune-teller and test it
    print("Testing the first fortune-teller:")
    teller = Fortune_Teller(fortune_list)
    print("Fortune : " + teller.tell())
    print("Testing the print of the last fortune")
    print(teller)
    print("Fortune : " + teller.tell())
    print("Testing the print of the last fortune")
    print(teller)
    print("Printing the full history:")
    teller.print_history()
    print("Printing the number of times index 1 occured")
    teller.print_count_for_num(1)
    print()

    #Create another fortune-teller
    print("Testing the second fortune-teller:")
    teller2 = Fortune(fortune_list)
    print("Testing when no fortunes have been told yet")
    print(teller2)
    print("Fortune : " + teller2.tell())
    print(teller2)
    for x in range(5):
        print("Fortune : " + teller2.tell())
    print("Printing the full history:")
    teller2.print_history()
    print("Printing the number of times index 2 occured")
    teller2.print_count_for_num(2)

    #EXTRA POINTS
    #Try telling 500 fortunes

# only run the main function if this file is being run (not imported)
if __name__ == "__main__":
    main()
