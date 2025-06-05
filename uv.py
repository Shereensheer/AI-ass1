from uv import App

app = App()

@app.route("/")
async def hello_world(request):
    return "Hello from UV!"

if __name__ == "__main__":
    app.run()


