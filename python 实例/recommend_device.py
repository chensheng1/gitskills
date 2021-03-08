#coding:utf-8
from math import sqrt
import pandas as pd
import sys
import MySQLdb

def get_connected_db():
    '''
    创建并返回一个有用连接
    '''
    db = MySQLdb.connect(host='127.0.0.1',
          port=3306,
          user='root',
          passwd='*fiber123',
          db='hubutraff',)
    return db

def db_to_df(table_name,where,*table_field):
    '''
    @param db_name:数据库表名
    @param *table_field:字段名
    @return:相同结构的pd.dataframe
    @param where:string,制约条件
    '''
    #获取参数相关信息
    field_num=len(table_field)
    field_index=[i for i in xrange(field_num)]
    #根据参数生成sql语句
    sql="select "
    for field in table_field:
        sql=sql+field+','
    sql=sql[:-1]+" from "+table_name+' '+where
    #执行查询,获得结果
    sql_result=execute_result(sql)
    #将结果导入df，并返回
    np_list=[]
    for i in sql_result:
        _inner_list=[]
        for ii in i:
            _inner_list.append(ii)
        np_list.append(_inner_list)
    df=pd.DataFrame(np_list,columns=list(table_field))
    return df
	
def execute_result(sql_string):
    '''
    执行sql并返回查询结果
    '''
    db=get_connected_db()
    cursor=db.cursor()
    results=''
    try:
        # 执行sql语句
        cursor.execute(sql_string)
        results=cursor.fetchall()
        #print results
        # 提交到数据库执行
        db.commit()
    except:
        # Rollback in case there is any error
        #return 'error'
        db.rollback()
    # 关闭数据库连接db
    db.close()
    return results

def get_user():
	df=db_to_df('my_device_test',"",'user','device_type','duration')
	user={}
	for i in df.values:
		if i[0] not in user:
			user[i[0]]={}
		user[str(i[0])][i[1]]=i[2]
	return user

def person(user1,user2):
	sum_xy=0
	sum_x=0
	sum_y=0
	sum_x2=0
	sum_y2=0
	n=0
	for key in user1:
		if key in user2:
			n+=1
			x=user1[key]
			y=user2[key]
			sum_xy += x*y
			sum_x += x
			sum_y += y
			sum_x2 +=pow(x,2)
			sum_y2 +=pow(y,2)
	if n==0:
		return 0
	denomitor=sqrt(sum_x2 - pow(sum_x, 2) / n)  * sqrt(sum_y2 - pow(sum_y, 2) / n)
	if denomitor==0:
		return 0
	else:
		return (sum_xy - (sum_x * sum_y)/n) / denomitor
	
def convertProductID2name(id):
	productid2name = {}
	if id in productid2name:
		return productid2name[id]
	else:
		return id	

def computeNearestNeighbor(user,username):
	distances=[]
	for instance in user:
		if instance != username:
			distance=person(user[username],user[instance])
			distances.append((instance,distance))
	
	distances.sort(key=lambda artistTuple: artistTuple[1],reverse=True)
	return distances
	
def recommend(user,ip):
	recommendations={}
	nearest = computeNearestNeighbor(user,ip)
	userRatings = user[ip]
	totalDistance = 0.0
	k=3
	for i in range(k):
		totalDistance += nearest[i][1]
	if totalDistance==0.0:
		totalDistance=1.0
	for i in range(k):
		weight = nearest[i][1] / totalDistance
		name=nearest[i][0]
		neighborRatings = user[name]
		for artist in neighborRatings:
				if not artist in userRatings:
					if artist not in recommendations:
						recommendations[artist] = (weight * neighborRatings[artist])
					else:
						recommendations[artist] += (weight * neighborRatings[artist])
		recommendations = list(recommendations.items())
		recommendations = [(convertProductID2name(k), v)for (k, v) in recommendations]
		recommendations.sort(key=lambda artistTuple: artistTuple[1], reverse = True)

		return recommendations[:12],nearest
	
def main(ip):
	list=[]
	user=get_user()
	if ip not in user:
		return 0,0
	k,nearuser = recommend(user,ip)
	for i in range(len(k)):
		list.append(k[i][0])
	return list,nearuser[:15] 

	
if __name__=='__main__':
	print main('10.185.155.28')