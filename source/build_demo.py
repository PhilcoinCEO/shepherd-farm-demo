# Builds the demo app (index.html at the repo root) from index.source.html.
# Usage: python3 source/ build_demo.py
import os
HERE=os.path.dirname(os.path.abspath(__file__))
REPO=os.environ.get('APP_REPO',os.path.join(HERE,'..'))
s=open(os.path.join(HERE,'index.source.html')).read()
s='\n'.join(l.strip() for l in s.split('\n'))
out='<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover"><meta name="theme-color" content="#18291B"><link rel="manifest" href="manifest.webmanifest"><link rel="apple-touch-icon" href="apple-touch-icon.png"><link rel="icon" type="image/png" href="icon-192.png"><meta name="apple-mobile-web-app-capable" content="yes"><meta name="mobile-web-app-capable" content="yes"><meta name="apple-mobile-web-app-status-bar-style" content="black"><meta name="apple-mobile-web-app-title" content="La Finca"><title>La Finca Pastoreo</title><style>:root{color-scheme:light;padding-top:env(safe-area-inset-top,0px);padding-bottom:env(safe-area-inset-bottom,0px)}body{margin:0;font:14px system-ui,sans-serif}img{max-width:100%}[hidden]{display:none!important}</style></head><body>'+s+'<script>if("serviceWorker" in navigator&&location.protocol==="https:")addEventListener("load",()=>navigator.serviceWorker.register("sw.js").catch(()=>{}));</script></body></html>'
open(os.path.join(REPO,'index.html'),'w').write(out); print(len(out))
