
a=set(['Jonn','Mary','Tina','Fiona','Claire','Eva','Ben','Bill','Bert'])
eng=set(['Jonn','Mary','Fiona','Claire','Ben','Bill'])
math=set(['Mary','Fiona','Claire','Eva','Ben'])
print("英文與數學都及格",eng&math)
print("數學不及格",a-math)
print("英文及格且數學不及格",eng-math)
