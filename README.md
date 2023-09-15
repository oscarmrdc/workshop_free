
https://ipinfo.io/50.58.239.155
https://www.ssllabs.com/ssltest/
https://securityheaders.com/
https://csp-evaluator.withgoogle.com/
https://security.snyk.io/package/maven/org.apache.tomcat:tomcat/9.0.37

https://iplogger.org/

-----------------------------------------------

INTERACTSH
https://github.com/projectdiscovery/interactsh
https://github.com/projectdiscovery/interactsh/releases

sudo apt install golang-go
go version
go install -v github.com/projectdiscovery/interactsh/cmd/interactsh-client@latest

vim ~/.zshrc
export GOPATH="$HOME/go"
PATH="$GOPATH/bin:$PATH"

interactsh-client -h

interactsh-client
interactsh-client -v

-----------------------------------------------

https://canarytokens.org

https://webhook.site/

-----------------------------------------------

https://ngrok.com/docs/secure-tunnels/ngrok-agent/reference/changelog/
https://ngrok.com/download

wget https://bin.equinox.io/c/bNyj1mQVY4c/ngrok-v3-stable-linux-amd64.tgz
tar -xzvf ngrok-v3-stable-linux-amd64.tgz

~/ngrok -v
sudo apachectl start
(python3 -m http.server)

~/ngrok http 80
https://02fd-179-6-12-98.ngrok-free.app

https://dashboard.ngrok.com/signup
https://dashboard.ngrok.com/get-started/your-authtoken

~/ngrok config add-authtoken your_token

~/ngrok http 80
https://a90d-179-6-12-98.ngrok-free.app

http://localhost:4040

~/ngrok http 80 --domain=chipmunk-gentle-heartily.ngrok-free.app --basic-auth="user:password"

-----------------------------------------------

https://chipmunk-gentle-heartily.ngrok-free.app/?url=https://www.google.com
https://chipmunk-gentle-heartily.ngrok-free.app/?url=https://webhook.site/406d1bee-89d3-4777-87d6-15bf7e2edca8

---------

https://webhook.site/ - Edit

text/html

<html>
<script>alert(document.location)</script>
</html>

https://chipmunk-gentle-heartily.ngrok-free.app/?url=https://webhook.site/406d1bee-89d3-4777-87d6-15bf7e2edca8

---------

cd /tmp
wget https://raw.githubusercontent.com/oscarmrdc/workshop_free/main/headers.py
pip install web.py==0.62
python3 headers.py 9090
~/ngrok http 9090

https://9371-179-6-12-98.ngrok-free.app
https://chipmunk-gentle-heartily.ngrok-free.app/?url=https://9371-179-6-12-98.ngrok-free.app



