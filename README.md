## install Mininet
```
git clone https://github.com/mininet/mininet
mininet/util/install.sh -a
```
## install Telegraf

```
# influxdata-archive_compat.key GPG Fingerprint: 9D539D90D3328DC7D6C8D3B9D8FF8E1F7DF8B07E
curl -s https://repos.influxdata.com/influxdata-archive_compat.key > influxdata-archive_compat.key
echo '393e8779c89ac8d958f81f942f9ad7fb82a25e133faddaf92e15b16e6ac9ce4c influxdata-archive_compat.key' | sha256sum -c && cat influxdata-archive_compat.key | gpg --dearmor | sudo tee /etc/apt/trusted.gpg.d/influxdata-archive_compat.gpg > /dev/null
echo 'deb [signed-by=/etc/apt/trusted.gpg.d/influxdata-archive_compat.gpg] https://repos.influxdata.com/debian stable main' | sudo tee /etc/apt/sources.list.d/influxdata.list
sudo apt-get update && sudo apt-get install telegraf
```
## install InfluxDB
```
wget https://dl.influxdata.com/influxdb/releases/influxdb2-2.7.0-amd64.deb
sudo dpkg -i influxdb2-2.7.0-amd64.deb
sudo service influxdb start
sudo service influxdb status
```

## setting InfluxDb
set name, organization, bucket, save token
http://localhost:8086

## install Grafana
https://grafana.com/grafana/download
```
sudo apt-get install -y adduser libfontconfig1 musl
wget https://dl.grafana.com/enterprise/release/grafana-enterprise_10.1.4_amd64.deb
sudo dpkg -i grafana-enterprise_10.1.4_amd64.deb
```
## enable Grafana
```
sudo /bin/systemctl deamon-reload
sudo /bin/systemctl enable grafana-server
sudo /bin/systemctl start Grafana-server
```
## install Ryu-controller
```
sudo apt install -y python3-pip  
git clone https://github.com/osrg/ryu.git 
cd ryu
sudo python3 ./setup.py install 
sudo pip3 install --upgrade ryu
```
## to write the telegraf configuration of the host A
in terminal 1 start mininet
```
sudo mn --custom /mininet/custom/topo_6_hosts.py --topo=mytopo
```
in terminal 2
```
mininet/util/m hA
telegraf --sample-config --input-filter ping --output-filter influxdb_v2 > telegraf-hA.conf
```
then modify the file telegraf-hA.conf
in the influx plugin update the urls, token, bucket and organization
in the ping plugin add in urls the hosts 


## start process
terminal 1 start mininet
```
sudo mn --custom -/mininet/custom/topo_6_hosts.py --topo=mytopo --controller=remote --arp --mac --nat
```
terminal 2 start ryu
```
ryu-manager controller.py
```
terminal 3 start telegraf
```
mininet/util/m hA
telegraf -config telegraf-hA.conf
```


## to add the delay
```
bash delay1.sh
```
## to process data
```
python3 data_processing.py
```
