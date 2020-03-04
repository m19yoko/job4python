import os
import yaml

from comm.sc_logger import SCLogger
from datetime import datetime

def main():
  print("処理開始:" + datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f%z"))

  basedir = os.path.dirname(__file__)
  yml_fil = os.path.join(basedir, "alert/test.query")

  with open(yml_fil, 'r', encoding='UTF-8') as conf:
    cf = yaml.load(conf, Loader=yaml.FullLoader)

#  log_path = os.path.join(cf["LOGDIR"], "SOC_test.log")

  SCLogger.init_logger("SOC_test.py", dirName=cf["LOGDIR"])

  SCLogger.destroy_logger()
  print("処理終了:" + datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f%z"))

if __name__ == "__main__":
  main()
