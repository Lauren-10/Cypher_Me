import re
import urllib.request
string_roman = ""
with open("EulerP/roman.txt", 'r') as file:
    for line_number, line in enumerate(file, 1):
        string_roman = string_roman + line

print (len(string_roman) - len(re.sub("DCCCC|LXXXX|VIIII|CCCC|XXXX|IIII", '**', string_roman)))