$opencv_createsamples = 'C:\Users\rithanya\Documents\Python\opencv-master\Build\opencv\build\x64\vc15\bin\opencv_createsamples.exe'
#& $opencv_createsamples -img cokelogo_round.jpg -bg bg.txt -info info/info.data -pngoutput info -maxxangle 0.5 -maxyangle 0.5 -maxzangle 0.5 -num 360
& $opencv_createsamples -img cokelogo_round.jpg -numpics 720 -vec posfrom1.vec -maxxangle 0.6 -maxyangle 0 -maxzangle 0.3 -maxidev 60 -bgcolor 0 -bgthresh 0 -w 50 -h 50 
#& $opencv_createsamples -info info/info.data -num 360 -w 20 -h 20 -vec positives.vec