print("online" if __import__("requests").get("https://archlinux.org").ok else "offline")