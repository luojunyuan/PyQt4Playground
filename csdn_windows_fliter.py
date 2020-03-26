
#! /usr/bin/env python 
# -*- coding: utf-8 -*- 
import win32gui
from win32.lib import win32con
from win32gui import *
 
#设置无重复的集
titles = set() 
def foo(hwnd,mouse):  
#判断是不是窗口、是不是可用的、是不是可见的
  if IsWindow(hwnd) and IsWindowEnabled(hwnd) and IsWindowVisible(hwnd):
      #把得到的结果赋值给a
      a=win32gui.GetWindowText(hwnd)
      #打出
    #   print(win32gui.GetWindowText(hwnd))
      #不为空时
      if a!='':      
        #当'Program Manager'不在a内时：
        if 'Program Manager' not in a:
          if '开始' not in a:
              if '管理员' not in a:
                  #关闭窗口
                  pass
                #   win32gui.PostMessage(hwnd, win32con.WM_CLOSE, 0, 0)
                  #最小化窗口
                  #win32gui.ShowWindow(hwnd, win32con.SW_MINIMIZE)
      #把所有的窗口添加到titles集内
      titles.add(GetWindowText(hwnd)) 
 
 
 
# 将软件窗口置于最前
#win32gui.SetForegroundWindow(hwnd)
 
if __name__ == '__main__':
  #枚举所有窗体，同时调用foo函数
  EnumWindows(foo, 0) 
  lt = [t for t in titles if t] 
  lt.sort() 
  for t in lt: 
    print(t)