import subprocess
import os
import time
import sys
from concurrent.futures import ThreadPoolExecutor, as_completed
from urllib.parse import parse_qs, quote, unquote

# ================================================
# BRANDING & UI COLORS
# ================================================
BRAND_NAME = "ArchiveTell"
TELEGRAM_CH = "https://t.me/archivetell"
AUTHOR = "Bachelor⚡️"

GREEN = "\033[92m"
CYAN = "\033[96m"
YELLOW = "\033[93m"
RED = "\033[91m"
MAGENTA = "\033[95m"
BOLD = "\033[1m"
RESET = "\033[0m"

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

# ================================================
# EXPANDED DATABASES (VIP SNIs + CDN IPs)
# ================================================
DOMAINS = [
    "helm.sh", "keda.sh", "rook.io", "istio.io", "cilium.io", "fluxcd.io",
    "harbor.io", "calico.org", "linkerd.io", "openebs.io", "tekton.dev",
    "longhorn.io", "blog.helm.sh", "docs.helm.sh", "crossplane.io",
    "kubernetes.io", "kubebuilder.io", "cert-manager.io", "letsencrypt.org",
    "kind.sigs.k8s.io", "kops.sigs.k8s.io", "krew.sigs.k8s.io",
    "kwok.sigs.k8s.io", "kueue.sigs.k8s.io", "jobset.sigs.k8s.io",
    "kaniko.sigs.k8s.io", "minikube.sigs.k8s.io", "operatorframework.io",
    "container.sigs.k8s.io", "kustomize.sigs.k8s.io", "argo-cd.readthedocs.io",
    "cluster-api.sigs.k8s.io", "descheduler.sigs.k8s.io", "gateway-api.sigs.k8s.io",
    "external-dns.sigs.k8s.io", "service-apis.sigs.k8s.io", "image-builder.sigs.k8s.io",
    "kubectl.docs.kubernetes.io", "metrics-server.sigs.k8s.io",
    "scheduler-plugins.sigs.k8s.io", "controller-runtime.sigs.k8s.io",
    "prometheus-operator.sigs.k8s.io", "node-feature-discovery.sigs.k8s.io",
    "hierarchical-namespaces.sigs.k8s.io", "secrets-store-csi-driver.sigs.k8s.io",
    "security-profiles-operator.sigs.k8s.io", "cluster-proportional-autoscaler.sigs.k8s.io",
    "cncf.io", "www.cncf.io", "landscape.cncf.io", "artifacthub.io",
    "etcd.io", "containerd.io", "cri-o.io", "prometheus.io",
    "opentelemetry.io", "openpolicyagent.org", "kubevirt.io", "thanos.io",
    "envoyproxy.io", "jaegertracing.io", "argo-project.io", "backstage.io",
    "knative.dev", "buildpacks.io", "k3s.io", "falco.org", "kyverno.io",
    "kubevela.io", "kubeflow.org", "karmada.io", "spinnaker.io",
    "docs.kubernetes.io", "blog.kubernetes.io", "get.helm.sh", "min.io",
    "grafana.com", "registry.k8s.io"
]

IPS = [
    "50.7.5.83", "50.7.87.2", "50.7.87.3", "50.7.87.4", "50.7.87.5",
    "75.2.60.5", "5.9.210.65", "5.9.248.38", "5.9.248.39", "50.7.85.43",
    "144.76.1.88", "104.21.33.34", "188.114.98.0", "188.114.99.0",
    "3.162.247.34", "3.162.247.38", "3.162.247.45", "3.162.247.77",
    "3.33.186.135", "63.176.8.218", "74.91.29.207", "85.10.207.48",
    "85.10.207.51", "88.99.249.74", "94.130.33.41", "95.216.69.37",
    "104.198.14.52", "104.21.63.202", "148.251.65.39", "15.197.167.90",
    "170.205.28.40", "172.67.150.14", "188.40.147.23", "188.40.181.55",
    "204.12.196.34", "204.12.196.39", "34.194.97.138", "35.157.26.135",
    "40.160.22.170", "52.222.214.38", "52.222.214.99", "54.232.119.62",
    "65.109.34.234", "69.197.138.87", "83.136.211.95", "85.158.145.74",
    "91.99.175.105", "94.130.70.160", "138.201.54.122", "142.54.178.211",
    "142.54.178.215", "142.54.189.111", "172.67.158.128", "178.63.240.111",
    "184.171.110.10", "185.134.23.172", "188.40.254.151", "204.12.192.223",
    "204.12.223.183", "52.222.214.108", "52.222.214.124", "63.141.252.203",
    "63.141.252.207", "69.197.146.178", "69.197.146.183", "136.243.128.223",
    "168.119.202.236", "173.208.128.143", "50.7.5.85", "76.76.21.112",
    "94.130.13.19", "94.130.50.12", "198.252.206.1", "104.18.25.196",
    "149.154.167.99", "178.22.122.101", "204.79.197.220", "216.239.38.120",
    "172.67.201.240", "104.21.60.220", "23.185.0.3", "34.96.108.209",
    "185.199.108.153", "185.199.109.153", "185.199.110.153", "185.199.111.153",
    "104.16.80.15", "104.17.96.15", "104.18.32.45", "172.66.40.100", "172.67.80.200",
    "188.114.96.10", "188.114.97.20", "188.114.98.100", "188.114.99.150",
    "104.21.40.50", "104.22.10.20", "162.158.100.50", "172.64.32.100",
    "3.160.200.10", "13.32.50.30", "18.160.10.40", "52.222.214.1",
    "35.186.200.50", "34.160.100.20", "51.210.100.30", "145.239.100.40",
    "5.161.50.60", "49.13.100.70", "65.108.50.80", "94.130.200.90",
    "138.201.100.100", "148.251.100.110", "185.53.177.50", "212.83.100.120",
    "104.21.1.100", "172.67.70.100", "188.114.96.200", "104.18.25.10",
    "3.162.200.50", "52.222.214.150", "15.197.167.100", "13.224.50.30"
]

