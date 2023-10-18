
python3 ssrf.py 9090
python3 ssrf_render.py 9091

ngrok http 9090 --domain={your_ngrok_domain} --basic-auth="user:password"
