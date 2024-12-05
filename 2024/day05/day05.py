rules = []
updates = []
with open('input.txt') as file:
    for line in file:
        if '|' in line:
            rules.append(line.strip())
        if ',' in line:
            updates.append(line.strip().split(','))


def validate_update(rules, update):
    for rule in rules:
        before, after = rule.split('|')

        try:
            if update.index(before) > update.index(after):
                return False
        except ValueError:
            continue

    return True



def part1(rules, updates):
    answerTotal = 0

    for update in updates:
        if validate_update(rules, update):
            answerTotal += int(update[int(len(update)/2)])

    print(f"Part 1: {answerTotal}")
    return True

# This is very brute-force. I think there must be a better way to do this. I
# insert every page into every index location and check the validity. If not
# valid, I insert into the next index location and check validity.
def insert_and_check(rules, fixed_list, page, index=0):
    draft_fixed_list = fixed_list.copy()
    draft_fixed_list.insert(index, page)
    if validate_update(rules, draft_fixed_list):
        return draft_fixed_list
    else:
        index += 1
        return insert_and_check(rules, fixed_list, page, index)


def part2(rules, updates):
    answerTotal = 0

    for update in updates:
        if not validate_update(rules, update):
            fixed = []
            for page in update:
                fixed = insert_and_check(rules, fixed, page)

            answerTotal += int(fixed[int(len(fixed)/2)])

    print(f"Part 2: {answerTotal}")
    return True

part1(rules, updates)
part2(rules, updates)
