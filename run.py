from app import main

match __name__:
    case "__main__":
        type, event = main()
        result = calculator_probability(type)
        print(result)
