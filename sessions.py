from argparse import Namespace


def get(args: Namespace) -> str:
    if args.session:
        return args.session
    try:
        session_file = args.session_file if args.session_file else ".session"
        with open(session_file) as f:
            return f.read().strip()
    except FileNotFoundError:
        raise Exception(
            f"Session file '{session_file}' not found. Please create it with your session token."
        )
