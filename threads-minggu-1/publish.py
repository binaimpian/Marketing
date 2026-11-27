#!/usr/bin/env python3
"""Terbitkan post Threads yang dah sampai masa.

Guna:  python3 publish.py posts-contractorguyy.json [--dry-run]

- Token Threads disuntik oleh proxy (host graph.threads.net), jadi skrip ni
  tak baca token dari mana-mana.
- Post diterbit kalau masanya (MYT) dah lepas, tapi tak lebih 3 jam lepas
  (supaya post lama tak tersembur sekali gus kalau tugas terlepas).
- Rekod post yang dah keluar disimpan dalam posted-<nama>.json.
- parts: senarai teks; bahagian 1 = hook, selebihnya dibalas bersambung.
- image_urls (untuk bahagian 1 sahaja): 0 = teks, 1 = gambar, 2+ = carousel.
"""
import json, sys, time, urllib.request, urllib.parse, urllib.error
from datetime import datetime, timedelta, timezone
from pathlib import Path

API = "https://graph.threads.net/v1.0"
MYT = timezone(timedelta(hours=8))
WINDOW = timedelta(hours=3)


def call(method, path, params=None):
    url = f"{API}/{path}"
    data = None
    if params:
        enc = urllib.parse.urlencode(params)
        if method == "GET":
            url += "?" + enc
        else:
            data = enc.encode()
    req = urllib.request.Request(url, data=data, method=method)
    try:
        with urllib.request.urlopen(req, timeout=60) as r:
            return json.load(r)
    except urllib.error.HTTPError as e:
        raise RuntimeError(f"{method} {path}: {e.code} {e.read().decode()[:400]}")


def wait_ready(cid):
    for _ in range(20):
        s = call("GET", cid, {"fields": "status,error_message"})
        if s.get("status") == "FINISHED":
            return
        if s.get("status") in ("ERROR", "EXPIRED"):
            raise RuntimeError(f"container {cid}: {s}")
        time.sleep(3)
    raise RuntimeError(f"container {cid} belum siap")


def create_container(text, imgs, reply_to=None):
    extra = {"reply_to_id": reply_to} if reply_to else {}
    if not imgs:
        cid = call("POST", "me/threads", {"media_type": "TEXT", "text": text, **extra})["id"]
        wait_ready(cid)
        return cid
    if len(imgs) == 1:
        cid = call("POST", "me/threads", {"media_type": "IMAGE", "image_url": imgs[0], "text": text, **extra})["id"]
        wait_ready(cid)
        return cid
    kids = []
    for u in imgs[:20]:
        k = call("POST", "me/threads", {"media_type": "IMAGE", "image_url": u, "is_carousel_item": "true"})["id"]
        wait_ready(k)
        kids.append(k)
    cid = call("POST", "me/threads", {"media_type": "CAROUSEL", "children": ",".join(kids), "text": text, **extra})["id"]
    wait_ready(cid)
    return cid


def main():
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    dry = "--dry-run" in sys.argv
    src = Path(args[0]) if args else Path(__file__).with_name("posts-contractorguyy.json")
    if not src.is_absolute():
        src = Path(__file__).parent / src
    state_f = src.with_name("posted-" + src.stem.replace("posts-", "") + ".json")
    posts = json.loads(src.read_text())
    state = json.loads(state_f.read_text()) if state_f.exists() else {}

    me = call("GET", "me", {"fields": "id,username"})
    now = datetime.now(MYT)
    print(f"Akaun: @{me['username']} | sekarang {now:%Y-%m-%d %H:%M} MYT")

    due = []
    for p in posts:
        if p["id"] in state:
            continue
        at = datetime.fromisoformat(f"{p['date']}T{p['time']}").replace(tzinfo=MYT)
        if at <= now <= at + WINDOW:
            due.append(p)
        elif now > at + WINDOW:
            print(f"TERLEPAS {p['id']} ({p['date']} {p['time']}), tak diterbit")
    if not due:
        print("Tiada post yang sampai masa.")
        return
    for p in due:
        parts = p.get("parts") or [p["content"]]
        if dry:
            print(f"[dry-run] akan terbit {p['id']} ({len(parts)} bahagian): {parts[0][:60]!r}")
            continue
        ids, prev = [], None
        for i, text in enumerate(parts):
            cid = create_container(text, (p.get("image_urls") or []) if i == 0 else [], prev)
            prev = call("POST", "me/threads_publish", {"creation_id": cid})["id"]
            ids.append(prev)
            time.sleep(5)
        link = call("GET", ids[0], {"fields": "permalink"}).get("permalink")
        state[p["id"]] = {"media_ids": ids, "permalink": link,
                          "posted_at": datetime.now(MYT).isoformat(timespec="minutes")}
        state_f.write_text(json.dumps(state, indent=2, ensure_ascii=False))
        print(f"DITERBIT {p['id']} -> {link}")


if __name__ == "__main__":
    main()
