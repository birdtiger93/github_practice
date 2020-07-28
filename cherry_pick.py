import os
import sys


def main(*argv):
    path = sys.argv[1]
    numCherryPick = int(sys.argv[2]) if len(sys.argv) > 2 else 9999

    with open(path, "r") as f:
        commits = f.read()
    commitNumList = []
    for commit in commits.splitlines():
        commitNumList.append(commit.split(' ')[0])
    cmd = "git cherry-pick "
    cherryPickCnt = 0
    while len(commitNumList) > 0 and cherryPickCnt < numCherryPick:
        cmd += commitNumList.pop() + " "
        cherryPickCnt += 1
    print(cmd)
    os.system(cmd)


if __name__ == "__main__":
    main()
