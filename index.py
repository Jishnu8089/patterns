# Basic syntax ...
# 
# for i  in range(5) :
#     for j in range(5) :
#         print("*" , end=" ")
#     print()

# for i in range(5 , 0 , -1) :
# #    print(i)
#     for j in range(i) :
#       print("*" , end=" ")
#     print()

# for i in range(6) :
# #    print(i)
#     for j in range(i) :
#       print("*" , end=" ")
#     print()


# Square Pattern ..

# n = 5 
# for i in range(n) :
#     for j in range(n) :
#         print("*" , end=" ")
#     print()    

# n = 6
# for item in range(n) :
#     for j in range(n) :
#         print("/" , end=" ")
#     print()


# Right Triangle ..
# n = 5 
# for i in range(1, n + 1) :
#     for j in range(i) :
#         print("*" , end=" ")
#     print()

# Inverted Triangle 

# n = 5 
# for i in range(n, 0 ,-1) :
#     for j in range(i) :
#         print("*" , end=" ")
#     print()


# n =5 

# for i in range(n , 0 ,-1) :
#     for j in range(i) :
#         print("$" , end=" " )
#     print()

# # Pyramid pattern ..
# n = 5
# for i in range(n) :
#     print(" " *  (n - i - 1) + 
#         "* " + (i + 1)) 
#     print()

# Number Triangle .

# n = 5 
# for i in range(1, n + 1) :
#     for j in range(1 , i + 1) :
#         print(j, end=" ")
#     print()

#  Diamond Pattern ..
# n = 5 
# for i in range(1 , n + 1) :
#     print(" " * (n - i) + "* " * i)
# for i in range(n - 1 , 0 , -1 ):
#     print(" " * (n - i)+ "* " * i)

# Floyd's Triangle ..
# n = 5 
# num = 1
# for i in range(1, n + 1):
#     for j in range(i) :
#         print(num ,end=" ")
#         num += 1
#     print()

# Alphabet  pattern ..
# n = 5 
# for i in range(1 , n + 1) :
#     ch = ord('A')
#     for j in range(i) :
#         print(chr(ch), end=" ")
#         ch += 1
#     print()









