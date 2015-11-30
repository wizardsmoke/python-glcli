
import os

FORMATS = [['.po', 'gettext'],
           ['.properties', 'javaproperties'],
           ['.ini', 'ini'],
           ['.json', 'js'],
           ['.resx', 'resx'],
           ['.xml', 'xliff'],
           ['.ts', 'qt'],
           ['.xliff', 'xliff'],
           ['.js', 'js'],
           ['.php', 'phparray'],
           ['.docx', 'docx'],
           ['.txt', 'plain'],
           ['.yml', 'ruby'],
           ['.strings', 'ios']
          ]

def autodetect_fileformat(filename):
    fileName, fileExt = os.path.splitext(os.path.basename(filename))
    
    if fileName == 'strings' and fileExt == '.xml':
        return 'android'
    
    for format in FORMATS:
        if format[0] == fileExt:
            return format[1]
        
    
    
