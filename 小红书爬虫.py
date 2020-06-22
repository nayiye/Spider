#                    _ooOoo_
#                   o8888888o
#                   88" . "88
#                   (| -_- |)
#                   O\  =  /O
#                ____/`---'\____
#              .'  \\|     |//  `.
#             /  \\|||  :  |||//  \
#            /  _||||| -:- |||||-  \
#            |   | \\\  -  /// |   |
#            | \_|  ''\---/''  |   |
#            \  .-\__  `-`  ___/-. /
#          ___`. .'  /--.--\  `. . __
#       ."" '<  `.___\_<|>_/___.'  >'"".
#      | | :  `- \`.;`\ _ /`;.`/ - ` : | |
#      \  \ `-.   \_ __\ /__ _/   .-` /  /
# ======`-.____`-.___\_____/___.-`____.-'======
#                    `=---='
# ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
#             佛祖保佑       永无BUG
# -*- encoding=utf8 -*-
__author__ = "Tom"

from airtest.core.api import *

from poco.drivers.android.uiautomation import AndroidUiautomationPoco

poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)

auto_setup(__file__)
#touch(Template(r"tpl1573194789937.png", record_pos=(0.36, 0.101), resolution=(1080, 1920)))
poco(desc='小红书').click()
#elem = poco(text='郑州')
#elem = poco(name='android.widget.TextView')

title_set = set()
time.sleep(5)

for i in range(3):
    ls = poco(name='com.xingin.xhs:id/qd')
    if not ls.exists():
        break
    for each in ls:
        each.click()
        close_btn_ad = poco(name='android.view.View')
        if close_btn_ad.exists():
            close_btn_ad.click()

        poco.swipe([0.5, 0.8], [0.5, 0.3])
        # 提取标题
        title = poco(name='com.xingin.xhs:id/bdk')
        if title.exists():
            title = title.get_text()
        else:
            title = '空'
        if title == '空' or title not in title_set:
            print('title:', title)

            # 提取昵称
            author = poco(name='com.xingin.xhs:id/nickNameTV')
            if author.exists():
                author = author.get_text()
            else:
                author = poco(name='com.xingin.xhs:id/matrixNickNameView')
                if author.exists():
                    author = author.get_text()
                else:
                    author = '空'
            print('author:', author)

            # 点赞数
            support_nums = poco(name='com.xingin.xhs:id/bd9')
            if support_nums.exists():
                support_nums = support_nums.get_text()
            else:
                support_nums = poco(name='com.xingin.xhs:id/likeTextView')
                if support_nums.exists():
                    support_nums = support_nums.get_text()
                else:
                    support_nums = '空'
            print('support nums:', support_nums)

            # 收藏数
            faviroate_nums = poco(name='com.xingin.xhs:id/bci')
            if faviroate_nums.exists():
                faviroate_nums = faviroate_nums.get_text()
            else:
                faviroate_nums = poco(name='com.xingin.xhs:id/tj')
                if faviroate_nums.exists():
                    faviroate_nums = faviroate_nums.get_text()
                else:
                    faviroate_nums = '空'
            print('faviorte nums:', faviroate_nums)

            # 评论数
            comment_nums = poco(name='com.xingin.xhs:id/bco')
            if comment_nums.exists():
                comment_nums = comment_nums.get_text()
            else:
                comment_nums = poco(name='com.xingin.xhs:id/commentTextView')
                if comment_nums.exists():
                    comment_nums = comment_nums.get_text()
                else:
                    comment_nums = '空'
            print('comment nums:', comment_nums)

            # 笔记内容
            content = poco(name='com.xingin.xhs:id/a3l')
            if content.exists():
                content = content.get_text()
            else:
                content = poco(name='com.xingin.xhs:id/noteContentText')
                if content.exists():
                    content = content.get_text()
                else:
                    content = '空'
            print('content:', content)
            title_set.add(title)
            print('=' * 80)

        back_btn = poco(name='com.xingin.xhs:id/hy')
        if back_btn.exists():
            back_btn.click()
        else:
            back_btn = poco(name='com.xingin.xhs:id/backButton')
            if back_btn.exists():
                back_btn.click()
            else:
                print('error...')

    poco.swipe([0.5, 0.8], [0.5, 0.35])
    poco.swipe([0.5, 0.8], [0.5, 0.4])


