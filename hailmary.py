import time
import os
import random
import sys
import re

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def print_doodle():
    """Prints a random space-themed ASCII doodle with random padding."""
    doodles = [
        r"""
  ^
 / \
|   |
/_-_\
        """,
        r"""
  _._
 =( _ )=
        """,
        r"""
  .--.
 ( o  )
  '--'
        """,
        r"""
   ___
 _/(o)\_
 ~~~~~~~
        """,
        r"""
  _..._
 | [__] |
 \______/
        """,
        r"""
 \#\ | /#/
 \#\_|_/#/
    / \
        """,
        r"""
  ___.
 (  _ \_
  \_.-'
        """,
        r"""
   ,/
 /'/___
 |/   |
        """,
        r"""
  /   \
 | o o |
  \ - /
        """,
        r"""
  * .
   \ /
  . * .
        """
    ]

    doodle = random.choice(doodles).strip('\n')
    # random left padding (0 to 40 to avoid wrapping on an 80-char terminal)
    padding = " " * random.randint(0, 40)

    print("\n")
    for line in doodle.split('\n'):
        print(padding + line)
    print("\n")

def clean_task_input(text):
    # strips leading numbers, dots, dashes, and parentheses so the program can cleanly add its own
    return re.sub(r'^\d+[\.\-\)]*\s*', '', text).strip()

