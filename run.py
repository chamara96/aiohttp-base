import asyncio
import signal
import sys

from app import create_app
from app.config import Config

try:
    import uvloop
except ImportError:
    pass
else:
    asyncio.set_event_loop_policy(uvloop.EventLoopPolicy())


def main():
    if "win" in sys.platform:
        signal.signal(signal.SIGINT, signal.SIG_DFL)
    app = create_app()
    app.run(host=Config.HOST, port=Config.PORT, debug=True)


if __name__ == "__main__":
    main()
