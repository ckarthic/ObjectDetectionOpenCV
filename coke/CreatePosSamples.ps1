$opencv_createsamples = 'C:\Users\rithanya\Documents\Python\opencv-master\Build\opencv\build\x64\vc15\bin\opencv_createsamples.exe'
#& $opencv_createsamples -img Source/logo_round/1.jpg -bg bg_trunc.txt -info info/info_round.data -pngoutput info -maxxangle 0 -maxyangle 0 -maxzangle 0 -num 2226
#& $opencv_createsamples -img cokelogo_round.jpg -numpics 720 -vec posfrom1.vec -maxxangle 0.6 -maxyangle 0 -maxzangle 0.3 -maxidev 60 -bgcolor 0 -bgthresh 0 -w 50 -h 50 
& $opencv_createsamples -info info_pos_orig.data -num 58 -w 60 -h 20 -vec pos_orig.vec -show