def main():
    clear_screen()
    print("i am rocky. you are grace. we fix stars now.")
    print("make list of tasks. use exclamation marks for priority, like 'build xenonite!!!'.")

    tasks = {}
    task_id = 1

    while True:
        raw_t = input("what is new task (or type 'done' to start working), question? ").strip()
        if raw_t.lower() == 'done':
            break
        if not raw_t:
            continue

        t = clean_task_input(raw_t)

        points = t.count('!')
        if points == 0:
            t = t + '!'
            points = 1

        tasks[task_id] = {'text': t.lower(), 'points': points, 'done': False}
        task_id += 1

    session_points = 0
    last_interaction_time = time.time()

    print("\ngood. list is made. we work now. math is math!")

    praises = [
        "you not just dumb human after all.",
        "you the smartest human i know. (only human i know, but still).",
        "amaze! you save earth today.",
        "you are good at task-doing. like me.",
        "fist my bump! we are heroes.",
        "you do not sleep much. good.",
        "you work fast. radiation not cook your brain yet.",
        "good job. i give you a xenonite star.",
        "you are scary space monster who does all the tasks.",
        "we survive! you and me, grace!",
        "you make good decisions. mostly.",
        "earth will not freeze. probably.",
        "amaze! amaze! amaze!",
        "you work hard. you earn your leaky space food.",
        "you are good friend, grace."
    ]

    frames = [
        r"""
               \             |             /
                \            |            /
                 \           |           /
                  .---------------------.
                 /                       \
           ---  /       _ _ _ _ _         \  ---
           --- |       |_|_|_|_|_|         | ---
               |       |_|_|_|_|_|         |
                \                         /
                 \                       /
                  '---------------------'
        """,
        r"""
                 |           \           |
                 |            \          |
                 |             \         |
                  .---------------------.
                 /                       \
             /  /       _ _ _ _ _         \  \
            /  |       |_|_|_|_|_|         |  \
           /   |       |_|_|_|_|_|         |   \
                \                         /
                 \                       /
                  '---------------------'
        """,
        r"""
                 /           /           \
                /           /             \
               /           /               \
                  .---------------------.
                 /                       \
            |   /       _ _ _ _ _         \   |
            |  |       |_|_|_|_|_|         |  |
            |  |       |_|_|_|_|_|         |  |
                \                         /
                 \                       /
                  '---------------------'
        """,
        r"""
                ~           ~           ~
                 ~         ~           ~
                  ~       ~           ~
                  .---------------------.
                 /                       \
           ~~~  /       _ _ _ _ _         \  ~~~
           ~~~ |       |_|_|_|_|_|         | ~~~
               |       |_|_|_|_|_|         |
                \                         /
                 \                       /
                  '---------------------'
        """,
        r"""
                 \           \           /
                  \           \         /
                   \           \       /
                  .---------------------.
                 /                       \
            \   /       _ _ _ _ _         \   /
             \ |       |_|_|_|_|_|         | /
              \|       |_|_|_|_|_|         |/
                \                         /
                 \                       /
                  '---------------------'
        """
    ]

    while True:
        if tasks and all(t['done'] for t in tasks.values()):
            print(f"\n{random.choice(praises)}")
            time.sleep(1.5)
            for _ in range(4):
                for frame in frames:
                    clear_screen()
                    print("\n" * 5)
                    print("          amaze! amaze! amaze!")
                    print(frame)
                    time.sleep(0.25)
            break

        cmd = input("\nwhat do you want to do (type 'break?', 'add', 'list', 'done', 'force quit', or task number), question? ").strip().lower()

        if cmd == 'done':
            urgent_left = [t for t in tasks.values() if t['points'] >= 3 and not t['done']]

            if urgent_left:
                print("\nno! bad! you have '!!!' tasks left. earth is dying!")
                print("you must finish these before you are done:")
                for u in urgent_left:
                    print(f"  {u['text']}")
                print("keep working, question?")
                last_interaction_time = time.time()
                print_doodle()
            else:
                print(f"\nyou finish early? okay. {random.choice(praises)}")
                time.sleep(1.5)
                for _ in range(4):
                    for frame in frames:
                        clear_screen()
                        print("\n" * 5)
                        print("          amaze! amaze! amaze!")
                        print(frame)
                        time.sleep(0.25)
                break

        elif cmd == 'force quit':
            print("\nyou force quit? you give up on earth? sad. goodbye.")
            sys.exit()

        elif cmd == 'break':
            elapsed = time.time() - last_interaction_time
            print("you ask for break, question? let's see what work you have done.")
            print("tasks:")
            has_pending = False
            for tid, t in tasks.items():
                if not t['done']:
                    print(f"  {tid}. {t['text']} ({t['points']} points)")
                    has_pending = True

            if has_pending:
                ans = input("you finish a task? enter number or 'none', question? ").strip().lower()
                if ans.isdigit() and int(ans) in tasks:
                    tid = int(ans)
                    if not tasks[tid]['done']:
                        tasks[tid]['done'] = True
                        session_points += tasks[tid]['points']
                        print("good! fist my bump!")

                        if "sleep" in tasks[tid]['text']:
                            print("i will watch you sleep. it is good science.")
                        if "taumoeba" in tasks[tid]['text']:
                            print("taumoeba! bad bad bad!")
                        if "eat" in tasks[tid]['text'] or "food" in tasks[tid]['text']:
                            print("rocky will go eat too.")
                        if "math" in tasks[tid]['text']:
                            print("math is math!")
                    else:
                        print("you already did that one. silly grace.")
            else:
                print("no tasks left!")

            mins_worked = int(elapsed // 60)
            if session_points >= 5 or elapsed >= 25 * 60:
                print(f"break approved! session points: {session_points}, solid work time: {mins_worked} mins.")
                input("take break. press enter when awake, question? ")
                session_points = 0
                last_interaction_time = time.time()
                print("timer and points reset. back to work!")
            else:
                print(f"sad! denied! you only have {session_points} points and {mins_worked} mins of solid work.")
                print("need 5 points or 25 mins. keep working! earth is dying!")
                last_interaction_time = time.time()

            print_doodle()

        elif cmd == 'add':
            raw_t = input("what is new task, question? ").strip()
            if raw_t:
                t = clean_task_input(raw_t)
                points = t.count('!')
                if points == 0:
                    t = t + '!'
                    points = 1
                tasks[task_id] = {'text': t.lower(), 'points': points, 'done': False}
                task_id += 1
                print("task added. i make it out of xenonite.")
            last_interaction_time = time.time()
            print_doodle()

        elif cmd == 'list':
            print("current tasks:")
            for tid, t in tasks.items():
                status = "done" if t['done'] else "pending"
                print(f"  {tid}. {t['text']} [{status}]")
            last_interaction_time = time.time()
            print_doodle()

        elif cmd.isdigit() and int(cmd) in tasks:
            tid = int(cmd)
            if not tasks[tid]['done']:
                tasks[tid]['done'] = True
                session_points += tasks[tid]['points']
                print(f"task {tid} marked done. good job. jazz hands!")

                if "sleep" in tasks[tid]['text']:
                    print("i will watch you sleep. it is good science.")
                if "taumoeba" in tasks[tid]['text']:
                    print("taumoeba! bad bad bad!")
                if "eat" in tasks[tid]['text'] or "food" in tasks[tid]['text']:
                    print("rocky will go eat too.")
                if "math" in tasks[tid]['text']:
                    print("math is math!")
            else:
                print("task already done. try again.")
            last_interaction_time = time.time()
            print_doodle()

        else:
            print("i do not understand. try 'break', 'add', 'list', 'done', 'force quit', or a task number.")
            last_interaction_time = time.time()
            print_doodle()

if __name__ == "__main__":
    main()
