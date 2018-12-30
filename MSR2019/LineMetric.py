import re
import collections


class LineMetric():

    max_indentation = 0
    sum_indentation = 0
    avg_indentation = 0
    max_line_length = 0
    num_blank_lines = 0
    blank_block_size = 0

    def __init__(self , code_block , number_of_lines):
        self.code = code_block
        self.num_line = number_of_lines

    def avg_line_length(self):
        line_length_sum = 0
        num_blank_lines_block = 0
        max_blank_lines_block = 0
        
        previous_line_blank = False
        block_counted = False

        lines  = self.code.split('\n')

        for line in lines:
            line_len = len(line)
            if (line_len > self.max_line_length):
                self.max_line_length = line_len
            line_length_sum += line_len

            if line.isspace() or line == "":
                self.num_blank_lines += 1
                previous_line_blank = True
                self.blank_block_size += 1 

                if self.blank_block_size > max_blank_lines_block:
                    max_blank_lines_block = self.blank_block_size

            else :
                previous_line_blank = False
                block_counted = False 
                blank_block_size = 0

                if blank_block_size > max_blank_lines_block:
                    max_blank_lines_block = blank_block_size


            if previous_line_blank and not block_counted :
                num_blank_lines_block += 1 
                block_counted = True
            
            avr_line_length = line_length_sum / self.num_line
            num_blank_lines = self.num_blank_lines / self.num_line
        return avr_line_length


    def max_line_len(self):
        line_length_sum = 0
        num_blank_lines_block = 0
        max_blank_lines_block = 0
        
        previous_line_blank = False
        block_counted = False

        lines  = self.code.split('\n')

        for line in lines:
            line_len = len(line)
            if (line_len > self.max_line_length):
                self.max_line_length = line_len
            line_length_sum += line_len

            if line.isspace() or line == "":
                self.num_blank_lines += 1
                previous_line_blank = True
                self.blank_block_size += 1 

                if self.blank_block_size > max_blank_lines_block:
                    max_blank_lines_block = self.blank_block_size

            else :
                previous_line_blank = False
                block_counted = False 
                blank_block_size = 0

                if blank_block_size > max_blank_lines_block:
                    max_blank_lines_block = blank_block_size


            if previous_line_blank and not block_counted :
                num_blank_lines_block += 1 
                block_counted = True
            
            avr_line_length = line_length_sum / self.num_line
            num_blank_lines = self.num_blank_lines / self.num_line
        return self.max_line_length

    def avg_blank_lines(self):
        
        line_length_sum = 0
        
        num_blank_lines_block = 0
        max_blank_lines_block = 0
        
        previous_line_blank = False
        block_counted = False

        lines  = self.code.split('\n')

        for line in lines:
            line_len = len(line)
            if (line_len > self.max_line_length):
                self.max_line_length = line_len
            line_length_sum += line_len

            if line.isspace() or line == "":
                self.num_blank_lines += 1
                previous_line_blank = True
                self.blank_block_size += 1 

                if self.blank_block_size > max_blank_lines_block:
                    max_blank_lines_block = self.blank_block_size

            else :
                previous_line_blank = False
                block_counted = False 
                blank_block_size = 0

                if blank_block_size > max_blank_lines_block:
                    max_blank_lines_block = blank_block_size


            if previous_line_blank and not block_counted :
                num_blank_lines_block += 1 
                block_counted = True
            
            avr_line_length = line_length_sum / self.num_line
            num_blank_lines = self.num_blank_lines / self.num_line
        return num_blank_lines




    def num_periods(self): #worked
        return self.code.count(".") /self.num_line

    def num_cammas(self): #worked
        return self.code.count(",") / self.num_line

    def num_space(self):
        return self.code.count(" ") / self.num_line #worked

    def num_assignments (self):
        return len(re.findall("[^=|>|<](=)[^=]" , self.code , 0)) / self.num_line # worked 

    def num_numbers(self):
        return len(re.findall(r"-?\d+" , self.code , 0))/self.num_line  #worked

    def num_arithmetic_opration (self):
        sum_arith = self.code.count("+") + self.code.count("-") + len(re.findall(r"[^/\*](/)[^/\*]" , self.code , 0)) + len(re.findall(r"[^/\*](\*)[^/\*]" , self.code , 0))  #worked
        return sum_arith/self.num_line

    def num_compare(self):
        sum_compare =  (self.code.count("==") + self.code.count("!=") + len(re.findall(r"[^<]<[^<=]" , self.code , 0)) + len(re.findall(r"[^>]>[^>=]" , self.code , 0)) + len(re.findall(r"[^<]<=[^<=]" , self.code , 0)) + len(re.findall(r"[^>]>=[^>=]" , self.code , 0))) #worked
        return sum_compare / self.num_line

    def num_comment (self):
        # return len(re.findall(r"\/\*([\s\S]*)\*\/", self.code , 0)) #works 
        return self.code.count("/*") + self.code.count("//")/self.num_line

    def branch_number(self): #worked
        return len(re.findall(r"(if\W+)" , self.code , 0))/self.num_line

    def loop_number(self): #worked
        return (len(re.findall(r"(\Wfor\W+)", self.code, 0)) + len(re.findall(r"(\Wwhile\W+)", self.code, 0)))/self.num_line 
    
    def num_println(self): #worked
        return self.code.count(".println(")
    
    def num_return_null(self): #worked
        return len(re.findall(r"(\Wreturn null;\W+)",self.code , 0))

    def num_throws(self): #worked
        return re.findall(r"(\Wthrows\W+)" , self.code, 0)

    def num_identifier(self): #works
        result = []
        keywords = [line.strip() for line in open('java_keywords.txt')]
        words = re.findall(r"[_a-zA-Z][_a-zA-Z0-9]*", self.code, 0)
        for word in words :
            if word not in keywords :
                result.append(word)
        return len(result) / self.num_line
        
    def max_identifier_length(self): #works
        result = []
        keywords = [line.strip() for line in open('java_keywords.txt')]
        words = re.findall(r"[_a-zA-Z][_a-zA-Z0-9]*", self.code, 0)
        for word in words :
            if word not in keywords :
                result.append(word)
        sortedwords = sorted(result, key=len)
        if len(result) == 0:
            return 0
        return len(sortedwords[-1])

    def avg_accolade(self): # number of { and (  --works
        char_dict = collections.Counter(self.code)
        result = char_dict['{']
        result += char_dict['(']
        return result/self.num_line

    def indentaion(self): #works
        indentation = 0
        lines = self.code.split('\n')
        for l in lines :
            for i in range(len(l)):
                if (l[i].isspace()):
                    indentation += 1
                else:
                    if (indentation) > self.max_indentation:
                        self.max_indentation = indentation
                    self.sum_indentation += indentation 
                    indentation = 0
                    break
        self.avg_indentation = self.sum_indentation / self.num_line
        return self.avg_indentation

    def max_indentations (self):
        indentation = 0
        lines = self.code.split('\n')
        for l in lines :
            for i in range(len(l)):
                if (l[i].isspace()):
                    indentation += 1
                else:
                    if (indentation) > self.max_indentation:
                        self.max_indentation = indentation
                    self.sum_indentation += indentation 
                    indentation = 0
                    break
        self.avg_indentation = self.sum_indentation / self.num_line
        return self.max_indentation


    def avg_keyword(self): #works
        words = [line.strip() for line in open('java_keywords.txt')]
        pattern = re.compile(r"\W+")
        word_count = 0
        line_fragments = pattern.split(self.code)
        
        for word in words:
            word_count += line_fragments.count(word)
        return word_count / self.num_line

    def most_occure_char(self): #works
        if self.code != '':
            return collections.Counter(self.code.lower()).most_common(1)[0][1]
        else:
            return 0


str = """
public class Temporary implements Directions 
{ 
	public static void main(String [] args) throws exception
	{
		UrRobot Karel >= new UrRobot(1, 1, East, 0);
		// Deliver the robot to the origin (1 , 1 ),
		// facing East, with no beepers.
		Karel.soon();
		Karel.move();
		if (a > b){
			return null; hhh
		}
		karel.move();
		/* helloo */
        system.println(folan)
		Karel.move(); 
		if (a < b ){
			if (folan dg){
                2+3;
                4 - 5 ;
                5 * 6 ;
                6 / 7 ;
			}
		}
        while (true){

        }
        /* another folan */
        for(i = 0; i < 10 ; i++){
            return null;
        }
		Karel.pickBeeper(); // some comment
		// Karel.turnOff();
        System.println(folan) /* some comment */
	}


    public void folan() throws another exception {
        // do something
    }
	
}
"""

str2 = """aaaaAARRTTeerAAAaWwwweeAssieueAAA"""

mml = LineMetric(str , 31)
print (mml.num_comment() )
