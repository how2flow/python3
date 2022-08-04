# Python 3.8
# file: arguments.py
# url: https://docs.python.org/ko/3/library/argparse.html
# author: steve.jeong

import argparse

'''
Example using
$ python3 arguments.py -h [--help]
$ python3 arguments.py -i=a [--input=a] -o=b [--output=b] ok good
'''

def main():
  parser = argparse.ArgumentParser(
      description = 'Argparse script.',
      formatter_class = argparse.ArgumentDefaultsHelpFormatter)
  # optional: Define in free.
  parser.add_argument(
      '-i', '--input', required=True, help='path of input file')
  parser.add_argument(
      '-o', '--output', required=True, dest='out_path', help='path of output')
  parser.add_argument(
      '-n', '--num', type=int, default=10, help='number')
  # positional: Define in order.
  parser.add_argument(
      'foo', default='foo', help='it is foo')
  parser.add_argument(
      'bar', default='bar', help='it is bar')
  # parse args
  args = parser.parse_args()
  # print args
  print('[option] input=%s output=%s num=%d' % (args.input, args.out_path, args.num))
  print('[position] foo=%s bar=%s' % (args.foo, args.bar))

if __name__ == '__main__':
  main()

# vim: ft=python ts=2 sw=2 sts=2 et
