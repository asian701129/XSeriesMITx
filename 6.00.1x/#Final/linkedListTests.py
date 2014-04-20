from linkedList import *
from findFront import *



#Test 0
eric = Frob('eric')
andrew = Frob('andrew')
ruth = Frob('ruth')
fred = Frob('fred')
martha = Frob('martha')

insert(eric, andrew)
insert(eric, ruth)
insert(eric, fred)
insert(ruth, martha)



#Test 1A
insert(Frob("gabby"), Frob("allison"))

#Test 1B
insert(Frob("gabby"), Frob("allison"))

#Test 2A
insert(Frob("gabby"), Frob("zara"))

#Test 2B
insert(Frob("gabby"), Frob("zara"))

#Test 3A
test_list = Frob('abby')
insert(test_list, Frob("xander"))
insert(test_list, Frob("beto"))

#Test 3B
test_list = Frob('abby')
insert(test_list, Frob("xander"))
insert(test_list, Frob("beto"))

#Test 4
insert(Frob("alvin"), Frob("alvin"))

#Test 5
test_list = Frob('allison')
insert(test_list, Frob("lyla"))
insert(test_list, Frob("christina"))
insert(test_list, Frob("ben"))


#Test 6
Frob('zsa zsa')
a = Frob('ashley')
m = Frob('marcella')
v = Frob('victor')

insert(test_list, m)
insert(m, a)
insert(a, v)

#Test 7
test_list = Frob('mark')
c = Frob('craig')

insert(test_list, Frob("sam"))
insert(test_list, Frob("nick"))
insert(test_list, c)
insert(c, Frob("xanthi"))
insert(test_list, Frob("jayne"))
insert(c, Frob("martha"))

#Test 8
test_list = Frob('leonid')
a = Frob('amara')
j1 = Frob('jennifer')
j2 = Frob('jennifer')
s = Frob('scott')

insert(test_list, s)
insert(s, j1)
insert(s, j2)
insert(j1, a)

#Test 9
test_list = Frob('eric')

insert(test_list, Frob("eric"))
insert(test_list, Frob("chris"))
insert(test_list, Frob("john"))
insert(test_list, Frob("john"))
insert(test_list, Frob("chris"))
insert(test_list, Frob("eric"))
insert(test_list, Frob("john"))
insert(test_list, Frob("chris"))
