import cv2
import sys

# medianBlur関数を実行する関数
def exec_median_blur(img):
    # medianBlur関数 : 画像をぼかす関数
    # 第一引数(必須) : 多次元配列(numpy.ndarray)
    # 第二引数(必須) : n x nの画素領域を指定する。
    # 戻り値 : 多次元配列(numpy.ndarray)
    return cv2.medianBlur(img, 5)

# GaussianBlur関数を実行する関数
def exec_gaussian_blur(img):
    # GaussianBlur関数 : 画像をぼかす関数
    # 第一引数(必須) : 多次元配列(numpy.ndarray)
    # 第二引数(必須) : ぼかすために必要な、n x mの画素領域を指定する。
    # 第三引数(必須) : 画像のx軸(横)方向へのぼかしを調節する値を設定する。
    # 第四引数(任意) : 画像のy軸(縦)方向へのぼかしを調節する値を設定する。
    # 戻り値 : 多次元配列(numpy.ndarray)
    return cv2.GaussianBlur(img, (5, 5), 10, 10)

# blur関数を実行する関数
def exec_blur(img):
    # blur関数 : 画像をぼかす関数
    # 第一引数(必須) : 多次元配列(numpy.ndarray)
    # 第二引数(必須) : ぼかすために必要な、n x mの画素領域を指定する。
    # 戻り値 : 多次元配列(numpy.ndarray)
    return cv2.blur(img, (10, 10))

# imread : 画像ファイルを読み込んで、多次元配列(numpy.ndarray)にする。
# imreadについて : https://kuroro.blog/python/wqh9VIEmRXS4ZAA7C4wd/
# 第一引数 : 画像のファイルパス
# 戻り値 : 行 x 列 x 色の三次元配列(numpy.ndarray)が返される。
img = cv2.imread("sample_median_blur.jpg")

# 画像ファイルが正常に読み込めなかった場合、プログラムを終了する。
if img is None:
    sys.exit("Could not read the image.")

# hconcat : 画像を連結する関数
imgs = cv2.hconcat([img, exec_median_blur(img)])

# imwrite : 画像の保存を行う関数
# 第一引数 : 保存先の画像ファイル名
# 第二引数 : 多次元配列(numpy.ndarray)
# <第二引数の例>
# [
# [
# [234 237 228]
# ...
# [202 209 194]
# ]
# [
# [10 27 16]
# ...
# [36 67 46]
# ]
# [
# [34 51 40]
# ...
# [50 81 60]
# ]
# ]
# imwriteについて : https://kuroro.blog/python/i0tNE1Mp8aEz8Z7n6Ggg/
cv2.imwrite('output_median_blur.jpg', imgs)
