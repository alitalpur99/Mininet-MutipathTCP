#!/bin/bash
#set terminal tex
set terminal pngcairo size 1600,900
#set terminal eps
#set terminal svg


#set terminal png font ",8"
set output "tcp-N-tcp_2.png"
#set output "2_cap_100-100_del_10-20-10-20.eps" 
#set output "2_cap_100-100_del_10-20-10-20.svg" 
#set output "2_cap_100-100_del_10-20-10-20.tex"

set key reverse right top font ",14" 
set key spacing 1.0
#set key width-4.5
#set key height 0.5

set multiplot layout 3,2 #title "2-node_rtt_exp-1_100_10_del_10-10_20-20_test_zoom_1" font "Arial-Bold,20"
set xlabel "Time (sec) " font ",16" 
set xrange [0:30]
set grid

#set termoption dash

offset_D=10424.327090

mul=1

########## Congestion Window & ssthresh ################

#set ylabel "Number of Packets " font ",16"
#set yrange [0:400] 
#set yrange [0:400]
#set title  "Congestion Window (cwnd)" font "Arial-Bold,6" offset 5,-10.7

#plot "cwnd_new_11_cong" using (($1-offset_D)*mul):($2) title "cong-cwnd -Subflow 1" with lines lt rgb "red", "cwnd_new_22_cong" using (($1-offset_D)*mul):($2) title "cwnd - Subflow 2" with lines lt rgb "blue", "ssthresh_new_11" using (($1-offset_D)*mul):($2) title "ssthresh - Subflow 1"  with points lt rgb "red", "ssthresh_new_22" using (($1-offset_D)*mul):($2) title "ssthresh - Subflow 2" with points lt rgb "blue"
#plot "cwnd_new_11_cong" using (($1-offset_D)*mul):($2) title "out-cwnd -Subflow 1" with points lt rgb "red", "cwnd_new_22_cong" using (($1-offset_D)*mul):($2) title "cwnd - Subflow 2" with points lt rgb "blue"

#plot "cwnd_new_11" using (($1-offset_D)*mul):($2) title "cwnd -Subflow 1" with lines lt rgb "red", "cwnd_new_22" using (($1-offset_D)*mul):($2) title "cwnd - Subflow 2" with lines lt rgb "blue"
plot "cwnd_new_11" using ($1-offset_D):($2) title "cwnd" with lines lt rgb "red"
#, "ssthresh_new_11" using ($1-offset_D):($2) title "ssthresh"  with points lt rgb "blue" 
#plot "cwnd_new_11_out" using (($1-offset_D)*mul):($2) title "cwnd" with lines lt rgb "red", "ssthresh_new_11" using (($1-offset_D)*mul):($2) title "ssthresh"  with points lt rgb "blue" 
#plot "cwnd_new_11_out" using (($1-offset_D)*mul):($2) title "out-cwnd -Subflow 1" with points lt rgb "red", "cwnd_new_22_out" using (($1-offset_D)*mul):($2) title "cwnd - Subflow 2" with points lt rgb "blue"
unset ylabel
unset title
#unset key


set autoscale y

################## In flight packets####################

set yrange [0:2000]
set ylabel "Number of Packets in Flight" font ",14"
#set title "Number of Packets in_Flight " font "Arial-Bold,6" offset 5,-10.7 
plot "in_flight_new_11" using (($1-offset_D)*mul):($2) title "TCP flow"  with lines lt rgb "red"
unset ylabel
unset title
#unset key
  
set autoscale y

###################### Delivery Delay ######################

#set key reverse right top font ",4"
#set key spacing 0.8
#set xrange [0:5]
#set yrange [0:100]
set ylabel "Delivery Delay (ms)" font ",16" 
#plot "fw_delay_new_11_cong" using (($1-offset_D)*mul):(($2-52212)) title "TCP flow"  with lines lt rgb "red"
unset ylabel
unset title

###################### ssthresh #####################

#set key reverse right top font ",4"
#set key spacing 0.8
set yrange[0:1000] 
set ylabel "ssthresh (bytes)" font ",14"
plot "ssthresh_new_11" using (($1-offset_D)*mul):($2) title "Subflow 1" with points lt rgb "red",
# "ssthresh_new_22" using (($1-offset_DD)*mul):($2) title "Subflow 2" with points lt rgb "blue"
unset ylabel
unset title  

set autoscale y

##################### rtt ##########################

#set key reverse right top font ",4"
#set key spacing 0.8
#set xrange [0:5]   
#set yrange [0:100]
set ylabel "Round Trip Time (ms)" font ",14"
plot "rtt_new_11" using (($1-offset_D)*mul):(($2)) title "TCP flow"  with lines lt rgb "red" 
unset ylabel
unset title 


################ srtt_f ############
#set yrange [0:100]  
set ylabel "Round Trip Time EST (ms)" font ",14"
plot "srtt_f_new_11_cong" using (($1-offset_D)*mul):(($2)) title "TCP flow"  with lines lt rgb "red"
unset ylabel
unset title 

############### backward delay ########
Aset yrange [240:260]
set ylabel "ACK Packet Delivery Delay (ms)" font ",14"
plot "bw_delay_new_11_cong" using (($1-offset_D)*mul):(($2-51711)) title "TCP flow"  with lines lt rgb "blue" 
unset ylabel
unset title 



unset multiplot

