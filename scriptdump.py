""" Python 2.70
    Written by : Praveen Kumar Verma 28 Feb,2016
    Aim : To generate hcv patients analytics data and save it to table
    Requirements:
                 1.Patients category table
                 2.Prescription_ref_chart table
                 3.List of patients table
                 4.MySQL configuration
     Steps:
                 1.get list of patients category
                 2.loop through all patients category
                 3.for each category get list of medications from prescription table
                 4.for each medication
                       1.get count ,cost,days of medication falling in respective category
                       2.calculate efficacy and len of respective drug count
                  5.get max_cost to calculate cost factor
                  6.put the results in a list
                  7.loop through list
                    1.calculate adherence,utilization,value
                    2.store the results in the list
                  8.again traverse through list
                  9.insert the values in to the database
          """        
                 
from __future__ import division
import MySQLdb
from MySQLdb import Error
try:
  cnx = MySQLdb.connect(host='52.32.132.162',user='root',passwd='BigData23',
                                db='Development_Dataset')              
  cursor=cnx.cursor()
  #query to drop table
  cursor.execute('DROP TABLE IF EXISTS hcv_analytics')
  create_table_hcv_analytics="""CREATE TABLE `hcv_analytics` (
								  `id` int(11) NOT NULL AUTO_INCREMENT,
								  `drug_id` int(11) NOT NULL,
								  `category_id` int(11) DEFAULT NULL,
								  `value` float DEFAULT NULL,
								  `count` int(11) DEFAULT NULL,
								  `efficacy` float NOT NULL,
								  `utilization` float NOT NULL,
								  `adherence` float NOT NULL,
								  `cost` float DEFAULT '0',
								  `best_value` float DEFAULT '0',
								  `total_length` int(11) DEFAULT NULL,
								  `max_cost` float DEFAULT '0',
								  `cost_gap` float DEFAULT '0',
                                  `safety`  float DEFAULT NULL,
								  PRIMARY KEY (`id`)
								) ENGINE=InnoDB AUTO_INCREMENT=1077 DEFAULT CHARSET=latin1;"""
  cursor.execute(create_table_hcv_analytics)							
  patients_category='select genotype,treatment,treatment_condition,cirrhosis,viral_load ,id from patients_cat '
  cursor.execute(patients_category)
  results=cursor.fetchall() #fetch the query results
  cursor.execute('DROP TABLE IF EXISTS payer_savings')
  cursor.execute("""CREATE TABLE payer_savings (
                  id int(11) auto_increment primary key,
                  category_id int(11) DEFAULT NULL,
                  total_saving float DEFAULT NULL
                ) ENGINE=InnoDB DEFAULT CHARSET=latin1;""")
  for row in results:
      
      drugs_data_query="select Genotype,Treatment,Treatment_Condition,medication,Cirrhosis,treatment_Period,Viral_Load,Medication_Info,id from prescription_ref_chart where Genotype= "+" '%s'  and Treatment= "+" '%s' and  Treatment_Condition = "+" '%s' and (( Cirrhosis = "+" '%s' or Cirrhosis = "+repr('Both')+" ))"+" and Viral_Load = '%s'"
      #print(drugs_data_query%(row[0],row[1],row[2],row[3],row[4]))
      cursor.execute(drugs_data_query%(row[0],row[1],row[2],row[3],row[4]))
      medication=cursor.fetchall()
      tot_len_subpop=0  #total length of particular category
      max_cost_subpop=0 #maximum cost in a category
      sub_pop_data=[]   #Array to hold data for medications
      best_value_subpop=0 #best value score in a category
      best_cost_subpop=0  #best cost in category having best value
      total_cost_subpop=0
      for med in medication:
          len_med=0  #total number  of patients for respective medication
          cost=0     #cost of medication
          eff_pass=0 #number of patients having svr '<1' or '1'
          days_med=0 #number of days medication taken for respected time
          count_res=0 #count of results
          safety_count = 0
          #print('%s %s %s %s %s %s '%(med[0],med[1],med[2],med[3],med[4],med[5]))
          hcv_query="select count(*)as count,avg(claims_cost),hcv_svr12,days_medication,(sum(safety_admission_hospital)+sum(safety_drug_interactions)+sum(safety_liver_failure)+sum(safety_anemia)) as safety from HCV_patients where hcv_genotype= "+" '%s'  and treatment= "+" '%s' and  hcv_treatment_condition = "+" '%s' and  medication = "+" '%s'  and  hcv_cirrhosis = "+" '%s'  and treatment_Period=  '%d'  group by hcv_svr12 "
          if(med[4]=='Both'):
            hcv_query= "select count(*)as count,avg(claims_cost),hcv_svr12,days_medication,(sum(safety_admission_hospital)+sum(safety_drug_interactions)+sum(safety_liver_failure)+sum(safety_anemia)) as safety from HCV_patients where hcv_genotype= "+" '%s'  and treatment= "+" '%s' and  hcv_treatment_condition = "+" '%s' and  medication = "+" '%s'  and (( hcv_cirrhosis = "+" '%s' or hcv_cirrhosis = "+repr('No')+" )  ) and treatment_Period= '%d' group by hcv_svr12 "
            #print(hcv_query%(med[0],med[1],med[2],med[3],'Yes',int(filter(str.isdigit, med[5].encode('ascii','ignore')))))
            cursor.execute(hcv_query%(med[0],med[1],med[2],med[3],'Yes',int(filter(str.isdigit, med[5].encode('ascii','ignore')))))
          else:
            
            if med[6] == 6:
              hcv_query="select count(*)as count,avg(claims_cost),hcv_svr12,days_medication,(sum(safety_admission_hospital)+sum(safety_drug_interactions)+sum(safety_liver_failure)+sum(safety_anemia)) as safety from HCV_patients where hcv_genotype= "+" '%s'  and treatment= "+" '%s' and  hcv_treatment_condition = "+" '%s' and  medication = "+" '%s'  and  hcv_cirrhosis = "+" '%s'  and treatment_Period= "+ '%d'+" and hcv_viral_load < = '%d' group by hcv_svr12 "
              #print(hcv_query%(med[0],med[1],med[2],med[3],med[4],int(filter(str.isdigit, med[5].encode('ascii','ignore'))),int(filter(str.isdigit, med[6].encode('ascii','ignore')))))
              cursor.execute(hcv_query%(med[0],med[1],med[2],med[3],med[4],int(filter(str.isdigit, med[5].encode('ascii','ignore'))),int(filter(str.isdigit, med[6].encode('ascii','ignore')))))
            else: 
               #print(hcv_query%(med[0],med[1],med[2],med[3],med[4],int(filter(str.isdigit, med[5].encode('ascii','ignore')))))
               cursor.execute(hcv_query%(med[0],med[1],med[2],med[3],med[4],int(filter(str.isdigit, med[5].encode('ascii','ignore')))))
          
          hcv_data=cursor.fetchall()
          for res in hcv_data:
                      count_res+=1
                      len_med+=res[0]  #add count
                      cost+=res[1]  #add cost
                      safety_count+=res[4] #add safety count
                      days_med+=(res[3]/7)/int(filter(str.isdigit, med[5].encode('ascii','ignore')))
                      if res[2]!='2':
                        eff_pass+=res[0]

                      #print('%f  %s  %d %d %d'%(days_med,med[5],res[3],res[3]/7,int(filter(str.isdigit, med[5].encode('ascii','ignore')))))
          avg_cost=cost/count_res  #calculate average cost
          
          if(max_cost_subpop<avg_cost):
            max_cost_subpop=avg_cost #get maximum cost in a sub population
          efficacy=  round((eff_pass/len_med)*100,2) #calculate efficacy
          tot_len_subpop+=len_med  #number of patients for particular category
          total_cost_subpop+= avg_cost*len_med
          total_days_med=int(filter(str.isdigit, med[5].encode('ascii','ignore')))*count_res
          adherence=(days_med/count_res)*100 #calculate adherence using MPR formula
          safety_percent = 100 - ((safety_count/len_med)*100)
          sub_pop_data.append([len_med,avg_cost,round(adherence,2),efficacy,row[5],med[8],safety_percent])
          #print('%d %d %d %.2f %d'%(len_med,avg_cost,days_med/7,efficacy,max_cost_subpop))
      #print(sub_pop_data)
      #loop through data 
	  #print(row[5],tot_len_subpop,best_cost_subpop,total_cost_subpop)
      for pop_data in sub_pop_data:
        cost_factor=((max_cost_subpop-pop_data[1])/max_cost_subpop)*100
        utilization = round((pop_data[0]/tot_len_subpop)*100,2)
        value=round((pop_data[2]+pop_data[3]+cost_factor+utilization)/40,2)
        if(best_value_subpop<value):   #get best value
          best_value_subpop=value
          best_cost_subpop=pop_data[1]
          
        pop_data+=[utilization,value]   #append utilization and value in a list
      #print (row[5],tot_len_subpop*best_cost_subpop-total_cost_subpop)
      cursor.execute('insert into payer_savings (category_id,total_saving) values( %.2f, %.2f)'%(row[5],total_cost_subpop-tot_len_subpop*best_cost_subpop))
      cnx.commit()
      #print(sub_pop_data,best_value_subpop,best_cost_subpop)
      #insert into hcv_analytics table  
      for p_data in sub_pop_data:
        query="insert into hcv_analytics (count,cost,adherence,efficacy,category_id,drug_id,utilization,value,best_value,total_length,max_cost,safety) values(%d,%.2f,%.2f,'%f',%d,%d,'%f','%f','%f','%d','%f','%f' ) "
        cursor.execute(query%(p_data[0],p_data[1],p_data[2],p_data[3],p_data[4],p_data[5],p_data[7],p_data[8],best_value_subpop,tot_len_subpop,max_cost_subpop,p_data[6]))
        cnx.commit()
                               
except MySQLdb.Error as err:
    print(err)
else:
  cnx.close()
  

