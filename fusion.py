import glob
import sys
from PIL import Image, ImageDraw, ImageFilter

def main():
    #引数読み込み
    args = importArgs()
    #フォルダ位置パス
    directory_path = "./sourceImage/*." + args[1]
    #全画像読み込み
    images = importImages(directory_path)
    #画像合成
    outImage = imageSynthesis(images)
    #画像保存
    saveImage(outImage, args)

def importArgs():
    tmp = sys.argv
    if (len(tmp) < 2):
        print("引数が足りません、第一引数にファイルタイプを記入してください。")
        print("例) >python3 fusion.py png")
        sys.exit(1)
    elif (len(tmp) > 2):
        print("引数が多すぎます。以下のように記入してください。")
        print("例) >python3 fusion.py png")
        sys.exit(1)
    else:
        return tmp

def importImages(directory_path):
    return glob.glob(directory_path)

def imageSynthesis(images):
    tmpImage = []
    for image in images:
        tmp = Image.open(image)
        tmp = tmp.convert('RGBA')
        tmpImage.append(tmp)
    if (len(tmpImage) < 2):
        print("このプログラムを利用するには（sourceImage）フォルダの中に少なくとも2枚の、先程指定された種類の画像を用意する必要があります")
        sys.exit(1)
    im = tmpImage[0]
    for i in range(len(tmpImage)):
        if i == 0:
            continue
        cal = 1 / (i + 1)
        im = Image.blend(im, tmpImage[i], cal)
        pr = int(int(i)/len(tmpImage) * 100)
        print("Progress:" + str(pr) + "% - " + "■" * pr )
    print("Progress:100% - " + "■" * 100)
    return im

def saveImage(outImage, args):
    outImage.save('./outputImage/result.' + args[1], quality=95)
    print("completed")



if __name__ == '__main__':
    main()