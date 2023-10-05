#####################################
#### PART 9: FUNCTION EXERCISES #####
#####################################


# Complete the tasks below by writing functions! Keep in mind, these can be
# really tough, it's all about breaking the problem down into smaller, logical
# steps. If you get stuck, don't feel bad about having to peek to the solutions!

#####################
## -- PROBLEM 1 -- ##
#####################

# Given a list of integers, return True if the sequence of numbers 1, 2, 3
# appears in the list somewhere.

# For example:


def arrayCheck(nums):
    if 1 in nums and 2 in nums and 3 in nums:
        return True
    else:
        return False


print(arrayCheck([1, 1, 2, 3, 1]))
print(arrayCheck([1, 1, 2, 4, 1]))
print(arrayCheck([1, 1, 2, 1, 2, 3]))


# True
# False
# True
#####################
## -- PROBLEM 2 -- ##
#####################

# Given a string, return a new string made of every other character starting
# with the first, so "Hello" yields "Hlo".

# For example:


def stringBits(str):
    new_str = ""
    for l in range(0, len(str), 2):
        new_str += str[l]
    print(new_str)


stringBits('Hello')
stringBits('Hi')
stringBits('Heeololeo')


# → 'Hlo'
# → 'H'
# → 'Hello'

#####################
## -- PROBLEM 3 -- ##
#####################

# Given two strings, return True if either of the strings appears at the very end
# of the other string, ignoring upper/lower case differences (in other words, the
# computation should not be "case sensitive").
#
# Note: s.lower() returns the lowercase version of a string.
#
# Examples:
#
# end_other('Hiabc', 'abc') → True
# end_other('AbC', 'HiaBc') → True
# end_other('abc', 'abXabc') → True


def end_other(a, b):
    lower_a = a.lower()
    lower_b = b.lower()
    lower_a_compared = ""
    lower_b_compared = ""
    if len(a) >= len(b):
        for la in range(len(lower_a) - 1, (len(lower_a) - 1) - (len(lower_b)), -1):
            lower_a_compared += lower_a[la]
        print(lower_a_compared[::-1] == lower_b)
    else:
        for lb in range(len(lower_b) - 1, (len(lower_b) - 1) - (len(lower_a)), -1):
            lower_b_compared += lower_b[lb]
        print(lower_b_compared[::-1] == lower_a)


end_other('AbC', 'HiaBc')
end_other('abc', 'abXabc')
end_other('AbC', 'HiaBc')
end_other('abcde', 'weweweabcde')
#####################
## -- PROBLEM 4 -- ##
#####################

# Given a string, return a string where for every char in the original,
# there are two chars.

# doubleChar('The') → 'TThhee'
# doubleChar('AAbb') → 'AAAAbbbb'
# doubleChar('Hi-There') → 'HHii--TThheerree'

# def doubleChar(str):
#
#   # CODE GOES HERE


#####################
## -- PROBLEM 5 -- ##
#####################

# Read this problem statement carefully!

# Given 3 int values, a b c, return their sum. However, if any of the values is a
# teen -- in the range 13-19 inclusive -- then that value counts as 0, except 15
# and 16 do not count as a teens. Write a separate helper "def fix_teen(n):"that
# takes in an int value and returns that value fixed for the teen rule.
#
# In this way, you avoid repeating the teen code 3 times (i.e. "decomposition").
# Define the helper below and at the same indent level as the main no_teen_sum().
# Again, you will have two functions for this problem!
#
# Examples:
#
# no_teen_sum(1, 2, 3) → 6
# no_teen_sum(2, 13, 1) → 3
# no_teen_sum(2, 1, 14) → 3

# def no_teen_sum(a, b, c):
#
#   # CODE GOES HERE
# def fix_teen(n):
#
#   # CODE GOES HERE

#####################
## -- PROBLEM 6 -- ##
#####################

# Return the number of even integers in the given array.
#
# Examples:
#
# count_evens([2, 1, 2, 3, 4]) → 3
# count_evens([2, 2, 0]) → 3
# count_evens([1, 3, 5]) → 0

# def count_evens(nums):
#
#   # CODE GOES HERE
