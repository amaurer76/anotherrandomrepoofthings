#!/usr/bin/python

from mininet.topo import Topo
from mininet.net import Mininet
from mininet.util import dumpNodeConnections
from mininet.log import setLogLevel

class Proj3Topo ( Topo ):
	def __init__( self ):
		Topo.__init__( self )
		h1 = self.addHost( 'h1' , ip='192.168.2.10')
		h2 = self.addHost( 'h2' , ip='192.168.2.20')
		h3 = self.addHost( 'h3' , ip='192.168.2.30')
		h4 = self.addHost( 'h4' , ip='192.168.2.40')

		s1 = self.addSwitch( 's1' )

		self.addLink( h1, s1 )
		self.addLink( h2, s1 )
		self.addLink( h3, s1 )	
		self.addLink( h4, s1 )

topos = { 'proj3topo': ( lambda: Proj3Topo() ) }
