import urllib.request

try:
    with urllib.request.urlopen("http://127.0.0.1:5000/", timeout=3) as r:
        print("Status:", r.status)
except Exception as exc:
    print("Application is not reachable:", exc)
