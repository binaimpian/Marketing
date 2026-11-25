import numpy as np, sys
from PIL import Image, ImageOps, ImageFilter
from scipy import ndimage
for name in sys.argv[1:]:
    im=ImageOps.exif_transpose(Image.open(f'team-raw/{name}.JPG')).convert('RGB')
    im.thumbnail((2000,2000), Image.LANCZOS)
    a=np.asarray(im).astype(np.float32)
    r,g,b=a[...,0],a[...,1],a[...,2]
    mx=np.maximum(r,b); gd=g-mx; ratio=g/(mx+1)
    alpha=1-np.clip((ratio-1.06)/0.12,0,1)*np.clip((gd-4)/12,0,1)
    fg=alpha>0.5
    lab,n=ndimage.label(fg)
    sizes=ndimage.sum(fg,lab,range(1,n+1))
    keep=lab==(np.argmax(sizes)+1)
    keep=ndimage.binary_fill_holes(keep)
    keep=ndimage.binary_dilation(keep,iterations=3)
    alpha=alpha*keep
    lim=np.maximum(r,b)
    g2=np.where(g>lim,lim+(g-lim)*0.15,g)
    out=np.dstack([r,g2,b,alpha*255]).clip(0,255).astype(np.uint8)
    o=Image.fromarray(out,'RGBA')
    A=o.split()[3].filter(ImageFilter.GaussianBlur(1.2)); o.putalpha(A)
    o=o.crop(o.getbbox())
    o.save(f'team-cut/{name}.png'); print(name,o.size)
