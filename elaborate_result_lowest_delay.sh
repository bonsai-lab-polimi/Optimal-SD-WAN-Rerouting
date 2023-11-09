#! usr/bin/bash

total_duration=300


start_time=$(date +%s)


while true; do

    python3 Tesi/data_processing_1m.py
    python3 Tesi/invert_csv.py
    python3 Tesi/data_extrapolation.py
    sleep 60s
done
