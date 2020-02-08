import unicodedata
import os
import sys
import yaml
import re
import subprocess
from datetime import datetime

def isDigit(num) -> bool:
  tmp = str(num)
  patt = '^[0-9]+$'

  repatt = re.compile(patt)
  return bool(repatt.match(tmp))

def writeSyslog(msg):
  cmdline = ['logger', '-t', 'SOCEngine', msg]

  try :
    res = subprocess.run(cmdline, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
  except :
    print(cmdline[0] + " is failed")
    print("message : " + res.stdout.decode())

def main() :
  print("処理開始:" + datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f%z"))
  # __file__はファイルのフルパスでなく、python3コマンドで指定したファイル名が格納される
  basedir = os.path.dirname(__file__)

  yml_fil = os.path.join(basedir, "test.query")

  # ファイルの有無チェック
  if not os.path.exists(yml_fil) :
    print("ymlファイルがありません")

  with open(yml_fil, 'r', encoding='UTF-8') as conf:
    cf = yaml.load(conf, Loader=yaml.FullLoader)

  # ディレクトリなかったら作成する
  for k, d in cf["LOG_DIFINITION"].items():
    if not os.path.isdir(d) :
      os.makedirs(d)

  qfil = "./test_id_q.query"
  with open(qfil, 'r', encoding='UTF-8') as q:
    qr = yaml.load(q, Loader=yaml.FullLoader)

  qr["query"]["filter"]["@timestamp"] = {"gte":"2019", "lt":"2021"}

  print(qr["query"]["filter"]["@timestamp"]["gte"] + "以上")
  print(qr["query"]["filter"]["@timestamp"]["lt"] + "未満")

  yymmdd = "201903051156"

  # ES風の日付に変換
  cht = yymmdd[:4] + "-" + yymmdd[4:6] + "-" + yymmdd[6:8] + "T" + yymmdd[8:10] + ":" + yymmdd[10:12] + "+09:00" 
  # 文字列→日付変換
  dtm = datetime.strptime(yymmdd, '%Y%m%d%H%M')

  print(cht)
  print(dtm)

  # 数値チェック
  num = 'a'
  if isDigit(num) :
    print(str(num) + 'は数値です')
  else :
    print(str(num) + 'は数値でnai')

  # 数値チェック
  num = '0'
  if isDigit(num) :
    print(str(num) + 'は数値です')
  else :
    print(str(num) + 'は数値でない')

  # 数値チェック
  num = '２'
  if isDigit(num) :
    print(str(num) + 'は半角数値です')
  else :
    print(str(num) + 'は半角数値でない')

  # リストの連結
  idxs = ['c001', 'c002', 'c003']

  idxs_str = ",".join(idxs)
  print("連結文字列:" + idxs_str)

  print("処理終了:" + datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f%z"))  

if __name__ == "__main__":
  main()