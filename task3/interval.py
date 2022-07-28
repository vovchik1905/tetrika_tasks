t1 = { 'lesson': [1594663200, 1594666800],
    'pupil': [1594663340, 1594663389, 1594663390, 1594663395, 1594663396, 1594666472],
    'tutor': [1594663290, 1594663430, 1594663443, 1594666473] }

t2 = {'lesson': [1594702800, 1594706400],
    'pupil': [1594702789, 1594704500, 1594702807, 1594704542, 1594704512, 1594704513, 1594704564, 1594705150, 1594704581, 1594704582, 1594704734, 1594705009, 1594705095, 1594705096, 1594705106, 1594706480, 1594705158, 1594705773, 1594705849, 1594706480, 1594706500, 1594706875, 1594706502, 1594706503, 1594706524, 1594706524, 1594706579, 1594706641],
    'tutor': [1594700035, 1594700364, 1594702749, 1594705148, 1594705149, 1594706463]}

t3 = {'lesson': [1594692000, 1594695600],
    'pupil': [1594692033, 1594696347],
    'tutor': [1594692017, 1594692066, 1594692068, 1594696341]}

t4 = {'lesson': [10,40],
    'pupil': [11, 53],
    'tutor': [4, 16, 25, 39]}

t5 = {'lesson': [10,60,70,80],
    'pupil': [11, 53, 62, 69, 74, 88],
    'tutor': [4, 16, 25, 90]}

def appearance(intervals: dict) -> int:
    lesson = intervals['lesson']
    pupil = intervals['pupil']
    tutor = intervals['tutor']
    main_interval = [0,0]
    main_interval[0], main_interval[1] = lesson[0], lesson[-1]
    answer = 0

    def lesson_online_check(moment_time: int) -> bool:
        start_lesson_times = lesson[::2]
        finish_lesson_times = lesson[1::2]
        for i in range(len(lesson) // 2):
            if moment_time >= start_lesson_times[i] and moment_time <= finish_lesson_times[i]:
                return True
        return False
    
    def pupil_online_check(moment_time: int) -> bool:
        start_pupil_times = pupil[::2]
        finish_pupil_times = pupil[1::2]
        for i in range(len(pupil) // 2):
            if moment_time >= start_pupil_times[i] and moment_time <= finish_pupil_times[i]:
                return True
        return False
    
    def tutor_online_check(moment_time: int) -> bool:
        start_tutor_times = tutor[::2]
        finish_tutor_times = tutor[1::2]
        for i in range(len(tutor) // 2):
            if moment_time >= start_tutor_times[i] and moment_time <= finish_tutor_times[i]:
                return True
        return False
    
    condition_of_start = False
    for t in range(main_interval[0], main_interval[1]):
        if lesson_online_check(t) and pupil_online_check(t) and tutor_online_check(t):
            if condition_of_start:
                answer+=1
            else:
                condition_of_start = True
        else:
            condition_of_start = False
    
    return answer

if __name__ == "__main__":
    print(appearance(t1))