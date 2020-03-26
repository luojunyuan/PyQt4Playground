# native
# from PyQt4.QtCore import QT_VERSION, QT_VERSION_STR, PYQT_VERSION, PYQT_VERSION_STR
# from sip import SIP_VERSION, SIP_VERSION_STR
#
# if __name__ == '__main__':
#     print(f"PyQt Version Number is: {PYQT_VERSION_STR} ({PYQT_VERSION})")
#     print(f"Qt Version is: {QT_VERSION_STR} ({QT_VERSION})")
#     print(f"Sip Version Number is: {SIP_VERSION_STR} ({SIP_VERSION})")

from PySide.QtCore import __version__, __version_info__, qVersion

if __name__ == '__main__':
    print(__version__)
    print(__version_info__)
    print(qVersion())

# import sys
# import os
# os.environ['QT_API'] = 'PyQt4'
# from qtpy.QtCore import *
# from qtpy.QtGui import *
# from qtpy.QtWidgets import *
# from sip import SIP_VERSION
#
# if __name__ == '__main__':
#     # I think I should to see the source code of qtpy
#     print(f"PyQt Version Number is: {PYQT_VERSION})")
#     print(f"Qt Version is: {QT_VERSION})")
#     print(f"Sip Version Number is: {SIP_VERSION}")
