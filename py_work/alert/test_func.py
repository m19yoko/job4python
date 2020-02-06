
from datetime import datetime

def main() :
  print("処理開始:" + datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f%z"))

  yymmdd = "201902041120"

  # ES風の日付に変換
  cht = yymmdd[:4] + "-" + yymmdd[4:6] + "-" + yymmdd[6:8] + "T" + yymmdd[8:10] + ":" + yymmdd[10:12] + "+09:00" 
  # 文字列→日付変換
  dtm = datetime.strptime(yymmdd, '%Y%m%d%H%M%S')

  print(cht)
  print(dtm)

  print("処理終了:" + datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f%z"))  

if __name__ == "__main__":
  main()