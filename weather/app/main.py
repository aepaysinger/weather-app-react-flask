from flask import Flask, escape, request


app = Flask(__name__)


@app.route("/")
def hello():
    name = request.args.get("name", "World")
    return f"Hello, {escape(name)}!"


def main():
    app.run()


if __name__ == "__main__":
    main()
