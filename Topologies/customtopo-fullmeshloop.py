"""Custom topology example REF: https://www.youtube.com/watch?v=yHUNeyaQKWY
Two Hosts and Four Switches in Full Mesh topology (all possible connection), hence with loops in topology.
Adding the 'topos' dict with a key/value pair to generate our newly defined
topology enables one to pass in '--topo=mytopo' from the command line.
NOTE: Must be used with Controller capable of detecting the loops in topology.
"""

from mininet.topo import Topo

class MyTopo( Topo ):
    "Simple topology example."

    def __init__( self ):
        "Create custom topo."

        # Initialize topology
        Topo.__init__( self )

        # Add hosts and switches
        H1 = self.addHost( 'h1' )
        H2 = self.addHost( 'h2' )
        S1 = self.addSwitch( 's1' )
        S2 = self.addSwitch( 's2' )
        S3 = self.addSwitch( 's3' )
        S4 = self.addSwitch( 's4' )
        SwitchList = (S1, S2, S3, S4)
        # Add links 
        #between switches
        for index in range(0, len(SwitchList)):
            for index2 in range( index+1, len(SwitchList)):
                self.addLink(SwitchList[index], SwitchList[index2])
    
                   
        #between host and switch
        self.addLink( S1, H1 )
        self.addLink( S3, H2 )
       # self.addLink( S3, S1 )
     #   self.addLink( S3, H2 )

topos = { 'mytopo': ( lambda: MyTopo() ) }
