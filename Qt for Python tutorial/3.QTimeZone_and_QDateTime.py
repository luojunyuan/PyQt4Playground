import argparse  # this is a built-in module
import pandas as pd

from qtpy.QtCore import QDateTime, QTimeZone


def transform_data(utc, timezone=None):
    utc_fmt = "yyyy-MM-ddTHH:mm:ss.zzzZ"
    new_date = QDateTime().fromString(utc, utc_fmt)
    if timezone:
        new_date.setTimeZone(new_date)
    return new_date


def read_data(fname):
    """使用panda.read_csv读入csv文件

    :param fname: file name
    :return: 我也不知道read_csv 返回出来是啥，但是这个返回出来的data直接打印就可以以漂亮的table方式呈现
    """
    df = pd.read_csv(fname)

    # filter
    # no attribute 'msg'
    # df = df.drop(df[df.msg < 0].index)
    magnitudes = df['msg']

    timezone = QTimeZone(b'Europe/Berlin')
    times = df['time'].apply(lambda x: transform_data(x, timezone))

    return times, magnitudes


if __name__ == "__main__":
    options = argparse.ArgumentParser()
    options.add_argument("-f", "--file", type=str, required=True)
    args = options.parse_args()
    data = read_data(args.file)
    print(data)
