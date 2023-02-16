#Author Anthony GRACE
#NUMBER: 473185590
#SIMPLE FUNCTION BLOCKS FOR MY_LIBRARY

'''
[][][][][][][]
SORTING 
[][][][][][][]

'''

'''
CHECK INT HIGHEST VALUE
'''
def maxOfThree(a, b, c):
#function basic booleen
    if a > b and a > c:
        return a
    elif b > a and b > c:
        return b
    else:
        return c
'''
CHECK CHAR UPPER AMOUNT 
'''
def countUppercase(string):
    count = 0
    for char in string:
        if char.isupper():
            count += 1
    return count
'''
CHECK WEATHER A STRING IS THE SAME AS ANOTHER STRING
'''
def isEqual(str1, str2):
    if str1 == str2:
        print("STRING EQUAL!")
        return True
    else:
        print("STRING NOT EQUAL!")
        return False
# Determine if the strings are equal and print the result
'''
SECOND VERSION
'''

def isEqual1(str1, str2):
    if(len(s1) != len(s1)):
           return(False)
    for i in range(0, len(s1)):
        if (s1[i] != s2[i]):
            return(False)
    return(True)
'''
#SUM THE LIST AD DIVIDE IT BY LENGTH, IF NO INPUT RETURN ZERO

def calculateAverage(lst):
    if len(lst) == 0:
        return 0
    else:
        return round(sum(lst) / len(lst), 2)

[][][][][][][]
NETWORKING
[][][][][][][]


'''
def get_ip_address(ifname):
    """Function to get the IP address of a network interface."""
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    return socket.inet_ntoa(fcntl.ioctl(
        s.fileno(),
        0x8915,  # SIOCGIFADDR
        struct.pack('256s', ifname[:15].encode())
    )[20:24])

def get_network_ips(ip_address):
    """Function to get all IP addresses on a network."""
    network = ".".join(ip_address.split(".")[:-1]) + "."
    return [network + str(i) for i in range(1, 256)]

def find_other_ips(interface_name):
    """Function to find all other IP addresses on a network."""
    ip_address = get_ip_address(interface_name)
    return get_network_ips(ip_address)
