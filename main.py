from flask import Flask, request
from statistics import quantiles
import numpy as np

app = Flask(__name__)


@app.route("/hello")
def hello():
    return "hello"


@app.route("/how-many-params")
def howManyParams():
    total = 0
    for vals in request.args.values():
        total += int(vals)
    return {"answer": total}


@app.route("/min")
def minimum():
    numOfParams = request.args.get("numOfParams")
    numbers = request.args.get("numbers")
    listOfNumbers = numbers.split(",")
    for i in range(0, int(numOfParams)):
        listOfNumbers[i] = int(listOfNumbers[i])

    minimumNumber = min(listOfNumbers)
    return str(minimumNumber)


@app.route("/max")
def maximum():
    numOfParams = request.args.get("numOfParams")
    numbers = request.args.get("numbers")
    listOfNumbers = numbers.split(",")
    for i in range(0, int(numOfParams)):
        listOfNumbers[i] = int(listOfNumbers[i])

    maximumNumber = max(listOfNumbers)
    return str(maximumNumber)


@app.route("/avg")
def average():
    numOfParams = int(request.args.get("numOfParams"))
    numbers = request.args.get("numbers")
    listOfNumbers = numbers.split(",")
    for i in range(0, numOfParams):
        listOfNumbers[i] = int(listOfNumbers[i])

    sumOfNumbers = sum(listOfNumbers)
    print(sumOfNumbers)
    average = sumOfNumbers / numOfParams
    return str(average)


@app.route("/median")
def median():
    numOfParams = int(request.args.get("numOfParams"))
    numbers = request.args.get("numbers")
    listOfNumbers = numbers.split(",")
    for i in range(0, numOfParams):
        listOfNumbers[i] = int(listOfNumbers[i])
    listOfNumbers.sort()
    index = (numOfParams - 1) // 2

    if numOfParams % 2:
        return str(listOfNumbers[index])
    else:
        return str((listOfNumbers[index] + listOfNumbers[index + 1]) / 2.0)


@app.route("/percentile")
def percentile():
    numOfParams = int(request.args.get("numOfParams"))
    numbers = request.args.get("numbers")
    listOfNumbers = numbers.split(",")
    for i in range(0, numOfParams):
        listOfNumbers[i] = int(listOfNumbers[i])
    listOfNumbers.sort()
    a = np.array(listOfNumbers)
    q = int(request.args.get("quantifier"))
    p = np.percentile(a, q)
    return str(p)


app.run(debug=True)
