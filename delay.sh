#! usr/bin/bash

total_duration=3600


start_time=$(date +%s)

mininet/util/m s3 tc qdisc add dev s3-eth1 root netem delay 50ms 5ms 25% distribution pareto

while true; do
    current_time=$(date +%s)
    elapsed_time=$((current_time - start_time))

    if [ $elapsed_time -ge $total_duration ]; then
        break  
    fi

    mininet/util/m s2 tc qdisc add dev s2-eth1 root netem delay 25ms 2ms 25% distribution pareto
    sleep 20s
    mininet/util/m s2 tc qdisc del dev s2-eth1 root 
    mininet/util/m s2 tc qdisc add dev s2-eth1 root netem delay 50ms 5ms 25% distribution pareto
    sleep 20s
    mininet/util/m s2 tc qdisc del dev s2-eth1 root 
    mininet/util/m s2 tc qdisc add dev s2-eth1 root netem delay 75ms 7ms 25% distribution pareto
    sleep 20s
    mininet/util/m s2 tc qdisc del dev s2-eth1 root 
    mininet/util/m s2 tc qdisc add dev s2-eth1 root netem delay 100ms 10ms 25% distribution pareto
    sleep 90s
    mininet/util/m s2 tc qdisc del dev s2-eth1 root 
    mininet/util/m s2 tc qdisc add dev s2-eth1 root netem delay 75ms 7ms 25% distribution pareto
    sleep 20s
    mininet/util/m s2 tc qdisc del dev s2-eth1 root 
    mininet/util/m s2 tc qdisc add dev s2-eth1 root netem delay 50ms 5ms 25% distribution pareto
    sleep 20s
    mininet/util/m s2 tc qdisc del dev s2-eth1 root 
    mininet/util/m s2 tc qdisc add dev s2-eth1 root netem delay 25ms 2ms 25% distribution pareto
    sleep 20s
    mininet/util/m s2 tc qdisc del dev s2-eth1 root 
    sleep 90s



done

mininet/util/m s3 tc qdisc del dev s3-eth1 root







