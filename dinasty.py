import sys
import argparse
import random

def main():

    '''
    Run the software to generate schedule
    '''

    # Initialize parser
    parser = argparse.ArgumentParser()

    # Parse arguments
    # parser.add_argument('--conf', dest='conf', default=4,  help='Select the number of times against team into same conference')
    # parser.add_argument('--extra', dest='extra', default=2, help='Select the number of times against team into another conference')
    parser.add_argument('--schedule', dest='schedule', default=False, action='store_true', help='Generate schedule dinasty')

    args = parser.parse_args()

    # Generate schedule
    # if args.schedule is None or args.conf is None or args.extra is None:
    #     print 'Missing parameter'
    # elif int(args.conf) % 2 != 0:
    #     print 'N. Conference Games against every other team must be even'
    # elif int(args.extra) % 2 != 0:
    #     print 'N. Extra-Conference Games against every other team must be even'
    if args.schedule is None:
        print 'Missing parameter'
    else:
        div1 = ['Boston', 'Charlotte', 'Chicago', 'Cleveland', 'Detroit', 'Indiana', 'Miami', 'New York', 'Philadelphia', 'Tampa']
        div2 = ['Dallas', 'Denver', 'Houston', 'Las Vegas', 'Los Angeles', 'Memphis', 'Phoenix', 'Salt Lake City', 'San Jose', 'Seattle']

        random.shuffle(div1)
        random.shuffle(div2)
        league = div1 + div2
        random.shuffle(league)
        schedule_conf_div1 = []
        schedule_conf_div2 = []
        schedule_extra = []
        schedule_dinasty = []

        out_file = open("schedule.txt", "w")
        out_file.write("\n")
        out_file.close()

        def create_schedule(list):
            """ Create a schedule for the teams in the list and return it"""
            s = []

            # if len(list) % 2 == 1: list = list + ["BYE"]

            for i in range(len(list) - 1):

                mid = len(list) / 2
                l1 = list[:mid]
                l2 = list[mid:]
                l2.reverse()

                # Switch sides after each round
                if (i % 2 == 1):
                    s = s + [zip(l1, l2)]
                else:
                    s = s + [zip(l2, l1)]

                list.insert(1, list.pop())

            return s

        schedule_conf_div1 = schedule_conf_div1 + create_schedule(div1)
        schedule_conf_div1 = schedule_conf_div1 + create_schedule(div1[::-1])
        schedule_conf_div2 = schedule_conf_div2 + create_schedule(div2)
        schedule_conf_div2 = schedule_conf_div2 + create_schedule(div2[::-1])

        while len(schedule_conf_div1) > 0 and len(schedule_conf_div2) > 0:
            nr = random.randint(0, len(schedule_conf_div1) - 1)
            game = []
            game.append(schedule_conf_div1[nr] + schedule_conf_div2[nr])
            schedule_dinasty.append(game)
            del schedule_conf_div1[nr]
            del schedule_conf_div2[nr]

        schedule_extra = schedule_extra + create_schedule(league)
        schedule_extra = schedule_extra + create_schedule(league[::-1])

        while len(schedule_extra) > 0:
            nr = random.randint(0, len(schedule_extra) - 1)
            game = []
            game.append(schedule_extra[nr])
            schedule_dinasty.append(game)
            del schedule_extra[nr]

        # if int(args.extra) // 2 < 1:
        #     for i in range(int(args.conf) // 2):
        #         schedule_conf_div1 = schedule_conf_div1 + create_schedule(div1)
        #         schedule_conf_div1 = schedule_conf_div1 + create_schedule(div1[::-1])
        #
        #         schedule_conf_div2 = schedule_conf_div2 + create_schedule(div2)
        #         schedule_conf_div2 = schedule_conf_div2 + create_schedule(div2[::-1])
        #
        #     while len(schedule_conf_div1) > 0 and len(schedule_conf_div2) > 0:
        #         nr = random.randint(0, len(schedule_conf_div1) - 1)
        #         game = []
        #         game.append(schedule_conf_div1[nr] + schedule_conf_div2[nr])
        #         schedule_dinasty.append(game)
        #         del schedule_conf_div1[nr]
        #         del schedule_conf_div2[nr]
        #
        #
        # else:
        #     for i in range(int(args.conf)//4):
        #         schedule_conf_div1 = schedule_conf_div1 + create_schedule(div1)
        #         schedule_conf_div1 = schedule_conf_div1 + create_schedule(div1[::-1])
        #
        #         schedule_conf_div2 = schedule_conf_div2 + create_schedule(div2)
        #         schedule_conf_div2 = schedule_conf_div2 + create_schedule(div2[::-1])
        #
        #     while len(schedule_conf_div1) > 0 and len(schedule_conf_div2) > 0:
        #         nr = random.randint(0, len(schedule_conf_div1) - 1)
        #         game = []
        #         game.append(schedule_conf_div1[nr] + schedule_conf_div2[nr])
        #         schedule_dinasty.append(game)
        #         del schedule_conf_div1[nr]
        #         del schedule_conf_div2[nr]
        #
        #     for i in range(int(args.extra) // 2):
        #         schedule_extra = schedule_extra + create_schedule(league)
        #         schedule_extra = schedule_extra + create_schedule(league[::-1])
        #
        #     while len(schedule_extra) > 0:
        #         nr = random.randint(0, len(schedule_extra) - 1)
        #         game = []
        #         game.append(schedule_extra[nr])
        #         schedule_dinasty.append(game)
        #         del schedule_extra[nr]

        week = 56
        while len(schedule_dinasty) > 0:
            nr = random.randint(0, len(schedule_dinasty) - 1)
            print schedule_dinasty[nr]
            print ('WEEK ' + str(week-len(schedule_dinasty)+1))
            with open("schedule.txt", "a") as myfile:
                myfile.write('GAME '+str(week-len(schedule_dinasty)+1)+'\n')
                myfile.write('\n'.join('@'.join(elems) for elems in schedule_dinasty[nr][0]))
                myfile.write('\n')
                myfile.write("------------------------------------------------------------------------ \n")
                del schedule_dinasty[nr]

if __name__ == "__main__":

    sys.exit(main())
