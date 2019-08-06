#   exceptions

def divide_by(first, second):
    try:
        return first / second

    except Exception as e:
        return "0으로 나눌수 없습니다. "
