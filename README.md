# Illumioexam
Illumio Online assessment

# Coding Environment
Python3

# Run the file:
Download everything in the folder and give exact directory for the CSV file(Path/to/fw.csv).
You can change the filename manually inside validate.py. Due to time limit not able to implement that.
-> python validate.py

# Implementation:
I have saved the direction,protocol,port and ip combination as form of key in Dictionary by reading input from fw.csv file(Basically the Rules file). Then in the accept function, i am just concatinating all the information and search in the dictionary key. But this has increased the maximum amount of keys significantly and as only considering the ips can add keys upto 256^4. So, the overall time complexity is 0(n^2) which is very inefficient. But within the time limit of 2 hours I was able to came up with the above solution.

Improvement:
To improve this we can only consider direction,protocol,port as a key combination of a dictionary and store IPs as values. We can store the list of IPs as sorted values. Then when we validate an IP in accept function we can provide the key combination(direction,protocol,port) and search through this list to find if that is valid or not. This whole search will take 0(log(n))- Binary search or 0(n)- Sequential search.

Note: Please download all the files and maintain the folder structure.





