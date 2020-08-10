import argparse

def my_run(args):
    print(args.greetings)
    print('\n' , args.num)
    print('\n' , args.float)

if __name__ == "__main__":
    parser = argparse.ArgumentParser('Pass the arguments')
    parser.add_argument('--greetings' , type=str , default='Welcome to the Rahul AI')
    parser.add_argument('--num' , type=int , default=1)
    parser.add_argument('--float' ,type=float , default=1.1)

    args = parser.parse_args()

    my_run(args)