import argparse
import json
import logging
from threading import Thread, Lock
from tqdm import tqdm
from datetime import datetime

from scanner.core import scan_port
from scanner.banner import grab_banner
from scanner.utils import get_service
from scanner.logger import setup_logger
from scanner.network import scan_network


results = []
lock = Lock()
progress = None


def worker(target_ip, mac, port):
    global progress

    try:
        if scan_port(target_ip, port):
            banner = grab_banner(target_ip, port)
            service = get_service(port)

            result = {
                "target": target_ip,
                "mac": mac,
                "port": port,
                "status": "open",
                "service": service,
                "banner": banner if banner else "N/A"
            }

            # ✅ clean print with tqdm
            tqdm.write(f"[+] {target_ip}:{port} OPEN ({service})")
            logging.info(f"Port {port} open on {target_ip}")
            results.append(result)

    except Exception as e:
        logging.error(f"Error scanning {target_ip}:{port}: {e}")

    finally:
        # ✅ accurate progress update
        with lock:
            progress.update(1)


def main():
    parser = argparse.ArgumentParser(description="Custom Port Scanner with Banner Detection")

    parser.add_argument("--target", help="Target IP or domain")
    parser.add_argument("--network", help="Network range (e.g. 192.168.1.0/24)")
    parser.add_argument("--start", type=int, default=1, help="Start port")
    parser.add_argument("--end", type=int, default=1000, help="End port")
    parser.add_argument("--timestamp", action="store_true", help="Add timestamp to output file")

    args = parser.parse_args()

    # setup logging
    setup_logger()
    logging.info("Scan started")

    targets = []

    # 🟣 network mode
    if args.network:
        print(f"\n🔍 Scanning network: {args.network}\n")
        devices = scan_network(args.network)
        targets = devices

    # 🟢 single target mode
    elif args.target:
        targets.append({"ip": args.target, "mac": "N/A"})

    else:
        print("❌ Please provide --target or --network")
        return

    print(f"\n🎯 Targets: {[t['ip'] for t in targets]}\n")

    # 🔥 scan each target independently
    for target in targets:
        ip = target["ip"]
        mac = target["mac"]

        print(f"\n🚀 Scanning {ip} ({mac})\n")

        local_threads = []

        total_ports = args.end - args.start + 1

        global progress
        progress = tqdm(total=total_ports, desc=f"{ip}", ncols=80)

        for port in range(args.start, args.end + 1):
            t = Thread(target=worker, args=(ip, mac, port))
            t.start()
            local_threads.append(t)

        for t in local_threads:
            t.join()

        progress.close()

    # filename handling
    if args.network:
        safe_target = args.network.replace(".", "_").replace("/", "_")
    else:
        safe_target = args.target.replace(".", "_")

    if args.timestamp:
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        output_file = f"results/{safe_target}_{timestamp}.json"
    else:
        output_file = f"results/{safe_target}.json"

    # save results
    with open(output_file, "w") as f:
        json.dump(results, f, indent=4)

    logging.info("Scan finished")

    print("\n✅ Scan complete!")
    print(f"📄 JSON saved to: {output_file}")


if __name__ == "__main__":
    main()
