import time
import os
import random
import sys
import re
import json

SAVE_FILE = "tasks.json"

def clear_screen():
    """Clears the terminal screen based on the OS."""
    os.system('cls' if os.name == 'nt' else 'clear')

def load_tasks():
    """Loads tasks from a JSON file if it exists."""
    if os.path.exists(SAVE_FILE):
        try:
            with open(SAVE_FILE, 'r') as f:
                data = json.load(f)
                return {int(k): v for k, v in data.items()}
        except:
            return {}
    return {}

def save_tasks(tasks):
    """Saves the current tasks to a JSON file."""
    with open(SAVE_FILE, 'w') as f:
        json.dump(tasks, f)

def clear_save():
    """Deletes the save file when tasks are cleared or completed."""
    if os.path.exists(SAVE_FILE):
        os.remove(SAVE_FILE)

def print_doodle():
    """Prints a random space-themed ASCII doodle with dynamic padding."""
    doodles = [
        # Constellation/Satellite
        r"""
 @  * .  . * * .        .        .   * ..
 @. /\ * ###     .      .        .            *
 @ /  \  * #####   .     * * * .
 ]/ [] \  ######### * .  * .  //    .  * .
 / [][] \###\#|#/###   ..    * .  //  * .  ..  *
 |  __  | ###\|/###  * * ___o |==// .      * *
 |  |!  |  # }|{  #        /\  \/  //|\
 |  ||  |    }|{           / /        | \
                           ` `        '  '
        """,
        # Abstract Satellite/Orbit
        r"""
   .       .
 +  :      .
       :       _
   .   !   '  (_)
      ,|.'
-  -- ---(-O-`--- --  -
      ,`|'`.
    ,   !    .
       :       :  "
       .     --+--
 .:        .       !
        """,
        # Standard Vertical Rocket
        r"""
                 ^
                / \
               /   \
              /     \
             |       |
             |  (o)  |
             |       |
            /|       |\
           / |       | \
          /  |_______|  \
         /___/ \___/ \___\
               |   |
              /|   |\
             ===   ===
        """,
        # Landscape/Sky
        r"""
                .                                              .
     * .                  .              .        .   * .
  .         .                    .       .           .      .        .
        o                            .                   .
         .              .                  .           .
         0     .
              .          .                ,                ,    ,
 .          \          .                        .
      .      \   ,
   .          o     .                .                   .            .
     .         \                 ,             .                .
            #\##\#      .                            .        .
          #  #O##\###                .                        .
   .        #*#  #\##\###                      .                     ,
        .   ##*#  #\##\##              .                    .
      .      ##*#  #o##\#         .                            ,       .
          .     *#  #\#     .                    .             .          ,
                      \          .                         .
____^/\___^--____/\____O______________/\/\---/\___________---______________
   /\^   ^  ^    ^                  ^^ ^  '\ ^          ^       ---
         --           -            --  -      -         ---  __       ^
   --  __                      ___--  ^  ^                        --  __
        """,
        # Ringed Planet
        r"""
                       * .                 .
           .                        *
                   _..._     .                  *
                 .'     '.             .
            ..._ |       | _...
          .'    '-.     .-'    '.       .
           '--..._ '...' _...--'
       * '-...-'        .
                            * .
        """,
        # UFO / Saucer
        r"""
                .       * .                 .
            .       _.-" "-._         .
               _.-"           "-._             *
         .   (_____________________)   *
              \__                 __/        .
                 "---.........---"
            * / | | | \        .
                    /  | | |  \              .
                   /   | | |   \
        """,
        # Restored High-Fidelity Black Hole
        r"""
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⠀⢤⠠⡔⣰⢂⡲⣄⠢⢄⠠⢀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠌⠰⡇⢾⣬⣷⣽⣧⣿⣵⣾⠽⡎⡶⠡⠌⠄⠂⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣤⠲⣢⢹⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⠡⢘⣥⣻⢬⢻⣿⣿⣿⣿⣿⣿⣤⢿⣱⢷⢔⡀⠂⠄⠀⠀⠀⠀⠀⠀⠀⡈⡌⣰⣸⠘⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠡⢂⡔⣧⣮⡾⣺⣗⣯⡿⠿⠿⠿⠾⣯⡽⣻⣭⡫⡻⣭⡘⠄⡀⠀⠀⠀⠀⠀⠁⠤⠍⠁⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠌⡐⢡⢊⢮⣾⣻⣪⡮⠊⠁⠀⠀⠀⠀⠀⠀⠈⢓⡷⡙⣮⡪⡻⡰⣀⠔⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡈⢀⠐⢂⣏⢻⣏⠓⡏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢋⡟⣿⣾⣿⣇⡟⣉⣿⡖⢳⣾⣰⣶⣀⣀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⠐⡠⢐⡼⣮⢯⣝⠟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢈⣾⣽⣿⣿⣿⣿⣿⣾⣯⢿⣿⣷⡯⠛⠤⠁⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣂⡡⢚⣯⣯⣿⣾⡧⠀⠆⠀⠀⠀⠀⠀⠀⢀⣀⣠⣠⣤⣾⣿⣿⣿⣿⣿⣿⣿⠿⡟⠟⠩⠁⠂⠁⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⣠⣴⣾⣿⣿⣿⣿⣿⣿⣿⣿⣤⣧⣤⣤⣴⣶⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢻⠟⢫⠙⠠⠁⠸⠄⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠄⣠⣤⣿⣿⣧⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⣏⡉⡿⡈⠈⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⢤⡚⡽⢿⢿⡿⣿⢿⡿⠿⠿⠿⠻⠯⠿⣿⣿⣯⣻⣿⠽⠟⠟⠛⠻⢛⡩⣵⡟⡢⣟⠏⠠⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠁⠀⠂⠐⠀⠂⠀⠁⠈⠀⠁⠀⠂⠘⠫⣓⡷⡇⣿⣯⣴⣬⣿⡗⣟⣾⡿⡡⢊⠐⢀⠄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠑⠳⡝⣷⢾⢧⡷⣿⣿⠿⠉⡈⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠂⠠⠀⠃⡜⢚⠓⠃⠀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
        """
    ]

    doodle = random.choice(doodles).strip('\n')
    lines = doodle.split('\n')

    max_width = max(len(line) for line in lines)
    max_padding = max(0, 79 - max_width)
    padding = " " * random.randint(0, max_padding)

    print("\n")
    for line in lines:
        print(padding + line)
    print("\n")

