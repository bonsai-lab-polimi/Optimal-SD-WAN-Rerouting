from mininet.topo import Topo
from mininet.link import TCLink

class MyTopo( Topo ):
  

    def build( self ):
        

        # Add hosts and switches
        HostA = self.addHost( 'hA' , ip='10.0.0.3' )
        Host1 = self.addHost( 'h1' , ip='10.0.0.1')
        Host2 = self.addHost( 'h2' , ip='10.0.0.2')
        Host4 = self.addHost( 'h4' , ip='10.0.0.4')
        Host5 = self.addHost( 'h5' , ip='10.0.0.5')
        Host6 = self.addHost( 'h6' , ip='10.0.0.6')
        Host7 = self.addHost( 'h7' , ip='10.0.0.7')

        Switch1 = self.addSwitch( 's1' )
        Switch2 = self.addSwitch( 's2' )
        Switch3 = self.addSwitch( 's3' )
        Switch4 = self.addSwitch( 's4' )
        Switch5 = self.addSwitch( 's5' )

        # Add links
        self.addLink( HostA, Switch1 )
        self.addLink( Switch1, Switch2 )
        self.addLink( Switch1, Switch3 )
        self.addLink( Switch2, Switch4, cls=TCLink, bw=1 )
        self.addLink( Switch3, Switch5, cls=TCLink, bw=1 )
        self.addLink( Switch2, Switch5, cls=TCLink, bw=1 )
        self.addLink( Switch3, Switch4, cls=TCLink, bw=1 )
        self.addLink( Switch4, Host1 )
        self.addLink( Switch4, Host4 )
        self.addLink( Switch4, Host5 )
        self.addLink( Switch5, Host2 )
        self.addLink( Switch5, Host6 )
        self.addLink( Switch5, Host7 )



topos = { 'mytopo': ( lambda: MyTopo() ) }

