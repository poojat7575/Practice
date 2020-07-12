def solution(day, jump):
    days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
    return days[(days.index(day) + jump) % 7]

if __name__ == "__main__":
    print(solution("Wed", 14)
