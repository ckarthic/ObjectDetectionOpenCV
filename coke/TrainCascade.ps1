$opencv_traincascade = 'C:\Users\rithanya\Documents\Python\opencv-master\Build\opencv\build\x64\vc15\bin\opencv_traincascade.exe'

& $opencv_traincascade -data cascade4 -vec pos_orig.vec -bg bg.txt -numPos 58 -numNeg 2700 -numStages 10 -w 60 -h 20
