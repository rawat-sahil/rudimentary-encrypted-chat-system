from optparse import OptionParser
from server import runServer
from client import runClient
from ca import runca


def main(options ,args):

    if options.CA:
        if options.port !=None :
            runca(options.port)
        else :
            print("-p is required to run ca")
            exit(0)

    elif options.server:
        if (options.port != None)and (options.caIP!=None) and (options.caPort!=None):
            runServer(options.port,options.caIP,options.caPort)

        else :
            print("-p is required to run server")
            exit(0)
    elif options.client:
        if (options.serverIP!=None) and(options.serverPort!=None) and (options.caIP!=None) and (options.caPort!=None):
            runClient(options.serverIP,options.serverPort,options.caIP,options.caPort)

        else :
            print("-i -j -k -l options are required to run client")
            exit(0)


if __name__=="__main__":
    parser = OptionParser()
    parser.add_option("-s", "--server", dest="server", action="store_true", default=False,
                      help="choose this option to run server")
    parser.add_option("-a", "--CA", dest="CA", action="store_true", default=False,
                      help="choose this option to run server as ca")
    parser.add_option("-p", "--port", dest="port", action="store", type="int", help="specify the port to run server")
    parser.add_option("-c", "--client", dest="client", action="store_true", default=False,
                      help="choose this option to run client")
    parser.add_option("-i", "--serverIP", dest="serverIP", action="store", type="string",default="127.0.0.1",
                      help="specify the ip of the server that you want to connect with.\n default value is 127.0.0.1")
    parser.add_option("-j", "--serverport", dest="serverPort", action="store", type="int",
                      help="specify the port of the server with the ip specified above")
    parser.add_option("-k", "--caIP", dest="caIP", action="store", type="string",default="127.0.0.1",
                      help="specify the ip of the CA that you want to fetch the certificate from.\n default value is 127.0.0.1")
    parser.add_option("-l", "--caport", dest="caPort", action="store", type="int",default=8081,
                      help="specify the port of the CA with the ip specified above.\n default value is 8081")

    (options, args) = parser.parse_args()
    main(options,args)
    print(options)
    print(args)