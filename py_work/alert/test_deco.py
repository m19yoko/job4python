# デコレータテスト用

def disp_para_dict(key, val):
  print(key + '=' + val)

def disp_para(i, val):
  print('引数' + str(i+1) + f' {val}')

def disp_para_cls(i, val):
  if i > 0 :
    print('引数' + str(i) + f' {val}')

# クラス用デコレータ
def deco_cls(func):
  def wrapper(*args, **kwargs):
    print(func.__name__ + '--start--')
    arg_l = list(args[1:])
    [ disp_para(i, v) for i, v in enumerate(arg_l) ]
    [ disp_para_dict(k, v) for k, v in kwargs.items() ]
            
    func(*args, **kwargs)
    print(func.__name__ + '--end--')
  return wrapper

def deco(func):
  def wrapper(*args, **kwargs):
    print(func.__name__ + '--start--')
    arg_l = list(args)
    [ disp_para(i, v) for i, v in enumerate(arg_l) ]
    [ disp_para_dict(k, v) for k, v in kwargs.items() ]
            
    func(*args, **kwargs)
    print(func.__name__  + '--end--')
  return wrapper

@deco
def test(msg):
  print('Hello Decorator ' + msg)

@deco
def test2(typ, msg=None):
  print('タイプ ' + typ)
  if msg:
    print('メッセージ ' + msg)


def main() :
  test("あああ")

  test2("Type-C")

  test2("Type-D", "あかさたな")
  test2("Type-E", msg="aiueo")

if __name__ == "__main__" :
  main()    