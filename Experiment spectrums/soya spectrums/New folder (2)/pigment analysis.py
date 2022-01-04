import pylab, numpy
from PIL import Image

im = Image.open('04.jpg') 
pix = im.load()
im_width, im_height=im.size
wl_offset=348.0
wl_maxed=702
wl_range=wl_maxed-wl_offset
wl_p_pix=wl_range/im_width

x_all=[]
y_all=[]
    
for i in range(0,im_width):      
    x_sum=0.0
    for j in range(0,im.height):      
            x_sum+=sum(pix[i,j])   
            
    x_all.append(i*wl_p_pix+wl_offset)
    y_all.append(x_sum)
    
y_max=max(y_all)
y_all=numpy.array(y_all,dtype='f')
y_trans=y_all/y_max
y_abs=1-y_trans
index_max=numpy.where(y_abs==max(y_abs))
index_max=numpy.array(index_max,dtype='i')
index_max=index_max*wl_p_pix+wl_offset
    


pylab.plot(x_all, y_abs, c='blue', linewidth=2.0)

## for chlorophyll b
brbmax = 480
brbmin = 460

rrbmax = 655
rrbmin = 635


## for chlorophyll a
bramax = 420
bramin = 440

rramax = 657
rramin = 677

## for carotenoid
cmax1 = 450
cmin1 = 460

cmax2 = 480
cmin2 = 488

cmax3 = 560
cmin3 = 570

pylab.axvspan(brbmin, brbmax, color='lightblue', alpha=0.5, label= 'Chl b' )
pylab.axvspan(rrbmin, rrbmax, color='lightblue', alpha=0.5,)

pylab.axvspan(bramin, bramax, color='lightgreen', alpha=0.5, label= 'Chl a' )
pylab.axvspan(rramin, rramax, color='lightgreen', alpha=0.5,)

pylab.axvspan(cmin1, cmax1, color='lightsalmon', alpha=0.5, label= 'Carotenoids' )
pylab.axvspan(cmin2, cmax2, color='lightsalmon', alpha=0.5,)
pylab.axvspan(cmin3, cmax3, color='lightsalmon', alpha=0.5,)


pylab.xlabel('Wavelength (nm)', fontsize = 16)
pylab.ylabel(' Relative Absorbance', fontsize = 16)
pylab.savefig('Bigleaf.png')

lgg = pylab.legend(bbox_to_anchor=(1.05, 1.0), loc='center',prop={'size': 8})
pylab.savefig('pigment analyzed.jpeg',
            dpi=300, 
            format='jpeg', 
            bbox_extra_artists=(lgg,),
            bbox_inches='tight')

pylab.show()
