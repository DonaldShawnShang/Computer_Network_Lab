#import socket module
from socket import *

# set server to ipv4 addressing and TCP protocol
serverSocket=socket(AF_INET,SOCK_STREAM)

#set the port for the server to listen to 12000
serverPort=12000

#bind the socket to all server to listen to
serverSocket.bind(('',serverPort))

#set the socket to listen
serverSocket.listen(1)

while True:

    #start serving
    tabs='\t\t\t'
    print('||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||')
    print(tabs,'Ready to serve...')
    print('||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||')

    #establish connection 
    #return HTML Message to client
    connectionSocket, addr=serverSocket.accept()
    message=connectionSocket.recv(1024).decode()

    #print data about the incoming connection
    print('\nincoming message : \t\t', message)
    print('\ntype of connectionSocket : \t', type(connectionSocket))
    print('socket type : ',tabs, connectionSocket.type)
    print('socket name : ',tabs, connectionSocket.getsockname())
    print('address : ',tabs, addr)


    # split the message string on spaces and return the first two elements.
    lst = message.split(' ')

    # if the arguments exist, assign them to be the method and filenames at index 0 & 1 respectively
    if (lst[0]):
        method = lst[0]
    if (lst[1]):
        filename = lst[1]

    print('method : ', tabs, method)
    print('filename : ',tabs, filename)

    try: # try to open the requested filename
        # if this fails, the server will return a 404 error.

        # if the file name string comes in with a prepended '/' remove it
        if (filename[0] == '/'):
            f = open(filename[1:])
            filename = filename[1:]
        else :
            f = open(filename)

        # read in the content-body of the file
        file_content = f.read()

        # preserve the output of the open() func
        outputdata = f
        print('\nopen() output : ', outputdata)

        # send HTTP header  lines into connectionSocket using the .send() method.
        # Encode your strings using .encode('utf-8')
        # Make sure newlines, spaces, etc. are formatted correctly so that the HTTP header is well formed.
        # Return status code 200
        response = '\nHTTP/1.1\n200\nOK\n\n' + file_content
        connectionSocket.send(response.encode('utf-8'))

        print('\n\tsuccessfully sent %s to the requester\n' % (filename))

    except IOError:

        # send response message for file not found.
        # status code is 404. Send the header as above,
        # open the "404.html" file and read its contents into
        # the output data variable.
        print('\n\tcould not open the file...\n\n\t...sending 404.html to the requester\n\n')
        error_content = open('/404.html')
        error_content = '\nHTTP/1.1\n404\nSomething went wrong, only a programmer can fix it...\n' + error_content.read()
        connectionSocket.send(error_content.encode())

connectionSocket.close()


