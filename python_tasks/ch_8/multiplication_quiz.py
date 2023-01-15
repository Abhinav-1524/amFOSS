import pyinputplus as pyip
import random, time
numberOfQuestions = 10
correctAnswers = 0
for i in range (1,numberOfQuestions+1):
    num1 = random.randint(0, 9)
    num2 = random.randint(0, 9)
    print('question no:',i ,' = ', num1, '*' ,num2)
    try:
        pyip.inputStr( allowRegexes=['^%s$' % (num1 * num2)],blockRegexes=[('.*', 'Incorrect!')],timeout=8, limit=3)    
    except pyip.TimeoutException:
        print('out of time')
    except pyip.RetryLimitException:
        print('out of tries')
    else:
        print('Correct!')
        correctAnswers += 1
    time.sleep(1) 
print('Score: ' , correctAnswers ,'/', numberOfQuestions)

