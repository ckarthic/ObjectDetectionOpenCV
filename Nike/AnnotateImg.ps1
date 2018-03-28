$datafile = 'info_nike_neg.data'
$opencv_annotations = 'C:\Users\rithanya\Documents\Python\opencv-master\Build\opencv\build\x64\vc15\bin\opencv_annotation.exe'
$folderpath = './Nike'


& $opencv_annotations --annotations=$datafile --images=$folderpath
