$opencv_traincascade = 'C:\Users\rithanya\Documents\Python\opencv-master\Build\opencv\build\x64\vc15\bin\opencv_traincascade.exe'

& $opencv_traincascade -data cascade -vec Pos.vec -bg Negative.txt -numPos 11 -numNeg 12 -numStages 10 -w 20 -h 20
