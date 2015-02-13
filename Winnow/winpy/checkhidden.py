"""
Functions to detect if something is meant to be isHidden
"""


import ctypes, os


def isHidden(filepath):
    name = os.path.basename(os.path.abspath(filepath))
    return name.startswith('.') or hasHiddenAttribute(filepath)


def hasHiddenAttribute(filepath):
    try:
        attrs = ctypes.windll.kernel32.GetFileAttributesW(unicode(filepath))
        assert attrs != -1
        result = bool(attrs & 2)
    except (AttributeError, AssertionError):
        result = False
    return result


def checkList(check):
	test = list()
	for each in check:
		if not isHidden(each):
			test.append(each)
	return test