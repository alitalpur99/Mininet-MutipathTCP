#!/bin/bash


#rm cwnd_new_1
#rm cwnd_new_2

SF1=f3b35d80
#e96c4d00



########forward delay data##############

#grep -rZ -E "tcp_cong" /home/lab/new-analysis/new-d-delay---1 > mptcp_fw_delay_1
grep -rZ -E "fw_delay" /home/lab/tcp-ali/new-result/syslog > mptcp_fw_delay_cong

#rm mptcp_fw_delay_1

# for subflow 1

grep -rZ -E "$SF1" mptcp_fw_delay_cong > fw_delay_sf1
awk '{print $7, $12}' fw_delay_sf1 > fw_delay_sf1_new
sed 's/]//' fw_delay_sf1_new > fw_delay_new_11_cong
#sed 's/.//' fw_delay_new_111 > fw_delay_new_11
head -n -5 fw_delay_new_11_cong > fw_delay_new_1
#rm fw_delay_sf1
rm fw_delay_sf1_new
#rm fw_delay_new_111
rm fw_delay_new_1


########backward delay data##############

#grep -rZ -E "tcp_cong" /home/lab/new-analysis/new-d-delay---1 > mptcp_bw_delay_1
grep -rZ -E "bw_delay" /home/lab/tcp-ali/new-result/syslog > mptcp_bw_delay_cong

#rm mptcp_fw_delay_1

# for subflow 1

grep -rZ -E "$SF1" mptcp_bw_delay_cong > bw_delay_sf1
awk '{print $7, $12}' bw_delay_sf1 > bw_delay_sf1_new
sed 's/]//' bw_delay_sf1_new > bw_delay_new_11_cong  
#sed 's/.//' fw_delay_new_111 > fw_delay_new_11
head -n -5 bw_delay_new_11_cong > bw_delay_new_1
rm bw_delay_sf1
rm bw_delay_sf1_new
#rm fw_delay_new_111
rm bw_delay_new_1   


########srtt_f delay data##############

#grep -rZ -E "tcp_cong" /home/lab/new-analysis/new-d-delay---1 > mptcp_fw_delay_1
grep -rZ -E " srtt_f " /home/lab/tcp-ali/new-result/syslog > mptcp_srtt_f_cong

#rm mptcp_fw_delay_1

# for subflow 1

grep -rZ -E "$SF1" mptcp_srtt_f_cong > srtt_f_sf1
awk '{print $7, $12}' srtt_f_sf1 > srtt_f_sf1_new
sed 's/]//' srtt_f_sf1_new > srtt_f_new_11_cong
#sed 's/.//' fw_delay_new_111 > fw_delay_new_11
head -n -5 srtt_f_new_11_cong > srtt_f_new_1
rm srtt_f_sf1
rm srtt_f_sf1_new
#rm fw_delay_new_111
rm srtt_f_new_1

#for subflow 2


############rtt data###############

grep -rZ -E "tcp_rtt_estm" /home/lab/tcp-ali/new-result/syslog > mptcp_rtt

#for subflow 1

grep -rZ -E "$SF1" mptcp_rtt > rtt_sf1
awk '{print $6, $10}' rtt_sf1 > rtt_sf1_new
sed 's/]//' rtt_sf1_new > rtt_new_111_1
sed 's/.//' rtt_new_111_1 > rtt_new_11
head -n -5 rtt_new_11 > rtt_new_1
#rm rtt_sf1
rm rtt_sf1_new
rm rtt_new_1



###############cwnd data###############

grep -rZ -E "tcp_out" /home/lab/tcp-ali/new-result/syslog > mptcp_cwnd_x1
grep -rZ -E "cwnd" /home/lab/tcp-ali/new-result/syslog > mptcp_cwnd_out
#grep -rZ -E "tcp_cong" /home/lab/tcp-ali/new-result/syslog > mptcp_cwnd_x2
#grep -rZ -E "cwnd" /home/lab/tcp-ali/new-result/syslog > mptcp_cwnd_cong

rm mptcp_cwnd_x1
#rm mptcp_cwnd_x2

########out########
# for subflow 1

grep -rZ -E "$SF1" mptcp_cwnd_out > cwnd_sf1
#awk '{print $7, $12}' cwnd_sf1 > cwnd_sf1_new
awk '{print $6, $11}' cwnd_sf1 > cwnd_sf1_new
sed 's/]//' cwnd_sf1_new > cwnd_new_11_out
#sed 's/[//' cwnd_sf1_new > cwnd_new_11_out
sed 's/.//' cwnd_new_11_out > cwnd_new_11
head -n -5 cwnd_new_11_out > cwnd_new_1
#rm cwnd_sf1_new
#rm cwnd_sf1
#rm cwnd_new_111
rm cwnd_new_1

##############in_flight data####################

grep -rZ -E "in_flight" /home/lab/tcp-ali/new-result/syslog > mptcp_in_flight
#grep -rZ -E "in_flight" /home/lab/new-analysis/mptcp_in_flight_1 > mptcp_in_flight
rm mptcp_in_flight_1 
# for subflow 1

grep -rZ -E "$SF1" mptcp_in_flight > in_flight_sf1
awk '{print $6, $11}' in_flight_sf1 > in_flight_sf1_new
sed 's/]//' in_flight_sf1_new > in_flight_new_11_1
sed 's/.//' in_flight_new_11_1 > in_flight_new_11
head -n -5 in_flight_new_11 > in_flight_new_1
#rm in_flight_sf1_new
#rm in_flight_sf1
#rm in_flight_new_111
#rm in_flight_new_1


#############ssthresh data################

#grep -rZ -E "tcp_cong" /home/lab/tcp/tcp-1-100-2p-20 > mptcp_ssthresh_1
grep -rZ -E "ssthresh" /home/lab/tcp-ali/new-result/syslog > mptcp_ssthresh
rm mptcp_ssthresh_1
# for subflow 1

grep -rZ -E "$SF1" mptcp_ssthresh > ssthresh_sf1
awk '{print $6, $11}' ssthresh_sf1 > ssthresh_sf1_new
sed 's/]//' ssthresh_sf1_new > ssthresh_new_111
sed 's/.//' ssthresh_new_111 > ssthresh_new_11
head -n -5 ssthresh_new_11 > ssthresh_new_1
rm ssthresh_sf1_new
rm ssthresh_sf1
#rm ssthresh_new_111 
rm ssthresh_new_1
 
