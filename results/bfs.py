import numpy as np
import scipy.stats
import argparse
import json

def mean_confidence_interval(data, confidence=0.95):
    a = 1.0 * np.array(data)
    n = len(a)
    m, se = np.mean(a), scipy.stats.sem(a)
    h = se * scipy.stats.t.ppf((1 + confidence) / 2., n-1)
    return h


def main(fi):
    f = open(fi,"r")
    infos = f.read()
    f.close()



    infos = infos.split("\n")
    nodes = []
    times = []
    for i in range(len(infos)-1):
        
        if i%2==1:
            nodes.append(int(infos[i]))
        else:
            times.append(float(infos[i]))




    new = {
        "times":{
            "max" : np.max(times),
            "mean" : np.mean(times),
            "median" : np.median(times),
            "min" : np.min(times),
            "confidence" : mean_confidence_interval(times),
            "values": times
        },
        "nodes":{
            "max" : float(np.max(nodes)),
            "mean" : float(np.mean(nodes)),
            "median" : float(np.median(nodes)),
            "min" : float(np.min(nodes)),
            "confidence" : mean_confidence_interval(nodes),
            "values": nodes
        }
    }

    f = open(fi,"w")
    f.write(json.dumps(new))
    f.close()
if __name__ == '__main__':

    parser = argparse.ArgumentParser(description='Execution parameters')

    parser.add_argument('--file',  type=str, help='File path')
    args = parser.parse_args()

    main(args.file)