def clean_task_input(text):
    """Strips leading numbers, dots, dashes, and parentheses."""
    return re.sub(r'^\d+[\.\-\)]*\s*', '', text).strip()

def print_task_list(tasks):
    """Prints the full task list with status indicators."""
    if not tasks:
        print("  (no tasks yet)")
        return
    for tid, t in tasks.items():
        status = " [done]" if t['done'] else ""
        priority = "!" * t['points']
        print(f"  {tid}. {t['text']} {priority}{status}")

def main():
    clear_screen()
    print("i am rocky. we fix stars now.")

    tasks = load_tasks()

    if tasks:
        task_id = max(tasks.keys()) + 1
        print("i remember your tasks from before! here is what we have:")
        print()
        print_task_list(tasks)
        print()
        print("we keep working.")
        time.sleep(1.5)
    else:
        print("make list of tasks. use exclamation marks for priority, like 'build xenonite!!!'")
        tasks = {}
        task_id = 1

        while True:
            raw_t = input("what is new task, question? or type 'done' to start working. ").strip()
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

        save_tasks(tasks)

    session_points = 0
    # Tracks the start of the current unbroken work session (resets only on actual taken breaks)
    session_start_time = time.time()
    # Counter for throttling doodles: show once every 5 commands
    command_count = 0
    # Track which long-work easter eggs have already fired
    shown_40min_egg = False
    shown_60min_egg = False

    print("\ngood. list is made. we work now.")
    print("commands: 'break', 'add', 'list', 'delete', 'done', 'quit', 'clear', or task number.")

    praises = [
        "you not just dumb human after all!",
        "you the smartest human i know. only human i know, but still.",
        "amaze! you save earth today.",
        "you are good at task-doing. like me.",
        "fist my bump! we are heroes.",
        "you do not sleep much. good.",
        "you work fast. radiation not cook your brain yet.",
        "good job. i give you a xenonite star.",
        "you are almost as smart as an eridian. good job.",
        "we survive!",
        "you make good decisions. mostly.",
        "earth will not freeze. probably.",
        "amaze! amaze! amaze!",
        "you work hard. you earn your leaky space food.",
        "you are good scientist."
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
        # --- Long-work easter eggs (checked every loop, based on session_start_time) ---
        elapsed_session = time.time() - session_start_time
        if not shown_40min_egg and elapsed_session >= 40 * 60:
            shown_40min_egg = True
            print()
            print("rocky have words of encouragement.")
            print("you work long time. rocky is... proud? that is right word, yes?")
            print("you are good human. earth is lucky to have you.")
            print("keep going. you are almost there. probably.")
        if not shown_60min_egg and elapsed_session >= 60 * 60:
            shown_60min_egg = True
            print()
            print("rocky have words of GREAT encouragement.")
            print("you work one whole hour. that is impressive even for eridian standard.")
            print("rocky want you to know: you are best human rocky know.")
            print("(rocky only know one human. but still. you are best.)")
            print("amaze. amaze. amaze.")

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
            clear_save()
            break

        cmd = input("\nwhat do you want to do, question? ").strip().lower()
        command_count += 1

        if cmd == 'done':
            urgent_left = [t for t in tasks.values() if t['points'] >= 3 and not t['done']]

            if urgent_left:
                print("\nno! bad! you have '!!!' tasks left. earth is dying!")
                print("you must finish these before you are done:")
                for u in urgent_left:
                    print(f"  {u['text']}")
                print("keep working, question?")
            else:
                print(f"\nyou finish early, question? okay. {random.choice(praises)}")
                time.sleep(1.5)
                for _ in range(4):
                    for frame in frames:
                        clear_screen()
                        print("\n" * 5)
                        print("          amaze! amaze! amaze!")
                        print(frame)
                        time.sleep(0.25)
                clear_save()
                break

        elif cmd == 'quit':
            print("\nyou quit, question? you give up on earth, question? rocky is sad. goodbye.")
            sys.exit()

        elif cmd == 'clear':
            print("\nyou want to forget everything, question? okay. memory wiped.")
            tasks = {}
            task_id = 1
            clear_save()

        elif cmd == 'break':
            elapsed = time.time() - session_start_time
            print("you ask for break, question? let's see what work you have done.")
            print("tasks:")
            has_pending = False
            for tid, t in tasks.items():
                if not t['done']:
                    print(f"  {tid}. {t['text']}")
                    has_pending = True

            if has_pending:
                ans = input("you finish a task, question? enter number or 'none'. ").strip().lower()
                if ans.isdigit() and int(ans) in tasks:
                    tid = int(ans)
                    if not tasks[tid]['done']:
                        tasks[tid]['done'] = True
                        session_points += tasks[tid]['points']
                        save_tasks(tasks)
                        print("good! fist my bump!")

                        if "sleep" in tasks[tid]['text']:
                            print("i will watch you sleep. it is good science.")
                        if "taumoeba" in tasks[tid]['text']:
                            print("taumoeba! bad bad bad!")
                        if "eat" in tasks[tid]['text'] or "food" in tasks[tid]['text']:
                            print("rocky will eat too.")
                        if "math" in tasks[tid]['text']:
                            print("math is math!")
                    else:
                        print("you already did that one. silly human.")
            else:
                print("no tasks left!")

            mins_worked = int(elapsed // 60)
            if session_points >= 5 or elapsed >= 25 * 60:
                print(f"break approved! session points: {session_points}, solid work time: {mins_worked} mins.")
                input("take break. press enter when awake. ")
                # Reset only when break is actually taken
                session_points = 0
                session_start_time = time.time()
                shown_40min_egg = False
                shown_60min_egg = False
                print("timer and points reset. back to work!")
            else:
                print(f"sad! denied! you only have {session_points} points and {mins_worked} mins of solid work.")
                print("need 5 points or 25 mins. keep working! earth is dying!")

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
                save_tasks(tasks)
                print("task added.")

        elif cmd == 'list':
            print("current tasks:")
            print_task_list(tasks)

        elif cmd == 'delete' or cmd.startswith('delete '):
            # Support both "delete" (interactive) and "delete 3" (inline)
            parts = cmd.split(None, 1)
            inline_num = parts[1] if len(parts) > 1 else None

            if inline_num and inline_num.isdigit() and int(inline_num) in tasks:
                tid = int(inline_num)
                deleted_text = tasks[tid]['text']
                del tasks[tid]
                save_tasks(tasks)
                print(f"task '{deleted_text}' is gone. like xenonite vapor.")
            else:
                if inline_num:
                    print("rocky does not see that number. here is what we have:")
                else:
                    print("current tasks:")
                print_task_list(tasks)
                ans = input("which task to delete, question? enter number or 'none'. ").strip().lower()
                if ans.isdigit() and int(ans) in tasks:
                    tid = int(ans)
                    deleted_text = tasks[tid]['text']
                    del tasks[tid]
                    save_tasks(tasks)
                    print(f"task '{deleted_text}' is gone. like xenonite vapor.")
                elif ans != 'none':
                    print("rocky does not see that number. try again.")

        elif cmd.isdigit() and int(cmd) in tasks:
            tid = int(cmd)
            if not tasks[tid]['done']:
                tasks[tid]['done'] = True
                session_points += tasks[tid]['points']
                save_tasks(tasks)
                print(f"task {tid} marked done. good job. jazz hands!")

                if "sleep" in tasks[tid]['text']:
                    print("i will watch you sleep. it is good science.")
                if "taumoeba" in tasks[tid]['text']:
                    print("taumoeba! bad bad bad!")
                if "eat" in tasks[tid]['text'] or "food" in tasks[tid]['text']:
                    print("rocky will eat too.")
                if "math" in tasks[tid]['text']:
                    print("math is math!")
            else:
                print("task already done. try again.")

        else:
            print("rocky does not understand. try 'break', 'add', 'list', 'delete', 'done', 'quit', 'clear', or a task number.")

        # Show doodle only every 5 commands
        if command_count % 5 == 0:
            print_doodle()

if __name__ == "__main__":
    main()
