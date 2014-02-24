import shutil 

src = '/Volumes/Echo/GIS/projects/streetview/tasks/201402_crashes_streetratings/exchange/from_20140108_steve/newyork_with_rating_date_uid_lines.json'
dst = '/Users/danielmsheehan/GitHub/streetview/tasks/201402_crashes_streetratings/newyork_with_rating_date_uid_lines.json'

print 'copy file'
shutil.copy2(src, dst)

print 'complete'