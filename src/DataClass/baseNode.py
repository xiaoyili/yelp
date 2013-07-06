__author__ = 'eric'


class baseNode(object):
    """
    base node

    """

    def __init__(self, id=None, name=None):
        assert id is not None

        self.id = id
        self.name = name
        self.outgoing = list()
        self.incoming = list()

    def add_outgoing(self, id=None):
        """
        add new outgoing node
        """
        if id in self.outgoing:
            print "ERR ... Node:" + str(id) + " exists in outgoing list"
        else:
            self.outgoing.append(id)
            print "... Node:" + str(id) + " added into outgoing list"


    def add_incoming(self, id=None):
        """
        add new incoming node
        """
        if id in self.incoming:
            print "ERR ... Node:" + str(id) + " exists in incoming list"
        else:
            self.incoming.append(id)
            print "... Node:" + str(id) + " added into incoming list"


    def print_linkage(self):
        """
        print linkage for this node
        """
        print "Node:" + str(self.id) + " have incoming links from:"
        for id in self.incoming:
            print str(id)
        print "Node:" + str(self.id) + " have outgoing links to:"
        for id in self.outgoing:
            print str(id)


if __name__ == '__main__':
    n1 = baseNode(id='0')
    n1.add_incoming(id='1')
    n1.add_incoming(id='1')
    n1.add_outgoing(id='2')
    n1.add_outgoing(id='2')
    n1.print_linkage()


