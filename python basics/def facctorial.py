

def factorial(n):
  if(n==1):
    return(1)
  else:
    ruturn(n*factorial(n-1))
num=8
result=factorial(num)
print("factorial of",num,"is",result)