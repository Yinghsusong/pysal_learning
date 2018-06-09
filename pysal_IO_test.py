#coding:utf-8
import pysal

shp = pysal.open(r'D:\常用数据\100wfault\aaa\全国断裂活动性配.shp')
poly = shp.__next__()

print(poly)
# <pysal.cg.shapes.Chain object at 0x0000024B7419E630>

print(len(shp))
# 5100
##############################################################################
db = pysal.open(r'D:\beifen\E盘备份\CON_TEST\Data\200704241.tif.vat.dbf','r')

print(db.header)
# ['Value', 'Count']

print(db.field_spec)
# [('N', 9, 0), ('F', 19, 11)]

print(db.__next__())
# [1, 3146715.0]

print(db[0])
# [1, 3146715.0]

print(db[0:3])
# [[1, 3146715.0], [2, 6718377.0], [3, 9905958.0]]

print(db[0:5,1])
# [3146715.0, 6718377.0, 9905958.0, 10638107.0, 1595941.0]

print(db[0:5,0:2])
# [[1, 3146715.0], [2, 6718377.0], [3, 9905958.0], [4, 10638107.0], [5, 1595941.0]]

print(db[-1,-1])
# [1595941.0]
####################################################################################

csv_file = pysal.open(r'D:\常用数据\DataWarehouse-master\File\beijingtianqi.csv')
print(csv_file.header)
# ['date', 'AQI', 'Range', 'Level', 'PM2.5', 'PM10', 'SO2', 'CO', 'NO2', 'O3', 'Order', 'Year']

print(csv_file[0])
# [[None, 87, '76~99', '良', 45.0, 111.3, 27.7, 1.5, 61.9, 64, 32, 2014]]

fromWKT = pysal.core.util.wkt.WKTParser()
print(csv_file.cast('AQI',fromWKT))
print(type(csv_file[1][0][1]))
# <class 'NoneType'>
####################################################################################

w = pysal.queen_from_shapefile(r'D:\学习资料\arcgis\Arcgis练习\ArcTutor\GP Service Examples\DataOnDemand\Scratch\ToGo\blockgrp.shp',idVariable='POP00')
print(w.n)
gal = pysal.open(r'D:\pysal_task\data\write_gal.gal','w')
gal.write(w)
gal.close()

####################################################################################

w = pysal.queen_from_shapefile(r'D:\学习资料\arcgis\Arcgis练习\ArcTutor\GP Service Examples\DataOnDemand\Scratch\ToGo\blockgrp.shp',idVariable='POP00')
print(w.n)
arcgis_txt = pysal.open(r'D:\pysal_task\data\arcgis_txt.txt','w','arcgis_text')
arcgis_txt.write(w)
arcgis_txt.close()

####################################################################################
w = pysal.queen_from_shapefile(r'D:\学习资料\arcgis\Arcgis练习\ArcTutor\GP Service Examples\DataOnDemand\Scratch\ToGo\blockgrp.shp',idVariable='POP00')
print(w.n)
arcgis_dbf = pysal.open(r'D:\pysal_task\data\arcgis_dbf.dbf','w','arcgis_dbf')
arcgis_dbf.write(w, useIdIndex=True)
arcgis_dbf.close()

####################################################################################
w = pysal.queen_from_shapefile(r'D:\学习资料\arcgis\Arcgis练习\ArcTutor\GP Service Examples\DataOnDemand\Scratch\ToGo\blockgrp.shp',idVariable='POP00')
print(w.n)
arcgis_swm = pysal.open(r'D:\pysal_task\data\arcgis_swm.swm','w')
arcgis_swm.write(w)
arcgis_swm.close()

####################################################################################
w = pysal.queen_from_shapefile(r'D:\学习资料\arcgis\Arcgis练习\ArcTutor\GP Service Examples\DataOnDemand\Scratch\ToGo\blockgrp.shp',idVariable='POP00')
print(w.n)
dat = pysal.open(r'D:\pysal_task\data\dat_file.dat','w')
dat.write(w)
dat.close()

####################################################################################
w = pysal.queen_from_shapefile(r'D:\学习资料\arcgis\Arcgis练习\ArcTutor\GP Service Examples\DataOnDemand\Scratch\ToGo\blockgrp.shp',idVariable='POP00')
print(w.n)
mat = pysal.open(r'D:\pysal_task\data\mat_file.mat','w')
mat.write(w)
mat.close()

####################################################################################
w = pysal.queen_from_shapefile(r'D:\学习资料\arcgis\Arcgis练习\ArcTutor\GP Service Examples\DataOnDemand\Scratch\ToGo\blockgrp.shp',idVariable='POP00')
print(w.n)
wk1 = pysal.open(r'D:\pysal_task\data\wk1_file.wk1','w')
wk1.write(w)
wk1.close()

####################################################################################
w = pysal.queen_from_shapefile(r'D:\学习资料\arcgis\Arcgis练习\ArcTutor\GP Service Examples\DataOnDemand\Scratch\ToGo\blockgrp.shp',idVariable='POP00')
print(w.n)
stata_txt = pysal.open('D:\pysal_task\data\stata_txt.txt','w','stata_text')
stata_txt.write(w,matrix_form=True)
stata_txt.close()

####################################################################################
w = pysal.queen_from_shapefile(r'D:\学习资料\arcgis\Arcgis练习\ArcTutor\GP Service Examples\DataOnDemand\Scratch\ToGo\blockgrp.shp',idVariable='POP00')
print(w.n)
mtx = pysal.open(r'D:\pysal_task\data\matrix_file.mtx','w')
mtx.write(w)
mtx.close()

####################################################################################
from pysal.core.util.weight_converter import weight_convert

gal_file = r'D:\pysal_task\data\write_gal.gal'
swm_file = r'D:\pysal_task\data\arcgis_swm.swm'
weight_convert(gal_file,swm_file,useIdIndex=True)
wold = pysal.open(gal_file,'r').read()
wnew = pysal.open(swm_file,'r').read()
print(wold.n==wnew.n)