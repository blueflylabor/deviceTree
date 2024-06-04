import os.path
import glob
import cv2
def convert(indire,outdir,width=128,height=128):
    #src=cv2.imread(indir,cv2.IMREAD_ANYCOLOR)
    src = cv2.imread(indire,cv2.IMREAD_ANYCOLOR)
    try:
        dst=cv2.resize(src,(width,height),interpolation=cv2.INTER_CUBIC)
        cv2.imwrite(os.path.join(outdir,os.path.basename(indir)),dst)
        #os.path.join()把两个路径连在一起，os.path.basename()是把括号里面的最后一个路径的名字读出来
        #在这儿就是1.JPG这样的，
        #cv2.imwrite(outdir,dst)
    except Exception as e:
        print(e)
indir=r"./imgs_/*.jpg"
outdir=r"./imgs"
for indir in glob.glob(indir):
     convert(indir,outdir)