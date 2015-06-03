import unicodedata


def is_cjk(unichar):
	"""Tests if a character is a sinogram or not"""
	try:
		return unicodedata.name(unichar).find('CJK UNIFIED IDEOGRAPH') >= 0
	except ValueError:
		# A control character 
		return False
	except:
		print(unichar)
		raise


def is_chinese_word(s):
    return all(is_cjk(c) for c in s)
