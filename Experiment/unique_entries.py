"""Find Unique Checksum entries in each S1/S2 log"""

import S1_get_stats
import S2_get_stats

print len(S1_get_stats.chksum1)
print len(S2_get_stats.chksum2)

seen1=[]
seen2=[]
uniq_S1 = [x for x in S1_get_stats.chksum1 if x not in seen1 and not seen1.append(x)]   
uniq_S2 = [x for x in S2_get_stats.chksum2 if x not in seen2 and not seen2.append(x)]   

print "Number of unique Checksum entries in S1",len(uniq_S1)
print "Number of unique Checksum entries in S2",len(uniq_S2)
