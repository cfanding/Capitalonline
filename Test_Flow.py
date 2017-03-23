# -*- coding: utf-8 -*-

"Combine tests for gnosis.xml.objectify package (req 2.3+)"
import unittest
import HTMLTestRunner
import sys
# 调用数组文件
import allcase_list
sys.path.append("D:\pythonScript\Capitalonline\GIC")


# 获取数组方法
alltestnames = allcase_list.caselist()


suite = unittest.TestSuite()
if __name__ == "__main__":
    # 这里我们可以使用 defaultTestLoader.loadTestsFromNames(),
    # 但如果不提供一个良好的错误消息时，它无法加载测试
    # 所以我们加载所有单独的测试，这样将会提高脚本错误的确定。
    for test in alltestnames:
        try:
            # 最关键的就是这一句，循环执行数据数的里的用例。
            suite.addTest(unittest.defaultTestLoader.loadTestsFromName(test))
        except Exception as error:
            print 'ERROR: Skipping tests from "%s".' % test
            try:
                __import__(test)
            except ImportError:
                print 'Could not import the test module.'
            else:
                print 'Could not load the test suite.'
            from traceback import print_exc
            print_exc()
    print
    print 'Running the tests...'

    filename = 'D:\\result25.html'
    print filename
    fp = file(filename, 'wb')

    runner = HTMLTestRunner.HTMLTestRunner(stream=fp,
                                           title=u'测试标题',
                                           description=u'测试结果详细报告')

    runner.run(suite)
