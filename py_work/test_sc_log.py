import os
from datetime import datetime
import logging

def getLogger(name, level=logging.INFO, saveName="SOC_base.log"):
  """
  Loggerを作成する。
  name：Loggerの名前（string)
  level:Loggingのレベル(int)
  saveName：Loggerの保存先（string)
  """
  #ロガーの定義
  logger = logging.getLogger(name)
  logger.setLevel(level)
  #フォーマットの定義
  formatter = logging.Formatter("%(asctime)s,%(name)s,%(levelname)s,%(message)s")
  #ファイル書き込み用
  fh = logging.FileHandler(saveName)
  fh.setFormatter(formatter)
  #コンソール出力用
  #sh = logging.StreamHandler()
  #sh.setFormatter(formatter)
  #それぞれロガーに追加
  logger.addHandler(fh)
  #logger.addHandler(sh)
  return logger

def killLogger(logger):
  """
  loggerを削除する
  logger：削除したいロガー(logging.Logger)
  """
  name = logger.name
  del logging.Logger.manager.loggerDict[name]
  
  return

def killhandler(logger, handles):
  """
  loggerから特定のハンドルを削除する
  logger：ハンドルを削除したいロガー(logging.Logger)
  handles：削除したいハンドル(list)
  """
  for handle in handles:
    logger.removeHandler(handle)
      
  return


def main():
  print("処理開始:" + datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f%z"))

  log_dir = os.environ["LOGDIR"]
  #if log_dir != None :
  print(log_dir)
  log_name = log_dir + "/SOC.log"

  logger = getLogger("SOCEngine_log", saveName=log_name)

  logger.info('Hello World!')
  logger.warn('警告発生!')

  killLogger(logger)

  print("処理終了:" + datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f%z"))

if __name__ == "__main__":
  main()

