"""
@Time  : 2024/2/21
@Author: panpan.fang@shopee.com
@File  : 5KeyKeyboard.py
@IDE   : PyCharm
5、标题:5键键盘的输出
    【5键键盘的输出】有一个特殊的 5键键盘，上面有 a,ctrl-c,ctrl-x,ctrl-v,ctrl-a五个键。
    a键在屏幕上输出一个字母 a;                            ---取决于有没有字母被选择：已有字母被选择，则屏幕为a；否则，则屏幕追加a
    ctrl-c将当前选择的字母复制到剪贴板;                    ---取决于有没有字母被选择，屏幕字母保持不变，剪贴板赋值
    ctrl-x将当前选择的 字母复制到剪贴板，并清空选择的字母;    ---取决于有没有字母被选择，屏幕字母清空，剪贴板赋值
    ctrl-v将当前剪贴板里的字母输出到屏幕;                   ---取决于有没有字母被选择：已有字母被选择，则屏幕为剪贴板的内容；否则，屏幕追加剪贴板的内容
    ctrl-a 选择当前屏幕上所有字母。                        ---取决于屏幕上有没有字母，有则有字母被选择；否则，没有字母被选择
注意:
    1、剪贴板初始为空，新的内容被复制到剪贴板时会覆盖原来的内容
    2、当屏幕上没有字母时，ctrl-a无效
    3、当没有选择字母时，ctrl-c和 ctrl-x无效
    4、当有字母被选择时，a和ctrl-v这两个有输出功能的键会先清空选择的字母，再进行输出
给定一系列键盘输入，输出最终屏幕上字母的数量。
输入描述:
    输入为一行，为简化解析，用数字 12345代表 a,ctrl-c,ctrl-x,ctrl-v,ctrl-a五个键的输入，数字用空格分隔
输出描述:
    输出一个数字，为最终屏目上字母的数量。
示例:
输入
111
输出
3
"""
class Solution:
    def test5KeyKeyboard(self,s: str):
        screen = ""
        clipboard = ""
        selected = False
        for i in s:
            if i == "1" and selected is True:
                screen = "a"
            elif i == "1" and selected is False:
                screen += "a"
            elif i == "2" and selected is True:
                clipboard = screen
            elif i == "3" and selected is True:
                clipboard = screen
                screen = ""
                selected = False
            elif i == "4" and selected is True:
                screen = clipboard
                selected = False
            elif i == "4" and selected is False:
                screen += clipboard
            elif i == "5" and screen:
                selected = True

        return print(len(s))

Solution().test5KeyKeyboard("11515244")