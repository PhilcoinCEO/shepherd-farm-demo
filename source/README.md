# App source

`index.source.html` is the readable source of Shepherd Farm OS. The files at the repo root are built from it.

```
python3 source/build_demo.py   # writes index.html (demo, sample data in the browser)
python3 source/build_live.py   # writes live/index.html (live app, Firebase)
```

Always edit `source/index.source.html`, rebuild both, then commit all three files together.
`firebase-config.js` is the public Firebase web config (safe to publish by design).
