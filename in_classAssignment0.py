#assignment 1
P = True
Q = False
R = True

var_P = (P or Q) and R
var_Q = P and R
var_R = Q and R
var_ans0 = var_P or var_Q or var_R
print(var_ans0)


p = True
q = False
r = True

var_p = (not p) and (not q)
var_q = q and (not r)
var_ans1 = var_p or var_q
print(var_ans1)

