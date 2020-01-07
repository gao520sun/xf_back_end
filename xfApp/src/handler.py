from xfApp.server import proflask

@proflask.route("/health", methods=["GET", "HEAD"])
def health():
    return "pong"


@proflask.route("/ping", methods=["GET", "HEAD"])
def ping():
    return "pong"