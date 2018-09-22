menu ="what would you like:\n\
1.A compliment?\n\
2.An insult?:\n\
3.A proverb?\n\
4.An idiom?\n\
Q.Quit\n"#prints when ran
answer = input(menu)#states 'answer' is text so numbers, decimals and letters can be used
if answer =="1":
    print("you look lovely today")
elif answer == "2":
    print("You smell funny")
elif answer =="3":
    print("The pen is mightier than the swoard")
elif answer =="4":#you can have as many elif's as you like
    print("Actions speak louder than words")
elif answer =="Q":
    print("Goodbye!!!")
else:
    print("pick something from the list!")
    
# == equal to
# <= greater than or equal to
# >= lesser than or equal to
# != not equalt to
