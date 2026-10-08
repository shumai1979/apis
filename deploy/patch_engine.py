F = "/data/scaleearn/terror_engine_v2.py"
s = open(F).read()
if "tiktok_publish" in s:
    print("already hooked"); raise SystemExit
hook = (
'    try:\n'
'        import sys as _tt; _tt.path.insert(0, "/data/scaleearn/tiktok"); import tiktok_publish as _ttp\n'
'        _r = _ttp.publish(final, story.get("title")); print("   TIKTOK", _r)\n'
'    except Exception as _e:\n'
'        print("   TIKTOK FAIL", _e)\n'
)
marker = '    st=load_state(); st.setdefault("done",[]).append(story["id"]); save_state(st); print("CONCLUIDO.")'
if marker in s:
    s = s.replace(marker, hook + marker, 1)
    open(F, "w").write(s)
    print("HOOKED OK")
else:
    print("MARKER NOT FOUND")
