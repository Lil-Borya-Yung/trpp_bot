import random
import time


'''startAnswer'''
startAnswer = 'Привет, {0.first_name}! Меня зовут Бен. Спроси у меня что-нибудь)'

benAnswers = [['Хо-хо-хо', 'answers/ho-ho.gif'],['Беееее','answers/bee.gif'], ['Нет.','answers/no.gif'], ['Да.','answers/yes.gif']]
def benTotalAnswer():
    random.seed(time.time())
    return random.choice(benAnswers)

benPhrases = ['Текст...','Мда...','Треш']
def benTotalPhrase():
    random.seed(time.time())
    return random.choice(benPhrases)
benGreetings = ['Привет, привет!!!', 'Салют!','Здравия желаю']
def benTotalGreetings():
    random.seed(time.time())
    return random.choice(benGreetings)
# benMood = ['Хорошо)', 'Не очень =(']

benGenGavs = ['По приказу Генерала Гавса! Ваш компаньон Бенджамин прибыл на службу!',
              'Да... Генерал Гавс мой непосредственный командир, я готов служить ему вечность!',
              'Если речь о Бравл Старс, то мой любимый герой это Генерал Гавс']
def benTotalGenGavs():
    random.seed(time.time())
    return random.choice(benGenGavs)

benGenGavs_IMG = ['gavs/1gavs.png','gavs/2gavs.png','gavs/3gavs.jpg']
#benTotalGenGavs_IMG = lambda : open(random.choice(benGenGavs_IMG),'rb')
