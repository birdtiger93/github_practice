import os
import sys


def main(*argv):
    path = sys.argv[1]
    numCherryPick = int(sys.argv[2]) if len(sys.argv) > 2 else 9999

    # get commit hashes from file
    commitNumList = []
    with open(path, "r") as f:
        commits = f.read()
    for commit in commits.splitlines():
        commitNumList.append(commit.split(' ')[0])

    # generate cherry-pick commands
    cmd = "git cherry-pick "
    cherryPickCnt = 0
    while len(commitNumList) > 0 and cherryPickCnt < numCherryPick:
        cmd += commitNumList.pop() + " "
        cherryPickCnt += 1

    # show generated cherry-pick commands
    print(cmd)

    # execute cherry-pick commands
    os.system(cmd)


if __name__ == "__main__":
    main()
