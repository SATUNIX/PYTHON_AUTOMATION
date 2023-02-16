class Sorting:
    @staticmethod
    def max_of_three(a, b, c):
        if a > b and a > c:
            return a
        elif b > a and b > c:
            return b
        else:
            return c

    @staticmethod
    def count_uppercase(string):
        count = 0
        for char in string:
            if char.isupper():
                count += 1
        return count

    @staticmethod
    def is_equal(str1, str2):
        if str1 == str2:
            print("STRING EQUAL!")
            return True
        else:
            print("STRING NOT EQUAL!")
            return False

    @staticmethod
    def is_equal_2(s1, s2):
        if len(s1) != len(s2):
            return False
        for i in range(0, len(s1)):
            if s1[i] != s2[i]:
                return False
        return True


class Networking:
    @staticmethod
    def get_ip_address(ifname):
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        return socket.inet_ntoa(fcntl.ioctl(
            s.fileno(),
            0x8915,  # SIOCGIFADDR
            struct.pack('256s', ifname[:15].encode())
        )[20:24])

    @staticmethod
    def get_network_ips(ip_address):
        network = ".".join(ip_address.split(".")[:-1]) + "."
        return [network + str(i) for i in range(1, 256)]

    @staticmethod
    def find_other_ips(interface_name):
        ip_address = Networking.get_ip_address(interface_name)
        return Networking.get_network_ips(ip_address)
