tcase1 = "Excuse me, where can I find a chicken rice shop?"
tans1 = ["Excuse me", "where can I find a chicken rice shop"]

tcase2 = "OMG!!! It is Friday....where should we go for dinner?"
tans2 = ["OMG", "It is Friday", "where should we go for dinner"]

tcase3 = "He’s nervous, but on the surface he looks calm and ready."
tans3 = ["He’s nervous", "but on the surface he looks calm and ready"]

def tokenise(input, expected_output):
  	#Replace all special characters
    result = input.replace('!', ',')
    result = result.replace('?', ',')
    result = result.replace('.', ',')
    #Split the string into list
    result = result.split(",")
    #Remove ,
    result = [w.replace(',', '') for w in result]
    #Remove empty elements
    result = [x for x in result if x]
    #Remove leading spaces
    result = [x.strip() for x in result]
    print('Pass' if result == expected_output else 'Failed!')

# Please make sure all test cases return 'Pass'
tokenise(tcase1, tans1)
tokenise(tcase2, tans2)
tokenise(tcase3, tans3)