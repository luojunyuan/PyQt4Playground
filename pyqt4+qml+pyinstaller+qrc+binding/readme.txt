see: https://gist.github.com/fyears/673b2d763720f3c26256

I changed pyside to pyqt4

there has a error
`QNetworkAccessFileBackendFactory: URL has no schema set, use file:// for files`
add 'file:///' before absolute path to fix it

---

there is a error when I build it 
```
---------------------------
Fatal error detected
---------------------------
Failed to execute script main

---------------------------
确定   
---------------------------
```

add `import PyQt4.QtNetwork` in main.py to fix it 

Now run `generate.cmd`
the exe file goes well!
