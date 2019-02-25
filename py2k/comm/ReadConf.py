#! /usr/bin/env python
# -*- coding: utf-8 -*-

# コンフィグファイル読込処理クラス
class ReadConf:
	COMMENT = ';'

	@classmethod
	def read_val(cls, cnf_path, session, key_nm):
		with open(cnf_path) as f:
			# 各要素内の改行キーを落とす
			lines = [l.strip() for l in f.readlines()]

		is_target = False
		for line in lines:
			if len(line) == 0:
				continue

			if line[0] == cls.COMMENT:
				continue

			# セミコロンより後ろは切り捨てる
			cm_pos = line.find(cls.COMMENT)
			if cm_pos != -1:
				line = line[:cm_pos].strip()

			if not is_target:
				if cls.is_target_session(session, line):
					is_target = True
			else:
				val = cls.get_key_val(key_nm, line)
				if val != None:
					return val

		return None

	# 該当行が指定されたsession行かどうか
	@classmethod
	def is_target_session(cls, session, dest):
		if dest == '[' + session + ']':
			return True
		else:
			return False

	
	# 該当行がsession行かどうか
	@classmethod
	def is_session(cls, dest):
		if dest[0] == '[' and dest[-1] == ']':
			return True
		else:
			return False

	# 該当キーの行ならば、値を返す。それ以外はNoneを返す
	@classmethod
	def get_key_val(cls, key_nm, dest):
		if (dest.startswith(key_nm + '=')):
			pos = dest.find('=')
			return dest[pos+1:]
		else:
			return None
		

