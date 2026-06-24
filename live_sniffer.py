import sys
import time

def parse_network_packet(packet_id, source_ip, dest_ip, port, data_payload):
    # Simulated packet analyzer mimicking real-world Wireshark capture engines
    print(f"[*] [PACKET #{packet_id:03}] Intercepting network layer data transit...")
    time.sleep(0.4)
    print(f"    │   Source Route : {source_ip}")
    print(f"    │   Destination  : {dest_ip}")
    print(f"    │   Target Port  : {port} (Vulnerability Inspection Mode)")
    
    # Analyze payload for critical security threat alerts
    if "iitk{" in data_payload or "cat /etc/passwd" in data_payload:
        print(f"    └── [🚨 THREAT DETECTED]: Malicious Payload Injection Signature Found!")
        print(f"        [!] Suspicious Data String: '{data_payload}'")
    else:
        print(f"    └── [✓] Traffic Status: Normal Data Packet verified.")
    print("-" * 65)

if __name__ == "__main__":
    print("=" * 65)
    print("        SARTHAK'S LIVE NETWORK PROTOCOL & PACKET INSPECTION TOOL      ")
    print("=" * 65)
    print("[+] Binding socket interface to local network card driver...")
    time.sleep(1)
    print("[+] Monitoring interface activated. Sniffing live port data streams...\n")
    time.sleep(0.5)

    # Simulated active raw packet data stream
    mock_traffic = [
        ("192.168.1.50", "142.250.190.46", 443, "GET /index.html HTTP/1.1"),
        ("203.0.113.5", "192.168.1.1", 80, "cat /etc/passwd; id; whoami"),
        ("192.168.1.50", "192.168.1.254", 53, "DNS Query: iitk.ac.in"),
        ("198.51.100.12", "192.168.1.10", 8080, "POST /api/v1/auth flag=iitk{n3tw0rk_sn1ff1ng_pwn3d}")
    ]

    for index, (src, dst, prt, payload) in enumerate(mock_traffic, start=1):
        parse_network_packet(index, src, dst, prt, payload)
        
    print("[+] Packet capture sequence complete. Logs compiled successfully.")
