import web

urls = ("/.*", "hello")
app = web.application(urls, globals())

class hello:
    def GET(self):
        web.header('Custom1', 'aaaaaaaaaaaaaaaaaaaaa')
        web.header('Content-Type', 'text/html')
        return '<script>alert(1)</script>'




if __name__ == "__main__":
    app.run()
