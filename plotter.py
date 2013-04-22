from __future__ import print_function
import pandas as pd
import numpy as np
import scipy.stats as stats
import matplotlib
import matplotlib.pyplot as plt

def load_algorithm(ALGNAME):
    """@todo: Docstring for load_algorithm

    :ALGNAME: 
    :returns: df

    """
    FILENAME = '{0}.csv'.format(ALGNAME)
    df = pd.read_csv(DATA_DIR+FILENAME)
    print('working on ' + FILENAME)
    return df

def runtimes(ffp, ALGNAME, scale, log_data=False,):
    """Makes an individual plot to show the runtime of ALGNAME

    :ffp: a dataframe indexed by processor count
    :ALGNAME: name of algorithm to be used in text
    :scale: scale of problem  to be used in text
    :log_data: log axes defaults to false
    :returns: nothing

    """
    if log_data:
        ffp.index = np.log2(ffp.index)
    ax = ffp[['t_s','t_p']].plot(style=linstyl,
                                   logy=log_data,
                                   title='{0} raw times at scale {1}'.format(ALGNAME, scale))
    ax.set_ylabel('seconds')

def speedups_plot(ALGS, scale):
    """Compare the algorithms by their speedups on the same sized data

    :ALGS: @todo
    :scale: @todo
    :returns: @todo

    """

    for ALGNAME in ALGS:
        df = load_algorithm(ALGNAME)
        #print(df)

        #ff is the frame fixed at a particular scale
        ff = df[df.scale==scale]
        ffp = ff.set_index('p')
        #runtimes(ffp, ALGNAME, scale, log_data)
        scalas = ffp['t_s']/ffp['t_p']
        scalad[ALGNAME] = scalas
    #compare algorithms by their speedups strong scaling
    scf = pd.DataFrame(scalad)
    ax = scf.plot(style=linstyl)
    ax.set_ylabel('speedup')
    ax.set_xlabel('processor count')
    ax.set_title('algorithms at scale {0}'.format(scale))

if __name__ == '__main__':
    DATA_DIR = u'/home/users/jfairbanks/Projects/hpc6220/term_proj/data/'
    ALGS = ['inner_product_test', 'pack_test',
            'reduction_test',  'scan_test',]

    linstyl = 'o-'
    log_data = False
    scale = 20
    scalad = dict()
    print("fixing a scale of problem, we examine strong scaling")
    #compute speedups
    speedups_plot(ALGS, scale)

    frames = dict()
    for ALGNAME in ALGS:
        df = load_algorithm(ALGNAME)
        #print(df)
        seq = df.set_index(['p','scale',])['t_p']
        print(seq)
        frames[ALGNAME] = seq
        #.plot(kind='bar')
        #algs as columns and scale as rows
    bigframe = pd.DataFrame(frames)
    print(bigframe)
    bigframe.plot(kind='bar')
