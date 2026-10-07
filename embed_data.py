# -*- coding: utf-8 -*-
"""將 ntc_reward_punishment.json 內嵌進 index.html，使雙擊開啟(file://)也能使用。
保留 fetch 優先（方便日後更新 JSON 免改 HTML），失敗時退回內嵌資料。
"""
import json
import os

BASE = r"I:\我的雲端硬碟\OpenCoad資料夾\2026東專校規準則"
HTML = os.path.join(BASE, "index.html")
JSONF = os.path.join(BASE, "reference_docs", "ntc_reward_punishment.json")

db = json.load(open(JSONF, encoding="utf-8"))
# 僅內嵌查詢需要的部分，縮小體積
slim = {"rewards": db["rewards"], "punishments": db["punishments"]}
embedded = json.dumps(slim, ensure_ascii=False, separators=(",", ":"))

html = open(HTML, encoding="utf-8").read()

old_load = """async function load(){
  const r = await fetch('./reference_docs/ntc_reward_punishment.json');
  DB = await r.json();
  render('');
}"""
new_load = """const EMBEDDED_DB = __EMBEDDED_JSON__;
async function load(){
  try{
    const r = await fetch('./reference_docs/ntc_reward_punishment.json');
    if(r.ok){ DB = await r.json(); }
    else{ DB = EMBEDDED_DB; }
  }catch(e){ DB = EMBEDDED_DB; }
  render('');
}"""

assert old_load in html, "load() pattern not found"
new_load = new_load.replace("__EMBEDDED_JSON__", embedded)
html = html.replace(old_load, new_load)
open(HTML, "w", encoding="utf-8").write(html)
print("EMBEDDED bytes:", len(embedded))
print("OK")
