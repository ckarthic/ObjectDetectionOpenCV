$opencv_traincascade = 'C:\Users\rithanya\Documents\Python\opencv-master\Build\opencv\build\x64\vc15\bin\opencv_traincascade.exe'

& $opencv_traincascade -data cascade3 -vec posfrom1.vec -bg bg.txt -numPos 600 -numNeg 150 -numStages 10 -w 50 -h 50
