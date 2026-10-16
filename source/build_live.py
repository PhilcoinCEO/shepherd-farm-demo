# Builds the live app (live/index.html) from index.source.html + firebase-config.js.
# Usage: python3 source/ build_live.py
import sys,re,os
HERE=os.path.dirname(os.path.abspath(__file__))
REPO=os.environ.get('APP_REPO',os.path.join(HERE,'..'))
mock = len(sys.argv)>1 and sys.argv[1]=="mock"
s=open(os.path.join(HERE,'index.source.html')).read()
s='\n'.join(l.strip() for l in s.split('\n'))
cfg=open(os.path.join(HERE,'firebase-config.js')).read()
if mock:
    head='<script src="mockfb.js"></script>'
    s=s.replace('(() => {\n"use strict";','(() => {\n"use strict"; window.__dbg=(c)=>eval(c);',1)
else: head="".join('<script src="https://www.gstatic.com/firebasejs/10.14.1/firebase-%s-compat.js"></script>' % n for n in ["app","auth","firestore","functions","storage"])
out='<!doctype html><html lang="es"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover"><meta name="theme-color" content="#18291B"><meta name="robots" content="noindex"><link rel="apple-touch-icon" href="../apple-touch-icon.png"><link rel="icon" type="image/png" href="../icon-192.png"><meta name="apple-mobile-web-app-capable" content="yes"><meta name="apple-mobile-web-app-title" content="La Finca"><title>La Finca Pastoreo</title><style>:root{color-scheme:light;padding-top:env(safe-area-inset-top,0px);padding-bottom:env(safe-area-inset-bottom,0px)}body{margin:0;font:14px system-ui,sans-serif}img{max-width:100%}[hidden]{display:none!important}</style>'+head+'<script>'+cfg+'</script></head><body>'+s+'</body></html>'
dest=os.path.join(HERE,'livetest','index.html') if mock else os.path.join(REPO,'live','index.html')
os.makedirs(os.path.dirname(dest),exist_ok=True); open(dest,'w').write(out); print(dest,len(out))
