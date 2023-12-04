import pyautogui
# from time import sleep
# sleep(5)
n = int(input())
for i in range(0,n+1):
    pyautogui.write('#'*i, interval=0.25)
    pyautogui.press('\n')




# n = int(input())
# for i in range(0, n):
# 	for j in range(0, i+1):
# 		print("#", end=" ")
# 	print()


# def pypart(n):
# 	myList = []
# 	for i in range(1,n+1):
# 		myList.append("*"*i)
# 	print("\n".join(myList))

# # Driver Code
# n = 5
# pypart(n)









