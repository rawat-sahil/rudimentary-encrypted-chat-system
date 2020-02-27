from optparse import OptionParser

parser=OptionParser()
parser.add_option("-s","--server",dest="server",action="store_true",default=False,help="choose this option to run server")
parser.add_option("-a","--CA",dest="CA",action="store_true",default=False,help="choose this option to run server as ca")
parser.add_option("-p","--port",dest="port",action="store",type="int",help="specify the port to run server")
parser.add_option("-c","--client",dest="client",action="store_true",default=False,help="choose this option to run client")
parser.add_option("-i","--serverIP",dest="serverIP",action="store",type="string",help="specify the ip of the server that you want to connect with")
parser.add_option("-j","--serverport",dest="serverPort",action="store",type="int",help="specify the port of the server with the ip specified above")
parser.add_option("-k","--CAIP",dest="CAIP",action="store",type="string",help="specify the ip of the CA that you want to fetch the certificate from")
parser.add_option("-l","--CAport",dest="CAPort",action="store",type="int",help="specify the port of the CA with the ip specified above")


(options,args)=parser.parse_args()
print(options)
print(args)