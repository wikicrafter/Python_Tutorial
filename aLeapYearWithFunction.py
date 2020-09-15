def isYearLeap(year):
#
# put your code here
  if year % 4 != 0:
    return False
  elif year % 100 != 0:
    return True 
  elif year % 400 != 0:
    return False 
  else:
    return True 

testData = [1900, 2019, 2020, 1987]
testResults = [False, True, True, False]
for i in range(len(testData)):
	yr = testData[i]
	print(yr,"->",end="")
	result = isYearLeap(yr)
	if result == testResults[i]:
		print("Leap year")
	else:
		print("Not a leap year")