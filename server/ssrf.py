import web
import requests

urls = ("/.*", "hello")
app = web.application(urls, globals())

class hello:
    def GET(self):
        data = web.input(url="https://www.google.com")
        url = data.url
        headers = {'Authorization': 'Basic YWRtaW5AZXZpbC5jb206c3VwZXJzZWNyZXQ='}
        out = requests.get(url, headers=headers)
        out = out.status_code
        return out

if __name__ == "__main__":
    app.run()
