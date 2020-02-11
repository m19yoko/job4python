#! /usr/bin/env python
# -*- coding: utf-8 -*-
from datetime import timedelta
from datetime import datetime
import os
import glob
import logging


class SCLogger:
  logger = None

  @classmethod
  def init_logger(cls, name, level=logging.INFO, dirName="./"):
    """
    Loggerを作成する。
    name：Loggerの名前（string)
    level:Loggingのレベル(int)
    logBaseName：Loggerのファイル名(SOC_xxx_yyyymmdd.logのxxxの部分)
    """
    #ロガーの定義
    cls.logger = logging.getLogger(name)
    cls.logger.setLevel(level)
    #フォーマットの定義
    formatter = logging.Formatter("%(process)d,%(asctime)s,%(levelname)s,%(name)s:%(message)s")
    #ファイル書き込み用
    saveName = "SOC_" + name + datetime.now().strftime("_%Y%m%d") + ".log"
    saveName = os.path.join(dirName, saveName)
    fh = logging.FileHandler(saveName)
    fh.setFormatter(formatter)
    #コンソール出力用
    #sh = logging.StreamHandler()
    #sh.setFormatter(formatter)
    #それぞれロガーに追加
    cls.logger.addHandler(fh)
    
    return

  @classmethod
  def destroy_logger(cls):
    """
    loggerを削除する
    logger：削除したいロガー(logging.Logger)
    """
    name = cls.logger.name
    del logging.Logger.manager.loggerDict[name]
    
    return

  @classmethod
  def writeInfo(cls, func_name="", msg="Info Message"):
    """
    Infoメッセージを書き込む
    func_name：関数名
    msg：メッセージ
    """
    cls.logger.info(func_name + ":" + msg)
    return

  @classmethod
  def writeWarn(cls, func_name="", msg="Warn Message"):
    """
    警告メッセージを書き込む
    func_name：関数名
    msg：メッセージ
    """
    cls.logger.warning(func_name + ":" + msg)
    return

  @classmethod
  def writeErr(cls, func_name="", msg="Err Message"):
    """
    エラーメッセージを書き込む
    func_name：関数名
    msg：メッセージ
    """
    cls.logger.error(func_name + ":" + msg)
    return

class SCLogClearnup:
  DEF_RETENTION_DAYS = 3
  DEF_WILD_CARD = "SOC_*.log"
  @classmethod
  def clearnup(cls, log_dir, wildcard = None):
    
    rt_days = cls.DEF_RETENTION_DAYS      
    wildcard = cls.DEF_WILD_CARD

    # ディレクトリ存在チェックをする
    if not os.path.isdir(log_dir):
      return None

    # 末尾がスラッシュでない場合はつける
    if log_dir[-1] != '/':
      log_dir += '/'

    del_file_nm = []
    dt_now = datetime.datetime.now()
    # 削除の閾日時を求める
    limit_time = dt_now - timedelta(days=int(rt_days))
    # ワイルドカードに一致するファイルを取得
    flist =  glob.glob(log_dir + wildcard)
    for f in flist:
      up_time = datetime.datetime.fromtimestamp(os.stat(f).st_mtime)
      if up_time < limit_time:
        del_file_nm.append(f)
        os.remove(f)    

    return del_file_nm


def pickup_para_dict(key, val):
  return key + '=' + val

def pickup_para(i, val):
  return '引数' + str(i+1) + f' {val}'


# クラス用デコレータ
def SCLogWriteCL(func):
  def wrapper(*args, **kwargs):
    msg = ""
    arg_l = list(args[1:])
    para_lst = [ pickup_para(i, v) for i, v in enumerate(arg_l) ]
    if len(para_lst) != 0 :
      msg = " ".join(para_lst)

    key_para_lst = [ pickup_para_dict(k, v) for k, v in kwargs.items() ]
    if len(key_para_lst) != 0 :
      msg += " ".join(key_para_lst)

    SCLogger.logger.info(func.__name__ + ':処理開始 ' + msg)

    ret = func(*args, **kwargs)
    if ret != None :
      SCLogger.logger.info(func.__name__ + ':処理終了 戻り値：'+ str(ret))
      return ret
    else :  
      SCLogger.logger.info(func.__name__ + ':処理終了')
  return wrapper


# クラス以外用デコレータ
def SCLogWrite(func):
  def wrapper(*args, **kwargs):
    msg = ""
    arg_l = list(args)
    para_lst = [ pickup_para(i, v) for i, v in enumerate(arg_l) ]
    if len(para_lst) != 0 :
      msg = " ".join(para_lst)

    key_para_lst = [ pickup_para_dict(k, v) for k, v in kwargs.items() ]
    if len(key_para_lst) != 0 :
      msg += " ".join(key_para_lst)

    SCLogger.logger.info(func.__name__ + ':処理開始 ' + msg)

    ret = func(*args, **kwargs)
    if ret != None :
      SCLogger.logger.info(func.__name__ + ':処理終了 戻り値：'+ str(ret))
      return ret
    else :  
      SCLogger.logger.info(func.__name__ + ':処理終了')
  return wrapper
