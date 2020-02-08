#! /usr/bin/env python
# -*- coding: utf-8 -*-
import datetime
from datetime import timedelta
import os
import glob

class SOCLogger:
    # ログのタイプ
    INFO = "info"
    WARN = "warn"
    ERR = "err"
    DEF_SCR_NM = "SOCEngine"

    # コンストラクタ
    def __init__(self, log_dir, scr_nm = None): 
        dt_now = datetime.datetime.now()
        ymd = dt_now.strftime('%Y%m%d')
        # プロセスID取得
        self.pid = str(os.getpid())
        if scr_nm != None:
            self.script_nm = scr_nm
        else:
            self.script_nm = self.DEF_SCR_NM

        # ディレクトリ存在チェックをする
        if os.path.isdir(log_dir):
            # ログファイルパスを生成
            self.log_file_path = os.path.join(log_dir, 
                                              'SOC_'+ self.script_nm  + '_' + ymd + '.log') 
            self.is_init = True 
        else:
            self.is_init = False


    # メッセージ書き込み処理
    def write_msg(self, msg, typ = INFO, fnc_nm = None):
        # 初期化処理が失敗している場合は即終了
        if not self.is_init :
            return False

        if fnc_nm == None:
            fnc_nm = self.script_nm

        dt_now = datetime.datetime.now()
        ymd = dt_now.strftime('%Y/%m/%d %H:%M:%S.%f')
        with open(self.log_file_path, mode='a') as f :
            f.write(self.pid + ',' + typ + ',' + fnc_nm + ',' + ymd + ',' + msg + '\n')
    
        return True

    # ファイル書き込み処理
    def write_file(self, file_path, typ = INFO, fnc_nm = None):
        # ファイル存在チェックをする
        if not os.path.isfile(file_path):
            return False
        
        with open(file_path) as f :
            lines = f.read()

        return self.write_msg(lines, typ, fnc_nm)

    # 開始ログ
    def write_start(self, fnc_nm = None):
        return self.write_msg('処理開始', self.INFO, fnc_nm)

    # 正常終了ログ
    def write_normal_end(self, fnc_nm = None):
        return self.write_msg('正常終了', self.INFO, fnc_nm)

    # 異常終了ログ
    def write_abnormal_end(self, fnc_nm = None):
        return self.write_msg('異常終了', self.ERR, fnc_nm)

    # 警告終了ログ
    def write_warning_end(self, fnc_nm = None):
        return self.write_msg('警告終了', self.WARN, fnc_nm)


class SOCLogClearnup:
    LOG_RETENTION_DAYS = "LOG_RETENTION_DAYS"
    DEF_RETENTION_DAYS = 3
    DEF_WILD_CARD = "SOC_*.log"
    @classmethod
    def clearnup(cls, log_dir, wildcard = None):
        # 環境変数を取得
        rt_days = os.getenv(cls.LOG_RETENTION_DAYS)
        if rt_days == None:
            rt_days = cls.DEF_RETENTION_DAYS

        if wildcard == None:
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

