#!/usr/bin/env python3
import os
import base64


def get_env0_config():
    """
    Read env0-related environment variables and return:
    - base_url
    - org_id
    - headers (with Basic auth)
    """
    base_url = os.environ.get("ENV0_API_URL", "https://api.env0.com")
    org_id = os.environ["ENV0_ORGANIZATION_ID"]
    api_key = os.environ["ENV0_API_KEY"]
    api_secret = os.environ["ENV0_API_SECRET"]

    token = base64.b64encode(f"{api_key}:{api_secret}".encode("utf-8")).decode("ascii")
    headers = {
        "Authorization": f"Basic {token}",
        "Content-Type": "application/json",
        "Accept": "application/json",
    }

    return base_url, org_id, headers
