#! usr/bin/bash

mininet/util/m s3 tc qdisc add dev s3-eth1 root netem delay 50ms 5ms 99% distribution pareto
mininet/util/m s4 tc qdisc add dev s4-eth5 root netem delay 5ms 
mininet/util/m s5 tc qdisc add dev s5-eth5 root netem delay 5ms

while true; do

    mininet/util/m s2 tc qdisc add dev s2-eth1 root netem delay 25ms 2ms 25% distribution pareto
    sleep $(( $RANDOM % 40 + 10 ))s
    mininet/util/m s2 tc qdisc del dev s2-eth1 root 
    mininet/util/m s2 tc qdisc add dev s2-eth1 root netem delay 50ms 5ms 25% distribution pareto
    sleep $(( $RANDOM % 40 + 10 ))s
    mininet/util/m s2 tc qdisc del dev s2-eth1 root 
    mininet/util/m s2 tc qdisc add dev s2-eth1 root netem delay 75ms 7ms 25% distribution pareto
    sleep $(( $RANDOM % 40 + 10 ))s
    mininet/util/m s2 tc qdisc del dev s2-eth1 root 
    mininet/util/m s2 tc qdisc add dev s2-eth1 root netem delay 100ms 10ms 25% distribution pareto
    sleep $(( $RANDOM % 160 + 40 ))s
    mininet/util/m s2 tc qdisc del dev s2-eth1 root 
    mininet/util/m s2 tc qdisc add dev s2-eth1 root netem delay 75ms 7ms 25% distribution pareto
    sleep $(( $RANDOM % 40 + 10 ))s
    mininet/util/m s2 tc qdisc del dev s2-eth1 root 
    mininet/util/m s2 tc qdisc add dev s2-eth1 root netem delay 50ms 5ms 25% distribution pareto
    sleep $(( $RANDOM % 40 + 10 ))s
    mininet/util/m s2 tc qdisc del dev s2-eth1 root 
    mininet/util/m s2 tc qdisc add dev s2-eth1 root netem delay 25ms 2ms 25% distribution pareto
    sleep $(( $RANDOM % 40 + 10 ))s
    mininet/util/m s2 tc qdisc del dev s2-eth1 root 
    sleep $(( $RANDOM % 160 + 40 ))s



done

mininet/util/m s3 tc qdisc del dev s3-eth1 root
mininet/util/m s4 tc qdisc del dev s4-eth5 root
mininet/util/m s5 tc qdisc del dev s5-eth5 root







