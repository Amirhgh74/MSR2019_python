import re 
from LineMetric import LineMetric
import pyodbc 
import csv

cnxn = pyodbc.connect("Driver={SQL Server};"
                        "Server=.;"
                        "Database=sotorrent18_09;"
                        "Trusted_Connection=yes;", autocommit=False)

cursor = cnxn.cursor()
cursor.execute("SELECT * FROM [FilteredCodeHistory]")

rows = cursor.fetchall()
line  = 169000
metricResult = []

# with open('finalResult.csv', mode='w', encoding = "utf8" ) as employee_file:
    # java_writer = csv.writer(employee_file, delimiter='~', quotechar='"', quoting=csv.QUOTE_MINIMAL)

for w in rows:
    code = w[4]
    line_count = w[3]
    print ("reading line " , line)
    formatted_code = code.replace("&#xD;&#xA;", "\n\t")

    metric = LineMetric(formatted_code , line_count)
    metricResult.append(metric.num_identifier())
    # print("num identifier")
    metricResult.append(metric.avg_line_length())
    # print("avg line length")
    metricResult.append(metric.avg_accolade())
    # print("accolade")
    metricResult.append(metric.max_line_len())
    # print("max line length")
    metricResult.append(metric.num_periods())
    # print("period")
    metricResult.append(metric.indentaion())
    # print("indentation")
    metricResult.append(metric.avg_keyword())
    # print("keywords")
    metricResult.append(metric.avg_blank_lines())
    # print("blank line")
    metricResult.append(metric.max_indentations())
    # print("max indentation")
    metricResult.append(metric.num_cammas())
    # print("comma")
    metricResult.append(metric.max_identifier_length())
    # print("max length")
    metricResult.append(metric.most_occure_char())
    # print("most accourance")
    metricResult.append(metric.num_comment())
    # print("comment")
    metricResult.append(metric.num_assignments())
    # print("assignment")
    metricResult.append(metric.num_numbers())
    # print("number")
    metricResult.append(metric.num_space())
    # print("space")
    metricResult.append(metric.num_compare())
    # print("compare")
    metricResult.append(metric.branch_number())
    # print("branch")
    metricResult.append(metric.loop_number())
    # print("loop")
    metricResult.append(metric.num_arithmetic_opration())
    # print("arithmatic")


    cursor.execute("INSERT INTO [finalCodeResult](RootBlockId , BlockId , CreationDate , LineCount ,AvgIdentifier  , AvgLineLength,  AvgAccolade  ,MaxLineLength, AvgPeriod, AngIndentation, AvgKeyword, AvgBlankLine, MaxIndentation, AvgComma, MaxIdentifierLength, MostAccouringChar, AvgComment, AvgAssignment, AvgNumber, AvgSpace, AvgCompare, AvgBranch, AvgLoop, AvgArithmatic  , Content)\
    VALUES(?, ?, ?, ?, ?,?, ?, ?, ?, ?,?, ?, ?, ?, ?,?, ?, ?, ?, ?,?, ?, ?, ?, ?)" , (w[0] , w[1] , w[2] , w[3],metricResult[0],metricResult[1],metricResult[2],metricResult[3],metricResult[4],metricResult[5],metricResult[6],metricResult[7],metricResult[8],metricResult[9],metricResult[10],metricResult[11],metricResult[12],metricResult[13],metricResult[14],metricResult[15],metricResult[16],metricResult[17],metricResult[18],metricResult[19]  , w[4]))

    line += 1
    metricResult.clear()

    # java_writer.writerow([w[0] , w[1] , w[2] , w[3],metricResult[0],metricResult[1],metricResult[2],metricResult[3],metricResult[4],metricResult[5],metricResult[6],metricResult[7],metricResult[8],metricResult[9],metricResult[10],metricResult[11],metricResult[12],metricResult[13],metricResult[14],metricResult[15],metricResult[16],metricResult[17],metricResult[18],metricResult[19]  , w[4]])
    if line % 10000 == 0:
        print ("commited " , line)
        cnxn.commit()


cnxn.commit()

print("DONE!")