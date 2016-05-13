#!/usr/bin/python
#save it in pox/ext directory
# Modidfied  version of original from William Yu wyu@ateneo.edu
# This file is part of POX.
# POX is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# POX is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with POX. If not, see <http://www.gnu.org/licenses/>.
# --------------------------------------------------------------------------------------------------------------
"""
This is a demonstration file created to show how to obtain flow 
and port statistics from OpenFlow 1.0-enabled switches. The flow
statistics handler contains a summary of web-only traffic.
"""
# TO DO: implement per switch, per port, per traffic type flow stats
#------------------------------------------------------------------------------------------

# standard includes
from pox.core import core
from pox.lib.util import dpidToStr
import pox.openflow.libopenflow_01 as of
import time
import matplotlib.pyplot as plt
import csv
# include as part of the betta branch
from pox.openflow.of_json import *

log = core.getLogger()

# handler for timer function that sends the requests to all the
# switches connected to the controller.
def _timer_func ():
  for connection in core.openflow._connections.values():
    connection.send(of.ofp_stats_request(body=of.ofp_flow_stats_request()))
    connection.send(of.ofp_stats_request(body=of.ofp_port_stats_request()))
  log.debug("Sent %i flow/port stats request(s)", len(core.openflow._connections))

# handler to display flow statistics received in JSON format
# structure of event.stats is defined by ofp_flow_stats()
def _handle_flowstats_received (event):
  stats = flow_stats_to_list(event.stats)
  log.debug("FlowStatsReceived from %s: %s", 
    dpidToStr(event.connection.dpid), stats)

  # Get number of bytes/packets in flows for web traffic only
  # I have added: Save stats to a text file (output_file, or separate files )
  web_bytes = 0
  web_flows = 0
  web_packet = 0
  output_file=open("output.txt", "a+") #my own: open a text(canbeanyotherformat) file and append the stats in it (r+, w+, a+)
  flows_file=open("flows.txt", "a+")
  bytes_file=open("bytes.txt", "a+")
  packets_file=open("packets.txt","a+")
  for f in event.stats:
    if f.match.tp_dst == 80 or f.match.tp_src == 80:
      web_bytes += f.byte_count
      web_packet += f.packet_count
      web_flows += 1 
  log.info("Web traffic from %s: %s bytes (%s packets) over %s flows", dpidToStr(event.connection.dpid), web_bytes, web_packet, web_flows)
  localtime = time.asctime( time.localtime(time.time()) ) # my own:to display local time
  # my own:print in Output File
  output_file.write( localtime + " Web traffic:" +"  Bytes:"+ str(web_bytes)+ '\t'+"  Packets:" + str(web_packet) +'\t'+"  Flows:"+str(web_flows) +"\n") # my own:print in Output File
   # write stats on separate files
  flows_file.write( str(web_flows)+ "\n")
  bytes_file.write(  str(web_bytes)+ "\n")
  packets_file.write(str(web_packet)+ "\n")
  
  #my own: to close the file
  output_file.close() 
  flows_file.close()
  bytes_file.close()
  packets_file.close()
"""y = []
with open('flows.csv','r') as csvfile:
  plots = csv.reader(csvfile, delimiter = ',')
  for row in plots:
    y.append(int(row[0]))
plt.plot(y, label='Loaded from file!')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Interesting Graph\nCheck it out')
plt.legend()
plt.show()"""
  
  
# handler to display port statistics received in JSON format
def _handle_portstats_received (event):
  stats = flow_stats_to_list(event.stats)
  log.debug("PortStatsReceived from %s: %s", 
    dpidToStr(event.connection.dpid), stats)
    
# main functiont to launch the module
def launch ():
  from pox.lib.recoco import Timer

  # attach handsers to listners
  core.openflow.addListenerByName("FlowStatsReceived", 
    _handle_flowstats_received) 
  core.openflow.addListenerByName("PortStatsReceived", 
    _handle_portstats_received) 

  # timer set to execute every 5 seconds
  Timer(5, _timer_func, recurring=True)
