# -*- coding: utf-8 -*-

"Combine tests for gnosis.xml.objectify package (req 2.3+)"
from TestPack import *
import unittest
import doctest
import HTMLTestRunner
import sys
sys.path.append("D:\pythonScript\Capitalonline\GIC")


if __name__ == '__main__':

    # suite = unittest.TestSuite()
    suite = doctest.DocTestSuite()
    # 罗列要执行的文件
    suite.addTest(unittest.makeSuite(test_login.Login))
    # suite.addTest(unittest.makeSuite(test_packaging_buy.PackageBuy))
    # suite.addTest(unittest.makeSuite(test_add_gpn.AddGPN))
    # suite.addTest(unittest.makeSuite(test_delete_gpn.DeleteGPN))
    # suite.addTest(unittest.makeSuite(test_delete_public.DeletePublic))
    # suite.addTest(unittest.makeSuite(test_delete_private.DeletePrivate))
    # suite.addTest(unittest.makeSuite(test_delete_vm.DeleteVM))

    filename = "D:\\result34.html"
    print filename
    fp = file(filename, 'wb')

    runner = HTMLTestRunner.HTMLTestRunner(stream=fp,
                                           title=u'测试结果',
                                           description=u'测试报告.')

    runner.run(suite)
