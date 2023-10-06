import influxdb_client 
from influxdb_client import InfluxDBClient, Point
from influxdb_client.client.write_api import SYNCHRONOUS
from datetime import datetime
from os import close
from ryu.base import app_manager
from ryu.controller import ofp_event
from ryu.controller.handler import CONFIG_DISPATCHER, MAIN_DISPATCHER
from ryu.controller.handler import set_ev_cls
from ryu.ofproto import ofproto_v1_3
from ryu.lib.packet import packet, ethernet
from ryu.lib import hub

class Mpls(app_manager.RyuApp):
    OFP_VERSIONS = [ofproto_v1_3.OFP_VERSION]


    def __init__(self, *args, **kwargs):
        super(Mpls, self).__init__(*args, **kwargs)

        # tabella dei MAC 
        self.mac_to_port = {}

        # tabella dei datapath 
        self.datapaths = {}

        # thread che lancia periodicamente le richieste
        self.monitor_thread = hub.spawn(self._monitor)


    def _monitor(self):
        hub.sleep(10)
        while True:
            self.change_path()
            hub.sleep(10)



    def change_path(self):
        datapath = None              
        ofproto = None               
        parser = None  
        url="http://10.10.5.101:8086"
        token="qMUeAlYWsvFj9yWmKFy4eh5_yLlXbqgj-8bdauCjg0d25UVbFsqW-cWYklQfJnk47izpidwnVmPL76JvTwAJFA=="
        org="Poli"
        bucket= "Poli"
        client = influxdb_client.InfluxDBClient(url=url, token=token, org=org)      
        with open("Tesi/result.txt", 'r') as file:
            content=file.read(1)
            if (content=="1"):
                #path that goes through s2 to h1
                print("path 1")
                datapath=self.datapaths[1]
                ofproto = datapath.ofproto               
                parser = datapath.ofproto_parser  
                match = parser.OFPMatch(eth_type=0x0800, ipv4_dst="10.0.0.1")
                actions = [
                    parser.OFPActionPushMpls(ethertype=34887),
                    parser.OFPActionSetField(mpls_label=1000),
                    parser.OFPActionOutput(2)                           
                ]
                inst = [parser.OFPInstructionActions(ofproto.OFPIT_APPLY_ACTIONS,
                                                actions)]
                mod = parser.OFPFlowMod(datapath=datapath, priority=4,
                                    match=match, instructions=inst)
                datapath.send_msg(mod)

                datapath=self.datapaths[2]
                ofproto = datapath.ofproto               
                parser = datapath.ofproto_parser  
                match = parser.OFPMatch(eth_type=0x8847, mpls_label=1000)
                actions = [
                    parser.OFPActionPopMpls(),
                    parser.OFPActionOutput(2)
                ]
                inst = [parser.OFPInstructionActions(ofproto.OFPIT_APPLY_ACTIONS,
                                                actions)]
                mod = parser.OFPFlowMod(datapath=datapath, priority=4,
                                    match=match, instructions=inst)
                datapath.send_msg(mod)
                #inverse direction
                match = parser.OFPMatch(eth_type=0x8847, mpls_label=1001)
                actions = [
                    parser.OFPActionPopMpls(),
                    parser.OFPActionOutput(1)
                ]
                inst = [parser.OFPInstructionActions(ofproto.OFPIT_APPLY_ACTIONS,
                                                actions)]
                mod = parser.OFPFlowMod(datapath=datapath, priority=4,
                                    match=match, instructions=inst)
                datapath.send_msg(mod) 

                datapath=self.datapaths[4]
                ofproto = datapath.ofproto               
                parser = datapath.ofproto_parser  
                match = parser.OFPMatch(eth_type=0x0800, ipv4_dst="10.0.0.3", ipv4_src="10.0.0.1")
                actions = [
                    parser.OFPActionPushMpls(ethertype=34887),
                    parser.OFPActionSetField(mpls_label=1001),
                    parser.OFPActionOutput(1)                           
                ]
                inst = [parser.OFPInstructionActions(ofproto.OFPIT_APPLY_ACTIONS,
                                                actions)]
                mod = parser.OFPFlowMod(datapath=datapath, priority=4,
                                    match=match, instructions=inst)
                datapath.send_msg(mod)            

            elif (content=="4"):
                #path that goes through s2 to h2
                print("path 4")
                datapath=self.datapaths[1]
                ofproto = datapath.ofproto               
                parser = datapath.ofproto_parser  
                match = parser.OFPMatch(eth_type=0x0800, ipv4_dst="10.0.0.2")
                actions = [
                    parser.OFPActionPushMpls(ethertype=34887),
                    parser.OFPActionSetField(mpls_label=2000),
                    parser.OFPActionOutput(2)                           
                ]
                inst = [parser.OFPInstructionActions(ofproto.OFPIT_APPLY_ACTIONS,
                                                actions)]
                mod = parser.OFPFlowMod(datapath=datapath, priority=4,
                                    match=match, instructions=inst)
                datapath.send_msg(mod)

                datapath=self.datapaths[2]
                ofproto = datapath.ofproto               
                parser = datapath.ofproto_parser  
                match = parser.OFPMatch(eth_type=0x8847, mpls_label=2000)
                actions = [
                    parser.OFPActionPopMpls(),
                    parser.OFPActionOutput(3)
                ]
                inst = [parser.OFPInstructionActions(ofproto.OFPIT_APPLY_ACTIONS,
                                                actions)]
                mod = parser.OFPFlowMod(datapath=datapath, priority=4,
                                    match=match, instructions=inst)
                datapath.send_msg(mod)
                #inverse direction
                match = parser.OFPMatch(eth_type=0x8847, mpls_label=2001)
                actions = [
                    parser.OFPActionPopMpls(),
                    parser.OFPActionOutput(1)
                ]
                inst = [parser.OFPInstructionActions(ofproto.OFPIT_APPLY_ACTIONS,
                                                actions)]
                mod = parser.OFPFlowMod(datapath=datapath, priority=4,
                                    match=match, instructions=inst)
                datapath.send_msg(mod) 

                datapath=self.datapaths[5]
                ofproto = datapath.ofproto               
                parser = datapath.ofproto_parser  
                match = parser.OFPMatch(eth_type=0x0800, ipv4_dst="10.0.0.3", ipv4_src="10.0.0.2")
                actions = [
                    parser.OFPActionPushMpls(ethertype=34887),
                    parser.OFPActionSetField(mpls_label=2001),
                    parser.OFPActionOutput(2)                           
                ]
                inst = [parser.OFPInstructionActions(ofproto.OFPIT_APPLY_ACTIONS,
                                                actions)]
                mod = parser.OFPFlowMod(datapath=datapath, priority=4,
                                    match=match, instructions=inst)
                datapath.send_msg(mod)       

            elif (content=="2"):
                #path that goes through s3 to h1
                print("path 2")
                datapath=self.datapaths[1]
                ofproto = datapath.ofproto               
                parser = datapath.ofproto_parser  
                match = parser.OFPMatch(eth_type=0x0800, ipv4_dst="10.0.0.1")
                actions = [
                    parser.OFPActionPushMpls(ethertype=34887),
                    parser.OFPActionSetField(mpls_label=1000),
                    parser.OFPActionOutput(3)                           
                ]
                inst = [parser.OFPInstructionActions(ofproto.OFPIT_APPLY_ACTIONS,
                                                actions)]
                mod = parser.OFPFlowMod(datapath=datapath, priority=4,
                                    match=match, instructions=inst)
                datapath.send_msg(mod)

                datapath=self.datapaths[3]
                ofproto = datapath.ofproto               
                parser = datapath.ofproto_parser  
                match = parser.OFPMatch(eth_type=0x8847, mpls_label=1000)
                actions = [
                    parser.OFPActionPopMpls(),
                    parser.OFPActionOutput(3)
                ]
                inst = [parser.OFPInstructionActions(ofproto.OFPIT_APPLY_ACTIONS,
                                                actions)]
                mod = parser.OFPFlowMod(datapath=datapath, priority=4,
                                    match=match, instructions=inst)
                datapath.send_msg(mod)
                #inverse direction
                match = parser.OFPMatch(eth_type=0x8847, mpls_label=1001)
                actions = [
                    parser.OFPActionPopMpls(),
                    parser.OFPActionOutput(1)
                ]
                inst = [parser.OFPInstructionActions(ofproto.OFPIT_APPLY_ACTIONS,
                                                actions)]
                mod = parser.OFPFlowMod(datapath=datapath, priority=4,
                                    match=match, instructions=inst)
                datapath.send_msg(mod) 

                datapath=self.datapaths[4]
                ofproto = datapath.ofproto               
                parser = datapath.ofproto_parser  
                match = parser.OFPMatch(eth_type=0x0800, ipv4_dst="10.0.0.3", ipv4_src="10.0.0.1")
                actions = [
                    parser.OFPActionPushMpls(ethertype=34887),
                    parser.OFPActionSetField(mpls_label=1001),
                    parser.OFPActionOutput(2)                            
                ]
                inst = [parser.OFPInstructionActions(ofproto.OFPIT_APPLY_ACTIONS,
                                                actions)]
                mod = parser.OFPFlowMod(datapath=datapath, priority=4,
                                    match=match, instructions=inst)
                datapath.send_msg(mod)            

            elif (content=="3"):
                #path that goes through s3 to h2
                print ("path 3")
                datapath=self.datapaths[1]
                ofproto = datapath.ofproto               
                parser = datapath.ofproto_parser  
                match = parser.OFPMatch(eth_type=0x0800, ipv4_dst="10.0.0.2")
                actions = [
                    parser.OFPActionPushMpls(ethertype=34887),
                    parser.OFPActionSetField(mpls_label=2000),
                    parser.OFPActionOutput(3)                           
                ]
                inst = [parser.OFPInstructionActions(ofproto.OFPIT_APPLY_ACTIONS,
                                                actions)]
                mod = parser.OFPFlowMod(datapath=datapath, priority=4,
                                    match=match, instructions=inst)
                datapath.send_msg(mod)

                datapath=self.datapaths[3]
                ofproto = datapath.ofproto               
                parser = datapath.ofproto_parser  
                match = parser.OFPMatch(eth_type=0x8847, mpls_label=2000)
                actions = [
                    parser.OFPActionPopMpls(),
                    parser.OFPActionOutput(2)
                ]
                inst = [parser.OFPInstructionActions(ofproto.OFPIT_APPLY_ACTIONS,
                                                actions)]
                mod = parser.OFPFlowMod(datapath=datapath, priority=4,
                                    match=match, instructions=inst)
                datapath.send_msg(mod)
                #inverse direction
                match = parser.OFPMatch(eth_type=0x8847, mpls_label=2001)
                actions = [
                    parser.OFPActionPopMpls(),
                    parser.OFPActionOutput(1)
                ]
                inst = [parser.OFPInstructionActions(ofproto.OFPIT_APPLY_ACTIONS,
                                                actions)]
                mod = parser.OFPFlowMod(datapath=datapath, priority=4,
                                    match=match, instructions=inst)
                datapath.send_msg(mod) 

                datapath=self.datapaths[5]
                ofproto = datapath.ofproto               
                parser = datapath.ofproto_parser  
                match = parser.OFPMatch(eth_type=0x0800, ipv4_dst="10.0.0.3", ipv4_src="10.0.0.2")
                actions = [
                    parser.OFPActionPushMpls(ethertype=34887),
                    parser.OFPActionSetField(mpls_label=2001),
                    parser.OFPActionOutput(1)                           
                ]
                inst = [parser.OFPInstructionActions(ofproto.OFPIT_APPLY_ACTIONS,
                                                actions)]
                mod = parser.OFPFlowMod(datapath=datapath, priority=4,
                                    match=match, instructions=inst)
                datapath.send_msg(mod)     
            current_time= datetime.now().strftime("%Y-%m-%d %H-%M-%S")
            write_api = client.write_api(write_options=SYNCHRONOUS)
            if content=="1" or content=="2":
                p=influxdb_client.Point("my_measurement").field("Chosen Host", 1)
            else: 
                p=influxdb_client.Point("my_measurement").field("Chosen Host", 2)  
            write_api.write(bucket=bucket, org=org, record=p)      
            p1=influxdb_client.Point("my_path").field("Chosen Path", int(content))   
            write_api.write(bucket=bucket, org=org, record=p1)  

        


    

    # execute at switch registration
    @set_ev_cls(ofp_event.EventOFPSwitchFeatures, CONFIG_DISPATCHER)


    def switch_features_handler(self, ev):
        datapath = ev.msg.datapath
        ofproto = datapath.ofproto
        parser = datapath.ofproto_parser

        self.datapaths[datapath.id] = datapath

        # match all packets
        match = parser.OFPMatch()
        # send to controller
        actions = [parser.OFPActionOutput(ofproto.OFPP_CONTROLLER,
                                          ofproto.OFPCML_NO_BUFFER)]
        inst = [parser.OFPInstructionActions(ofproto.OFPIT_APPLY_ACTIONS,
                                             actions)]
        mod = parser.OFPFlowMod(datapath, priority=1,
                                match=match, instructions=inst)
        datapath.send_msg(mod)


        if datapath.id == 1:

            match = parser.OFPMatch(eth_type=0x0800, ipv4_dst="10.0.0.1")
            actions = [
                parser.OFPActionPushMpls(ethertype=34887),
                parser.OFPActionSetField(mpls_label=1000),
                parser.OFPActionOutput(2)                           
            ]
            inst = [parser.OFPInstructionActions(ofproto.OFPIT_APPLY_ACTIONS,
                                             actions)]
            mod = parser.OFPFlowMod(datapath=datapath, priority=4,
                                match=match, instructions=inst)
            datapath.send_msg(mod)

            match = parser.OFPMatch(eth_type=0x0800, ipv4_dst="10.0.0.2")
            actions = [
                parser.OFPActionPushMpls(ethertype=34887),
                parser.OFPActionSetField(mpls_label=2000),
                parser.OFPActionOutput(2)                           
            ]
            inst = [parser.OFPInstructionActions(ofproto.OFPIT_APPLY_ACTIONS,
                                             actions)]
            mod = parser.OFPFlowMod(datapath=datapath, priority=4,
                                match=match, instructions=inst)
            datapath.send_msg(mod)
            
            match = parser.OFPMatch(eth_type=0x0800, ipv4_dst="10.0.0.4")
            actions = [
                parser.OFPActionPushMpls(ethertype=34887),
                parser.OFPActionSetField(mpls_label=4000),
                parser.OFPActionOutput(2)                           
            ]
            inst = [parser.OFPInstructionActions(ofproto.OFPIT_APPLY_ACTIONS,
                                             actions)]
            mod = parser.OFPFlowMod(datapath=datapath, priority=4,
                                match=match, instructions=inst)
            datapath.send_msg(mod)

            match = parser.OFPMatch(eth_type=0x0800, ipv4_dst="10.0.0.7")
            actions = [
                parser.OFPActionPushMpls(ethertype=34887),
                parser.OFPActionSetField(mpls_label=7000),
                parser.OFPActionOutput(2)                           
            ]
            inst = [parser.OFPInstructionActions(ofproto.OFPIT_APPLY_ACTIONS,

                                             actions)]
            mod = parser.OFPFlowMod(datapath=datapath, priority=4,
                                match=match, instructions=inst)
            datapath.send_msg(mod)
           
            match = parser.OFPMatch(eth_type=0x0800, ipv4_dst="10.0.0.5")
            actions = [
                parser.OFPActionPushMpls(ethertype=34887),
                parser.OFPActionSetField(mpls_label=5000),
                parser.OFPActionOutput(3)                           
            ]
            inst = [parser.OFPInstructionActions(ofproto.OFPIT_APPLY_ACTIONS,
                                             actions)]
            mod = parser.OFPFlowMod(datapath=datapath, priority=4,
                                match=match, instructions=inst)
            datapath.send_msg(mod)

            match = parser.OFPMatch(eth_type=0x0800, ipv4_dst="10.0.0.6")
            actions = [
                parser.OFPActionPushMpls(ethertype=34887),
                parser.OFPActionSetField(mpls_label=6000),
                parser.OFPActionOutput(3)                           
            ]
            inst = [parser.OFPInstructionActions(ofproto.OFPIT_APPLY_ACTIONS,
                                             actions)]
            mod = parser.OFPFlowMod(datapath=datapath, priority=4,
                                match=match, instructions=inst)
            datapath.send_msg(mod)

            match = parser.OFPMatch(eth_type=0x0806, arp_spa="10.10.5.101")
            actions = [
                parser.OFPActionOutput(1)                           
            ]
            inst = [parser.OFPInstructionActions(ofproto.OFPIT_APPLY_ACTIONS,
                                             actions)]
            mod = parser.OFPFlowMod(datapath=datapath, priority=16,
                                match=match, instructions=inst)
            datapath.send_msg(mod)   

            match = parser.OFPMatch(eth_type=0x0806, arp_tpa="10.10.5.101")
            actions = [
                parser.OFPActionOutput(4)                           
            ]
            inst = [parser.OFPInstructionActions(ofproto.OFPIT_APPLY_ACTIONS,
                                             actions)]
            mod = parser.OFPFlowMod(datapath=datapath, priority=14,
                                match=match, instructions=inst)
            datapath.send_msg(mod) 

            match = parser.OFPMatch(eth_type=0x0800, ipv4_dst="10.10.5.101")
            actions = [
                parser.OFPActionOutput(4)                           
            ]
            inst = [parser.OFPInstructionActions(ofproto.OFPIT_APPLY_ACTIONS,
                                             actions)]
            mod = parser.OFPFlowMod(datapath=datapath, priority=10,
                                match=match, instructions=inst)
            datapath.send_msg(mod) 

            match = parser.OFPMatch(eth_type=0x0800, ipv4_dst="10.0.0.3")
            actions = [
                parser.OFPActionOutput(1)                           
            ]
            inst = [parser.OFPInstructionActions(ofproto.OFPIT_APPLY_ACTIONS,
                                             actions)]
            mod = parser.OFPFlowMod(datapath=datapath, priority=10,
                                match=match, instructions=inst)
            datapath.send_msg(mod) 



        if datapath.id == 2:

            match = parser.OFPMatch(eth_type=0x8847, mpls_label=1000)
            actions = [
                parser.OFPActionPopMpls(),
                parser.OFPActionOutput(2)
            ]
            inst = [parser.OFPInstructionActions(ofproto.OFPIT_APPLY_ACTIONS,
                                             actions)]
            mod = parser.OFPFlowMod(datapath=datapath, priority=4,
                                match=match, instructions=inst)
            datapath.send_msg(mod)

            match = parser.OFPMatch(eth_type=0x8847, mpls_label=2000)
            actions = [
                parser.OFPActionPopMpls(),
                parser.OFPActionOutput(3)
            ]
            inst = [parser.OFPInstructionActions(ofproto.OFPIT_APPLY_ACTIONS,
                                             actions)]
            mod = parser.OFPFlowMod(datapath=datapath, priority=4,
                                match=match, instructions=inst)
            datapath.send_msg(mod)
            
            match = parser.OFPMatch(eth_type=0x8847, mpls_label=4000)
            actions = [
                parser.OFPActionPopMpls(),
                parser.OFPActionOutput(2)
            ]
            inst = [parser.OFPInstructionActions(ofproto.OFPIT_APPLY_ACTIONS,
                                             actions)]
            mod = parser.OFPFlowMod(datapath=datapath, priority=4,
                                match=match, instructions=inst)
            datapath.send_msg(mod)

            match = parser.OFPMatch(eth_type=0x8847, mpls_label=7000)
            actions = [
                parser.OFPActionPopMpls(),
                parser.OFPActionOutput(3)
            ]
            inst = [parser.OFPInstructionActions(ofproto.OFPIT_APPLY_ACTIONS,
                                             actions)]
            mod = parser.OFPFlowMod(datapath=datapath, priority=4,
                                match=match, instructions=inst)
            datapath.send_msg(mod)
            
            match = parser.OFPMatch(eth_type=0x8847, mpls_label=1001)
            actions = [
                parser.OFPActionPopMpls(),
                parser.OFPActionOutput(1)
            ]
            inst = [parser.OFPInstructionActions(ofproto.OFPIT_APPLY_ACTIONS,
                                             actions)]
            mod = parser.OFPFlowMod(datapath=datapath, priority=4,
                                match=match, instructions=inst)
            datapath.send_msg(mod)                        

            match = parser.OFPMatch(eth_type=0x8847, mpls_label=2001)
            actions = [
                parser.OFPActionPopMpls(),
                parser.OFPActionOutput(1)
            ]
            inst = [parser.OFPInstructionActions(ofproto.OFPIT_APPLY_ACTIONS,
                                             actions)]
            mod = parser.OFPFlowMod(datapath=datapath, priority=4,
                                match=match, instructions=inst)
            datapath.send_msg(mod)                        

            match = parser.OFPMatch(eth_type=0x8847, mpls_label=4001)
            actions = [
                parser.OFPActionPopMpls(),
                parser.OFPActionOutput(1)
            ]
            inst = [parser.OFPInstructionActions(ofproto.OFPIT_APPLY_ACTIONS,
                                             actions)]
            mod = parser.OFPFlowMod(datapath=datapath, priority=4,
                                match=match, instructions=inst)
            datapath.send_msg(mod)                   
            
            match = parser.OFPMatch(eth_type=0x8847, mpls_label=7001)
            actions = [
                parser.OFPActionPopMpls(),
                parser.OFPActionOutput(1)
            ]
            inst = [parser.OFPInstructionActions(ofproto.OFPIT_APPLY_ACTIONS,
                                             actions)]
            mod = parser.OFPFlowMod(datapath=datapath, priority=4,
                                match=match, instructions=inst)
            datapath.send_msg(mod)                        
                 



        if datapath.id == 3:            
            match = parser.OFPMatch(eth_type=0x8847, mpls_label=5000)
            actions = [
                parser.OFPActionPopMpls(),
                parser.OFPActionOutput(3)
            ]
            inst = [parser.OFPInstructionActions(ofproto.OFPIT_APPLY_ACTIONS,
                                             actions)]
            mod = parser.OFPFlowMod(datapath=datapath, priority=4,
                                match=match, instructions=inst)
            datapath.send_msg(mod)

            match = parser.OFPMatch(eth_type=0x8847, mpls_label=6000)
            actions = [
                parser.OFPActionPopMpls(),
                parser.OFPActionOutput(2)
            ]
            inst = [parser.OFPInstructionActions(ofproto.OFPIT_APPLY_ACTIONS,
                                             actions)]
            mod = parser.OFPFlowMod(datapath=datapath, priority=4,
                                match=match, instructions=inst)
            datapath.send_msg(mod)       

            match = parser.OFPMatch(eth_type=0x8847, mpls_label=5001)
            actions = [
                parser.OFPActionPopMpls(),
                parser.OFPActionOutput(1)
            ]
            inst = [parser.OFPInstructionActions(ofproto.OFPIT_APPLY_ACTIONS,
                                             actions)]
            mod = parser.OFPFlowMod(datapath=datapath, priority=4,
                                match=match, instructions=inst)
            datapath.send_msg(mod)                        

            match = parser.OFPMatch(eth_type=0x8847, mpls_label=6001)
            actions = [
                parser.OFPActionPopMpls(),
                parser.OFPActionOutput(1)
            ]
            inst = [parser.OFPInstructionActions(ofproto.OFPIT_APPLY_ACTIONS,
                                             actions)]
            mod = parser.OFPFlowMod(datapath=datapath, priority=4,
                                match=match, instructions=inst)
            datapath.send_msg(mod)                        
            
            
        if datapath.id == 4:
            match = parser.OFPMatch(eth_type=0x0800, ipv4_dst="10.0.0.3", ipv4_src="10.0.0.1")
            actions = [
                parser.OFPActionPushMpls(ethertype=34887),
                parser.OFPActionSetField(mpls_label=1001),
                parser.OFPActionOutput(1)                           
            ]
            inst = [parser.OFPInstructionActions(ofproto.OFPIT_APPLY_ACTIONS,
                                             actions)]
            mod = parser.OFPFlowMod(datapath=datapath, priority=4,
                                match=match, instructions=inst)
            datapath.send_msg(mod)

            match = parser.OFPMatch(eth_type=0x0800, ipv4_dst="10.0.0.3", ipv4_src="10.0.0.4")
            actions = [
                parser.OFPActionPushMpls(ethertype=34887),
                parser.OFPActionSetField(mpls_label=4001),
                parser.OFPActionOutput(1)                           
            ]
            inst = [parser.OFPInstructionActions(ofproto.OFPIT_APPLY_ACTIONS,
                                             actions)]
            mod = parser.OFPFlowMod(datapath=datapath, priority=4,
                                match=match, instructions=inst)
            datapath.send_msg(mod)
            
            match = parser.OFPMatch(eth_type=0x0800, ipv4_dst="10.0.0.3", ipv4_src="10.0.0.5")
            actions = [
                parser.OFPActionPushMpls(ethertype=34887),
                parser.OFPActionSetField(mpls_label=5001),
                parser.OFPActionOutput(2)                           
            ]
            inst = [parser.OFPInstructionActions(ofproto.OFPIT_APPLY_ACTIONS,
                                             actions)]
            mod = parser.OFPFlowMod(datapath=datapath, priority=4,
                                match=match, instructions=inst)
            datapath.send_msg(mod)   

            match = parser.OFPMatch(eth_type=0x0800, ipv4_dst="10.0.0.1")
            actions = [
                parser.OFPActionOutput(3)                           
            ]
            inst = [parser.OFPInstructionActions(ofproto.OFPIT_APPLY_ACTIONS,
                                             actions)]
            mod = parser.OFPFlowMod(datapath=datapath, priority=6,
                                match=match, instructions=inst)
            datapath.send_msg(mod)     

            match = parser.OFPMatch(eth_type=0x0800, ipv4_dst="10.0.0.4")
            actions = [
                parser.OFPActionOutput(4)                           
            ]
            inst = [parser.OFPInstructionActions(ofproto.OFPIT_APPLY_ACTIONS,
                                             actions)]
            mod = parser.OFPFlowMod(datapath=datapath, priority=6,
                                match=match, instructions=inst)
            datapath.send_msg(mod)   

            match = parser.OFPMatch(eth_type=0x0800, ipv4_dst="10.0.0.5")
            actions = [
                parser.OFPActionOutput(5)                           
            ]
            inst = [parser.OFPInstructionActions(ofproto.OFPIT_APPLY_ACTIONS,
                                             actions)]
            mod = parser.OFPFlowMod(datapath=datapath, priority=6,
                                match=match, instructions=inst)
            datapath.send_msg(mod)       


        if datapath.id == 5:

            match = parser.OFPMatch(eth_type=0x0800, ipv4_dst="10.0.0.3", ipv4_src="10.0.0.2")
            actions = [
                parser.OFPActionPushMpls(ethertype=34887),
                parser.OFPActionSetField(mpls_label=2001),
                parser.OFPActionOutput(2)                           
            ]
            inst = [parser.OFPInstructionActions(ofproto.OFPIT_APPLY_ACTIONS,
                                             actions)]
            mod = parser.OFPFlowMod(datapath=datapath, priority=4,
                                match=match, instructions=inst)
            datapath.send_msg(mod)

            match = parser.OFPMatch(eth_type=0x0800, ipv4_dst="10.0.0.3", ipv4_src="10.0.0.6")
            actions = [
                parser.OFPActionPushMpls(ethertype=34887),
                parser.OFPActionSetField(mpls_label=6001),
                parser.OFPActionOutput(1)                           
            ]
            inst = [parser.OFPInstructionActions(ofproto.OFPIT_APPLY_ACTIONS,
                                             actions)]
            mod = parser.OFPFlowMod(datapath=datapath, priority=4,
                                match=match, instructions=inst)
            datapath.send_msg(mod)
            
            match = parser.OFPMatch(eth_type=0x0800, ipv4_dst="10.0.0.3", ipv4_src="10.0.0.7")
            actions = [
                parser.OFPActionPushMpls(ethertype=34887),
                parser.OFPActionSetField(mpls_label=7001),
                parser.OFPActionOutput(2)                           
            ]
            inst = [parser.OFPInstructionActions(ofproto.OFPIT_APPLY_ACTIONS,
                                             actions)]
            mod = parser.OFPFlowMod(datapath=datapath, priority=4,
                                match=match, instructions=inst)
            datapath.send_msg(mod)

            match = parser.OFPMatch(eth_type=0x0800, ipv4_dst="10.0.0.2")
            actions = [
                parser.OFPActionOutput(3)                           
            ]
            inst = [parser.OFPInstructionActions(ofproto.OFPIT_APPLY_ACTIONS,
                                             actions)]
            mod = parser.OFPFlowMod(datapath=datapath, priority=6,
                                match=match, instructions=inst)
            datapath.send_msg(mod)   

            match = parser.OFPMatch(eth_type=0x0800, ipv4_dst="10.0.0.6")
            actions = [
                parser.OFPActionOutput(4)                           
            ]
            inst = [parser.OFPInstructionActions(ofproto.OFPIT_APPLY_ACTIONS,
                                             actions)]
            mod = parser.OFPFlowMod(datapath=datapath, priority=6,
                                match=match, instructions=inst)
            datapath.send_msg(mod)   

            match = parser.OFPMatch(eth_type=0x0800, ipv4_dst="10.0.0.7")
            actions = [
                parser.OFPActionOutput(5)                           
            ]
            inst = [parser.OFPInstructionActions(ofproto.OFPIT_APPLY_ACTIONS,
                                             actions)]
            mod = parser.OFPFlowMod(datapath=datapath, priority=6,
                                match=match, instructions=inst)
            datapath.send_msg(mod)   
                 
          

