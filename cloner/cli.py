import argparse
from subprocess import call


def main():
    parser = argparse.ArgumentParser(
        description="Script to clone repos into my github folder, and also symbolically link to the desktop."
    )
    parser.add_argument("repo", type=str, help="Repository to clone.")
    parser.add_argument(
        "--github",
        type=str,
        default="/Users/rhysthomas/Documents/GitHub",
        metavar="<path>",
        help="Path to your Github folder.",
    )
    parser.add_argument(
        "--desktop",
        type=str,
        default="/Users/rhysthomas/Desktop",
        metavar="<path>",
        help="Path to your Desktop folder.",
    )

    args = parser.parse_args()

    repo = args.repo
    name = repo.split("/")[-1].replace(".git", "")

    gitdir = args.github
    deskdir = args.desktop

    clone_cmd = f"git clone {repo} {gitdir}/{name}"
    symb_cmd = f"ln -s {gitdir}/{name} {deskdir}/{name}"

    call(clone_cmd.split(" "))
    call(symb_cmd.split(" "))


if __name__ == "__main__":
    main()
