#!/usr/bin/env python2
import sys
from argparse import ArgumentParser

if __name__ == "__main__":
    aparser = ArgumentParser(description="labauth")
    
    aparser.add_argument("command", help="command to run")
    
    args = aparser.parse_args()

    if args.command == 'runserver':
        from labauth import app
        app.run(debug=True)
    elif args.command == 'initdb':
        from labauth import db
        db.create_all()
    else:
        print("[i] command not found, exitting")
        sys.exit(-1)
