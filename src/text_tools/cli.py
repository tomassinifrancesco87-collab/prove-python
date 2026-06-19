from .service import execute_operation
import argparse

def main()->None:
    parser = argparse.ArgumentParser()
    parser.add_argument("text",type=str)
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--word_count",action="store_const",const="word_count",dest="operazione")
    group.add_argument("--char_count",action="store_const",const="char_count",dest="operazione")
    group.add_argument("--reverse",action="store_const",const="reverse",dest="operazione")

    args = parser.parse_args()

    risultato = execute_operation(args.text,args.operazione)

    print(f"Risultato: {risultato}")


if __name__ == "__main__":
    main()
   