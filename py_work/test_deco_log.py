import os
import sys
import yaml
from comm.sc_logger import SCLogger
import comm.sc_logger as scl
from datetime import datetime

@scl.SCLogWrite
def test(msg):
  msg2 = 'Hello Decorator ' + msg
  print(msg2)
  scl.SCLogger.writeInfo(sys._getframe().f_code.co_name, msg2)

@scl.SCLogWrite
def test2(typ, msg=None):
  print('タイプ ' + typ)
  if msg:
    print('メッセージ ' + msg)

class deco_test :
  @scl.SCLogWriteCL
  def __init__(self, msg=None):
      if msg:
        self.__in_msg = msg
      else:
        self.__in_msg = "Nooon"

  @scl.SCLogWriteCL
  def disp_msg(self, msg, msg2) :
    print('Message in ' + msg + ' ' + msg2)

  @scl.SCLogWriteCL
  def disp_in_msg(self):
    print("In Message " + self.__in_msg)

  @scl.SCLogWriteCL
  def msg_rtn(self, msg) -> str:
    retmsg = "return value " + msg
    return retmsg

  # クラスメソッドのデコレータを先に書く
  @classmethod
  @scl.SCLogWriteCL
  def static_disp(cls, msg):
    print("Static disp " + msg)


def main():
  print("処理開始:" + datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f%z"))

  basedir = os.path.dirname(__file__)
  yml_fil = os.path.join(basedir, "alert/test.query")

  with open(yml_fil, 'r', encoding='UTF-8') as conf:
    cf = yaml.load(conf, Loader=yaml.FullLoader)

  SCLogger.init_logger("test_deco", dirName=cf["LOGDIR"])

  test("テストメッセージ")

  tc1 = deco_test()
  tc1.disp_msg("aaa", "bbb")

  tc2 = deco_test("construct para")
  tc2.disp_in_msg()
  rt = tc2.msg_rtn("あああ")
  print(rt)

  SCLogger.destroy_logger()
  print("処理終了:" + datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f%z"))

if __name__ == "__main__":
  main()