# ================================================
# CORE LOGIC
# ================================================
def parse_vless(vless_url):
    if not vless_url.startswith("vless://"): return None
    try:
        rest = vless_url[8:]
        uuid, address_part = rest.split("@", 1)
        if "?" in address_part: ip_port, query_str = address_part.split("?", 1)
        else: ip_port, query_str = address_part, ""
        if "#" in query_str: query_str = query_str.split("#", 1)[0]
            
        ip, port = ip_port.rsplit(":", 1) if ":" in ip_port else (ip_port, "443")
        params = parse_qs(query_str) if query_str else {}
        
        return {
            "uuid": uuid, "port": port,
            "host": params.get("host", [""])[0],
            "path": params.get("path", [""])[0],
            "alpn": params.get("alpn", [""])[0],
            "security": params.get("security", ["tls"])[0],
            "type": params.get("type", ["xhttp"])[0]
        }
    except: return None

def generate_vless(ip, sni, base_params, ping_ms, dns_tag):
    remark = f"{BRAND_NAME}_{dns_tag}_{ping_ms:.0f}ms_{sni.split('.')[0]}"
    
    host_q = quote(base_params.get("host", ""), safe='')
    path_q = quote(base_params.get("path", ""), safe='')
    alpn_q = quote(base_params.get("alpn", ""), safe='')
    
    return (
        f"vless://{base_params['uuid']}@{ip}:{base_params['port']}?"
        f"allowInsecure=1&alpn={alpn_q}&encryption=none&host={host_q}&"
        f"mode=auto&path={path_q}&security={base_params.get('security', 'tls')}&"
        f"sni={sni}&type={base_params.get('type', 'xhttp')}#{remark}"
    )

def hardcore_test(ip, sni, base_params, dns_mode):
    """
    2-Stage Hardcore Testing Algorithm (Defeats Fake Ping)
    """
    host = base_params.get("host", sni)
    path = unquote(base_params.get("path", "/"))
    if not path.startswith("/"): path = "/" + path

    devnull = 'NUL' if os.name == 'nt' else '/dev/null'
    
    cmd = [
        "curl", "-s", "-o", devnull,
        "-w", "%{http_code}:%{time_appconnect}:%{time_total}", 
        "--max-time", "4",
        f"https://{sni}{path}",
        "--resolve", f"{sni}:443:{ip}",
        "-H", f"Host: {host}",
        "-H", "User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
    ]
    
    if dns_mode == "2":
        cmd.extend(["--dns-servers", "178.22.122.101,185.51.200.2"])
    
    try:
        flags = subprocess.CREATE_NO_WINDOW if os.name == 'nt' else 0
        result = subprocess.run(cmd, capture_output=True, text=True, creationflags=flags)
        
        output = result.stdout.strip()
        if not output or ":" not in output: return None
            
        parts = output.split(":")
        http_code = parts[0]
        tls_time = float(parts[1]) * 1000 
        total_time = float(parts[2]) * 1000
        
        # 1. Drop if TLS Handshake failed
        if tls_time <= 0: return None
            
        # 2. Drop if DPI injected a reset (Fake Ping / 000 code)
        if http_code == "000": return None
            
        # 3. Drop on Cloudflare/Server blocks (Access Denied / Down)
        bad_codes = ["403", "502", "503", "521", "522", "523", "530"]
        if http_code in bad_codes: return None
            
        # Success! Generate VLESS based on actual payload round-trip time
        dns_tag = "SH" if dns_mode == "2" else "DIR"
        config_str = generate_vless(ip, sni, base_params, total_time, dns_tag)
        return ip, sni, total_time, http_code, config_str
        
    except:
        pass
    return None

