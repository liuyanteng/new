# -*- coding=utf-8 -*-
import time
from base.baseaction import Baseaction


class HomePageAction(Baseaction):

    # 给 home 模型定义了一个动作，可以实现自动进入首页的操作
    def auto_enter_home(self):

        # 通过强制等待让加载界面消失
        time.sleep( 3 )

        # 执行三次滑屏操作 【因此这个操作具有通用性，所以我们选择将它放置于Base当中】
        self.swipe_left()
