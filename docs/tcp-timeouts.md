# TCP Timeouts

## Query 

### Keep-alive Settings

```bash
# Time a connection needs to be idle before the first keep-alive probe is sent [common default is 7200 seconds (2 hours)]
cat /proc/sys/net/ipv4/tcp_keepalive_time
# or
sysctl net.ipv4.tcp_keepalive_time

# Interval between subsequent keep-alive probes [common default is 75 seconds]
cat /proc/sys/net/ipv4/tcp_keepalive_intvl
# or
sysctl net.ipv4.tcp_keepalive_intvl

# Number of keep-alive probes sent before the connection is closed [common default is 9 probes]
cat /proc/sys/net/ipv4/tcp_keepalive_probes
# or
sysctl net.ipv4.tcp_keepalive_probes
```

### SYN Retransmissions

``` 
# Number of times initial SYN packets for an active TCP connection attempt will be retransmitted [common default is 6]
sysctl net.ipv4.tcp_syn_retries
```

### TIME_WAIT Timeout

```bash
# Duration a TCP connection stays in the TIME_WAIT state [common default is 60 seconds]
sysctl net.ipv4.tcp_tw_timeout
```

### Established Connection Timeout

```bash
# Netfilter's established TCP connection tracking timeout [default is 432000 seconds (5 days)]
cat /proc/sys/net/ipv4/netfilter/ip_conntrack_tcp_timeout_established
```

### General Connection Status

```bash
# List connections and timeout or timewait information
netstat -o | grep -i "timeout"
netstat -o | grep -i "timewait"
```

## Define

Changes made to `/proc/sys` are temporary and will revert after a reboot. Permanent changes should be made to `/etc/sysctl.conf`.

### Temporary changes
```bash
sudo sysctl -w net.ipv4.tcp_keepalive_time=1200 # Sets idle time to 20 minutes
sudo sysctl -w net.ipv4.tcp_keepalive_intvl=15 # Sets probe interval to 15 seconds
sudo sysctl -w net.ipv4.tcp_keepalive_probes=5 # Sets probe count to 5
sudo sysctl -w net.ipv4.tcp_tw_timeout=30 # Sets TIME_WAIT to 30 seconds
sudo sysctl -w net.ipv4.tcp_syn_retries=3 # Sets SYN retries to 3
sudo sysctl -w net.ipv4.netfilter.ip_conntrack_tcp_timeout_established=18000 # Sets established timeout to 5 hours
```

### Permanent changes
Add or modfify the following lines in `/etc/sysctl.conf`.

```bash
net.ipv4.tcp_keepalive_time = 1200
net.ipv4.tcp_keepalive_intvl = 15
net.ipv4.tcp_keepalive_probes = 5
net.ipv4.tcp_tw_timeout = 30
net.ipv4.tcp_syn_retries = 3
net.ipv4.netfilter.ip_conntrack_tcp_timeout_established = 18000
```

```bash
# Apply the changes
sudo sysctl -p
```

## Timeouts explained

1. **Retransmission Timeout (RTO):**
	- Definition: The RTO is the duration TCP waits for an acknowledgment (ACK) of a sent data segment before retransmitting that segment. If no acknowledgment is received before the timer expires, the segment is resent. This timeout is dynamically adjusted by TCP based on the Round Trip Time (RTT) measurements of the connection to optimize performance.
	- Impact: A short RTO can lead to unnecessary retransmissions, increasing network congestion, while a long RTO can cause significant delays if packets are lost.
2. **Connection Timeout (SYN Retransmissions):**
	- Definition: This refers to the time a client waits for a response during the initial connection establishment (the TCP three-way handshake). If the server doesn't respond within this period, the connection attempt fails.
	- Impact: If this timeout is too short, connections might fail prematurely in high-latency environments. If too long, applications might wait excessively for unresponsive servers.
3. **Keep-alive Timeout:**
	- Definition: Once a TCP connection is established and becomes idle, keep-alive messages can be sent periodically to check if the connection is still active and the peer is reachable. If a certain number of probes go unanswered, the connection is terminated.
	- Parameters: Typically controlled by three parameters:
		- Idle Time: The period of inactivity before the first keep-alive probe is sent.
		- Probe Interval: The time between subsequent keep-alive probes.
		- Probe Count: The number of unacknowledged probes before the connection is considered broken.
	- Impact: Prevents "half-open" connections (where one side crashes but the other remains unaware), freeing up resources.
4. **TIME_WAIT State Timeout:**
	- Definition: After a TCP connection is gracefully terminated, the closing side enters a TIME_WAIT state for a certain period. This state ensures that any delayed packets from the previous connection are delivered and prevents new connections from inadvertently receiving old packets if the same port pair is immediately reused.
	- Impact: A long TIME_WAIT timeout can lead to port exhaustion on busy servers handling many short-lived connections.
5. **Established Connection Timeout (Idle Timeout):**
	- Definition: This timeout dictates how long an established TCP connection can remain idle (without any data exchange) before it is automatically closed by the operating system or an intermediary device (like a firewall). This is often influenced by keep-alive settings.
	- Impact: Helps free up system resources from inactive connections. Setting it too low can prematurely terminate legitimate but temporarily idle connections.
