from __future__ import division
import MySQLdb
from MySQLdb import Error
try:
    cnx = MySQLdb.connect(host='localhost',user='pkv121',passwd='12345',
                                db='Development_Dataset')              
    cursor=cnx.cursor()
    cursor.execute("select count(*) as count ,hcv_genotype,hcv_cirrhosis,treatment,hcv_svr12,hcv_viral_load from HCV_patients where medication = '' group by hcv_genotype,treatment, hcv_cirrhosis")
    result = cursor.fetchall()
    for res in result:
        query = "select id from patients_cat where genotype = '%s' and cirrhosis= '%s' and treatment =  '%s' "
        cursor.execute(query%(res[1],res[2],res[3]))
        result_id = cursor.fetchall()
        for id in result_id:
            print(id[0],res[0],res[1],res[2],res[3]) 
            query1 = "insert into hcv_analytics_predict (category_id,count,genotype,treatment,cirrhosis) values ( %d, %d , '%s', '%s', '%s')"
            cursor.execute(query1%(id[0],res[0],res[1],res[3],res[2]))
            cnx.commit()
except MySQLdb.Error as err:
    print(err)
else:
  cnx.close()  