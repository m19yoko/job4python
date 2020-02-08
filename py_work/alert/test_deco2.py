# デコレータテスト用(クラス版)
import test_deco as tdc

class deco_test :
  @tdc.deco_cls
  def __init__(self, msg=None):
      if msg:
        self.__in_msg = msg
      else:
        self.__in_msg = "Nooon"

  @tdc.deco_cls
  def disp_msg(self, msg, msg2) :
    print('Message in ' + msg + ' ' + msg2)

  @tdc.deco_cls
  def disp_in_msg(self):
    print("In Message " + self.__in_msg)

  # クラスメソッドのデコレータを先に書く
  @classmethod
  @tdc.deco_cls
  def static_disp(cls, msg):
    print("Static disp " + msg)


def main():
  c = deco_test()
  c.disp_msg("dududu", 'dadada')

  c2 = deco_test("init string!")
  c2.disp_in_msg()

  deco_test.static_disp("あかさたな")

if __name__ == "__main__":
  main()
