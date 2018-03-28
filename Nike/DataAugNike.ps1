$folderpath = './Train/'
$opencv_createsamples = 'C:\Users\rithanya\Documents\Python\opencv-master\Build\opencv\build\x64\vc15\bin\opencv_createsamples.exe'
$numpics = 11


& $opencv_createsamples -info info_nike_demo.data -num $numpics -vec PosNew.vec -maxxangle 0.6 -maxyangle 0 -maxzangle 0.3 -maxidev 60 -bgcolor 0 -bgthresh 0 -w 20 -h 20 
