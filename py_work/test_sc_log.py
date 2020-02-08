import os
from datetime import datetime

def main():
  print("処理開始:" + datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f%z"))

  log_dir = os.environ["LOGDIR"]
  #if log_dir != None :
  print(log_dir)

  print("処理終了:" + datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f%z"))

if __name__ == "__main__":
  main()

