#! usr/bin/bash

total_duration=300


start_time=$(date +%s)


while true; do
    current_time=$(date +%s)
    elapsed_time=$((current_time - start_time))

    if [ $elapsed_time -ge $total_duration ]; then
        break  
    fi
    python3 Tesi/data_processing_1m.py
    python3 Tesi/invert_csv.py
    python3 Tesi/data_extrapolation.py
    sleep 60s
done
