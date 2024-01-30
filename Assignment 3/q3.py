for x1 in range(2):
    for x2 in range(2):
        for x3 in range(2):
            for x4 in range(2):
                result = x4 ^ (x1*x4) ^ (x1*x2*x4) ^ (x1*x2*x3*x4)
                print(x1, "&", x2, "&", x3, "&",x4, "&",result,"\\\\")
                #print("x1:",x1, "x2:",x2,"x3:",x3,"x4:",x4,"Result:", result)
                
#x1: 0 x2: 0 x3: 0 x4: 0 Result: 0
#x1: 0 x2: 0 x3: 0 x4: 1 Result: 1
#x1: 0 x2: 0 x3: 1 x4: 0 Result: 0
#x1: 0 x2: 0 x3: 1 x4: 1 Result: 1
#x1: 0 x2: 1 x3: 0 x4: 0 Result: 0
#x1: 0 x2: 1 x3: 0 x4: 1 Result: 1
#x1: 0 x2: 1 x3: 1 x4: 0 Result: 0
#x1: 0 x2: 1 x3: 1 x4: 1 Result: 1
#x1: 1 x2: 0 x3: 0 x4: 0 Result: 0
#x1: 1 x2: 0 x3: 0 x4: 1 Result: 0
#x1: 1 x2: 0 x3: 1 x4: 0 Result: 0
#x1: 1 x2: 0 x3: 1 x4: 1 Result: 0
#x1: 1 x2: 1 x3: 0 x4: 0 Result: 0
#x1: 1 x2: 1 x3: 0 x4: 1 Result: 1
#x1: 1 x2: 1 x3: 1 x4: 0 Result: 0
#x1: 1 x2: 1 x3: 1 x4: 1 Result: 0

