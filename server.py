from twisted.internet.protocol import DatagramProtocol
from twisted.internet import reactor


class Server(DatagramProtocol):
    def __init__(self) -> None:
        # super().__init__()
        self.clients = set()

    def datagramReceived(self, datagram: bytes, addr):
        datagram = datagram.decode("utf-8")
        if datagram == "ready":
            address = "\n".join([str(x) for x in self.clients])
            self.clients.add(addr)
            self.transport.write(address.encode('utf-8'), addr)
        # return super().datagramReceived(datagram, addr)


if __name__ == '__main__':
    reactor.listenUDP(9999, Server())
    reactor.run()
