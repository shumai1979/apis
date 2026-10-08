#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""TikTok publisher for Contos do Escuro (auto token refresh + draft/direct)."""
import json, os, time, sys, urllib.parse, urllib.request, urllib.error

TT = "/data/scaleearn/tiktok"
CFG = os.path.join(TT, "config.json")
TOKEN_URL = "https://open.tiktokapis.com/v2/oauth/token/"

def _read(p):
    try:
        return open(p).read().strip()
    except Exception:
        return ""

def _cfg():
    try:
        return json.load(open(CFG))
    except Exception:
        return {"mode": "sandbox", "direct": False}

def _paths():
    c = _cfg()
    if c.get("mode") == "production":
        return (os.path.join(TT, "client_key.txt"),
                os.path.join(TT, "client_secret.txt"),
                os.path.join(TT, "token_prod.json"))
    return (os.path.join(TT, "sandbox_client_key.txt"),
            os.path.join(TT, "sandbox_client_secret.txt"),
            os.path.join(TT, "token_sandbox.json"))

def _load_token(tokfile):
    return json.load(open(tokfile))

def _save_token(tokfile, t):
    t["_saved_at"] = int(time.time())
    json.dump(t, open(tokfile, "w"))

def _post_form(url, data):
    body = urllib.parse.urlencode(data).encode()
    req = urllib.request.Request(url, data=body,
        headers={"Content-Type": "application/x-www-form-urlencoded"})
    with urllib.request.urlopen(req, timeout=40) as r:
        return json.loads(r.read().decode())

def _post_json(url, obj, at):
    body = json.dumps(obj).encode()
    req = urllib.request.Request(url, data=body, headers={
        "Authorization": "Bearer " + at,
        "Content-Type": "application/json; charset=UTF-8"})
    try:
        with urllib.request.urlopen(req, timeout=60) as r:
            return r.status, json.loads(r.read().decode())
    except urllib.error.HTTPError as e:
        return e.code, json.loads(e.read().decode() or "{}")

def refresh():
    ck_f, cs_f, tokfile = _paths()
    t = _load_token(tokfile)
    resp = _post_form(TOKEN_URL, {
        "client_key": _read(ck_f), "client_secret": _read(cs_f),
        "grant_type": "refresh_token", "refresh_token": t["refresh_token"]})
    if resp.get("access_token"):
        resp.setdefault("open_id", t.get("open_id"))
        _save_token(tokfile, resp)
        return resp
    raise RuntimeError("refresh failed: " + json.dumps(resp)[:300])

def valid_token():
    ck_f, cs_f, tokfile = _paths()
    t = _load_token(tokfile)
    age = int(time.time()) - t.get("_saved_at", 0)
    if age > int(t.get("expires_in", 86400)) - 900:
        t = refresh()
    return t["access_token"]

def _put_file(upload_url, video, size):
    body = open(video, "rb").read()
    req = urllib.request.Request(upload_url, data=body, method="PUT", headers={
        "Content-Type": "video/mp4",
        "Content-Range": "bytes 0-%d/%d" % (size - 1, size)})
    with urllib.request.urlopen(req, timeout=600) as r:
        return r.status

def post_draft(video, caption=None):
    at = valid_token()
    size = os.path.getsize(video)
    st, resp = _post_json("https://open.tiktokapis.com/v2/post/publish/inbox/video/init/",
        {"source_info": {"source": "FILE_UPLOAD", "video_size": size,
                          "chunk_size": size, "total_chunk_count": 1}}, at)
    if resp.get("error", {}).get("code") not in ("ok", None):
        raise RuntimeError("init error: " + json.dumps(resp)[:300])
    d = resp["data"]
    _put_file(d["upload_url"], video, size)
    return d["publish_id"]

def post_direct(video, caption=None, privacy="SELF_ONLY"):
    at = valid_token()
    size = os.path.getsize(video)
    body = {"post_info": {"title": caption or "", "privacy_level": privacy,
                          "disable_duet": False, "disable_comment": False,
                          "disable_stitch": False},
            "source_info": {"source": "FILE_UPLOAD", "video_size": size,
                            "chunk_size": size, "total_chunk_count": 1}}
    st, resp = _post_json("https://open.tiktokapis.com/v2/post/publish/video/init/", body, at)
    if resp.get("error", {}).get("code") not in ("ok", None):
        raise RuntimeError("init error: " + json.dumps(resp)[:300])
    d = resp["data"]
    _put_file(d["upload_url"], video, size)
    return d["publish_id"]

def publish(video, caption=None):
    c = _cfg()
    if c.get("direct"):
        return ("direct", post_direct(video, caption, c.get("privacy", "PUBLIC_TO_EVERYONE")))
    return ("draft", post_draft(video, caption))

if __name__ == "__main__":
    args = sys.argv[1:]
    if not args:
        print("usage: tiktok_publish.py [--refresh|--direct] <video> [caption]"); sys.exit(1)
    if args[0] == "--refresh":
        r = refresh(); print("refreshed. expires_in:", r.get("expires_in"), "open_id:", (r.get("open_id") or "")[:10]); sys.exit(0)
    force_direct = False
    if args[0] == "--direct":
        force_direct = True; args = args[1:]
    video = args[0]; caption = args[1] if len(args) > 1 else None
    print(post_direct(video, caption) if force_direct else publish(video, caption))
