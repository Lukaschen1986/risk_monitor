df_pivot = pd.pivot_table(df, index="ticketingdate", columns="hour", values=content, aggfunc=np.sum, fill_value=0)
df_pivot_zero = pd.DataFrame(np.zeros((len(df_pivot),24)), columns=range(24), index=df_pivot.index)
df_pivot_zero += df_pivot
df_pivot_zero = df_pivot_zero.fillna(0.0)
df_pivot = df_pivot_zero/1000.0 
min_val = np.array(df_pivot).flatten()
min_val = min_val[min_val != 0]
min_val = np.sort(min_val)[1] 

# parameter
lam = df_pivot.apply(np.mean, axis=0).astype(int) # pois
mu = df_pivot.apply(np.mean, axis=0) # norm/t
sigma = df_pivot.apply(np.std, axis=0) # norm/t    
## pois
pois_quantile_l = stats.poisson.ppf(quantile_l, lam)
pois_quantile_r = stats.poisson.ppf(quantile_r, lam)
## norm
norm_quantile_l = stats.norm.ppf(quantile_l, mu, sigma)
norm_quantile_r = stats.norm.ppf(quantile_r, mu, sigma)
## t
t_quantile_l = stats.t.ppf(quantile_l, freedom, mu, sigma)
t_quantile_r = stats.t.ppf(quantile_r, freedom, mu, sigma)
