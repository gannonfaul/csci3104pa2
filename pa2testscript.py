from __future__ import print_function
import pa2solution
import sys

def run_test_case(test_file_name):
    print('Testing ', test_file_name)
    T = None
    inp_list = []
    ret_list = []
    max_occ = None
    success = True
    try:
        in_file = open(test_file_name, 'r')
        for line in in_file:
            line = line.strip()
            str_list = line.split(',')
            if str_list[0] == 'T':
                tval = str_list[1]
                tval = tval.strip()
                T = int(tval)
                # print('T = ', T)
            elif str_list[0] =='I':
                l = int(str_list[1])
                u = int(str_list[2])
                assert l < u
                # print('I', l, u)
                inp_list.append( (l,u))
            elif str_list[0] =='O':
                l = int(str_list[1])
                u = int(str_list[2])
                assert l < u
                # print('O', l, u)
                ret_list.append( (l,u))
            elif str_list[0] =='M':
                a = int(str_list[1])
                b = int(str_list[2])
                # print('M', a, b)
                max_occ = (a,b)
        print('Done.')
        user_out_list = pa2solution.free_time_intervals(inp_list, T)
        if user_out_list:
            user_out_list = sorted(user_out_list)
            ret_list = sorted(ret_list)
            if user_out_list == ret_list:
                print('\t Test free_time_intervals Passed!')
            else:
                print('\t Test Failed')
                print('\t\t Input: ', inp_list)
                print('\t\t T: ', T)
                print('\t\t Expected Output:', ret_list)
                print('\t\t Your Output:', user_out_list)
                success = False
        else:
            print('\t free_time_intervals either not implemented or does not return a list.')
            success = False
        user_max_occ = pa2solution.max_logged_in(inp_list, T)
        if user_max_occ:
            if (user_max_occ == max_occ):
                print('\t Test max_logged_in passed!')
            else:
                success = False
                print('\t Test max_logged_in failed:')
                print('\t\t Input: ', inp_list)
                print('\t\t T: ', T)
                print('\t\t Expected Output:', max_occ)
                print('\t\t Your Output:', user_max_occ)
        else:
            print('\t max_logged_in not implemented or does not return a list.')
            success = False
        return success
    except IOError as e:
        print('Fatal: error while reading', test_file_name)
        raise


if __name__ == '__main__':
    if len(sys.argv) <= 1:
        print('Usage:', sys.argv[0], 'testfile1 testfile2 ...')
        sys.exit(1)
    n = len(sys.argv)
    succ = True
    for j in range(1,n):
        s = run_test_case(sys.argv[j])
        if not s:
            succ = False
    if succ:
        print('All test cases passed :-)')
    else:
        print('Some test cases failed :-(')
