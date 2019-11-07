import requests
from bs4 import BeautifulSoup
import time
import random
import os

class McqTest:
    def getIntFromChar(self, x):
        diction = {'A':0,'B':1,'C':2,'D':3,'E':4,'F':5}
        rev_diction = {0:'A',1:'B',2:'C',3:'D',4:'E',5:'F'}
        if(type(x) == type(1)):
            return rev_diction.get(x)
        elif(type(x) == type('ABC')):
            x = x.upper()
            return diction.get(x)
        else:
            return -1.0

    def startEvaluation(self, url):
        page = requests.get(url)
        if(page.status_code == 200):
            soup = BeautifulSoup(page.text,'html.parser')
            questions = soup.find_all('div',{'class':'question-main'})
            # for i in questions:
            #     print(i.text)
            #     print()
            findoptions = soup.find_all('div',{'class':'question-inner'})
            temp_ans = []
            for i in range(len(findoptions)):
                temp_ans.append(int(findoptions[i].find('p',{'class':'hidden'}).find('input')['value']) -1)
            
            temp_options = []
            for i in findoptions:
                temp_options.append(i.find_all('label'))
            # print(temp_ans)

            correct_count = 0
            for index in range(len(questions)):
                print(questions[index].text)
                print("=================================")
                for i in range(0,len(temp_options[index]),2):
                    print("{}   {}".format(temp_options[index][i].text,temp_options[index][i+1].text))
                    # print("index i = ",i)
                    # print("index is ",index)
                    # print("len(temp_ans)={} and len(questions)={}".format(len(temp_ans),len(temp_options)))
                print("="*15)

                input_ans = input("Choose Ans: ")
                if(type(input_ans) == type('stirng')):
                    if(temp_ans[index] == self.getIntFromChar(input_ans)):
                        print("Correct")
                        # print(self.getIntFromChar(input_ans))
                        correct_count+= 1
                    else:
                        print("Wrong. Correct Answere is: "+ self.getIntFromChar(temp_ans[index]))

                print("*"*15)
                time.sleep(1)

            print("{}Your Score: {}/{}".format(" "*3,correct_count,len(questions))) 
            
if __name__ == "__main__":
    mcq = McqTest()
    # This two lines are here for debugging purpose
    # pageurl = 'https://www.examveda.com/computer-fundamentals/practice-mcq-question-on-computer-fundamental-miscellaneous/?page={}'.format(5)
    # mcq.startEvaluation(pageurl)
    
    i=0
    x = [i+1 for i in range(14)]
    random.shuffle(x)
    pageurl = 'https://www.examveda.com/computer-fundamentals/practice-mcq-question-on-computer-fundamental-miscellaneous/?page={}'.format(x[i])

    while True:
        # print(pageurl)
        mcq.startEvaluation(pageurl)
        exitorload = input("Load Next Questions?(L/l) Or Exit?(E/e) :")
        if(exitorload == 'e' or exitorload == 'E'):
            break
        elif(exitorload == 'l' or exitorload == 'L'):
            i+=1
            pageurl = pageurl[0:-1]+str(x[i])
        else:
            break
        time.sleep(2)
        os.system("clear")
