from http.server import HTTPServer, BaseHTTPRequestHandler
import json
import datetime
import socket
import os

try:
    import redis
    r = redis.Redis(host=os.getenv('Redis_HOST', 'redis'), port=6379)
    r.ping()
    REDIS_AVAILABLE = True

except:
    REDIS_AVAILABLE = False

class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        
        #Count hits using Redis
        hits = 0
        if REDIS_AVAILABLE:
            hits = r.incr('hits')

        response = {
            "message": "Hello from DevOps Lab!",
            "hostname": socket.gethostname(),
            "timestamp": str(datetime.datetime.now()),
            "path": self.path,
            "owner": "digensclub",
            "hit_counts": int(hits),
            "redis_connected": REDIS_AVAILABLE

        }
        self.wfile.write(json.dumps(response, indent=2).encode())

    def log_message(self, format, *args):
        print(f"[{datetime.datetime.now()}] {args[0]} {args[1]} {args[2]}")

if __name__ == '__main__':
    port = 8000
    print(f"Starting server on port {port}")
    print(f"Redis availabe: {REDIS_AVAILABLE}")
    HTTPServer(('0.0.0.0', port), Handler).serve_forever()