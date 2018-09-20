import json
import re
from flask import Flask, request as freq
from flask_cors import CORS

app = Flask(__name__, static_folder='static', static_url_path='')
CORS(app)

request = {
    'campus': ['UTSG'],
    'terms': ['2018 Fall'],
    'breadths': [],
    'credits': [0.5, 1.0],
    'departments': [],
    'levels': [],
    'taken': ['CSC148H1', 'PHY132H1', 'MAT135H1', 'MAT136H1', 'ECO101H1', 'ECO102H1',
              'COG250Y1', 'CSC165H1', 'CSC207H1', 'MAT223H1', 'APM236H1', 'CSC236H1'],
    'timetable': [
        [
            # Fall timetable
        ],
        [
            ('MONDAY', 9, 12), ('MONDAY', 15, 17),
            ('TUESDAY', 9, 11), ('TUESDAY', 14, 17), ('TUESDAY', 20, 21),
            ('WEDNESDAY', 11, 12), ('WEDNESDAY', 18, 21),
            ('THURSDAY', 13, 17), ('FRIDAY', 15, 17)
        ],
    ]
}


def get_credits(code):
    return 0.5 + 0.5 * (code[6] == 'Y')


def does_clash(tup1, tup2):
    if tup1[0] == tup2[0]:
        if tup1[1] <= tup2[1] < tup1[2] or tup1[1] < tup2[2] <= tup2[2]:
            return True
        elif tup2[1] <= tup1[1] < tup2[2] or tup2[1] < tup1[2] <= tup2[2]:
            return True
    return False


def split_main(string, callable):
    output = []
    bracket = 0
    temp = ''
    for char in string:
        if char == '(':
            bracket += 1
        elif char == ')':
            bracket -= 1
        elif callable(char) and bracket == 0:
            output.append(temp)
            temp = ''
            continue
        temp += char

    output.append(temp)
    return output


def is_satisfied(prereqs, request):
    course_code = r".*([A-Z]{3}[0-9]{3}[HY][0-9]).*"

    if ',' not in prereqs and '/' not in prereqs and ';' not in prereqs:
        # Find course code
        code = re.match(course_code, prereqs)
        if not code:
            return True
        else:
            code = code.group(1)
            return code in request['taken']
    else:
        parts = split_main(prereqs, lambda x: x == ',' or x == ';')
        if len(parts) > 1:
            parts_satisfied = [is_satisfied(part, request) for part in parts]
            return len(parts_satisfied) == sum(parts_satisfied)
        else:
            parts = split_main(prereqs, lambda x: x == '/')
            if len(parts) > 1:
                parts_satisfied = [
                    is_satisfied(part, request)
                    for part in parts
                ]
                return sum(parts_satisfied) > 0
            else:
                return is_satisfied(prereqs[1:-1], request)


def irrelevant_course(course, request):
    return ((not course['term'] in request['terms'] and len(request['terms']))
            or course['code'][:-1] in request['taken']
            or (len(request['levels']) and not course['level'] in request['levels'])
            or (len(request['campus']) and not course['campus'] in request['campus'])
            or not is_satisfied(course['prerequisites'], request)
            or (get_credits(course['code']) not in request['credits'] and len(request['credits']))
            or (len(request['departments']) and not course['department'] in request['departments'])
            or sum([completed_course in course['exclusions'] for completed_course in request['taken']])
            or (not set(course['breadths']).intersection(set(request['breadths'])))
            and (len(request['breadths'])))


def irrelevant_section(section, request):
    return (not section['enrolment'] < section['size'] or
            not section['code'].startswith('L')
            or not len(section['times']))


def set_times(term, section, request):
    times = []
    for time in section['times']:
        tup = (time['day'], time['start'] / 3600, time['end'] / 3600)
        for scheduled_class in request['timetable'][term]:
            if does_clash(json.loads(scheduled_class), tup):
                section['times'] = []
                return

        times.append(tup)

    section['times'] = times


def build_output(course, section):
    return {
        'id': course['id'],
        'course': course['code'] + ' ' + section['code'],
        'level': course['level'],
        'credits': get_credits(course['code']),
        'term': course['term'],
        'campus': course['campus'],
        'department': course['department'],
        'seats': section['size'] - section['enrolment'],
        'breadths': ', '.join(map(str, course['breadths'])),
        'name': course['name'],
        'description': course['description'],
        'pre': course['prerequisites'],
        'times': section['times']
    }


def finder(request):
    shown = []
    lines = []

    course_file = open("courses.json", 'r', encoding='utf8')
    for line in course_file:
        course = json.loads(line, encoding='utf8')
        course_id = (course['code'] + ' ' + course['term'])

        if course_id in shown or irrelevant_course(course, request):
            continue

        for section in course['meeting_sections']:
            set_times('Winter' in course['term'], section, request)

            if 'L990' in section['code']:
                section['times'].append(['ONLINE', 0.0, 0.0])

            if irrelevant_section(section, request):
                continue

            shown.append(course_id)
            lines.append(build_output(course, section))

    return lines


@app.route("/get-courses", methods=['POST'])
def get_courses():
    request = json.loads(json.loads(freq.data)['request'])
    return json.dumps(finder(request))


@app.route('/')
def root():
    return app.send_static_file('index.html')
