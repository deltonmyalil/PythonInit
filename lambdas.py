#lambdas are just like functions but without a name
# to ge the square of a number
y = int(input("Enter the num to be squared>>>"))
result = (lambda x:x*x)(y)
print(result)

'''
format of lambda:
(lambda var:<expresssion>)(argument)

lambdas does not contain return stmt
'''