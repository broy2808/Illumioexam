import csv #helps to process .csv files
from ipaddress import ip_address as ip_addr #ipaddress provides the capabilities to create, manipulate and operate on IPv4 and IPv6 addresses and networks
import os.path

class Firewall:
  def __init__(self, file):
    if not os.path.isfile(file):
            raise Exception("File not existed")
    self.file = file
    #dictionary of all the rules
    
    self.rules=self.process()  
    
  #Function to check if the packet can be accepted based on the rules in input file fw.csv
  def accept_packet(self,direction,protocol,port,ip_addresssingle):
     #Direction only process inbound or outbound
     if (str(direction)).lower() =="inbound" or (str(direction)).lower() =="outbound"  :
                d1=(str(direction)).lower()
     else:
        d1=""
        print((str(direction)).lower(), " - Invalid Direction!")
        
     #Protocol only process tcp and udp 
     if (str(protocol)).lower() =="tcp" or (str(protocol)).lower() =="udp"  :
                p1=(str(protocol)).lower()
     else:
         p1=""
         print((str(protocol)).lower()," - Invalid Protocol!")
         
     if port in range(1,65536):
         port=port
     else:
        port=""
     #check ipadress
     ip=ip_addr(ip_addresssingle)
     #Combine all to a single string
     combine=d1+p1+str(port)+str(ip)
     if combine in self.rules:
         return True
     else:
        return False
    
  #Function to process the input file
  def process(self):
      allrules={}
      with open(self.file) as csv_file:
          csv_reader = csv.reader(csv_file, delimiter=',')
          line_count = 0
          #process individual rows
          for row in csv_reader:
            
            print(f'\tDirection: {row[0]} , protocol: {row[1]} , port: {row[2]}, ip_address:  {row[3]}.')
            line_count += 1
            cur=[]
            #Direction only process inbound or outbound
            if (str(row[0])).lower() =="inbound" or (str(row[0])).lower() =="outbound"  :
                direction=(str(row[0])).lower()
            else:
                direction=""
                
            #Protocol only process tcp and udp 
            if (str(row[1])).lower() =="tcp" or (str(row[1])).lower() =="udp"  :
                protocol=(str(row[1])).lower()
            else:
                protocol=""
                
            ports=[]
            #Check the if multiple ports are present and process accordingly. Make a list of all the ports
            if "-" in str(row[2]).lower():
                start,end=str(row[2]).lower().split("-")
                for i in range(int(start),int(end)+1):
                    ports.append(i)
            else:
                ports.append(int(row[2]))

            ips=[]
            #Check the if multiple ips are present and process accordingly. Make a list of all the ips
            if "-" in str(row[3]).lower():
                start,end=str(row[3]).lower().split("-")
                start = ip_addr(start)
                end = ip_addr(end)
                while start <= end:
                   ips.append(str(start))
                   start += 1
            else:
                ips.append(str(row[3]))
            #Make a combination of all the ports and ips. Combine diection,protocol, ports, ips to a string and save into dictionary
            for x in ports:
                for y in ips:
                    com=direction+protocol+str(x)+y
                    if com not in allrules:
                        allrules[com]=1
            
         
      print(f'Processed {line_count} lines.')
      return allrules

class TestFirewall:
    def __init__(self,file):
        self.fw=Firewall(file)
        self.test()
    def test(self):
        print(self.fw.accept_packet("inbound", "tcp", 80, "192.168.1.2"))
        print(self.fw.accept_packet("inbound", "udp", 53, "192.168.2.1"))
        print(self.fw.accept_packet("outbound", "tcp", 10234, "192.168.10.11"))
        print(self.fw.accept_packet("inbound", "tcp", 81, "192.168.1.2"))
        print(self.fw.accept_packet("inbound", "udp", 24, "52.12.48.92"))
        #Invalid direction
        print(self.fw.accept_packet("in", "udp", 24, "192.168.1.2"))
        #Invalid protocol
        print(self.fw.accept_packet("inbound", "udpip", 24, "192.168.1.2"))
        #Invalid port- Return False
        print(self.fw.accept_packet("outbound", "tcp", 102341, "192.168.10.11"))

#Test the function validity
TestFirewall("path/to/fw.csv")
#Note I have not used any try cache as I am expecting all valid inputs will be processed.

