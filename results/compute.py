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

    # Read file
    f = open(fi,"r")
    infos = f.read()
    f.close()

    # Divide into distinct metrics
    infos = infos.split("\n")
    nodes = []
    times = []
    pont = []
    left = []
    acti = []
    expa = []

    j=0
    for i in range(len(infos)-1):
        print("i = ", i, "Infos[i] =", infos[i])
        j=j+1
        if j == 1 :
            times.append(float(infos[i]))
        elif j == 2 :
            nodes.append(int(infos[i]))
        elif j == 3 :
            pont.append(float(infos[i]))
        elif j == 4 :
            left.append(float(infos[i]))
        elif j == 5 :
            acti.append(float(infos[i]))
        else :
            expa.append(float(infos[i]))
            j=0
            

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
        },
        "pont":{
            "max" : float(np.max(pont)),
            "mean" : float(np.mean(pont)),
            "median" : float(np.median(pont)),
            "min" : float(np.min(pont)),
            "confidence" : mean_confidence_interval(pont),
            "values": pont
        },
        "left":{
            "max" : float(np.max(left)),
            "mean" : float(np.mean(left)),
            "median" : float(np.median(left)),
            "min" : float(np.min(left)),
            "confidence" : mean_confidence_interval(left),
            "values": left
        },
        "acti":{
            "max" : float(np.max(acti)),
            "mean" : float(np.mean(acti)),
            "median" : float(np.median(acti)),
            "min" : float(np.min(acti)),
            "confidence" : mean_confidence_interval(acti),
            "values": acti
        },
        "expa":{
            "max" : float(np.max(expa)),
            "mean" : float(np.mean(expa)),
            "median" : float(np.median(expa)),
            "min" : float(np.min(expa)),
            "confidence" : mean_confidence_interval(expa),
            "values": expa
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
