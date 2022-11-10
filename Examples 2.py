case1 = "You have to keep your mind as wide-open as your eyes, because almost nothing is what it seems."
ans1 = 'You have to keep your mind as wideopen as your eyes because almost nothing is what it seems'
case2 = "You can have my email address, here it is: XXX@email.com"
ans2 = 'You can have my email address here it is XXXemailcom'
case3 = "This is the final stop for this train. Please mind the gap."
ans3 = 'This is the final stop for this train Please mind the gap'

#import punctuation symbol
import string

def remove_punc(input, expected_output):
    #split sentence and remove all punctuation and rejoin
    result = "".join([w for w in input if w not in string.punctuation])
    #check in input == expected_output
    print('Pass' if result == expected_output else 'Failed!')

# Please make sure all test cases return 'Pass'
remove_punc(case1, ans1)
remove_punc(case2, ans2)
remove_punc(case3, ans3)