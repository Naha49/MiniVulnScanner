import nmap

def run_scan():
    scanner = nmap.PortScanner()

    ip_range = input("Entrez une plage IP (ex : 192.168.1.0/24) : ")
    ports = input("Ports à scanner (ex : 22,80,443 ou 1-1024) : ")

    print(f"\n[+] Scan en cours sur {ip_range} avec les ports {ports}...\n")

    try:
        scanner.scan(hosts=ip_range, arguments=f"-p {ports} --open")
    except Exception as e:
        print("Erreur lors du scan :", e)
        return

    for host in scanner.all_hosts():
        print(f"\nHôte : {host}")
        print(f"  État : {scanner[host].state()}")
        for proto in scanner[host].all_protocols():
            ports = scanner[host][proto].keys()
            for port in ports:
                service = scanner[host][proto][port]['name']
                print(f"  Port : {port} | Service : {service}")

if __name__ == "__main__":
    run_scan()
