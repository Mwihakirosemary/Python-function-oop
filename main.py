def greet(lst):
    for i in lst:
        print(i)
        for ele in i:
            print(ele)
          
greet([{"name":"Mary","age":20},{"name":"jane","age":20}])
