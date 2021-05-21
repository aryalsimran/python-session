import mymodule
print(mymodule.greeting("simran"))
from mymodule import greeting
print(greeting("simran"))
from mymodule import greeting,age
print(greeting("simran"),"Age=",age)


