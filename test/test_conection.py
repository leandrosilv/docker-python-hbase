# -*- coding: utf-8 -*-
#!/usr/bin/env python

import StringIO
import glob
import base64
import gc
import shutil
from StringIO import StringIO

from thrift import Thrift
from thrift.transport import TSocket, TTransport, THttpClient
from thrift.protocol import TCompactProtocol, TBinaryProtocol

from hbase import ttypes
from hbase.Hbase import Client, ColumnDescriptor, Mutation
from hbase import Hbase
from tendo import singleton

global thriftServer
global thriftPort
global saslServiceName
thriftServer = "127.0.0.1"
thriftPort = "9090"
saslServiceName = "hbase"
tablename = "namespace:table"

def execute():
    mutationsbatch = []
    mutations_attributes = {}

    sock = TSocket.TSocket(thriftServer, thriftPort)
    transport = TTransport.TSaslClientTransport(sock, thriftServer, saslServiceName)
    #protocol = TCompactProtocol.TCompactProtocol(transport)
    protocol = TBinaryProtocol.TBinaryProtocol(transport)
    client = Hbase.Client(protocol)
    transport.open()

    mutations = [
        Hbase.Mutation(column="c:coluna1", value='Texto da coluna 1'),
        Hbase.Mutation(column="c:coluna2", value='Texto da coluna 2')
        ]
    row_key = '00001'

    mutationsbatch.append(Hbase.BatchMutation(row=row_key, mutations=mutations))

    client.mutateRows(tablename, mutationsbatch, mutations_attributes)

    print('OK')

    del mutations
    del mutationsbatch

    mutationsbatch = []

    transport.close()

    del client
    del protocol
    del transport
    del sock

execute()