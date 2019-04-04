__author__ = "Moath Maharmeh"
__license__ = "GNU General Public License v2.0"
__version__ = "1.0"
__email__ = "moath@vegalayer.com"
__created__ = "4/Apr/2019"
__modified__ = "4/Apr/2019"
__status__ = "Production"
__project_page__ = "https://github.com/iomoath/yara-scanner"

import os
import common_functions

report_element = """
    <tr>
        <td align="center">
           <font face="Arial, Helvetica, sans-serif">%INDEX%</font>
        </td>
        <td align="center">
           <font face="Arial, Helvetica, sans-serif">%FILE_PATH%</font>
        </td>
        <td align="center">
           <font face="Arial, Helvetica, sans-serif">%MATCHES%</font>
        </td>
        <td align="center">
           <font face="Arial, Helvetica, sans-serif">%YARA_RULES_FILE_NAME%</font>
        </td>
    </tr>
"""

report_template = """
<html>
   <head>
      <title>%REPORT_TITLE% - %REPORT_DATE_TIME%</title>
      <style>
         table
         {
         border-bottom: 1px Solid Black;         
         border-right: 1px Solid Black;         
         border-collapse : collapse;  
         }
         table td, table th  
         {    
         border-left: 1px Solid Black;         
         border-top: 1px Solid Black;              
         border-bottom:none;    
         border-right:none;
         max-width: 550px;
         word-wrap: break-word;
         }
      </style>
   </head>
   <body>
      <center>
         <h2>%REPORT_TITLE%</h2>
         <h3>%REPORT_DATE_TIME%</h3>
         <table border="1" cellspacing="2" cellpadding="2">
            <tr>
               <td align="center", style="font-weight: bold;">
                  <font face="Arial, Helvetica, sans-serif"></font>
               </td>
               <td align="center", style="font-weight: bold;">
                  <font face="Arial, Helvetica, sans-serif">File Path</font>
               </td>
               <td align="center", style="font-weight: bold;">
                  <font face="Arial, Helvetica, sans-serif">Rules Matched</font>
               </td>
               <td align="center", style="font-weight: bold;">
                  <font face="Arial, Helvetica, sans-serif">Yara Rules</font>
               </td>
            </tr>
               %TABLE_CONTENT%
         </table>
      </center>
   </body>
</html>
"""

def yara_match_list_to_string(yara_mathes):
    text = ''
    for x in yara_mathes:
        text += str(x) + ', '

    text = text.rstrip(' ')
    text = text.rstrip(',')
    text = '[{}]'.format(text)
    return text

def generate_report(matches_list):
    """
      Generates an html report for files that has a match with Yara-Rules
      :param matches_list: list of dictionaries containing match details for each file. example {"file": file_path, "yara_rules_file": rule_path, "match_list": matches}
      :return: list of dictionaries containing match details for each file
      """
    report_title = 'YaraScanner - Scan Report'
    report_datetime = common_functions.get_datetime()

    report = report_template.replace('%REPORT_TITLE%', report_title)
    report = report.replace('%REPORT_DATE_TIME%', report_datetime)

    table_content = ""

    index = 1
    for match in matches_list:
        if match is None:
            continue

        element = report_element.replace('%INDEX%', str(index))
        element = element.replace('%FILE_PATH%', match['file'])

        matches_str =  yara_match_list_to_string(match['match_list'])

        rule_file_name = ''
        if os.path.isfile(match['yara_rules_file']):
            rule_file_name = os.path.basename(match['yara_rules_file'])


        element = element.replace('%MATCHES%', matches_str)
        element = element.replace('%YARA_RULES_FILE_NAME%', rule_file_name)
        table_content += element
        index += 1

    report = report.replace('%TABLE_CONTENT%', table_content)
    return report