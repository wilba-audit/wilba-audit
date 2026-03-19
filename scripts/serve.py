"""
WILBA Audit Responder — production server entry point.
Uses waitress instead of gunicorn to avoid worker timeout issues
with long-running outbound API calls (Anthropic, SendGrid).
"""
import os
from waitress import serve
from scripts.audit_email_responder import app

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    print(f"Starting WILBA Audit Responder on port {port} (waitress)")
    serve(app, host="0.0.0.0", port=port, threads=4, channel_timeout=300)