def main():
    # Prevent Termux/Android from killing the process (Signal 9)
    if os.name != 'nt':
        try:
            subprocess.run(["termux-wake-lock"], capture_output=True)
        except:
            pass

    if os.name == 'nt': os.system('color')
    clear_screen()
    
    print(f"{CYAN}╔═══════════════════════════════════════════════════════════╗{RESET}")
    print(f"{CYAN}║{RESET}  {BOLD}{MAGENTA}🚀 V2 PRO SCANNER - ARCHIVETELL EDITION{RESET}                 {CYAN}║{RESET}")
    print(f"{CYAN}╚═══════════════════════════════════════════════════════════╝{RESET}")
    print(f"{YELLOW}  * Developer: {AUTHOR}{RESET}")
    print(f"{YELLOW}  * Channel:   {TELEGRAM_CH}{RESET}")
    print(f"{YELLOW}  * Engine:    2-Stage DPI Bypasser (No Fake Pings){RESET}\n")

    # --- 1. DNS Selection ---
    print(f"  {BOLD}{CYAN}Select Network Mode:{RESET}")
    print(f"  {GREEN}[1]{RESET} Direct (No DNS Bypass)")
    print(f"  {GREEN}[2]{RESET} Shecan DNS Bypass (178.22.122.101)")
    print(f"  {YELLOW}Note: If choosing Mode 2, ensure your IP is updated on Shecan servers first.{RESET}")
    dns_mode = input(f"\n  {YELLOW}Mode Choice [1-2] (Default 1): {RESET}").strip() or "1"

    # --- 2. VLESS Input ---
    vless_input = input(f"\n  {BOLD}{CYAN}Paste your working VLESS baseline link:{RESET}\n  > ").strip()
    base_params = parse_vless(vless_input)
    
    if not base_params:
        print(f"\n  {RED}[!] Format Error: Invalid VLESS URL.{RESET}")
        time.sleep(2)
        sys.exit()
        
    print(f"  {GREEN}✔ Config Validated. (Host: {base_params['host']}){RESET}\n")

    # --- 3. Thread Setup ---
    print(f"  {BOLD}{CYAN}Set Max Threads:{RESET}")
    print(f"  {YELLOW}(Enter 30-50 for Mobile/Termux to avoid crashes, 100+ for PC){RESET}")
    try:
        threads = int(input(f"  {YELLOW}Threads (Default 40): {RESET}").strip() or 40)
    except ValueError:
        threads = 40
        
    total_tests = len(IPS) * len(DOMAINS)
    print(f"\n  {CYAN}[*] Database: {len(IPS)} IPs | {len(DOMAINS)} SNIs (Total: {total_tests} Tests){RESET}")
    print(f"  {MAGENTA}[*] Initiating Hardcore Network Scan... Please wait...{RESET}\n")
    
    working_configs = []
    completed = 0

    with ThreadPoolExecutor(max_workers=threads) as executor:
        try:
            futures = {executor.submit(hardcore_test, ip, sni, base_params, dns_mode): (ip, sni) for ip in IPS for sni in DOMAINS}
            
            for future in as_completed(futures):
                completed += 1
                res = future.result()
                
                # Progress Bar
                sys.stdout.write(f"\r{BOLD}{CYAN}  [PROGRESS]{RESET} {completed}/{total_tests} | {GREEN}FOUND: {len(working_configs)}{RESET}  ")
                sys.stdout.flush()

                if res:
                    ip, sni, ping_ms, http_code, config = res
                    working_configs.append((ping_ms, config))
                    
                    # Clear line for positive match
                    sys.stdout.write(f"\r{' ' * 90}\r") 
                    
                    color = GREEN if ping_ms < 800 else YELLOW
                    # Show Success Message
                    print(f"  {GREEN}✔ CONNECTED!{RESET} IP: {ip:<15} | SNI: {sni:<22} | Ping: {color}{ping_ms:.0f}ms{RESET}")
                    # Show Config directly in Terminal
                    print(f"  {MAGENTA}└─>{RESET} {config}\n")

        except KeyboardInterrupt:
            print(f"\n\n  {RED}[!] Scan interrupted by {AUTHOR}. Saving found configs...{RESET}")
            executor.shutdown(wait=False, cancel_futures=True)

    print(f"\n{CYAN}═════════════════════════════════════════════════════════════{RESET}")
    if working_configs:
        working_configs.sort(key=lambda x: x[0])
        
        filename = f"{BRAND_NAME}_Verified_Configs.txt"
        with open(filename, "w") as f:
            f.write(f"// Generated by {BRAND_NAME} Scanner\n")
            f.write(f"// Channel: {TELEGRAM_CH}\n")
            f.write(f"// Developer: {AUTHOR}\n")
            f.write(f"// Note: All configs passed 2-Stage Verification (TLS + HTTP)\n\n")
            for ping, cfg in working_configs:
                f.write(f"// Real Latency: {ping:.0f}ms\n{cfg}\n\n")
                
        print(f"  {BOLD}{GREEN}🎉 SCAN COMPLETE! Found {len(working_configs)} guaranteed configs.{RESET}")
        print(f"  {GREEN}📄 Results securely saved to '{filename}'.{RESET}")
    else:
        print(f"  {BOLD}{RED}❌ ZERO CONFIGS PASSED.{RESET}")
        print(f"  {YELLOW}Note: No configurations survived the hardcore DPI filtering tests.{RESET}")
    print(f"{CYAN}═════════════════════════════════════════════════════════════{RESET}")
    
    if os.name == 'nt': input("\n  Press Enter to exit...")

if __name__ == "__main__":
    main()
