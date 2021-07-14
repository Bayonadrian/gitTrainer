from enum import Enum
import os.path as path

startPath = path.realpath('gitManual/markdowns/basics/start.md')
quickstartPath = path.realpath('gitManual/markdowns/basics/quickstart.md')
stepOne = path.realpath('gitManual/markdowns/basics/stepOne.md')
stepTwo = path.realpath('gitManual/markdowns/basics/stepTwo.md')
stepTree = path.realpath('gitManual/markdowns/basics/stepTree.md')
stepFour = path.realpath('gitManual/markdowns/basics/stepFour.md')
stepFive = path.realpath('gitManual/markdowns/basics/stepFive.md')

class basics(Enum):

    with open(startPath, 'r') as start:

        START = start.read()
        GIT = 'Por cierto si no sabes que es git, te recomiendo este video: https://youtu.be/DinilgacaWs'

    with open(quickstartPath, 'r') as quickstart:

        QUICK = quickstart.read()

    with open(stepOne, 'r') as stepOne:

        ONE = stepOne.read()

    with open(stepTwo, 'r') as stepTwo:

        TWO = stepTwo.read()

    with open(stepTree, 'r') as stepTree:

        TREE = stepTree.read()

    with open(stepFour, 'r') as stepFour:

        FOUR = stepFour.read()

    with open(stepFive, 'r') as stepFive:

        FIVE = stepFive.read()