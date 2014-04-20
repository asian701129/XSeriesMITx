# laceStringsTester

# chose the function you want to test
from laceStrings import *
# Test Cases
# Black Box Testing

# equal length s1 s2
# 'efgh' and 'abcd' should give 'eafbgchd'
str3 = laceStrings('efgh', 'abcd')
print str3

# s1 > s2
# 'efghi' and 'abcd' should give 'eafbgchdi'
str3 = laceStrings('efghi', 'abcd')
print str3

# s1 < s2
# 'abcd' and 'efghi' should give 'aebfcgdhi'
str3 = laceStrings('abcd', 'efghi')
print str3



from laceStringsRecur import *
# Test Cases
# Black Box Testing

# equal length s1 s2
# 'efgh' and 'abcd' should give 'eafbgchd'
str3 = laceStringsRecur('efgh', 'abcd')
print str3

# s1 > s2
# 'efghi' and 'abcd' should give 'eafbgchdi'
str3 = laceStringsRecur('efghi', 'abcd')
print str3

# s1 < s2
# 'abcd' and 'efghi' should give 'aebfcgdhi'
str3 = laceStringsRecur('abcd', 'efghi')
print str3