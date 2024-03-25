from app import main
from app.probability import calculator_probability

match __name__:
    case "__main__":
        type, event = main()
        result = calculator_probability(type)
        print(result)