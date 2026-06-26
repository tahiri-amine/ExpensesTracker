import argparse
from tracker import ExpenseTracker  
parser = argparse.ArgumentParser(description="Expenss tracker")
sub_parser = parser.add_subparsers(dest="command")
add = sub_parser.add_parser("add")
add.add_argument("-a",help="-a : amount like 2DH or 50DH",type= float,required=True)
add.add_argument("-cat",help="-cat: category like food drinks transport etc...",required=True)
add.add_argument("-nt",help="-nt: a note like if the -cat was food than note could be vegitables",default="no note")
sub_parser.add_parser("list")
sub_parser.add_parser("summary")
delete = sub_parser.add_parser("delete")
delete.add_argument("-id",help="the id of the catergory is a number integre like 1,2,3...",type=int)
delete.add_argument("-all",action="store_true")
modify = sub_parser.add_parser("modify")
modify.add_argument("-id",required=True,type=int,help="id is an integer like 1,2,3,4,....")
modify.add_argument("-cat",help="-cat:category like food transport ect...")
modify.add_argument("-nt",help="nt: stand for notes")
args = parser.parse_args()
obj = ExpenseTracker()
if args.command =="add":
    obj.add(args.a,args.cat,args.nt)
elif args.command == "list":
    obj.list()
elif args.command == "summary":
    obj.summary()
elif args.command =="modify":
    if args.cat or args.nt:
            obj.modify_category(args.id,args.cat,args.nt)
    elif  not args.nt and not args.cat:
        print("provid at lest -cat or -nt")
elif args.command == "delete":
    if args.all:
        obj.expenses = []
        obj.save()
    elif not args.id:
        print("you have to enter the flag -id fllowing by an id or to enter the flag --all")
    else:
        obj.delete(args.id)
