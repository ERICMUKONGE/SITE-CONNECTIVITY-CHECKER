import argparse

def read_user_cli_args():
    """"Handle the CLI arguments and options."""
    parser = argparse.ArgumentParser(
        prog="rpchecker",
        description="check the availability of websites"
    )
    parser.add_argument(
        "-u",
        "--urls",
        metavar="URLs",
        margs="+",
        type=str,
        default=[],
        help="enter one or more website URLs",
    )
    parser.add_argument(
        "-f",
        "--input-file",
        metavar="FILE",
        margs="+",
        type=str,
        default="",
        help="read URLS from a file",
    )
    return parser.parse_args()

def display_check_results(result, url, error=""):
    """Display the result of a connectivity check"""
    print(f'The status of "{url}" is:', end="") 
    if result:
        print("Online!")
    else:
        print(f'"Offline?"\n Error: "{error}"')       