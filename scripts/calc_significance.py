from fact.analysis import li_ma_significance, split_on_off_source_independent
from fact.io import read_data


df = read_data('crab_gammas_dl3.hdf5', key='events')


on, off = split_on_off_source_independent(
    df.query('gamma_prediction > 0.85'),
    0.025,
)

with open('build/significance.tex', 'w') as f:
    f.write(r'\SI{')
    f.write(
        '{:.1f}'.format(li_ma_significance(len(on), len(off), 0.2))
    )
    f.write(r'}{σ}')
