# サロゲートペア文字を扱うサンプルプログラム

# サロゲートを省く関数
def leaveOnlyBMP(s):
  return "".join(filter(lambda c: ord(c) < 0x10000, s))

# サロゲート文字をカウント
def countSurogate(s):
  surogate_chars = list(filter(lambda c: ord(c) >= 0x10000, s))
  return len(surogate_chars)

def main():
  with open("sample.txt", mode="r", encoding="utf-8") as f:
    val = f.read()

    cnt = countSurogate(val)
    print('サロゲート文字数：' + str(cnt))

    chg = leaveOnlyBMP(val)

    print(chg)

if __name__ == "__main__":
  main()
