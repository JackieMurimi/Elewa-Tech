#(p∨¬q) and q
p = True
q = False
r = True

var_p = p or (not q)
var_q = q
var_ans = var_p and var_q
print(var_ans)

#(p or q) not (¬q and ¬p)
var_p = p or q
var_q = (not q) and (not p)
var_ans1 = var_p; not (var_q)
print(var_ans1)

#(p ∨ q) ∧ (p or  ¬ q)
var_p = p or q
var_q = p or (not q)
var_ans2 = var_p and var_q
print(var_ans2)

#p ∨ (q ∧ r)
var_p = p
var_q = q and r
var_ans3 = var_p or var_q
print(var_ans3)

#¬(p ∧ q) ∨ (p ∨ q)
var_p = not(p and q)
var_q = p or q
var_ans4 = var_p or var_q
print(var_ans4)

#question two
#a and  b ∧ ¬c =  a or (b ∧ (¬c))
a = True
b = False
c = True

var_a = a
var_b = b and (not c)
var_c = b and (not c)



#(p ∧ q) ∨ (¬p ∧ q) ∨ (¬p ∧ ¬q).

