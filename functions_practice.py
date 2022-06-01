def hello():
    print(hello("Hello User"))

def pack(a,b,c):
    return [a,b,c]
print(pack("a", "b", "c"))

def eat_lunch(first_eat):
    if len(first_eat) == 0:
        print("lunch box is empty")
    else:
        for i in range(len(first_eat)):
          if i == 0:
             print(f"First I eat {first_eat[0]}")
          else:
             print(f"Next I eat {first_eat[i]}")
eat_lunch([])
eat_lunch(["rice"])
eat_lunch(["rice", "beans", "yam", ])

