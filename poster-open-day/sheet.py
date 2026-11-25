import sys,glob
from PIL import Image, ImageOps, ImageDraw
fs=sorted(sys.argv[2:]); W=360
ims=[(f,ImageOps.exif_transpose(Image.open(f))) for f in fs]
for _,im in ims: im.thumbnail((W,W))
cols=6; rows=(len(ims)+cols-1)//cols
sheet=Image.new('RGB',(cols*W,rows*(W+24)),'white'); d=ImageDraw.Draw(sheet)
for i,(f,im) in enumerate(ims):
    x=(i%cols)*W; y=(i//cols)*(W+24); sheet.paste(im,(x,y)); d.text((x+5,y+W+5),f.split('/')[-1],fill='black')
sheet.save(sys.argv[1],quality=75)
