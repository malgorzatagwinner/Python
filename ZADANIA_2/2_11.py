#!/usr/bin/env python3
# -*- coding: utf -8-*-
import sys

def kreskowanie(word):
    """Funkcja oddziela slowa podkreslnikiem
    >>> kreskowanie('test jeden')
    't_e_s_t_ _j_e_d_e_n'
    >>> kreskowanie('to jest drugi test')
    't_o_ _j_e_s_t_ _d_r_u_g_i_ _t_e_s_t'
    >>> kreskowanie('trzeci test tez nie jest taki trudny')
    't_r_z_e_c_i_ _t_e_s_t_ _t_e_z_ _n_i_e_ _j_e_s_t_ _t_a_k_i_ _t_r_u_d_n_y'
    """
    
    word = "_".join(list(word))
    return word

if __name__ == '__main__':
    #testy
    import doctest
    doctest.testmod()

    if len(sys.argv) > 1:
        # w podanych plikach
        for filename in sys.argv[1:]:
            with open(filename) as f:
                print(kreskowanie(f.read()))
    else:
        # na standardowym wejściu
        data = sys.stdin.read().rstrip()
        print(kreskowanie(data))
  
