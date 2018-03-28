$infofile = 'info.data'
$opencv_createsamples = 'C:\Users\rithanya\Documents\Python\opencv-master\Build\opencv\build\x64\vc15\bin\opencv_createsamples.exe'
$numpics = 120


& $opencv_createsamples -info $infofile -num $numpics -vec Pos50.vec -maxxangle 0.6 -maxyangle 0 -maxzangle 0.3 -maxidev 60 -bgcolor 0 -bgthresh 0 -w 50 -h 50 
