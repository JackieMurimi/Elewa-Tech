#new examples of logical operators
#OR test
x = True
y = False

var_0 = x or y
print(var_0)

#AND test run
var_a = x and y
var_b = x and x
print(var_a)
print(var_b)

#Not test
var_c = not y
print(var_c)

var_d = not x
print(var_d)

#demo of logical operation
p = True
q = False

#assignment demo 1 
var_q = p or (not q) #p and negative q
var_s = (not p) and q #negative p and q
ans = var_q and var_s #full rep of the question
print(ans) #print my ans

#demo 
p = True
q = False
r = True

#create segments of the questions
var_p = p or q
var_q = r or (not q)

var_ans0 = var_p and var_q

var_r = (p or r)
#full operation
var_ans1 = var_ans0 or (not var_r)
print(var_ans1)


