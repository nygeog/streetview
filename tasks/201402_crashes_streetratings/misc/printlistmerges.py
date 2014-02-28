for i in range(1995, 2014):
	i = str(i)
	print '.merge(df'+i+", how='outer', on='svsuid')"